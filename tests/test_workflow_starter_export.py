import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "export_workflow_starter.py"


def load_exporter(path=SCRIPT, name="workflow_export_under_test"):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EXPORT = load_exporter()


def encoded_json(value):
    return (json.dumps(value, indent=2) + "\n").encode()


class GitFixture:
    """A small committed repository; none of its contents depend on this checkout."""

    def __init__(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.run("init", "-q")
        self.catalog = {
            "schema_version": 1,
            "source_repository": "example/workflow",
            "collection_version": "7.4.2",
            "skills": [],
            "external_methods": [{"name": "online-reference", "version": "3.1.0", "owner": "separate source"}],
        }
        self.write("README.md", b"Portable workflow\n")
        self.write("LICENSE", b"MIT License\n\nCopyright (c) Fixture original-work contributors\n\n"
                   b"The above copyright notice and this permission notice shall be included in all "
                   b"copies or substantial portions of the Software.\n")
        self.write("INSTALL.md", b"Use tools/vendor_guidance.py and complete packages.\n")
        self.write("AGENTS.md", b"Use the recipient's configured guide.\n")
        self.write("VERSION", b"1.2.3\n")
        self.write("guidance/catalog.json", encoded_json({"guidance_version": "1.2.3", "modules": []}))
        self.write("guidance/KERNEL.md", b"Shared workflow\n")
        self.write("docs/WORKFLOW.md", b"Repository workflow\n")
        self.write("docs/SKILL-WORKFLOW.md", b"Complete package workflow\n")
        self.write("docs/CONSUMER-CONTRACT.md", b"Pinned consumer contract\n")
        self.write("distribution/workflow-starter/templates/Agent-Operating-Guide.md", b"Recipient guide template\n")
        self.write("distribution/notion-starter/INSTALLATIE.md", b"Optional Notion adapter\n")
        self.write("distribution/notion-starter/templates/Agent-Operating-Guide.md", b"Optional adapter template\n")
        self.write("tools/vendor_guidance.py", b"#!/usr/bin/env python3\nprint('read before use')\n", executable=True)
        self.write("asset.bin", b"\xff\x00\x80\x00binary\x00\xfe")
        # Excluded source text must never contaminate or block the portable payload.
        excluded = ("https://app.notion.com/p/" + "a" * 32).encode()
        self.write("tests/test_private_fixture.py", excluded)
        self.write(".github/workflows/test.yml", excluded)
        self.add_skill("alpha", "1.2.0", True)
        self.add_skill("beta", "2.3.1", False)
        self.write("skills/beta/LICENSE", b"An existing package-specific license must remain unchanged.\n")
        self.write_catalog()
        self.first_commit = self.commit("First complete collection", day=2)

    def close(self):
        self.directory.cleanup()

    def run(self, *args, data=None, env=None):
        result = subprocess.run(
            ["git", "-C", str(self.root), *args], input=data,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env,
        )
        if result.returncode:
            raise AssertionError(result.stderr.decode(errors="replace"))
        return result.stdout

    def write(self, name, data, executable=False):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        if executable:
            target.chmod(0o755)

    def add_skill(self, name, version, implicit):
        self.catalog["skills"].append({"name": name, "path": "skills/" + name,
                                       "version": version, "allow_implicit_invocation": implicit})
        self.write("skills/" + name + "/SKILL.md", ("---\nname: " + name + "\ndescription: Fixture method\n---\n\nMethod\n").encode())
        policy = "policy:\n  allow_implicit_invocation: " + str(implicit).lower() + "\n"
        self.write("skills/" + name + "/agents/openai.yaml", policy.encode())
        self.write("skills/" + name + "/references/sources.md", b"MIT License\nCopyright (c) Fixture author\n\nAttribution must remain byte-identical.\n")
        self.write("skills/" + name + "/scripts/check.py", b"#!/usr/bin/env python3\nprint('fixture')\n", executable=True)

    def write_catalog(self):
        self.write("skills/catalog.json", encoded_json(self.catalog))

    def commit(self, message, day=2):
        self.run("add", "--all")
        env = dict(os.environ, GIT_AUTHOR_DATE=f"2024-03-{day:02d}T12:34:56+00:00",
                   GIT_COMMITTER_DATE=f"2024-03-{day:02d}T12:34:56+00:00")
        self.run("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--allow-empty", "-qm", message, env=env)
        return self.run("rev-parse", "HEAD").decode().strip()

    def selected_source(self, ref="HEAD"):
        names = self.run("ls-tree", "-rz", "--name-only", ref).decode().split("\0")
        return {name: self.run("show", ref + ":" + name) for name in names
                if name and name.split("/", 1)[0] not in {"tests", ".github"}}


class WorkflowStarterExportTests(unittest.TestCase):
    def setUp(self):
        self.fixture = GitFixture()
        self.addCleanup(self.fixture.close)

    def test_manifest_retains_all_snapshot_files_versions_legal_text_and_hashes(self):
        files = EXPORT.build_files(repo=self.fixture.root)
        manifest = json.loads(files["BRONNEN.json"])
        source = self.fixture.selected_source()
        self.assertEqual(source, {path: files[path] for path in manifest["source_files"]})
        self.assertEqual(set(source), set(manifest["source_files"]))
        self.assertEqual(manifest["source_commit"], self.fixture.first_commit)
        self.assertIsNone(manifest["exporter_revision"])
        self.assertFalse(manifest["exporter_matches_source_snapshot"])
        self.assertEqual(manifest["exporter_sha256"], EXPORT.digest(SCRIPT.read_bytes()))
        self.assertEqual(manifest["source_tree"], self.fixture.run("rev-parse", "HEAD^{tree}").decode().strip())
        self.assertEqual(manifest["source_repository"], self.fixture.catalog["source_repository"])
        self.assertEqual(manifest["guidance_version"], "1.2.3")
        self.assertEqual(manifest["skill_collection_version"], "7.4.2")
        self.assertEqual(manifest["package_version"], "7.4.2+git." + self.fixture.first_commit[:12])
        self.assertEqual(manifest["prepared_date"], "2024-03-02")
        self.assertIn("INSTALL.md", files)
        self.assertIn("tools/vendor_guidance.py", files)
        self.assertIn("distribution/workflow-starter/templates/Agent-Operating-Guide.md", files)
        self.assertIn("distribution/notion-starter/INSTALLATIE.md", files)
        self.assertEqual(set(files) - {"BRONNEN.json"}, set(manifest["files"]))
        for name, metadata in manifest["files"].items():
            self.assertEqual(metadata, {"sha256": EXPORT.digest(files[name]), "bytes": len(files[name])}, name)
        for name, metadata in manifest["source_files"].items():
            self.assertEqual(metadata["source_sha256"], metadata["bundled_sha256"], name)
            self.assertEqual(metadata["source_sha256"], EXPORT.digest(source[name]), name)
            self.assertEqual(metadata["source_git_blob"], self.fixture.run("rev-parse", "HEAD:" + name).decode().strip())
        self.assertEqual(manifest["privacy_variants"], [])
        report = json.loads(files["VERIFICATIE.json"])
        self.assertEqual(report["base_methods"], len(self.fixture.catalog["skills"]))
        self.assertEqual(report["unchanged_method_main_texts"], len(self.fixture.catalog["skills"]))
        self.assertEqual(report["skill_archives_with_original_work_notice"], len(self.fixture.catalog["skills"]))
        self.assertEqual(report["explicit_only"], ["beta"])
        self.assertEqual(report["documented_provenance_redactions"], 0)
        self.assertNotIn("source_tree_matches_verified_remote", report)
        self.assertEqual([method["name"] for method in manifest["external_methods"]], ["online-reference"])
        self.assertTrue(manifest["external_methods"][0]["optional"])
        self.assertFalse(manifest["external_methods"][0]["bundled"])
        self.assertNotIn("packages/online-reference.tar.gz", files)

    def test_catalog_and_versions_are_read_from_selected_ref_despite_dirty_worktree(self):
        old_files = EXPORT.build_files(self.fixture.first_commit, repo=self.fixture.root)
        self.fixture.catalog["collection_version"] = "8.0.0"
        self.fixture.catalog["skills"][0]["version"] = "4.0.0"
        self.fixture.add_skill("gamma", "0.7.1", True)
        self.fixture.write_catalog()
        self.fixture.write("VERSION", b"2.0.0\n")
        self.fixture.write("guidance/catalog.json", encoded_json({"guidance_version": "2.0.0", "modules": []}))
        second = self.fixture.commit("Different collection and guidance", day=3)
        current = EXPORT.build_files(repo=self.fixture.root)
        manifest = json.loads(current["BRONNEN.json"])
        self.assertEqual(manifest["source_commit"], second)
        self.assertEqual(manifest["guidance_version"], "2.0.0")
        self.assertEqual(manifest["skill_collection_version"], "8.0.0")
        self.assertEqual(len(manifest["skills"]), 3)
        self.assertEqual(manifest["skills"][0]["version"], "4.0.0")
        self.assertEqual(manifest["prepared_date"], "2024-03-03")
        self.fixture.write("INSTALL.md", ("https://app.notion.com/p/" + "b" * 32).encode())
        (self.fixture.root / "skills/alpha/SKILL.md").unlink()
        self.fixture.write("untracked-secret.md", ("/home/" + "person/private").encode())
        self.assertEqual(current, EXPORT.build_files(repo=self.fixture.root))
        self.assertEqual(old_files, EXPORT.build_files(self.fixture.first_commit, repo=self.fixture.root))
        self.fixture.run("tag", "selected-snapshot", second)
        self.assertEqual(current, EXPORT.build_files("selected-snapshot", repo=self.fixture.root))
        self.assertEqual(current, EXPORT.build_files(second, repo=self.fixture.root))

    def test_exporter_revision_is_claimed_only_when_executed_code_matches_snapshot(self):
        self.fixture.write("tools/export_workflow_starter.py", SCRIPT.read_bytes())
        matching = self.fixture.commit("Matching exporter code")
        files = EXPORT.build_files(repo=self.fixture.root)
        manifest = json.loads(files["BRONNEN.json"])
        self.assertEqual(manifest["exporter_revision"], matching)
        self.assertTrue(manifest["exporter_matches_source_snapshot"])
        self.assertEqual(manifest["exporter_sha256"], EXPORT.digest(files["tools/export_workflow_starter.py"]))
        self.fixture.write("tools/export_workflow_starter.py", b"# An older committed exporter\n")
        self.fixture.commit("Different exporter code")
        files = EXPORT.build_files(repo=self.fixture.root)
        manifest = json.loads(files["BRONNEN.json"])
        self.assertIsNone(manifest["exporter_revision"])
        self.assertFalse(manifest["exporter_matches_source_snapshot"])
        self.assertEqual(manifest["exporter_sha256"], EXPORT.digest(SCRIPT.read_bytes()))
        self.assertEqual(files["tools/export_workflow_starter.py"], b"# An older committed exporter\n")

    def test_archives_are_complete_deterministic_and_retain_executable_modes(self):
        files = EXPORT.build_files(repo=self.fixture.root)
        self.assertEqual(files, EXPORT.build_files(repo=self.fixture.root))
        manifest = json.loads(files["BRONNEN.json"])
        for skill in manifest["skills"]:
            prefix = skill["path"] + "/"
            expected = {skill["name"] + "/" + path[len(prefix):]: data
                        for path, data in files.items() if path.startswith(prefix)}
            self.assertEqual(len(skill["packaging_additions"]), 1)
            notice_path, notice = next(iter(skill["packaging_additions"].items()))
            expected_notice_path = skill["name"] + "/" + ("AGENT-GUIDANCE-LICENSE" if skill["name"] == "beta" else "LICENSE")
            self.assertEqual(notice_path, expected_notice_path)
            self.assertEqual(notice["source_path"], "LICENSE")
            self.assertEqual(notice["source_sha256"], EXPORT.digest(files["LICENSE"]))
            self.assertEqual(notice["sha256"], EXPORT.digest(files["LICENSE"]))
            self.assertTrue(notice["packaging_addition"])
            expected[notice_path] = files["LICENSE"]
            package = files[skill["archive"]]
            self.assertEqual(skill["archive_sha256"], EXPORT.digest(package))
            self.assertEqual(skill["archive_bytes"], len(package))
            self.assertEqual(package[4:8], b"\x00" * 4)
            self.assertEqual(set(skill["files"]), {path for path in files if path.startswith(prefix)})
            with tarfile.open(fileobj=io.BytesIO(package), mode="r:gz") as archive:
                actual = {}
                for member in archive.getmembers():
                    self.assertTrue(member.isfile())
                    self.assertEqual((member.mtime, member.uid, member.gid), (0, 0, 0))
                    self.assertEqual(member.mode, 0o755 if member.name.endswith("/scripts/check.py") else 0o644)
                    actual[member.name] = archive.extractfile(member).read()
                self.assertEqual(expected, actual)
                self.assertIn(b"MIT License", actual[skill["name"] + "/references/sources.md"])
                self.assertEqual(actual[notice_path], files["LICENSE"])
                self.assertIn(b"Copyright (c) Fixture original-work contributors", actual[notice_path])
                self.assertEqual(set(skill["archive_files"]), set(actual))
                for path, metadata in skill["archive_files"].items():
                    self.assertEqual(metadata["sha256"], EXPORT.digest(actual[path]))
                    self.assertEqual(metadata["bytes"], len(actual[path]))
                    self.assertEqual(actual[path], files[metadata["source_path"]])
                    self.assertEqual(metadata["packaging_addition"], path == notice_path)
                if skill["name"] == "beta":
                    self.assertEqual(actual["beta/LICENSE"], files["skills/beta/LICENSE"])
        first, second = self.fixture.root / "first.zip", self.fixture.root / "second.zip"
        EXPORT.write_zip(first, files)
        EXPORT.write_zip(second, files)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with zipfile.ZipFile(first) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual({EXPORT.ARCHIVE_ROOT + "/" + path for path in files}, set(archive.namelist()))
            self.assertEqual(files, {name.split("/", 1)[1]: archive.read(name) for name in archive.namelist()})
            self.assertEqual(archive.getinfo(EXPORT.ARCHIVE_ROOT + "/tools/vendor_guidance.py").external_attr >> 16, 0o100755)

    def test_license_notice_addition_never_overwrites_existing_package_licenses(self):
        self.fixture.write("skills/beta/AGENT-GUIDANCE-LICENSE", b"Existing alternate notice\n")
        self.fixture.write("skills/beta/AGENT-GUIDANCE-LICENSE-2", b"Another existing notice\n")
        self.fixture.commit("Existing license names must survive")
        files = EXPORT.build_files(repo=self.fixture.root)
        skill = next(skill for skill in json.loads(files["BRONNEN.json"])["skills"] if skill["name"] == "beta")
        self.assertEqual(set(skill["packaging_additions"]), {"beta/AGENT-GUIDANCE-LICENSE-3"})
        self.assertEqual(set(skill["files"]), {path for path in files if path.startswith("skills/beta/")})
        self.assertNotIn("skills/beta/AGENT-GUIDANCE-LICENSE-3", files)
        with tarfile.open(fileobj=io.BytesIO(files[skill["archive"]]), mode="r:gz") as archive:
            for name in ("LICENSE", "AGENT-GUIDANCE-LICENSE", "AGENT-GUIDANCE-LICENSE-2"):
                self.assertEqual(archive.extractfile("beta/" + name).read(), files["skills/beta/" + name])
            self.assertEqual(archive.extractfile("beta/AGENT-GUIDANCE-LICENSE-3").read(), files["LICENSE"])

    def test_standalone_packages_require_a_nonempty_committed_root_notice(self):
        self.fixture.write("LICENSE", b"")
        self.fixture.commit("Empty root notice")
        with self.assertRaisesRegex(ValueError, "root LICENSE is required"):
            EXPORT.build_files(repo=self.fixture.root)
        self.fixture.run("rm", "LICENSE")
        self.fixture.commit("Missing root notice")
        with self.assertRaisesRegex(ValueError, "root LICENSE is required"):
            EXPORT.build_files(repo=self.fixture.root)

    def test_privacy_rejects_concrete_locations_and_allows_docs_placeholders_and_patterns(self):
        private_locations = [
            "https://app.notion.com/p/" + "a" * 32,
            "https://notion.so/private-" + "b" * 32,
            "https://private.notion.site/" + "Home",
            "/workspace/" + "scratch/example",
            "/home/" + "someone/notes",
            "/Users/" + "Someone/Documents",
            "/root/" + "private-notes",
            "C:" + "\\Users\\Example\\Documents",
            "~" + "/private-notes",
        ]
        for location in private_locations:
            with self.subTest(location=location):
                with self.assertRaises(ValueError):
                    EXPORT.privacy_check("candidate.md", location.encode())
        for encoding in ("utf-16", "utf-32"):
            with self.assertRaises(ValueError):
                EXPORT.privacy_check("candidate.txt", private_locations[0].encode(encoding))
        for location in private_locations:
            with self.assertRaises(ValueError):
                EXPORT.privacy_check("candidate.json", encoded_json({"private": location}))
        with self.assertRaises(ValueError):
            EXPORT.privacy_check("candidate.json", encoded_json({"private": private_locations[0]}).replace(b"/", b"\\/"))
        for location in (
            "https://www.notion.com/help/category/databases",
            "https://developers.notion.com/reference/intro",
            "https://app.notion.com/p/<OWN_GUIDE>",
            "https://app.notion.com/p/{OWN_GUIDE}",
            r'https?://(?:app\.notion\.com/p/|notion\.so/)[a-f0-9]{32}',
            r'/workspace/(?:scratch|default)/',
        ):
            EXPORT.privacy_check("help.md", location.encode())
        regex_source = ('import re\npattern = re.compile(r"/' + 'home/agent/' + '")\n').encode()
        EXPORT.privacy_check("safety_check.py", regex_source)
        # Only regex arguments are ignored; a real location on the same line still fails.
        with self.assertRaises(ValueError):
            EXPORT.privacy_check("safety_check.py", regex_source + ('actual = "/' + 'home/person/private"\n').encode())

    def test_committed_private_source_fails_without_rewriting(self):
        for payload in (("https://app.notion.com/p/" + "c" * 32).encode(), ("/home/" + "person/private").encode()):
            self.fixture.write("docs/private-source.md", b"MIT License\n" + payload + b"\n")
            ref = self.fixture.commit("Private source is not exportable")
            original = self.fixture.run("show", ref + ":docs/private-source.md")
            with self.assertRaises(ValueError):
                EXPORT.build_files(ref, repo=self.fixture.root)
            self.assertEqual(original, self.fixture.run("show", ref + ":docs/private-source.md"))
            self.assertEqual(original, (self.fixture.root / "docs/private-source.md").read_bytes())

    def test_unsafe_paths_are_rejected_before_archive_writes(self):
        for name in ("", ".", "../outside", "/absolute", "x/../../outside", "x\\outside",
                     "x/./outside", "x//outside", "x/", "C:/outside", ".git/config", ".GIT/config",
                     "trailing. /name", "trailing./name", "line\nbreak"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    EXPORT.safe_name(name)
                target = self.fixture.root / "unsafe.zip"
                with self.assertRaises(ValueError):
                    EXPORT.write_zip(target, {name: b"unsafe"})
                self.assertFalse(target.exists())

    def test_symlink_and_submodule_source_entries_fail_closed(self):
        link = self.fixture.root / "docs/linked.md"
        link.symlink_to("../README.md")
        self.fixture.commit("Symlink")
        with self.assertRaisesRegex(ValueError, "Unsupported source entry"):
            EXPORT.build_files(repo=self.fixture.root)
        self.fixture.run("rm", "docs/linked.md")
        self.fixture.commit("Remove symlink")
        self.fixture.run("update-index", "--add", "--cacheinfo", "160000," + self.fixture.first_commit + ",modules/example")
        self.fixture.run("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Submodule")
        with self.assertRaisesRegex(ValueError, "Unsupported source entry"):
            EXPORT.build_files(repo=self.fixture.root)

    def test_unknown_or_noncommit_refs_fail(self):
        for ref in ("not-a-known-ref", "HEAD:README.md", "--help", "", "HEAD\nREADME.md"):
            with self.subTest(ref=ref):
                with self.assertRaises(ValueError):
                    EXPORT.build_files(ref, repo=self.fixture.root)

    def test_incomplete_catalog_or_reserved_generated_source_fails(self):
        self.fixture.write("BRONNEN.json", b"{}")
        self.fixture.commit("Reserved metadata collision")
        with self.assertRaisesRegex(ValueError, "collides"):
            EXPORT.build_files(repo=self.fixture.root)
        self.fixture.run("rm", "BRONNEN.json")
        self.fixture.commit("Remove collision")
        (self.fixture.root / "skills/alpha/agents/openai.yaml").unlink()
        self.fixture.commit("Missing package support file")
        with self.assertRaisesRegex(ValueError, "Incomplete skill package"):
            EXPORT.build_files(repo=self.fixture.root)

    def test_cli_exports_requested_snapshot_and_reports_actual_dynamic_count(self):
        target = self.fixture.root / "cli.zip"
        result = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(self.fixture.root),
                                 "--source-ref", self.fixture.first_commit, "--output", str(target)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        report = json.loads(result.stdout)
        self.assertEqual(report["source_commit"], self.fixture.first_commit)
        self.assertEqual(report["methods"], len(self.fixture.catalog["skills"]))
        self.assertEqual(report["sha256"], EXPORT.digest(target.read_bytes()))
        bad_target = self.fixture.root / "invalid.zip"
        result = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(self.fixture.root),
                                 "--source-ref", "unknown-snapshot", "--output", str(bad_target)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(bad_target.exists())
        self.assertNotIn(b"Traceback", result.stderr)

    def test_import_has_no_git_process_or_repository_read_side_effect(self):
        with mock.patch("subprocess.run", side_effect=AssertionError("Import must not execute git")), \
             mock.patch.object(Path, "read_bytes", side_effect=AssertionError("Import must not read repository payload")):
            module = load_exporter(name="workflow_export_import_safety")
        self.assertTrue(callable(module.build_files))


if __name__ == "__main__":
    unittest.main()
