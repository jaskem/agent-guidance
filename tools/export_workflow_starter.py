#!/usr/bin/env python3
"""Export one committed workflow snapshot; never install skills or access a service."""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile
from urllib.parse import unquote, urlsplit
import zipfile

REPO = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = "workflow-starter"
EXCLUDED_ROOTS = frozenset({".github", "tests"})
GENERATED_FILES = frozenset({"BRONNEN.json", "VERIFICATIE.json"})
# The ZIP format needs a representable timestamp; this is its epoch, not a release date.
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)
URL = re.compile(r"https?://[^\s<>\[\]`\"']+", re.I)
MACHINE_PATH = re.compile(
    r"(?<![\w.-])(?:/(?:workspace|home|Users)/[^\s<>\[\]`\"'(){}|?*]+"
    r"|/root/[^\s<>\[\]`\"'(){}|?*]+"
    r"|[A-Z]:[\\/](?:Users|Documents and Settings|workspace)[\\/]"
    r"[^\r\n<>\[\]`\"'(){}|?*]+"
    r"|~/[^\s<>\[\]`\"'(){}|?*]+)",
    re.I,
)
REGEX_FUNCTIONS = frozenset(
    {"compile", "search", "match", "fullmatch", "findall", "finditer", "sub", "subn", "split"}
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str, repo: Path = REPO) -> bytes:
    result = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(repo), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(f"Git could not read the selected snapshot: {detail}")
    return result.stdout


def safe_name(name: str) -> str:
    """Require a portable, normalized relative path before creating an archive entry."""
    if not isinstance(name, str) or not name:
        raise ValueError(f"Unsafe artifact path: {name!r}")
    path = PurePosixPath(name)
    if (
        path.is_absolute()
        or path.as_posix() != name
        or any(part.casefold() in {".", "..", ".git"} or part.endswith((" ", ".")) for part in path.parts)
        or not path.parts
        or "\\" in name
        or ":" in name
        or any(ord(char) < 32 or ord(char) == 127 for char in name)
    ):
        raise ValueError(f"Unsafe artifact path: {name!r}")
    return name


def _without_regex_literals(name: str, text: str) -> str:
    """Scan locations, not literal regular expressions in Python safety checks."""
    if not name.endswith(".py"):
        return text
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return text
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))

    def position(row: int, column: int) -> int:
        # AST columns count UTF-8 bytes; the privacy scan operates on characters.
        return offsets[row - 1] + len(lines[row - 1].encode("utf-8")[:column].decode("utf-8"))

    spans = []
    for node in ast.walk(tree):
        if not (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "re"
            and node.func.attr in REGEX_FUNCTIONS
        ):
            continue
        pattern = node.args[0] if node.args else next(
            (keyword.value for keyword in node.keywords if keyword.arg == "pattern"), None
        )
        if isinstance(pattern, ast.Constant) and isinstance(pattern.value, str):
            spans.append((
                position(pattern.lineno, pattern.col_offset),
                position(pattern.end_lineno, pattern.end_col_offset),
            ))
    for start, end in sorted(spans, reverse=True):
        text = text[:start] + " " * (end - start) + text[end:]
    return text


def privacy_check(name: str, data: bytes) -> None:
    """Reject concrete workspace page URLs and user-machine paths without redacting."""
    if data.startswith((b"\xff\xfe\x00\x00", b"\x00\x00\xfe\xff")):
        text = data.decode("utf-32", errors="replace")
    elif data.startswith((b"\xff\xfe", b"\xfe\xff")):
        text = data.decode("utf-16", errors="replace")
    else:
        text = data.decode("utf-8", errors="replace")
    text = _without_regex_literals(name, text)
    # JSON and source literals may escape separators; this only changes the scan.
    text = text.replace("\\/", "/").replace("\\\\", "\\")
    for match in URL.finditer(text):
        token = match.group().rstrip(".,;:!?)")
        try:
            parsed = urlsplit(token)
        except ValueError:
            continue
        host = (parsed.hostname or "").lower()
        path = unquote(parsed.path).lstrip("/")
        # Empty paths and placeholder-only paths are instructions, not page locations.
        if not path or any(char in path for char in "{}\\|*"):
            continue
        concrete = path.split("/", 1)[-1] if path.startswith("p/") else path
        if not concrete or concrete.startswith(("<", "[")):
            continue
        page_host = (
            host == "app.notion.com"
            or host in {"notion.so", "www.notion.so"}
            or host.endswith(".notion.site")
        )
        if page_host:
            raise ValueError(f"Private Notion page location found in {name}")
    if MACHINE_PATH.search(text):
        raise ValueError(f"User machine location found in {name}")


def _json(data: object) -> bytes:
    return (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def _catalog(files: dict[str, bytes]) -> dict:
    try:
        catalog = json.loads(files["skills/catalog.json"])
        skills = catalog["skills"]
        version = catalog["collection_version"]
        repository = catalog["source_repository"]
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Snapshot has no valid skill catalog and collection version") from exc
    if not isinstance(skills, list) or not isinstance(version, str) or not version.strip():
        raise ValueError("Invalid catalog skills or collection version")
    if not isinstance(repository, str) or not repository.strip():
        raise ValueError("Catalog must identify its source repository")
    names, paths = set(), set()
    for skill in skills:
        if not isinstance(skill, dict):
            raise ValueError("Invalid catalog skill")
        name, path = skill.get("name"), skill.get("path")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"Invalid skill name: {name!r}")
        safe_name(path)
        if name in names or path in paths or any(
            path.startswith(previous + "/") or previous.startswith(path + "/") for previous in paths
        ):
            raise ValueError("Duplicate or overlapping catalog skills")
        if not isinstance(skill.get("version"), str) or not skill["version"].strip():
            raise ValueError(f"Missing skill version: {name}")
        if not isinstance(skill.get("allow_implicit_invocation"), bool):
            raise ValueError(f"Missing invocation policy: {name}")
        if path + "/SKILL.md" not in files or path + "/agents/openai.yaml" not in files:
            raise ValueError(f"Incomplete skill package: {name}")
        policy = files[path + "/agents/openai.yaml"].decode("utf-8")
        expected = "true" if skill["allow_implicit_invocation"] else "false"
        if not re.search(r"^\s*allow_implicit_invocation:\s*" + expected + r"\s*$", policy, re.M):
            raise ValueError(f"Invocation policy mismatch: {name}")
        names.add(name)
        paths.add(path)
    external = catalog.get("external_methods", [])
    if not isinstance(external, list) or any(
        not isinstance(method, dict) or not isinstance(method.get("name"), str) for method in external
    ):
        raise ValueError("Invalid external-method declarations")
    return catalog


def _skill_archive_entries(
    name: str, files: dict[str, bytes], *, source_path: str | None = None, modes: dict[str, int] | None = None
) -> dict[str, tuple[str, bytes, int, bool]]:
    safe_name(name)
    if "/" in name:
        raise ValueError(f"Invalid skill archive root: {name}")
    prefix = safe_name(source_path or "skills/" + name) + "/"
    if not files.get("LICENSE"):
        raise ValueError("Snapshot root LICENSE is required for standalone skill archives")
    entries = {
        safe_name(name + "/" + path[len(prefix):]): (path, data, (modes or {}).get(path, 0o644), False)
        for path, data in files.items() if path.startswith(prefix)
    }
    notice = "LICENSE"
    suffix = 1
    existing = {path.casefold() for path in entries}
    while any(path == (name + "/" + notice).casefold() or path.startswith((name + "/" + notice + "/").casefold())
              for path in existing):
        notice = "AGENT-GUIDANCE-LICENSE" + ("" if suffix == 1 else "-" + str(suffix))
        suffix += 1
    entries[name + "/" + notice] = ("LICENSE", files["LICENSE"], (modes or {}).get("LICENSE", 0o644), True)
    return entries


def _tar_gz(entries: dict[str, tuple[str, bytes, int, bool]]) -> bytes:
    stream = io.BytesIO()
    with gzip.GzipFile(fileobj=stream, filename="", mode="wb", compresslevel=9, mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
            for path, (_, data, mode, _) in sorted(entries.items()):
                entry = tarfile.TarInfo(safe_name(path))
                entry.size = len(data)
                entry.mtime = 0
                entry.mode = mode
                archive.addfile(entry, io.BytesIO(data))
    return stream.getvalue()


def skill_archive(
    name: str, files: dict[str, bytes], *, source_path: str | None = None, modes: dict[str, int] | None = None
) -> bytes:
    """Compose complete canonical files plus the exact original-work license notice."""
    return _tar_gz(_skill_archive_entries(name, files, source_path=source_path, modes=modes))


def build_files(source_ref: str = "HEAD", *, repo: Path = REPO) -> dict[str, bytes]:
    """Read bytes and metadata only from the single commit resolved by source_ref."""
    if not isinstance(source_ref, str) or not source_ref or any(ord(char) < 32 for char in source_ref):
        raise ValueError("A nonempty source ref is required")
    commit = git("rev-parse", "--verify", "--end-of-options", source_ref + "^{commit}", repo=repo).decode().strip()
    tree = git("rev-parse", commit + "^{tree}", repo=repo).decode().strip()
    timestamp = int(git("show", "-s", "--format=%ct", commit, repo=repo).strip())
    files: dict[str, bytes] = {}
    origins, modes = {}, {}
    for entry in git("ls-tree", "-r", "-z", "--full-tree", commit, repo=repo).split(b"\0"):
        if not entry:
            continue
        metadata, encoded_path = entry.split(b"\t", 1)
        mode, kind, sha = metadata.decode("ascii").split()
        try:
            path = safe_name(encoded_path.decode("utf-8"))
        except UnicodeDecodeError as exc:
            raise ValueError("Source paths must be portable UTF-8") from exc
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise ValueError(f"Unsupported source entry (symlink or submodule): {path}")
        if path.split("/", 1)[0] in EXCLUDED_ROOTS:
            continue
        if path in GENERATED_FILES:
            raise ValueError(f"Source collides with generated metadata: {path}")
        data = git("cat-file", "blob", sha, repo=repo)
        privacy_check(path, data)
        files[path] = data
        modes[path] = int(mode, 8) & 0o777
        origins[path] = {
            "source_git_blob": sha,
            "source_mode": mode,
            "source_sha256": digest(data),
            "bundled_sha256": digest(data),
        }
    catalog = _catalog(files)
    try:
        guidance_version = files["VERSION"].decode("utf-8").strip()
        guidance_catalog = json.loads(files["guidance/catalog.json"])
    except (KeyError, UnicodeDecodeError, ValueError) as exc:
        raise ValueError("Snapshot has no valid guidance version/catalog") from exc
    if (
        not isinstance(guidance_catalog, dict)
        or not guidance_version
        or guidance_catalog.get("guidance_version") != guidance_version
    ):
        raise ValueError("Guidance VERSION and catalog version differ")
    snapshot_files = dict(files)
    skills = []
    for skill in catalog["skills"]:
        archive_path = "packages/" + skill["name"] + ".tar.gz"
        if archive_path in files:
            raise ValueError(f"Source collides with generated skill archive: {archive_path}")
        content = {path: {"sha256": digest(data), "bytes": len(data), "mode": origins[path]["source_mode"]}
                   for path, data in sorted(snapshot_files.items()) if path.startswith(skill["path"] + "/")}
        entries = _skill_archive_entries(skill["name"], snapshot_files, source_path=skill["path"], modes=modes)
        archive_files = {
            path: {"source_path": source_path, "sha256": digest(data), "bytes": len(data),
                   "mode": origins[source_path]["source_mode"], "packaging_addition": added}
            for path, (source_path, data, _, added) in sorted(entries.items())
        }
        additions = {
            path: {**metadata, "source_sha256": origins[metadata["source_path"]]["source_sha256"],
                   "reason": "Retain the original-work notice in standalone installations"}
            for path, metadata in archive_files.items() if metadata["packaging_addition"]
        }
        archive = _tar_gz(entries)
        files[archive_path] = archive
        skills.append({**skill, "archive": archive_path, "archive_sha256": digest(archive),
                       "archive_bytes": len(archive), "files": content, "archive_files": archive_files,
                       "packaging_additions": additions, "distribution_variant": "license-notice-added"})
    external = [{**method, "optional": True, "bundled": False,
                 "bundle_status": "Not bundled; requires its separate accepted source and installation"}
                for method in catalog.get("external_methods", [])]
    report = {
        "scope": "Artifact verification only; no recipient workspace accessed or installed",
        "source_commit": commit,
        "source_tree": tree,
        "source_files_verified": len(origins),
        "all_source_bytes_unchanged": True,
        "base_methods": len(skills),
        "unchanged_method_main_texts": len(skills),
        "skill_archives_with_original_work_notice": len(skills),
        "implicit_methods": sum(skill["allow_implicit_invocation"] for skill in skills),
        "explicit_only": [skill["name"] for skill in skills if not skill["allow_implicit_invocation"]],
        "documented_provenance_redactions": 0,
        "private_notion_page_links_in_text_payload": 0,
        "user_machine_paths_in_text_payload": 0,
        "external_methods_not_bundled": [method["name"] for method in external],
        "runtime_installation_test": "Not performed; requires the recipient's own workspace and accepted instructions",
    }
    files["VERIFICATIE.json"] = _json(report)
    exporter_bytes = Path(__file__).read_bytes()
    exporter_matches = snapshot_files.get("tools/export_workflow_starter.py") == exporter_bytes
    manifest = {
        "schema_version": 1,
        "package_id": "workflow-starter-" + commit[:12],
        "package_version": catalog["collection_version"] + "+git." + commit[:12],
        "prepared_date": datetime.fromtimestamp(timestamp, timezone.utc).date().isoformat(),
        "source_commit_timestamp": timestamp,
        "source_repository": catalog["source_repository"],
        "source_commit": commit,
        "source_tree": tree,
        "exporter_revision": commit if exporter_matches else None,
        "exporter_sha256": digest(exporter_bytes),
        "exporter_matches_source_snapshot": exporter_matches,
        "guidance_version": guidance_version,
        "skill_collection_version": catalog["collection_version"],
        "existing_guide_setup_policy": "Preserve accepted version; no automatic upgrade or downgrade",
        "privacy_variants": [],
        "excluded_source_roots": sorted(EXCLUDED_ROOTS),
        "source_files": origins,
        "skills": skills,
        "external_methods": external,
        "files": {name: {"sha256": digest(data), "bytes": len(data)} for name, data in sorted(files.items())},
    }
    files["BRONNEN.json"] = _json(manifest)
    return files


def write_zip(target: Path, files: dict[str, bytes]) -> None:
    """Write a deterministic archive, retaining tracked executable file modes."""
    for name in files:
        safe_name(name)
    origins = json.loads(files.get("BRONNEN.json", b"{}")).get("source_files", {})
    if any(metadata.get("source_mode") not in {"100644", "100755"} for metadata in origins.values()):
        raise ValueError("Only regular source files may be archived")
    target = Path(target)
    if target.is_symlink():
        raise ValueError("Archive output must not be a symlink")
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(files.items()):
            entry = zipfile.ZipInfo(ARCHIVE_ROOT + "/" + path, date_time=ZIP_EPOCH)
            entry.create_system = 3
            entry.compress_type = zipfile.ZIP_DEFLATED
            mode = int(origins.get(path, {}).get("source_mode", "100644"), 8)
            entry.external_attr = mode << 16
            archive.writestr(entry, data)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(files):
            raise ValueError("Archive roundtrip failed")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-ref", "--ref", help="Committed source snapshot (default: HEAD)")
    parser.add_argument("--repo", type=Path, default=REPO, help="Local source repository")
    parser.add_argument("--exporter-revision", help="Deprecated alias for --source-ref; cannot name a second revision")
    args = parser.parse_args(argv)
    if args.source_ref is not None and args.exporter_revision is not None and args.source_ref != args.exporter_revision:
        parser.error("--exporter-revision is a source-ref alias; conflicting revisions are not allowed")
    source_ref = args.source_ref if args.source_ref is not None else args.exporter_revision
    try:
        files = build_files("HEAD" if source_ref is None else source_ref, repo=args.repo)
        write_zip(args.output, files)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    manifest = json.loads(files["BRONNEN.json"])
    print(json.dumps({"output": str(args.output), "files": len(files), "bytes": args.output.stat().st_size,
                      "sha256": digest(args.output.read_bytes()), "methods": len(manifest["skills"]),
                      "source_commit": manifest["source_commit"], "source_tree": manifest["source_tree"],
                      "private_links": 0}))


if __name__ == "__main__":
    main()
