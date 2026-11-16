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

    def test_missing_disclosed_reference_is_rejected(self):
        (self.package / 'references/diagnosis.md').unlink()
        self.assertTrue(any('missing reference' in e for e in check(self.root)))

    def test_stale_bundled_package_version_is_rejected(self):
        path = self.package / 'references/sources.md'
        original = path.read_text()
        for declaration in ('Current package version: 2.0.0.',
                            'Package version: 2.0.0.', 'Package version 2.0.0.'):
            with self.subTest(declaration=declaration):
                path.write_text(original.replace('Current package version: 2.1.0.', declaration))
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
