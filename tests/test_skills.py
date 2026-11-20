from pathlib import Path
import json
import shutil
import tempfile
import unittest

from tools.check_skills import check

ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')
        shutil.copytree(ROOT / 'docs', self.root / 'docs')
        self.package = self.root / 'skills/evidence-driven-development'

    def test_complete_packages(self):
        self.assertEqual(check(self.root), [])

    def change_catalog(self, change):
        path = self.root / 'skills/catalog.json'
        catalog = json.loads(path.read_text())
        change(catalog)
        path.write_text(json.dumps(catalog))

    def set_conditional_routes(self, name, routes):
        def change(catalog):
            entry = next(entry for entry in catalog['skills'] if entry['name'] == name)
            entry['conditional_routes'] = routes
        self.change_catalog(change)

    def disclose_methods(self, name, *targets):
        path = self.root / f'skills/{name}/SKILL.md'
        path.write_text(path.read_text() + '\nConditional methods: '
                        + ', '.join(f'`{target}`' for target in targets) + '.\n')

    def change_coverage(self, change):
        path = self.root / 'skills/source-coverage.json'
        coverage = json.loads(path.read_text())
        change(coverage)
        path.write_text(json.dumps(coverage))

    def test_missing_coverage_record_is_rejected(self):
        (self.root / 'skills/source-coverage.json').unlink()
        self.assertTrue(any('coverage' in e for e in check(self.root)))

    def change_router(self, change):
        path = self.root / 'docs/METHOD-ROUTING.md'
        path.write_text(change(path.read_text()))

    def test_catalog_method_missing_from_routing_is_rejected(self):
        self.change_router(lambda text: '\n'.join(
            line for line in text.splitlines()
            if '| [teach](' not in line))
        self.assertTrue(any('no selection entry: teach' in e for e in check(self.root)))

    def test_unknown_routed_method_is_rejected(self):
        self.change_router(lambda text: text.replace(
            '../skills/teach/SKILL.md', '../skills/unknown-method/SKILL.md'))
        self.assertTrue(any('unknown method: unknown-method' in e for e in check(self.root)))

    def test_duplicate_route_is_rejected(self):
        def duplicate(text):
            line = next(line for line in text.splitlines() if '| [teach](' in line)
            return text.replace(line, line + '\n' + line)
        self.change_router(duplicate)
        self.assertTrue(any('duplicate method entry: teach' in e for e in check(self.root)))

    def test_route_without_observable_finish_is_rejected(self):
        def remove_finish(text):
            line = next(line for line in text.splitlines() if '| [teach](' in line)
            return text.replace(line, '|'.join(line.split('|')[:3]) + ' |')
        self.change_router(remove_finish)
        self.assertTrue(any('request and observable finish' in e for e in check(self.root)))

    def test_unreadable_router_is_not_success(self):
        (self.root / 'docs/METHOD-ROUTING.md').unlink()
        self.assertTrue(any('routing: missing' in e for e in check(self.root)))

    def test_duplicate_provider_entry_is_rejected(self):
        self.change_coverage(lambda c: c['mapping'].append(c['mapping'][0]))
        self.assertTrue(any('duplicate coverage source' in e for e in check(self.root)))

    def test_incomplete_provider_coverage_is_rejected(self):
        self.change_coverage(lambda c: c['mapping'].pop())
        self.assertTrue(any('coverage source counts' in e for e in check(self.root)))

    def test_coverage_target_must_be_in_collection(self):
        self.change_coverage(lambda c: c['mapping'][0].update(destination='missing-method'))
        self.assertTrue(any('unknown coverage destination' in e for e in check(self.root)))

    def test_missing_coverage_evidence_is_rejected(self):
        self.change_coverage(lambda c: c['mapping'][0].update(evidence_path='skills/missing.md'))
        self.assertTrue(any('missing coverage evidence' in e for e in check(self.root)))

    def test_coverage_evidence_stays_in_owning_package(self):
        self.change_coverage(lambda c: c['mapping'][0].update(
            evidence_path='skills/code-review/references/axes.md'))
        self.assertTrue(any('coverage evidence disagrees' in e for e in check(self.root)))

    def test_unknown_dependency_is_rejected(self):
        p = self.root / 'skills/catalog.json'
        catalog = json.loads(p.read_text())
        catalog['skills'][0]['dependencies'] = ['missing-method']
        p.write_text(json.dumps(catalog))
        self.assertTrue(any('unknown dependency' in e for e in check(self.root)))

    def test_circular_dependency_is_rejected(self):
        p = self.root / 'skills/catalog.json'
        catalog = json.loads(p.read_text())
        first, second = catalog['skills'][:2]
        first['dependencies'] = [second['name']]
        second['dependencies'] = [first['name']]
        p.write_text(json.dumps(catalog))
        self.assertTrue(any('cyclic skill dependency' in e for e in check(self.root)))

    def test_dependency_must_be_disclosed_in_owning_skill(self):
        path = self.package / 'SKILL.md'
        path.write_text(path.read_text().replace('code-review', 'a separate review method'))
        self.assertTrue(any('dependency not disclosed in SKILL.md: code-review' in e
                            for e in check(self.root)))

    def test_conditional_routes_allow_distinct_triggers_and_task_composition_cycles(self):
        self.set_conditional_routes('plan-work', [
            {'to': 'research', 'when': 'Evidence is missing'},
            {'to': 'research', 'when': 'Sources conflict'},
        ])
        self.set_conditional_routes('research', [
            {'to': 'plan-work', 'when': 'Findings need an implementation sequence'},
        ])
        self.disclose_methods('plan-work', 'research')
        self.disclose_methods('research', 'plan-work')
        self.assertEqual(check(self.root), [])

    def test_unknown_conditional_route_target_is_rejected(self):
        self.set_conditional_routes('plan-work', [
            {'to': 'missing-method', 'when': 'Evidence is missing'},
        ])
        self.assertTrue(any('unknown conditional route target: missing-method' in e
                            for e in check(self.root)))

    def test_missing_conditional_route_target_is_rejected(self):
        self.set_conditional_routes('plan-work', [{'when': 'Evidence is missing'}])
        self.assertTrue(any('unknown conditional route target' in e for e in check(self.root)))

    def test_conditional_route_requires_nonempty_trigger(self):
        self.disclose_methods('plan-work', 'research')
        for trigger in ('', ' \n\t ', None, 3):
            with self.subTest(trigger=trigger):
                self.set_conditional_routes('plan-work', [{'to': 'research', 'when': trigger}])
                self.assertTrue(any('non-empty trigger' in e for e in check(self.root)))

    def test_duplicate_conditional_route_is_rejected(self):
        self.disclose_methods('plan-work', 'research')
        self.set_conditional_routes('plan-work', [
            {'to': 'research', 'when': 'Evidence is missing'},
            {'to': 'research', 'when': 'Evidence is missing'},
        ])
        self.assertTrue(any('duplicate conditional route' in e for e in check(self.root)))

    def test_conditional_route_cannot_target_itself(self):
        self.set_conditional_routes('plan-work', [
            {'to': 'plan-work', 'when': 'The plan needs refinement'},
        ])
        self.assertTrue(any('conditional route cannot target itself' in e
                            for e in check(self.root)))

    def test_conditional_route_must_be_disclosed_in_owning_skill(self):
        path = self.root / 'skills/plan-work/SKILL.md'
        # A supporting reference or a longer method name is not main-text disclosure.
        path.write_text(path.read_text().replace('research', 'evidence gathering')
                        + '\nThe research-methodology example is supplementary.\n')
        reference = self.root / 'skills/plan-work/references/sources.md'
        reference.write_text(reference.read_text() + '\nUse research when evidence is missing.\n')
        self.set_conditional_routes('plan-work', [
            {'to': 'research', 'when': 'Evidence is missing'},
        ])
        self.assertTrue(any('conditional route not disclosed in SKILL.md: research' in e
                            for e in check(self.root)))

    def test_conditional_routes_require_array_of_objects(self):
        for routes in (None, {}, 'research', [None], ['research']):
            with self.subTest(routes=routes):
                self.set_conditional_routes('plan-work', routes)
                self.assertTrue(any('conditional' in e and 'must be' in e
                                    for e in check(self.root)))

    def test_missing_disclosed_reference_is_rejected(self):
        (self.package / 'references/diagnosis.md').unlink()
        self.assertTrue(any('missing reference' in e for e in check(self.root)))

    def test_external_reference_supplements_are_validated(self):
        self.assertEqual(check(self.root), [])
        self.change_catalog(lambda c: c['external_methods'][-1].update(supplements=['missing-method']))
        self.assertTrue(any('invalid external supplement targets' in e for e in check(self.root)))

    def test_external_reference_supplement_requires_trigger_and_owner(self):
        self.change_catalog(lambda c: c['external_methods'][-1].update(when='', selection_owner='elsewhere.md'))
        errors = check(self.root)
        self.assertTrue(any('external supplement requires a trigger' in e for e in errors))
        self.assertTrue(any('external supplement must use the central router' in e for e in errors))

    def test_external_reference_supplement_rejects_duplicate_targets(self):
        self.change_catalog(lambda c: c['external_methods'][-1].update(supplements=['teach', 'teach']))
        self.assertTrue(any('duplicate external supplement target' in e for e in check(self.root)))

    def test_external_method_cannot_mask_local_or_duplicate_owner(self):
        self.change_catalog(lambda c: c['external_methods'].append(c['external_methods'][0].copy()))
        self.assertTrue(any('duplicate or locally owned external method' in e for e in check(self.root)))
        self.change_catalog(lambda c: c['external_methods'][0].update(name='teach'))
        self.assertTrue(any('locally owned external method: teach' in e for e in check(self.root)))

    def test_external_method_requires_an_explicit_route(self):
        self.change_router(lambda text: text.replace('`logo-design`', 'the separate logo method'))
        self.assertTrue(any('external method has no explicit route: logo-design' in e for e in check(self.root)))

    def test_external_method_requires_owner_and_destination(self):
        self.change_catalog(lambda c: c['external_methods'][0].update(owner='', distribution_targets=[]))
        failures = check(self.root)
        self.assertTrue(any('external method needs owner' in e for e in failures))
        self.assertTrue(any('external method needs distribution_targets' in e for e in failures))

    def test_stale_bundled_package_version_is_rejected(self):
        path = self.package / 'references/sources.md'
        original = path.read_text()
        catalog = json.loads((self.root / 'skills/catalog.json').read_text())
        current = next(entry['version'] for entry in catalog['skills']
                       if entry['name'] == self.package.name)
        original_declaration = f'Current package version: {current}.'
        self.assertIn(original_declaration, original)
        mismatched = '0.0.0' if current != '0.0.0' else '0.0.1'
        for declaration in (f'Current package version: {mismatched}.',
                            f'Package version: {mismatched}.', f'Package version {mismatched}.'):
            with self.subTest(declaration=declaration):
                path.write_text(original.replace(original_declaration, declaration))
                self.assertTrue(any('bundled package version disagrees' in e for e in check(self.root)))

    def test_reference_cannot_depend_on_host_files(self):
        p = self.package / 'SKILL.md'
        p.write_text(p.read_text() + '\n[hidden rule](../../../outside.md)\n')
        self.assertTrue(any('escapes package' in e for e in check(self.root)))

    def test_unlisted_skill_is_rejected(self):
        extra = self.root / 'skills/unregistered'
        extra.mkdir()
        (extra / 'SKILL.md').write_text('not registered')
        self.assertTrue(any('catalog/package mismatch' in e for e in check(self.root)))

    def test_invocation_policy_cannot_silently_change(self):
        p = self.package / 'agents/openai.yaml'
        p.write_text(p.read_text().replace('allow_implicit_invocation: true', 'allow_implicit_invocation: false'))
        self.assertTrue(any('invocation metadata disagrees' in e for e in check(self.root)))

    def test_unpinned_upstream_is_rejected(self):
        p = self.root / 'skills/catalog.json'
        catalog = json.loads(p.read_text())
        catalog['upstream_review']['commit'] = 'main'
        p.write_text(json.dumps(catalog))
        self.assertTrue(any('exact commit' in e for e in check(self.root)))

    def test_invalid_yaml_scalar_is_rejected(self):
        p = self.package / 'SKILL.md'
        p.write_text(p.read_text().replace('description: Execute', 'description: Scope: Execute'))
        self.assertTrue(any('invalid name/description' in e for e in check(self.root)))

    def test_misspelled_policy_section_is_rejected(self):
        p = self.package / 'agents/openai.yaml'
        p.write_text(p.read_text().replace('policy:', 'polciy:'))
        self.assertTrue(any('invalid agent metadata' in e for e in check(self.root)))

    def test_skill_name_elsewhere_does_not_validate_prompt(self):
        p = self.package / 'agents/openai.yaml'
        p.write_text('interface:\n  display_name: "$evidence-driven-development"\n'
                     '  short_description: "A helpful description"\n'
                     '  default_prompt: "Run this"\n'
                     'policy:\n  allow_implicit_invocation: true\n')
        self.assertTrue(any('example prompt must name' in e for e in check(self.root)))


if __name__ == '__main__':
    unittest.main()
