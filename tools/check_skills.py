#!/usr/bin/env python3
"""Check our deliberately small, self-contained skill package format offline."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from collections import Counter
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


def check_coverage(root: Path, catalog: dict, names: set[str]) -> list[str]:
    """Check the declared consolidation evidence, not its editorial conclusions."""
    errors = []
    try:
        relative = catalog['coverage_record']
        if not isinstance(relative, str) or not relative:
            raise ValueError('coverage_record must name a repository file')
        path = (root / relative).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('coverage_record escapes repository')
        coverage = json.loads(path.read_text(encoding='utf-8'))
        counts = coverage['expected_source_counts']
        mapping = coverage['mapping']
        if (coverage['schema_version'] != 1 or not isinstance(mapping, list)
                or not isinstance(counts, dict) or not counts
                or any(not isinstance(k, str) or type(v) is not int or v < 1
                       for k, v in counts.items())):
            raise ValueError('expected schema 1, source counts and mapping array')
        if coverage['active_collection_count'] != len(names):
            errors.append('coverage collection count disagrees with catalog')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'invalid coverage record: {exc}']

    sources = set()
    actual_counts = Counter()
    for item in mapping:
        if not isinstance(item, dict) or not isinstance(item.get('source'), str):
            errors.append('invalid coverage mapping entry')
            continue
        source = item['source']
        if source in sources:
            errors.append(f'duplicate coverage source: {source}')
        sources.add(source)
        provider, separator, method = source.partition(':')
        if not separator or not method:
            errors.append(f'invalid coverage source: {source}')
        actual_counts[provider] += 1
        destination = item.get('destination')
        if not isinstance(destination, str):
            errors.append(f'unknown coverage destination: {destination}')
            continue
        if destination not in names and destination not in ('central-router', 'provider-only'):
            errors.append(f'unknown coverage destination: {destination}')
        evidence = item.get('evidence_path')
        resource = item.get('resource')
        if not isinstance(evidence, str) or not isinstance(resource, str):
            errors.append(f'missing coverage evidence: {source}')
            continue
        expected = f'skills/{destination}/{resource}' if destination in names else resource
        if evidence != expected:
            errors.append(f'coverage evidence disagrees with destination/resource: {source}')
        path = (root / evidence).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f'missing coverage evidence: {source}: {evidence}')
        elif destination in names and not path.is_relative_to((root / 'skills' / destination).resolve()):
            errors.append(f'coverage evidence disagrees with owning package: {source}')
    if dict(actual_counts) != counts:
        errors.append('coverage source counts disagree with complete mapping')
    return errors


def check_routing(root: Path, names: set[str]) -> list[str]:
    """Require every catalog method to have a selectable result and finish.

    This checks the route table contract, not an agent's semantic choice.
    """
    try:
        text = (root / 'docs/METHOD-ROUTING.md').read_text(encoding='utf-8')
        table = text.split('## Select the work\n', 1)[1].split('\n## ', 1)[0]
    except (OSError, IndexError):
        return ['routing: missing canonical selection table']
    errors = []
    routes = []
    for line in table.splitlines():
        if not line.startswith('|'):
            continue
        targets = re.findall(r'\]\(\.\./skills/([^/]+)/SKILL\.md\)', line)
        if not targets:
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(targets) != 1 or len(cells) != 3 or not cells[0] or not cells[2]:
            errors.append('routing: each method needs one request and observable finish')
        routes.extend(targets)
    counts = Counter(routes)
    for name in sorted(names - counts.keys()):
        errors.append(f'routing: catalog method has no selection entry: {name}')
    for name in sorted(counts.keys() - names):
        errors.append(f'routing: unknown method: {name}')
    for name, count in sorted(counts.items()):
        if count != 1:
            errors.append(f'routing: duplicate method entry: {name}')
    return errors


def mentions_method(text: str, name: str) -> bool:
    """Match a complete method name, not a prefix of another method's name."""
    return re.search(rf'(?<![\w-]){re.escape(name)}(?![\w-])', text) is not None


def check_external_methods(root: Path, catalog: dict, local_names: set[str]) -> list[str]:
    """Check declared external ownership/routing, not remote installation."""
    errors = []
    entries = catalog.get('external_methods', [])
    if not isinstance(entries, list):
        return ['external_methods must be a list']
    try:
        router = (root / 'docs/METHOD-ROUTING.md').read_text(encoding='utf-8')
    except OSError:
        router = ''
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append('external method must be an object')
            continue
        name = entry.get('name')
        if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append('invalid external method name')
            continue
        if name in seen or name in local_names:
            errors.append(f'duplicate or locally owned external method: {name}')
        seen.add(name)
        if not re.fullmatch(r'\d+\.\d+\.\d+', str(entry.get('version', ''))):
            errors.append(f'{name}: external method needs a semantic version')
        for field in ('owner', 'distribution'):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f'{name}: external method needs {field}')
        targets = entry.get('distribution_targets')
        if (not isinstance(targets, list) or not targets
                or any(not isinstance(target, str) or not target.strip() for target in targets)):
            errors.append(f'{name}: external method needs distribution_targets')
        if f'`{name}`' not in router:
            errors.append(f'external method has no explicit route: {name}')
    return errors


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
    skill_texts: dict[str, str] = {}
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
        skill_texts[name] = text
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
            if file.relative_to(package).as_posix() == 'references/sources.md':
                declared = re.findall(
                    r'(?:Current package version|Package version):?\s+(\d+\.\d+\.\d+)', body)
                if any(version != entry['version'] for version in declared):
                    errors.append(f'{name}: bundled package version disagrees with catalog')
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

    # Name presence is structural disclosure only: it does not establish a
    # sensible trigger, actual invocation, or correct semantic route selection.
    dependencies = {}
    for entry in entries:
        if (not isinstance(entry, dict) or not isinstance(entry.get('name'), str)
                or entry['name'] not in seen):
            continue
        name = entry['name']
        required = entry.get('dependencies', [])
        if not isinstance(required, list) or any(not isinstance(x, str) for x in required):
            errors.append(f'{name}: dependencies must be a list of skill names')
            continue
        if len(set(required)) != len(required):
            errors.append(f'{name}: duplicate dependency')
        for dependency in required:
            if dependency not in seen:
                errors.append(f'{name}: unknown dependency: {dependency}')
            elif name in skill_texts and not mentions_method(skill_texts[name], dependency):
                errors.append(f'{name}: dependency not disclosed in SKILL.md: {dependency}')
        dependencies[name] = required

    # Conditional routes are not mandatory load dependencies; legitimate task
    # composition can return to an earlier method, so only dependencies form a DAG.
    for entry in entries:
        if (not isinstance(entry, dict) or not isinstance(entry.get('name'), str)
                or entry['name'] not in seen):
            continue
        name = entry['name']
        routes = entry.get('conditional_routes', [])
        if not isinstance(routes, list):
            errors.append(f'{name}: conditional_routes must be a list of objects')
            continue
        pairs = set()
        for route in routes:
            if not isinstance(route, dict):
                errors.append(f'{name}: conditional route must be an object')
                continue
            target, trigger = route.get('to'), route.get('when')
            if not isinstance(target, str) or target not in seen:
                errors.append(f'{name}: unknown conditional route target: {target}')
            elif target == name:
                errors.append(f'{name}: conditional route cannot target itself')
            elif name in skill_texts and not mentions_method(skill_texts[name], target):
                errors.append(f'{name}: conditional route not disclosed in SKILL.md: {target}')
            if not isinstance(trigger, str) or not trigger.strip():
                errors.append(f'{name}: conditional route requires a non-empty trigger')
                continue
            if isinstance(target, str):
                # Ignore surrounding padding; do not infer semantic equivalence.
                pair = (target, trigger.strip())
                if pair in pairs:
                    errors.append(f'{name}: duplicate conditional route: {target}: {trigger.strip()}')
                pairs.add(pair)

    visited, active = set(), set()
    def visit(name):
        if name in active:
            errors.append(f'{name}: cyclic skill dependency')
            return
        if name in visited:
            return
        active.add(name)
        for dependency in dependencies.get(name, []):
            visit(dependency)
        active.remove(name)
        visited.add(name)
    for name in dependencies:
        visit(name)

    actual = set((root / 'skills').glob('*/SKILL.md'))
    if actual != listed:
        errors.append('catalog/package mismatch: ' + str(sorted(str(p) for p in actual ^ listed)))
    errors.extend(check_coverage(root, catalog, seen))
    errors.extend(check_routing(root, seen))
    errors.extend(check_external_methods(root, catalog, seen))
    return errors


if __name__ == '__main__':
    failures = check(Path(__file__).resolve().parents[1])
    for failure in failures:
        print(f'ERROR: {failure}', file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print('skill packages OK: catalog, metadata, method composition, local references and source coverage')
