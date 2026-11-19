import importlib.util
import io
import json
from pathlib import Path
import tarfile
import unittest

SPEC = importlib.util.spec_from_file_location("export_notion_starter", Path(__file__).resolve().parents[1] / "tools" / "export_notion_starter.py")
EXPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORT)


class NotionStarterExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = EXPORT.build_files()
        cls.manifest = json.loads(cls.files["BRONNEN.json"])

    def test_all_payload_hashes_and_complete_method_archives(self):
        self.assertEqual(set(self.files) - {"BRONNEN.json"}, set(self.manifest["files"]))
        for path, metadata in self.manifest["files"].items():
            self.assertEqual(EXPORT.digest(self.files[path]), metadata["sha256"], path)
        for skill in self.manifest["skills"]:
            name = skill["name"]
            prefix = skill["path"] + "/"
            expected = {name + "/" + p[len(prefix):]: b for p, b in self.files.items() if p.startswith(prefix)}
            with tarfile.open(fileobj=io.BytesIO(self.files[skill["archive"]]), mode="r:gz") as archive:
                actual = {m.name: archive.extractfile(m).read() for m in archive.getmembers()}
            self.assertEqual(expected, actual, name)

    def test_private_locations_fail_closed(self):
        for text in ("https://app.notion.com/p/" + "a" * 32, "https://notion.so/private-" + "b" * 32, "https://private.notion.site/Home", "/workspace/scratch/example", "C:\\Users\\Example"):
            with self.assertRaises(ValueError):
                EXPORT.privacy_check("candidate.md", text.encode())
        EXPORT.privacy_check("help.md", b"https://www.notion.com/help/category/databases")

    def test_privacy_variant_is_limited_and_licensed(self):
        changes = [p for p, v in self.manifest["source_files"].items() if v["source_sha256"] != v["bundled_sha256"]]
        self.assertEqual(changes, ["skills/grill-me/references/sources.md"])
        self.assertIn(b"MIT License", self.files[changes[0]])
        for path, data in self.files.items():
            if not path.endswith(".tar.gz"):
                EXPORT.privacy_check(path, data)

    def test_source_shape_change_requires_review(self):
        with self.assertRaises(ValueError):
            EXPORT.filter_provenance("skills/grill-me/references/sources.md", b"Unexpected new source")

    def test_archive_path_safety(self):
        for name in ("../outside", "/absolute", "x/../../outside", "x\\outside"):
            with self.assertRaises(ValueError):
                EXPORT.safe_name(name)


if __name__ == "__main__":
    unittest.main()
