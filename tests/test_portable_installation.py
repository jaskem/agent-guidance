from pathlib import Path
import json
import subprocess
import tempfile
import unittest

from tools.check_portability import check


class PortableInstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        for name in ("README.md", "AGENTS.md", "docs/METHOD-ROUTING.md"):
            self.write(name, "Use [installation](INSTALL.md) for adoption.\n")
        for name in ("INSTALL.md", "LICENSE", "docs/INSTALL-FILES.md", "docs/INSTALL-REPOSITORY.md"):
            self.write(name, "Neutral source\n")
        self.write("skills/catalog.json", json.dumps({"external_methods": [{
            "name": "optional-example", "optional": True, "bundled": False,
            "fallback": "Use the base method and public documentation",
        }]}))

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_neutral_untracked_installation_and_public_attribution(self):
        self.write("references.md", "Public source https://github.com/example/project and retained copyright notice")
        self.assertEqual(check(self.root), [])

    def test_private_destinations_fail_before_publication(self):
        for url in ("https://app.notion.com/p/" + "a" * 32,
                    "https://notion.so/" + "00000000-0000-0000-0000-000000000000",
                    "https://example.notion.site/Private-home"):
            with self.subTest(url=url):
                self.write("recipient.md", url)
                self.assertTrue(any("Private Notion" in e for e in check(self.root)))

    def test_machine_locations_fail_but_placeholder_and_regex_are_valid(self):
        self.write("recipient.md", "/" + "home/" + "example/private-guide.md")
        self.assertTrue(any("machine location" in e for e in check(self.root)))
        self.write("recipient.md", "{{OWN_GUIDE_LOCATION}}")
        self.write("scanner.py", 'import re\nPATTERN = re.compile(r"/home/[a-z]+/")\n')
        self.assertEqual(check(self.root), [])

    def test_missing_entry_route_and_inherited_external_dependency_fail(self):
        self.write("AGENTS.md", "No installation route")
        self.write("skills/catalog.json", json.dumps({"external_methods": [{
            "name": "private-default", "optional": False, "bundled": False,
        }]}))
        errors = check(self.root)
        self.assertTrue(any("AGENTS.md" in e for e in errors))
        self.assertTrue(any("private-default" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
