#!/usr/bin/env python3
"""Legacy entrypoint for the portable workflow export; Notion is an optional adapter."""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "export_workflow_starter", Path(__file__).with_name("export_workflow_starter.py")
)
_CORE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_CORE)

REPO = _CORE.REPO
digest = _CORE.digest
privacy_check = _CORE.privacy_check
safe_name = _CORE.safe_name
skill_archive = _CORE.skill_archive
write_zip = _CORE.write_zip
main = _CORE.main


def build_files(
    exporter_revision: str | None = None, *, source_ref: str | None = None, repo: Path = REPO
) -> dict[str, bytes]:
    """The deprecated positional revision selects the same snapshot as source_ref."""
    if exporter_revision is not None and source_ref is not None and exporter_revision != source_ref:
        raise ValueError("exporter_revision is a source-ref alias; conflicting revisions are not allowed")
    selected = source_ref if source_ref is not None else exporter_revision
    return _CORE.build_files("HEAD" if selected is None else selected, repo=repo)


if __name__ == "__main__":
    main()
