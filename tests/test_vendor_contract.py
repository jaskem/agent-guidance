from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "tools/vendor_guidance.py"
VERIFY = ROOT / "tools/verify_consumer.py"


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args), cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )


class VendorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        head = run("git", "-C", str(ROOT), "rev-parse", "HEAD")
        if head.returncode != 0:
            raise unittest.SkipTest("tests require a committed git checkout")
        cls.head = head.stdout.strip()
        dirty = run("git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=no")
        if dirty.stdout.strip():
            raise unittest.SkipTest("tests require clean tracked source checkout")

    def vendor(self, consumer: Path, commit: str | None = None) -> subprocess.CompletedProcess[str]:
        return run(
            sys.executable,
            str(VENDOR),
            "--source-root",
            str(ROOT),
            "--consumer-root",
            str(consumer),
            "--source-commit",
            commit or self.head,
            "--module",
            "kernel",
            "--module",
            "expert-operating-model",
            "--module",
            "architecture-engineering",
        )

    def test_vendor_is_deterministic_and_verifier_detects_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            first = self.vendor(consumer)
            self.assertEqual(first.returncode, 0, first.stderr)
            lock = consumer / ".agent-guidance.lock.json"
            first_bytes = lock.read_bytes()

            second = self.vendor(consumer)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first_bytes, lock.read_bytes())

            verify = run(sys.executable, str(consumer / "tools/verify_agent_guidance.py"), "--root", str(consumer))
            self.assertEqual(verify.returncode, 0, verify.stderr)

            target = consumer / "docs/agent/shared/KERNEL.md"
            target.write_text(target.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
            verify_drift = run(
                sys.executable, str(consumer / "tools/verify_agent_guidance.py"), "--root", str(consumer)
            )
            self.assertNotEqual(verify_drift.returncode, 0)
            self.assertIn("hash mismatch", verify_drift.stderr)

    def test_verifier_rejects_unexpected_shared_file(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            result = self.vendor(consumer)
            self.assertEqual(result.returncode, 0, result.stderr)
            extra = consumer / "docs/agent/shared/local.md"
            extra.write_text("must not be here\n", encoding="utf-8")
            verify = run(sys.executable, str(consumer / "tools/verify_agent_guidance.py"), "--root", str(consumer))
            self.assertNotEqual(verify.returncode, 0)
            self.assertIn("unexpected file under shared destination", verify.stderr)

    def test_verifier_validates_schema_version(self) -> None:
        cases = (
            (1, True),
            (1.0, True),
            (True, False),
            (False, False),
            (2, False),
            ("1", False),
            (None, False),
        )
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            result = self.vendor(consumer)
            self.assertEqual(result.returncode, 0, result.stderr)
            lock = consumer / ".agent-guidance.lock.json"
            data = json.loads(lock.read_text(encoding="utf-8"))
            for schema_version, valid in cases:
                with self.subTest(schema_version=schema_version):
                    data["schema_version"] = schema_version
                    lock.write_text(json.dumps(data), encoding="utf-8")
                    verify = run(
                        sys.executable, str(consumer / "tools/verify_agent_guidance.py"), "--root", str(consumer)
                    )
                    self.assertEqual(verify.returncode, 0 if valid else 1, verify.stderr)
                    if not valid:
                        self.assertIn("schema_version", verify.stderr)

    def test_verifier_validates_required_version_tag(self) -> None:
        missing = object()
        cases = (
            ("v1.2.3", True),
            ("v1.2.3-rc.1", True),
            ("v1.2.3+build.4", True),
            ("v01.002.0003", True),
            (missing, False),
            (None, False),
            (True, False),
            (1, False),
            ("", False),
            ("vgarbage", False),
            ("v1", False),
            ("v1.2", False),
            ("1.2.3", False),
            ("v1.2.3-", False),
            ("v1.2.3+", False),
            ("v1.2.3-rc.1+build.4", False),
        )
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            result = self.vendor(consumer)
            self.assertEqual(result.returncode, 0, result.stderr)
            lock = consumer / ".agent-guidance.lock.json"
            data = json.loads(lock.read_text(encoding="utf-8"))
            for version, valid in cases:
                with self.subTest(version="missing" if version is missing else version):
                    if version is missing:
                        data["source"].pop("version", None)
                    else:
                        data["source"]["version"] = version
                    lock.write_text(json.dumps(data), encoding="utf-8")
                    verify = run(
                        sys.executable, str(consumer / "tools/verify_agent_guidance.py"), "--root", str(consumer)
                    )
                    self.assertEqual(verify.returncode, 0 if valid else 1, verify.stderr)
                    if not valid:
                        self.assertIn("source.version", verify.stderr)

    def test_vendor_rejects_wrong_commit_pin(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            wrong = "0" * 40
            result = self.vendor(consumer, wrong)
            self.assertEqual(result.returncode, 2)
            self.assertIn("does not match requested pin", result.stderr)

    def test_lock_hashes_match_vendored_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            consumer = Path(td) / "consumer"
            result = self.vendor(consumer)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads((consumer / ".agent-guidance.lock.json").read_text(encoding="utf-8"))
            for item in data["modules"]:
                payload = (consumer / item["destination"]).read_bytes()
                self.assertEqual(hashlib.sha256(payload).hexdigest(), item["sha256"])


if __name__ == "__main__":
    unittest.main()
