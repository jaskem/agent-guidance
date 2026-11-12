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
        self.package = self.root / 'skills/evidence-driven-development'

    def test_complete_packages(self):
        self.assertEqual(check(self.root), [])

    def test_missing_disclosed_reference_is_rejected(self):
        (self.package / 'references/diagnosis.md').unlink()
        self.assertTrue(any('missing reference' in e for e in check(self.root)))

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
