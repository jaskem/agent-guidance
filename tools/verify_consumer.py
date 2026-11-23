#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
VERSION_TAG = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+(?:[-+][0-9A-Za-z.-]+)?$")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_relative(value: str, label: str) -> PurePosixPath:
    p = PurePosixPath(value)
    if not value or p.is_absolute() or ".." in p.parts or "." in p.parts:
        raise ValueError(f"{label} must be a normalized relative path: {value!r}")
    return p


def load_lock(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"lock file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in lock file: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("lock root must be an object")
    return data


def verify(root: Path, lock_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        lock = load_lock(lock_path)
    except ValueError as exc:
        return [str(exc)]

    schema_version = lock.get("schema_version")
    if isinstance(schema_version, bool) or schema_version != 1:
        errors.append("schema_version must equal 1")

    source = lock.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
        source = {}
    if not isinstance(source.get("repository"), str) or not source.get("repository"):
        errors.append("source.repository must be a non-empty string")
    commit = source.get("commit")
    if not isinstance(commit, str) or not SHA40.fullmatch(commit):
        errors.append("source.commit must be a lowercase 40-character SHA")
    version = source.get("version")
    if not isinstance(version, str) or not VERSION_TAG.fullmatch(version):
        errors.append("source.version must match vMAJOR.MINOR.PATCH with an optional '-' or '+' suffix")

    try:
        destination_root_rel = safe_relative(lock.get("destination_root", ""), "destination_root")
    except (TypeError, ValueError) as exc:
        errors.append(str(exc))
        destination_root_rel = PurePosixPath("__invalid__")

    modules = lock.get("modules")
    if not isinstance(modules, list) or not modules:
        errors.append("modules must be a non-empty array")
        modules = []

    ids: set[str] = set()
    destinations: set[str] = set()
    expected_shared_files: set[str] = set()

    for idx, module in enumerate(modules):
        prefix = f"modules[{idx}]"
        if not isinstance(module, dict):
            errors.append(f"{prefix} must be an object")
            continue
        module_id = module.get("id")
        if not isinstance(module_id, str) or not module_id:
            errors.append(f"{prefix}.id must be non-empty")
        elif module_id in ids:
            errors.append(f"duplicate module id: {module_id}")
        else:
            ids.add(module_id)

        try:
            source_rel = safe_relative(module.get("source", ""), f"{prefix}.source")
            dest_rel = safe_relative(module.get("destination", ""), f"{prefix}.destination")
        except (TypeError, ValueError) as exc:
            errors.append(str(exc))
            continue

        dest_str = dest_rel.as_posix()
        if dest_str in destinations:
            errors.append(f"duplicate module destination: {dest_str}")
        destinations.add(dest_str)

        try:
            dest_rel.relative_to(destination_root_rel)
        except ValueError:
            errors.append(f"{prefix}.destination must be inside destination_root")
            continue

        expected = module.get("sha256")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected):
            errors.append(f"{prefix}.sha256 must be lowercase SHA-256")
            continue
        path = root / Path(*dest_rel.parts)
        expected_shared_files.add(dest_str)
        if not path.is_file():
            errors.append(f"missing vendored module: {dest_str}")
        else:
            actual = sha256_file(path)
            if actual != expected:
                errors.append(f"hash mismatch for {dest_str}: expected {expected}, got {actual}")

    verifier = lock.get("verifier")
    if not isinstance(verifier, dict):
        errors.append("verifier must be an object")
    else:
        try:
            safe_relative(verifier.get("source", ""), "verifier.source")
            verifier_dest = safe_relative(verifier.get("destination", ""), "verifier.destination")
        except (TypeError, ValueError) as exc:
            errors.append(str(exc))
            verifier_dest = None
        expected = verifier.get("sha256")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected):
            errors.append("verifier.sha256 must be lowercase SHA-256")
        elif verifier_dest is not None:
            path = root / Path(*verifier_dest.parts)
            if not path.is_file():
                errors.append(f"missing vendored verifier: {verifier_dest.as_posix()}")
            else:
                actual = sha256_file(path)
                if actual != expected:
                    errors.append(
                        f"hash mismatch for verifier {verifier_dest.as_posix()}: expected {expected}, got {actual}"
                    )

    shared_root = root / Path(*destination_root_rel.parts)
    if shared_root.exists() and shared_root.is_dir():
        actual_shared = {
            p.relative_to(root).as_posix()
            for p in shared_root.rglob("*")
            if p.is_file()
        }
        unexpected = sorted(actual_shared - expected_shared_files)
        missing_from_tree = sorted(expected_shared_files - actual_shared)
        for path in unexpected:
            errors.append(f"unexpected file under shared destination: {path}")
        for path in missing_from_tree:
            if not any(path in err for err in errors):
                errors.append(f"missing file under shared destination: {path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify vendored agent-guidance lock and local hashes.")
    parser.add_argument("--root", default=".", help="Consumer repository root (default: current directory).")
    parser.add_argument(
        "--lock-file", default=".agent-guidance.lock.json", help="Lock path relative to consumer root."
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    lock_path = root / args.lock_file
    errors = verify(root, lock_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"agent-guidance verification OK: {lock_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
