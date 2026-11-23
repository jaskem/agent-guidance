#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from export_workflow_starter import privacy_check

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    "VERSION",
    "docs/WORKFLOW.md",
    "docs/CONSUMER-CONTRACT.md",
    "guidance/KERNEL.md",
    "guidance/EXPERT-OPERATING-MODEL.md",
    "guidance/catalog.json",
    "schemas/consumer-lock.schema.json",
    "tools/vendor_guidance.py",
    "tools/verify_consumer.py",
]
# Detect concrete private dependencies and consumer workflow filenames without
# publishing a particular recipient's project inventory as a denylist.
CONSUMER_WORKFLOW_PATH = re.compile(r"\bdocs/[A-Za-z0-9_-]+-WORKFLOW\.md\b")



def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"missing required file: {rel}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
catalog = json.loads((ROOT / "guidance/catalog.json").read_text(encoding="utf-8"))
if catalog.get("schema_version") != 1:
    fail("catalog schema_version must be 1")
if catalog.get("guidance_version") != version:
    fail("VERSION and catalog guidance_version differ")
if catalog.get("source_repository") != "jaskem/agent-guidance":
    fail("catalog source_repository must be jaskem/agent-guidance")

modules = catalog.get("modules")
if not isinstance(modules, list) or not modules:
    fail("catalog modules must be a non-empty array")
ids = set()
paths = set()
for item in modules:
    if not isinstance(item, dict):
        fail("catalog module entry must be an object")
    module_id = item.get("id")
    path = item.get("path")
    kind = item.get("kind")
    if not all(isinstance(x, str) and x for x in (module_id, path, kind)):
        fail(f"invalid catalog module entry: {item}")
    if module_id in ids:
        fail(f"duplicate module id: {module_id}")
    if path in paths:
        fail(f"duplicate module path: {path}")
    ids.add(module_id); paths.add(path)
    source = ROOT / path
    if not source.is_file():
        fail(f"catalog module file missing: {path}")

shared_markdown = {
    p.relative_to(ROOT).as_posix()
    for p in (ROOT / "guidance").rglob("*.md")
}
if shared_markdown != paths:
    fail(
        "catalog/shared markdown mismatch: "
        + f"unlisted={sorted(shared_markdown - paths)} missing={sorted(paths - shared_markdown)}"
    )

for rel in sorted(shared_markdown):
    text = (ROOT / rel).read_text(encoding="utf-8")
    try:
        privacy_check(rel, text.encode("utf-8"))
    except ValueError as exc:
        fail(str(exc))
    if CONSUMER_WORKFLOW_PATH.search(text):
        fail(f"consumer-specific workflow path found in shared module {rel}")

# Semantic repository neutrality still requires the ownership review in AGENTS.md;
# a finite vocabulary blacklist cannot prove that an arbitrary rule is reusable.

schema = json.loads((ROOT / "schemas/consumer-lock.schema.json").read_text(encoding="utf-8"))
required = set(schema.get("required", []))
if required != {"schema_version", "source", "destination_root", "modules", "verifier"}:
    fail("consumer lock schema top-level required fields changed unexpectedly")

print(f"foundation OK: version {version}, {len(modules)} shared modules")
