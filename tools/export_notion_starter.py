#!/usr/bin/env python3
"""Build a pinned, privacy-filtered transfer artifact; never install or call Notion."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile
import zipfile

SOURCE_COMMIT = "44699577c3a47d5831a861c981851c468edf5217"
SOURCE_TREE = "3dc6f398ca26c8ab19f0fe3a35edd903d52dd4ea"
PACKAGE_ID = "notion-starter-1.0.0"
REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "distribution" / "notion-starter"
PRIVATE_NOTION = re.compile(
    r"https?://(?:app\.notion\.com/p/|(?:www\.)?notion\.so/|[a-z0-9-]+\.notion\.site/)"
    r"[^\s<>)\]`\"]+", re.I
)
HOST_PATH = re.compile(r"/workspace/(?:scratch|default)/|/home/agent/|[A-Z]:\\Users\\", re.I)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO), *args])


def safe_name(name: str) -> str:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name:
        raise ValueError(f"Unsafe artifact path: {name}")
    return path.as_posix()


def privacy_check(name: str, data: bytes) -> None:
    text = data.decode("utf-8")
    if PRIVATE_NOTION.search(text) or HOST_PATH.search(text):
        raise ValueError(f"Private location found in {name}")


def filter_provenance(name: str, data: bytes) -> tuple[bytes, dict | None]:
    if name != "skills/grill-me/references/sources.md":
        return data, None
    text = data.decode("utf-8")
    paragraphs = text.split("\n\n")
    matches = [i for i, p in enumerate(paragraphs) if PRIVATE_NOTION.search(p)]
    if matches != [1]:
        raise ValueError("Unexpected private provenance shape; review the source before exporting")
    paragraphs[1] = (
        "Canonical source is jaskem/agent-guidance. The distribution record owns the "
        "released source revision, package version and installed copies. A private "
        "historical distribution reference was omitted for this portable transfer. "
        "No personal source location is required to use this method."
    )
    filtered = "\n\n".join(paragraphs).encode("utf-8")
    return filtered, {
        "path": name,
        "source_sha256": digest(data),
        "bundled_sha256": digest(filtered),
        "variant": "portable-provenance-1",
        "reason": "Private historical distribution reference removed; licenses and method unchanged",
    }


def skill_archive(name: str, files: dict[str, bytes]) -> bytes:
    stream = io.BytesIO()
    prefix = f"skills/{name}/"
    with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w") as archive:
            for path, data in sorted(files.items()):
                if path.startswith(prefix):
                    entry = tarfile.TarInfo(safe_name(name + "/" + path[len(prefix):]))
                    entry.size = len(data)
                    entry.mtime = 0
                    entry.mode = 0o644
                    archive.addfile(entry, io.BytesIO(data))
    return stream.getvalue()


def build_files(exporter_revision: str | None = None) -> dict[str, bytes]:
    if git("rev-parse", f"{SOURCE_COMMIT}^{{tree}}").decode().strip() != SOURCE_TREE:
        raise ValueError("Pinned source tree differs from verified remote tree")
    catalog = json.loads(git("show", f"{SOURCE_COMMIT}:skills/catalog.json"))
    skills = catalog["skills"]
    if len(skills) != 28 or len({s["name"] for s in skills}) != 28:
        raise ValueError("Expected the accepted 28-method catalog")
    roots = ["guidance/"] + [s["path"] + "/" for s in skills]
    named = {"skills/catalog.json", "skills/source-coverage.json", "docs/METHOD-ROUTING.md", "docs/SKILL-WORKFLOW.md"}
    entries = git("ls-tree", "-r", "-z", SOURCE_COMMIT).split(b"\0")
    files: dict[str, bytes] = {}
    origins: dict[str, dict] = {}
    redactions = []
    for entry in entries:
        if not entry:
            continue
        meta, encoded_path = entry.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        path = encoded_path.decode()
        if path not in named and not any(path.startswith(p) for p in roots):
            continue
        if kind != "blob" or mode != "100644":
            raise ValueError(f"Unexpected source file type: {path}")
        original = git("cat-file", "blob", sha)
        data, redaction = filter_provenance(path, original)
        privacy_check(path, data)
        files[safe_name(path)] = data
        origins[path] = {"source_git_blob": sha, "source_sha256": digest(original), "bundled_sha256": digest(data)}
        if redaction:
            redactions.append(redaction)
    if len(redactions) != 1:
        raise ValueError("Expected exactly one documented provenance redaction")
    for path in sorted(DOCS.rglob("*")):
        if path.is_file():
            if path.is_symlink():
                raise ValueError("Symlinks are not allowed")
            name = safe_name(path.relative_to(DOCS).as_posix())
            data = path.read_bytes()
            privacy_check(name, data)
            files[name] = data
    for skill in skills:
        path = skill["path"] + "/SKILL.md"
        original = git("show", f"{SOURCE_COMMIT}:{path}")
        if files.get(path) != original:
            raise ValueError(f"Method body changed: {path}")
        policy = files[skill["path"] + "/agents/openai.yaml"].decode()
        expected = "true" if skill.get("allow_implicit_invocation") else "false"
        if f"allow_implicit_invocation: {expected}" not in policy:
            raise ValueError(f"Invocation policy mismatch: {path}")
        files[f"packages/{skill['name']}.tar.gz"] = skill_archive(skill["name"], files)
    report = {
        "scope": "Artifact verification only; no recipient workspace accessed or installed",
        "source_tree_matches_verified_remote": True,
        "base_methods": len(skills),
        "unchanged_method_main_texts": 28,
        "implicit_methods": sum(bool(s.get("allow_implicit_invocation")) for s in skills),
        "explicit_only": [s["name"] for s in skills if not s.get("allow_implicit_invocation")],
        "documented_provenance_redactions": len(redactions),
        "private_notion_page_links_in_text_payload": 0,
        "runtime_installation_test": "Not performed; requires recipient account and own Guide",
    }
    files["VERIFICATIE.json"] = (json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode()
    manifest = {
        "package_id": PACKAGE_ID,
        "package_version": "1.0.0",
        "prepared_date": "2026-11-19",
        "source_repository": "jaskem/agent-guidance",
        "source_commit": SOURCE_COMMIT,
        "source_tree": SOURCE_TREE,
        "exporter_revision": exporter_revision or "unpublished-working-copy",
        "guidance_version": "0.6.0",
        "skill_collection_version": catalog["collection_version"],
        "new_guide_setup_baseline": "0.0.6",
        "existing_guide_setup_policy": "Preserve accepted version; no automatic upgrade or downgrade",
        "privacy_variants": redactions,
        "source_files": origins,
        "skills": [{**s, "archive": f"packages/{s['name']}.tar.gz", "distribution_variant": "portable-provenance-1" if s["name"] == "grill-me" else "unchanged"} for s in skills],
        "files": {name: {"sha256": digest(data), "bytes": len(data)} for name, data in sorted(files.items())},
    }
    files["BRONNEN.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    return files


def write_zip(target: Path, files: dict[str, bytes]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(files.items()):
            entry = zipfile.ZipInfo("Notion-installatie/" + safe_name(path), date_time=(2026, 11, 19, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(files):
            raise ValueError("Archive roundtrip failed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--exporter-revision")
    args = parser.parse_args()
    files = build_files(args.exporter_revision)
    write_zip(args.output, files)
    print(json.dumps({"output": str(args.output), "files": len(files), "bytes": args.output.stat().st_size, "sha256": digest(args.output.read_bytes()), "methods": 28, "private_links": 0}))


if __name__ == "__main__":
    main()
