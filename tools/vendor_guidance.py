#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath

SHA40 = re.compile(r"^[0-9a-f]{40}$")


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


def git(source_root: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(source_root), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise ValueError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Vendor pinned shared agent guidance into a consumer repository.")
    parser.add_argument("--source-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--consumer-root", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--module", action="append", dest="modules", required=True, help="Module id; repeatable.")
    parser.add_argument("--destination-root", default="docs/agent/shared")
    parser.add_argument("--lock-file", default=".agent-guidance.lock.json")
    parser.add_argument("--verifier-destination", default="tools/verify_agent_guidance.py")
    args = parser.parse_args()

    source_root = Path(args.source_root).resolve()
    consumer_root = Path(args.consumer_root).resolve()
    requested_commit = args.source_commit.lower()

    try:
        if not SHA40.fullmatch(requested_commit):
            raise ValueError("--source-commit must be a lowercase 40-character SHA")
        actual_head = git(source_root, "rev-parse", "HEAD").lower()
        if actual_head != requested_commit:
            raise ValueError(f"source checkout HEAD {actual_head} does not match requested pin {requested_commit}")
        dirty = git(source_root, "status", "--porcelain", "--untracked-files=no")
        if dirty:
            raise ValueError("source checkout has modified tracked files; vendor only from a clean exact commit")

        catalog = load_json(source_root / "guidance/catalog.json")
        version = catalog.get("guidance_version")
        repository = catalog.get("source_repository")
        if not isinstance(version, str) or not version:
            raise ValueError("catalog guidance_version is invalid")
        if not isinstance(repository, str) or not repository:
            raise ValueError("catalog source_repository is invalid")
        modules = catalog.get("modules")
        if not isinstance(modules, list):
            raise ValueError("catalog modules must be an array")
        by_id = {}
        for item in modules:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not isinstance(item.get("path"), str):
                raise ValueError("catalog contains invalid module entry")
            if item["id"] in by_id:
                raise ValueError(f"duplicate catalog module id: {item['id']}")
            by_id[item["id"]] = item

        requested_ids = sorted(set(args.modules))
        if "kernel" not in requested_ids:
            raise ValueError("consumers must vendor the 'kernel' module")
        unknown = [mid for mid in requested_ids if mid not in by_id]
        if unknown:
            raise ValueError(f"unknown module id(s): {', '.join(unknown)}")

        destination_root_rel = safe_relative(args.destination_root, "--destination-root")
        lock_rel = safe_relative(args.lock_file, "--lock-file")
        verifier_dest_rel = safe_relative(args.verifier_destination, "--verifier-destination")
        consumer_root.mkdir(parents=True, exist_ok=True)
        destination_root = consumer_root / Path(*destination_root_rel.parts)
        lock_path = consumer_root / Path(*lock_rel.parts)

        prior_destinations: set[str] = set()
        if lock_path.exists():
            prior = load_json(lock_path)
            for item in prior.get("modules", []):
                if isinstance(item, dict) and isinstance(item.get("destination"), str):
                    prior_destinations.add(item["destination"])
        elif destination_root.exists():
            unexpected = [p for p in destination_root.rglob("*") if p.is_file()]
            if unexpected:
                raise ValueError(
                    "shared destination already contains files but no existing lock; migrate/clear it explicitly first"
                )

        entries = []
        new_destinations: set[str] = set()
        for module_id in requested_ids:
            item = by_id[module_id]
            source_rel = safe_relative(item["path"], f"catalog module {module_id} path")
            source_path = source_root / Path(*source_rel.parts)
            if not source_path.is_file():
                raise ValueError(f"catalog source missing for {module_id}: {source_rel.as_posix()}")
            try:
                relative_under_guidance = source_rel.relative_to(PurePosixPath("guidance"))
            except ValueError as exc:
                raise ValueError(f"shared module must live under guidance/: {source_rel.as_posix()}") from exc
            dest_rel = destination_root_rel / relative_under_guidance
            dest_path = consumer_root / Path(*dest_rel.parts)
            atomic_write(dest_path, source_path.read_bytes())
            new_destinations.add(dest_rel.as_posix())
            entries.append(
                {
                    "id": module_id,
                    "source": source_rel.as_posix(),
                    "destination": dest_rel.as_posix(),
                    "sha256": sha256_file(dest_path),
                }
            )

        for stale in sorted(prior_destinations - new_destinations):
            try:
                stale_rel = safe_relative(stale, "prior module destination")
                stale_rel.relative_to(destination_root_rel)
            except ValueError:
                continue
            stale_path = consumer_root / Path(*stale_rel.parts)
            if stale_path.is_file():
                stale_path.unlink()

        verifier_source_rel = PurePosixPath("tools/verify_consumer.py")
        verifier_source = source_root / Path(*verifier_source_rel.parts)
        verifier_dest = consumer_root / Path(*verifier_dest_rel.parts)
        atomic_write(verifier_dest, verifier_source.read_bytes())

        lock = {
            "schema_version": 1,
            "source": {
                "repository": repository,
                "commit": requested_commit,
                "version": f"v{version}",
            },
            "destination_root": destination_root_rel.as_posix(),
            "modules": sorted(entries, key=lambda x: x["id"]),
            "verifier": {
                "source": verifier_source_rel.as_posix(),
                "destination": verifier_dest_rel.as_posix(),
                "sha256": sha256_file(verifier_dest),
            },
        }
        lock_bytes = (json.dumps(lock, indent=2, sort_keys=True) + "\n").encode("utf-8")
        atomic_write(lock_path, lock_bytes)
        print(f"vendored {len(entries)} module(s) at {requested_commit} into {consumer_root}")
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
