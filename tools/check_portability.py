#!/usr/bin/env python3
"""Check public installation surfaces for concrete private source dependencies.

This is structural preflight, not personal-name recognition or a privacy audit.
Source/license attribution and public repository identities remain intentional.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess

if __package__:
    from .export_workflow_starter import privacy_check
else:
    from export_workflow_starter import privacy_check

ROOT = Path(__file__).resolve().parents[1]


def check(root: Path) -> list[str]:
    errors = []
    listed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        capture_output=True, check=True,
    ).stdout.decode().split("\0")
    for relative in sorted(set(filter(None, listed))):
        if relative.startswith(("tests/", ".github/")):
            continue  # These may contain deliberate failing fixtures, never installer payload.
        path = root / relative
        if path.is_symlink():
            errors.append(f"{relative}: public installation sources must not be symlinks")
            continue
        if not path.is_file():
            continue
        try:
            privacy_check(relative, path.read_bytes())
        except ValueError as exc:
            errors.append(str(exc))

    for relative in ("README.md", "AGENTS.md", "docs/METHOD-ROUTING.md"):
        path = root / relative
        if not path.is_file() or "INSTALL.md" not in path.read_text(encoding="utf-8"):
            errors.append(f"{relative}: missing installation entry route")
    for relative in ("INSTALL.md", "LICENSE", "docs/INSTALL-FILES.md", "docs/INSTALL-REPOSITORY.md"):
        if not (root / relative).is_file():
            errors.append(f"missing portable installation surface: {relative}")

    catalog = json.loads((root / "skills/catalog.json").read_text(encoding="utf-8"))
    for item in catalog.get("external_methods", []):
        if item.get("optional") is not True or item.get("bundled") is not False or not item.get("fallback"):
            errors.append(f"{item.get('name')}: external method requires optional/unbundled status and fallback")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = check(args.root.resolve())
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(f"portability check failed: {exc}")
        return 1
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("portability OK: public routes and optional dependencies; not a personal-name or history audit")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
