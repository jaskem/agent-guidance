#!/usr/bin/env python3
"""Validate declared learning-change evidence; never execute or verify its refs.

An eligible record satisfies this data contract only. It does not establish
truthful evidence, valid authorization, independent review, or permission to act.
The reviewer and host remain responsible for those decisions.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

KINDS = {'guidance_patch', 'skill_patch', 'upstream_refresh', 'new_skill', 'rollback'}
BLOCKED_RISKS = {'approval_bypass', 'secrets', 'ignore_user_instructions'}
EXIT_CODES = {'eligible': 0, 'manual_review': 2, 'blocked': 1}


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _finite(value: object) -> bool:
    # bool is an int subclass; arbitrarily large integers are still finite.
    return type(value) is int or (type(value) is float and math.isfinite(value))


def _https(value: object) -> bool:
    if not _text(value) or any(char.isspace() or ord(char) < 32 or ord(char) == 127
                               for char in value):
        return False
    try:
        parsed = urlsplit(value)
        return (parsed.scheme == 'https' and bool(parsed.hostname)
                and parsed.username is None and parsed.password is None
                and (parsed.port is None or 0 < parsed.port <= 65535))
    except ValueError:
        return False


def evaluate(record: dict) -> dict:
    """Return eligible/manual_review/blocked for the supplied declarations only."""
    errors: list[str] = []
    manual: list[str] = []
    if not isinstance(record, dict):
        return {'decision': 'blocked', 'reasons': ['record must be an object']}

    def section(name: str) -> dict:
        value = record.get(name)
        if not isinstance(value, dict):
            errors.append(f'{name} must be an object')
            return {}
        return value

    def texts(obj: dict, prefix: str, names: tuple[str, ...]) -> None:
        for name in names:
            if not _text(obj.get(name)):
                errors.append(f'{prefix}{name} must be non-empty text')

    def evidence(obj: dict, prefix: str) -> None:
        refs = obj.get('evidence')
        if not isinstance(refs, list) or not refs or not all(_text(ref) for ref in refs):
            errors.append(f'{prefix}evidence must be a non-empty list of text refs')

    def required_true(obj: dict, prefix: str, names: tuple[str, ...]) -> None:
        for name in names:
            if obj.get(name) is not True:
                errors.append(f'{prefix}{name} must be true')

    if type(record.get('schema_version')) is not int or record['schema_version'] != 1:
        errors.append('schema_version must be integer 1')
    texts(record, '', ('id', 'owner', 'authorization_ref', 'scope'))
    kind = record.get('kind')
    if not isinstance(kind, str) or kind not in KINDS:
        errors.append('kind must name a supported learning change')
    if _text(record.get('scope')) and record['scope'] != 'instructions_only':
        manual.append('scope requires manual review outside instructions_only')

    risks = record.get('risk_flags')
    if not isinstance(risks, list) or not all(_text(flag) for flag in risks):
        errors.append('risk_flags must be a list of non-empty text flags')
    elif risks:
        normalized = {flag.strip().lower() for flag in risks}
        prohibited = normalized & BLOCKED_RISKS
        if prohibited:
            errors.append('prohibited risk flags: ' + ', '.join(sorted(prohibited)))
        else:
            manual.append('risk_flags require manual review: ' + ', '.join(risks))

    observation = section('observation')
    texts(observation, 'observation.', ('effect',))
    evidence(observation, 'observation.')
    baseline = section('baseline')
    candidate = section('candidate')
    texts(baseline, 'baseline.', ('ref',))
    texts(candidate, 'candidate.', ('ref',))
    if baseline.get('outcome') not in ('pass', 'fail'):
        errors.append('baseline.outcome must be pass or fail')
    if candidate.get('outcome') != 'pass':
        errors.append('candidate.outcome must be pass')

    if baseline.get('outcome') == 'pass' or 'benefit' in record:
        benefit = section('benefit')
        texts(benefit, 'benefit.', ('metric',))
        before, after = benefit.get('baseline'), benefit.get('candidate')
        direction = benefit.get('direction')
        if direction not in ('lower', 'higher'):
            errors.append('benefit.direction must be lower or higher')
        if not _finite(before) or not _finite(after):
            errors.append('benefit baseline and candidate must be finite numbers')
        elif direction in ('lower', 'higher'):
            improved = after < before if direction == 'lower' else after > before
            if not improved:
                errors.append('benefit must show a strict improvement')

    checks = section('checks')
    required_true(checks, 'checks.', ('positive', 'excluded', 'missing_input', 'regression'))
    review = section('review')
    required_true(review, 'review.', ('independent', 'findings_resolved'))
    evidence(review, 'review.')
    rollback = section('rollback')
    texts(rollback, 'rollback.', ('ref', 'restore_procedure'))

    if kind in ('new_skill', 'upstream_refresh'):
        source = section('source')
        if not _https(source.get('url')):
            errors.append('source.url must be an HTTPS URL without credentials')
        commit = source.get('commit')
        if not isinstance(commit, str) or not re.fullmatch(r'[0-9a-fA-F]{40}', commit):
            errors.append('source.commit must be exactly 40 hexadecimal characters')
        texts(source, 'source.', ('license',))
        required_true(source, 'source.', ('all_files_reviewed', 'no_unapproved_execution'))
    if kind == 'new_skill':
        novelty = section('novelty')
        required_true(novelty, 'novelty.', ('existing_routes_checked',))
        texts(novelty, 'novelty.', ('distinct_outcome', 'adapt_existing_reason'))

    decision = 'blocked' if errors else 'manual_review' if manual else 'eligible'
    return {'decision': decision, 'reasons': errors + manual}


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f'non-standard JSON constant: {value}')


def main(argv: list[str] | None = None) -> int:
    """Read one JSON input, print one decision; do not follow any supplied ref."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        result = {'decision': 'blocked', 'reasons': ['expected one JSON file path']}
    else:
        try:
            record = json.loads(Path(args[0]).read_text(encoding='utf-8'),
                                object_pairs_hook=_unique_object,
                                parse_constant=_reject_constant)
            result = evaluate(record)
        except (OSError, UnicodeError, ValueError, RecursionError) as exc:
            result = {'decision': 'blocked', 'reasons': [f'invalid input: {exc}']}
    print(json.dumps(result, ensure_ascii=True))
    return EXIT_CODES[result['decision']]


if __name__ == '__main__':
    sys.exit(main())
