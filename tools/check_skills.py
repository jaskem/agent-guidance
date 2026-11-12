#!/usr/bin/env python3
"""Check our deliberately small, self-contained skill package format offline."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def read_metadata(text: str) -> dict[str, dict]:
    """Parse only the two sections and JSON-quoted strings our generator emits."""
    result: dict[str, dict] = {}
    section = None
    for line in text.splitlines():
        if not line.strip():
            continue
        if line in ('interface:', 'policy:'):
            section = line[:-1]
            if section in result:
                raise ValueError('duplicate metadata section')
            result[section] = {}
            continue
        match = re.fullmatch(r'  ([a-z_]+): (.+)', line)
        if not match or section is None:
            raise ValueError('unsupported metadata structure')
        key, raw = match.groups()
        allowed = ('display_name', 'short_description', 'default_prompt') if section == 'interface' else ('allow_implicit_invocation',)
        if key not in allowed or key in result[section]:
            raise ValueError('unknown or duplicate metadata field')
        value = json.loads(raw)
        if section == 'interface' and (not isinstance(value, str) or not value):
            raise ValueError('interface fields must be non-empty quoted strings')
        if section == 'policy' and not isinstance(value, bool):
            raise ValueError('invocation policy must be boolean')
        result[section][key] = value
    if set(result.get('interface', {})) != {'display_name', 'short_description', 'default_prompt'}:
        raise ValueError('missing interface metadata')
    if set(result.get('policy', {})) != {'allow_implicit_invocation'}:
        raise ValueError('missing invocation policy')
    return result


def check(root: Path) -> list[str]:
    errors: list[str] = []
    catalog_path = root / 'skills/catalog.json'
    try:
        catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
        entries = catalog['skills']
        if catalog['schema_version'] != 1 or not isinstance(entries, list) or not entries:
            raise ValueError('expected schema_version 1 and a non-empty skill list')
        if not re.fullmatch(r'[0-9a-f]{40}', catalog['upstream_review']['commit']):
            raise ValueError('upstream review must pin an exact commit')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'invalid skill catalog: {exc}']

    seen: set[str] = set()
    listed: set[Path] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append('skill entry must be an object')
            continue
        name = entry.get('name', '')
        if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append(f'invalid name: {name!r}')
            continue
        if name in seen:
            errors.append(f'duplicate skill: {name}')
        seen.add(name)
        if entry.get('path') != f'skills/{name}':
            errors.append(f'{name}: path must be skills/{name}')
            continue
        if not isinstance(entry.get('allow_implicit_invocation'), bool):
            errors.append(f'{name}: invocation policy must be boolean')
        if not re.fullmatch(r'\d+\.\d+\.\d+', str(entry.get('version', ''))):
            errors.append(f'{name}: missing semantic package version')
        package = root / entry['path']
        listed.add(package / 'SKILL.md')
        if package.is_symlink():
            errors.append(f'{name}: linked package is not self-contained')
            continue
        try:
            text = (package / 'SKILL.md').read_text(encoding='utf-8')
            yaml = (package / 'agents/openai.yaml').read_text(encoding='utf-8')
        except OSError as exc:
            errors.append(f'{name}: missing package file: {exc.filename}')
            continue
        # Our authoring format intentionally uses only two plain, one-line fields.
        header = re.match(r'\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n', text)
        if (not header or header[1] != name or not header[2].strip()
                or re.search(r':\s|\s#|^[\[\]{}&*!|>\x27\"%@`]', header[2])):
            errors.append(f'{name}: invalid name/description frontmatter')
        try:
            metadata = read_metadata(yaml)
            if metadata['policy']['allow_implicit_invocation'] != entry.get('allow_implicit_invocation'):
                errors.append(f'{name}: invocation metadata disagrees with catalog')
            if f'${name}' not in metadata['interface']['default_prompt']:
                errors.append(f'{name}: example prompt must name the skill')
        except ValueError as exc:
            errors.append(f'{name}: invalid agent metadata: {exc}')
        for file in sorted(package.rglob('*')):
            if file.is_symlink():
                errors.append(f'{name}: symlink not allowed: {file.name}')
                continue
            if not file.is_file() or file.suffix != '.md':
                continue
            body = file.read_text(encoding='utf-8')
            if '[TODO:' in body:
                errors.append(f'{name}: unfinished template in {file.name}')
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', body):
                parsed = urlsplit(target)
                if parsed.scheme in ('https', 'http') or target.startswith('#'):
                    continue
                if parsed.scheme or parsed.netloc:
                    errors.append(f'{name}: non-portable reference: {target}')
                    continue
                destination = (file.parent / unquote(parsed.path)).resolve()
                if not destination.is_relative_to(package.resolve()):
                    errors.append(f'{name}: reference escapes package: {target}')
                elif not destination.is_file():
                    errors.append(f'{name}: missing reference: {target}')

    actual = set((root / 'skills').glob('*/SKILL.md'))
    if actual != listed:
        errors.append('catalog/package mismatch: ' + str(sorted(str(p) for p in actual ^ listed)))
    return errors


if __name__ == '__main__':
    failures = check(Path(__file__).resolve().parents[1])
    for failure in failures:
        print(f'ERROR: {failure}', file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print('skill packages OK: catalog, metadata and local references')
