# Skill workflow

This document owns packaging and distribution of the base source collection declared in `skills/catalog.json`, plus its optional external integration contracts. Start at [INSTALL.md](../INSTALL.md) for a recipient installation. Files, supported native skill hosts and a recipient-chosen Notion workspace are separate adapters; none is universally required. Consumer workflows and the shared-guidance contract retain their existing authority.

## Sources and destinations

| Material | Canonical owner | Other locations |
| --- | --- | --- |
| Personal preferences and cross-project navigation | User's private operating guide and memory | Short pointer in the user's custom instructions |
| Product semantics, code and technical evidence | Existing project source owner | Links and dated summaries only |
| Plans, tasks, decisions and progress | Verified project-specific owner, including Notion when established | One owner per record; no parallel tracker |
| Cross-repository shared roles and playbooks | `guidance/` | Exact pinned vendored consumers |
| Installable engineering methods | `skills/<name>/` and `skills/catalog.json` here | Host personal-skill installations and private Notion Skill distributions |
| Context and documents without a repository owner | Existing private document/memory destinations | Avoid independently maintained copies |

For repository-owned skills, this Git repository is canonical; a host registry, durable file tree or the recipient's own Notion Skills are distributions. Keep the full package and accepted source pin. The catalog derives membership, package versions and invocation policy; historical counts are not installation criteria.

The `external_methods` entries are optional, unbundled integration contracts. Their recorded versions describe reviewed sources/adapters, not an installation in the recipient's account. Resolve a recipient's accepted package and local customizations before using or updating it. No private author's Notion adapter or asset library is needed for the base collection. The method router gives a base/public fallback for logo work and official web-platform references. Installation states and exact recipient locations belong in their private distribution record, not this catalog.

## Selecting a method

Start with the configured context route in [METHOD-ROUTING.md](METHOD-ROUTING.md), reusing this session's verified guide and fetching only the relevant standalone object or project/task context. The general [work cycle](../guidance/playbooks/work-cycle.md) owns execution and closure across result types. Skill availability does not prove that a host read the guide or applied the method.

- Substantive authorized feature or bug fix: [evidence-driven-development](../skills/evidence-driven-development/SKILL.md).
- Explicit instruction-system review or a recurring instruction defect: [maintain-agent-instructions](../skills/maintain-agent-instructions/SKILL.md).
- Planning, domain decisions, prototypes, review-only, durable resumption and guided learning: use the [method router](METHOD-ROUTING.md).
- Ordinary explanation or small editorial change: use repository instructions; do not initiate a development ceremony.
- Planning-only: retain the user's planning boundary. A skill never supplies implementation, merge, deployment or scheduling permission.

Packages permit implicit selection when their descriptions match, except grill-me which remains explicitly requested. Select supported agents only within current user/host authorization when useful or required by the method. No source package grants additional authority. Preserve scoped ownership and verify their integration. The host may cache its skill list. Being present in GitHub, installed, enabled and actually loaded are distinct states. If the same name is available from a personal installation and Notion, use one source for the task, not both. Check recorded revision/hash if they disagree; do not automatically prefer the more recently edited copy.

## Authoring and updating

1. Read the current source and exact reviewed upstream material. Keep one responsibility per package; use direct relative links for optional branches. Inspect all referenced files before import. Retain license and attribution for copied material.
2. Make a bounded source change. Use the host's mandated authoring workspace when needed, then copy the verified package to this canonical repository for review. Until publication it is a candidate, not a released source.
3. Run `python tools/check_skills.py`, foundation checks and the full unittest suite from a clean committed checkout. Every catalog method needs one route with a discriminating request and observable finish. The check rejects absent, duplicate and unknown primary routes, invalid conditional targets/triggers and undisclosed method dependencies; it does not prove semantic selection or actual invocation. Run the host's package validator in the actual installation workspace as well. The portable checker intentionally accepts only our simple two-field frontmatter format; it is not a general YAML parser or a security boundary.
4. Exercise a normal request, an excluded request and missing-input behavior. Use fresh-context tests for substantial changes where supported. Save concrete observations in the existing audit/work record, not a fabricated pass percentage.
5. Review requirements and implementation quality separately. Follow normal branch/PR checks. Publish the source before marking its installation as the current canonical release. Version a changed skill independently; keep shared `VERSION` unchanged when `guidance/` is unchanged.
6. Install each complete package through the host's supported workflow. Save exact source commit, package version and content hashes in the private distribution record. Verify the remote package after reconciliation; a local file is not installation proof.
7. If Notion is selected, create real Skills, including every supporting file. Enable and read them back where supported; report unsupported settings separately. A plain document or database row is not a skill installation. Use the same package bytes; place installation provenance in the distribution record rather than modifying the packaged method separately.

An upstream update is a candidate for review, never a silent replacement. When the user has granted bounded automatic maintenance, follow the selected instruction-feedback-loop for a compared, reviewed and recoverable activation. The existing source/package/distribution checks still apply; record the grant reference and use the learning evidence checker before promotion. Check actual catalog coverage and prefer repairing an existing route or skill over duplicating one. Preserve user changes, compare to the last imported version and resolve material conflicts. Stop only the blocked operation if tools or sources are unavailable; report the actual limitation. Do not broaden scheduled maintenance to GitHub or skill upgrades without a separate schedule authorization.

Establish the distribution scope before comparing or changing destinations. A targeted update compares, updates and verifies only the involved packages and distributions; it does not imply a complete catalog reconciliation or a cleanup of unrelated skills. Missing access to the complete catalog limits catalog-wide claims, but need not block an independently verifiable targeted update.

A complete catalog reconciliation is a separately scoped installation, migration or explicitly requested reconciliation operation under existing authority. For that operation, reconcile the complete active Notion Skills database against the local packages and only the recipient-accepted external methods for that destination, not only the enabled list. Reuse existing member pages, import complete packages and enable matching automatic/connected-agent settings. If complete catalog access is unavailable, leave reconciliation incomplete and report the uncovered state; do not infer membership from a partial list.

Within a complete reconciliation, disable or archive an identified non-member only when its retirement is in scope and covered by existing authority, preserving recoverable source history and unrelated content. A targeted update does not authorize deleting, archiving or disabling unrelated or third-party skills. Provider originals remain outside the active catalog; removing their apps requires an explicit removal request.

Before replacing a Notion package, retain its current attachment Folder IDs; after import compare the live `Bestanden` references and exported package. If superseded native Folders remain searchable, preserve their IDs/files and mark them historical only after proving they are outside the current package; never infer missing backlinks from an unsupported API. A metadata-only change can alter the host's export version ID: recheck the affected full exports, record the new IDs and keep prior provenance without bumping the unchanged package version.

Readback must account for host serialization: Notion exports may add a page ID and use block-style YAML scalars; personal-skill hosts may regenerate UI metadata and icons. Compare method bodies, parsed name/description and supporting references against the canonical package, and record host-owned differences separately. Put literal filenames in inline code so rich-text imports do not turn them into unintended web links.

## Verification limits

File checks detect structural drift, missing dependencies and invocation mismatch. Behavioral trials cover their specific cases. Neither guarantees future reasoning or correct use in every host. Keep post-installation failures as evidence for the existing instruction feedback loop.
