import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock

from test_workflow_starter_export import EXPORT, GitFixture, load_exporter

LEGACY_SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "export_notion_starter.py"
LEGACY = load_exporter(LEGACY_SCRIPT, "legacy_notion_export_under_test")


class NotionStarterCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = GitFixture()
        self.addCleanup(self.fixture.close)

    def test_legacy_default_and_deprecated_revision_select_the_same_snapshot(self):
        expected = EXPORT.build_files(repo=self.fixture.root)
        self.assertEqual(expected, LEGACY.build_files(repo=self.fixture.root))
        self.assertEqual(expected, LEGACY.build_files(self.fixture.first_commit, repo=self.fixture.root))
        self.assertEqual(expected, LEGACY.build_files(source_ref=self.fixture.first_commit, repo=self.fixture.root))
        with self.assertRaisesRegex(ValueError, "conflicting"):
            LEGACY.build_files("older-ref", source_ref="other-ref", repo=self.fixture.root)
        with self.assertRaises(ValueError):
            LEGACY.build_files("", repo=self.fixture.root)

    def test_legacy_cli_is_byte_identical_and_rejects_a_second_revision(self):
        expected_target = self.fixture.root / "generic.zip"
        EXPORT.write_zip(expected_target, EXPORT.build_files(repo=self.fixture.root))
        target = self.fixture.root / "legacy.zip"
        result = subprocess.run([sys.executable, str(LEGACY_SCRIPT), "--repo", str(self.fixture.root),
                                 "--exporter-revision", self.fixture.first_commit, "--output", str(target)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertEqual(target.read_bytes(), expected_target.read_bytes())
        self.assertEqual(json.loads(result.stdout)["source_commit"], self.fixture.first_commit)
        invalid = self.fixture.root / "conflicting.zip"
        result = subprocess.run([sys.executable, str(LEGACY_SCRIPT), "--repo", str(self.fixture.root),
                                 "--source-ref", "HEAD", "--exporter-revision", "different-ref",
                                 "--output", str(invalid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b"conflicting", result.stderr)
        self.assertFalse(invalid.exists())

    def test_compatibility_import_is_safe_and_helpers_use_the_shared_core(self):
        with mock.patch("subprocess.run", side_effect=AssertionError("No process during import")):
            module = load_exporter(LEGACY_SCRIPT, "legacy_notion_import_safety")
        self.assertIs(module.main, module._CORE.main)
        self.assertIs(module.write_zip, module._CORE.write_zip)
        self.assertIs(module.privacy_check, module._CORE.privacy_check)


if __name__ == "__main__":
    unittest.main()
