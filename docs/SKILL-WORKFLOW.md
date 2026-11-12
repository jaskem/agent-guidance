# Skill workflow

This document owns packaging and distribution of this repository's optional skills. Consumer workflows and the shared-guidance contract retain their existing authority.

## Sources and destinations

| Material | Canonical owner | Other locations |
| --- | --- | --- |
| Personal preferences and cross-project navigation | User's private operating guide and memory | Short pointer in the user's custom instructions |
| Product semantics, code, acceptance and repository work state | Existing consumer repository owner | Links and dated summaries only |
| Cross-repository shared roles and playbooks | `guidance/` | Exact pinned vendored consumers |
| Installable engineering methods | `skills/<name>/` and `skills/catalog.json` here | Host personal-skill installations and private Notion Skill distributions |
| Context and documents without a repository owner | Existing private document/memory destinations | Avoid independently maintained copies |

For these two repository-owned skills, GitHub is the source and Notion is a distribution. This exception prevents a second editable master. A separate personal skill can have Notion as its owner; record that choice before creating copies.

## Selecting a method

- Substantive authorized feature, bug fix or implementation review: [evidence-driven-development](../skills/evidence-driven-development/SKILL.md).
- Explicit instruction-system review or a recurring instruction defect: [maintain-agent-instructions](../skills/maintain-agent-instructions/SKILL.md).
- Ordinary explanation or small editorial change: use repository instructions; do not initiate a development ceremony.
- Planning-only: retain the user's planning boundary. A skill never supplies implementation, merge, deployment or scheduling permission.

Both packages permit implicit selection when their descriptions match. The host may cache its skill list. Being present in GitHub, installed, enabled and actually loaded are distinct states. If the same name is available from a personal installation and Notion, use one source for the task, not both. Check recorded revision/hash if they disagree; do not automatically prefer the more recently edited copy.

## Authoring and updating

1. Read the current source and exact reviewed upstream material. Keep one responsibility per package; use direct relative links for optional branches. Inspect all referenced files before import. Retain license and attribution for copied material.
2. Make a bounded source change. Use the host's mandated authoring workspace when needed, then copy the verified package to this canonical repository for review. Until publication it is a candidate, not a released source.
3. Run `python tools/check_skills.py`, foundation checks and the full unittest suite from a clean committed checkout. Run the host's package validator in the actual installation workspace as well. The portable checker intentionally accepts only our simple two-field frontmatter format; it is not a general YAML parser or a security boundary.
4. Exercise a normal request, an excluded request and missing-input behavior. Use fresh-context tests for substantial changes where supported. Save concrete observations in the existing audit/work record, not a fabricated pass percentage.
5. Review requirements and implementation quality separately. Follow normal branch/PR checks. Publish the source before marking its installation as the current canonical release. Version a changed skill independently; keep shared `VERSION` unchanged when `guidance/` is unchanged.
6. Install each complete package through the host's supported workflow. Save exact source commit, package version and content hashes in the private distribution record. Verify the remote package after reconciliation; a local file is not installation proof.
7. For Notion, create real Skills, including every supporting file. Enable and read back them. A plain document or database row is not a skill installation. Use the same package bytes; place installation provenance in the distribution record rather than modifying the packaged method separately.

An upstream update is a candidate for review, never a silent replacement. Preserve user changes, compare to the last imported version and resolve material conflicts. Stop only the blocked operation if tools or sources are unavailable; report the actual limitation. Do not broaden scheduled maintenance to GitHub or skill upgrades without a separate schedule authorization.

Readback must account for host serialization: Notion exports may add a page ID and use block-style YAML scalars; personal-skill hosts may regenerate UI metadata and icons. Compare method bodies, parsed name/description and supporting references against the canonical package, and record host-owned differences separately. Put literal filenames in inline code so rich-text imports do not turn them into unintended web links.

## Verification limits

File checks detect structural drift, missing dependencies and invocation mismatch. Behavioral trials cover their specific cases. Neither guarantees future reasoning or correct use in every host. Keep post-installation failures as evidence for the existing instruction feedback loop.
