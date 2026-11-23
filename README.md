# Agent Guidance

Canonical, repository-independent guidance for AI-assisted product and engineering work across repositories.

This repository owns only guidance that is genuinely reusable across consumers. Product semantics, architecture, workflow scenarios, roadmaps, release rules, and domain-specific expertise stay in their natural repositories.

## Install for your own environment

Ask an AI agent with access to this repository:

> Install this workflow in my own environment. Follow INSTALL.md, inspect the relevant existing setup, preserve my content and settings, and complete and verify the authorized installation. Ask only for missing destination or scope decisions.

Agents start at [AGENTS.md](AGENTS.md), which routes installation requests to [INSTALL.md](INSTALL.md). Choose durable files/Git, your own Notion workspace, a supported native skill host, or a repository consumer. Notion, a paid service and access to the author's accounts are not requirements. The installer reconciles existing owners and local changes; it does not import someone else's context or permissions.

The [catalog](skills/catalog.json) supplies the complete current base collection and invocation settings. Optional external methods require their own accessible, reviewed installation. A read-only explanation does not install anything. [MIT](LICENSE) permits reuse of original repository material; retained [third-party notices](docs/THIRD-PARTY-NOTICES.md) continue to apply.

## Consumer model

Each consumer repository keeps a small local `AGENTS.md` that:

1. loads the vendored `docs/agent/shared/KERNEL.md` on every task;
2. points to its own repository workflow and source-of-truth documents;
3. routes only materially relevant shared roles/playbooks;
4. routes repository-specific roles/playbooks kept outside the shared vendor directory.

Shared guidance is **vendored, not remotely imported at runtime**. Consumers pin an exact canonical commit and optional human-readable version in `.agent-guidance.lock.json`. The vendored files and verifier are byte-hashed. Updating guidance is an explicit consumer repository change/PR.

## Installable skills

Use the [single coherent skillset](docs/SKILLSET.md) and [method router](docs/METHOD-ROUTING.md) to select the catalogued task-scoped procedures or the appropriate host capability. The [catalog](skills/catalog.json) owns names, package versions, invocation policy and required dependencies. The [general work cycle](guidance/playbooks/work-cycle.md) connects context, authorized execution, result-specific evidence and closure. Specialist methods cover quality constraints, lasting instrumentation, migrations, CI/CD, image art direction and designed visual narratives; the UI methods retain UI ownership.

The set integrates useful techniques from the reviewed provider repositories into the actual packages. Their [source coverage](skills/source-coverage.json) retains the original review entries; [provider consolidation](docs/OPTIONAL-SKILL-SUITES.md) explains compatibility. It does not create a second mandatory lifecycle.

Follow the [skill workflow](docs/SKILL-WORKFLOW.md) for complete package installation, validation and readback in the chosen host. Use supported agents only within the current user's and host's authority when useful for independent work or verification, preserving one writer per object and parent integration. Shared guidance and consumer pins remain independent of package versions.

The further [design/workflow integration](docs/DESIGN-WORKFLOW-INTEGRATION-2026-11-20.md) adds reusable brand systems and interactive motion, targeted improvements to existing methods, early useful delegation and explicit visual-runtime selection. The catalog declares conditional method routes and the separately managed logo-design extension. Structural CI checks detect missing/disclosed routes; they do not guarantee host invocation.

## Controlled continuous improvement

The [instruction feedback loop](guidance/playbooks/instruction-feedback-loop.md) handles real reusable failures and explicitly authorized periodic maintenance through one owner: capture, diagnose, candidate, compare, review, bounded activation and verified recovery. The [implementation record](docs/LEARNING-WORKFLOW-2026-11-21.md) explains the evidence checker and limits. A maintenance grant does not enlarge itself, override consumer pins or turn an upstream discovery into a trusted installation.

## Shared source

- `guidance/KERNEL.md` — small always-on cross-repository senior-collaborator behavior.
- `guidance/EXPERT-OPERATING-MODEL.md` — deprecated compatibility module; it adds no behavior beyond the kernel and remains temporarily for explicit consumer migration.
- `guidance/roles/` — reusable decision lenses.
- `guidance/playbooks/` — reusable situation procedures.
- `guidance/resources/` — four optional, problem-oriented advisory references and a small index; selected explicitly, read only when relevant.
- `guidance/catalog.json` — machine-readable module catalog and guidance version.
- `schemas/consumer-lock.schema.json` — consumer pin/lock contract.
- `tools/vendor_guidance.py` — deterministic vendoring from an exact local canonical checkout.
- `tools/verify_consumer.py` — local hash/drift verification with no network dependency.

## Optional reference selection

The [resource index](guidance/resources/index.md) maps concrete questions to existing roles and optional catalog modules (`kind: reference`). Resources are not skills to install or a second workflow. Consumers may select individual references using the existing `--module` option; selecting a role does not add dependencies. The index is optional too. Vendoring makes content locally available, not automatically active. Missing optional references do not block ordinary work or cause remote imports.

The four topics are Playwright diagnosis, uncertain writes/recovery, product/UX assumptions, and CI efficiency. Source links record reviewed upstream commits; the pages contain original synthesis and examples, not mirrored external skill packages. Their practical benefit remains to be evaluated through normal work. Release and explicit consumer migration are separate from this canonical change.

## Non-goals

This repository does not own:

- a consumer repository's source-of-truth order;
- repository-specific workflow/scenario matrices;
- product/domain architecture or invariants;
- roadmap/checkpoint state;
- product-specific terminology or acceptance criteria;
- consumer-specific specialist roles.

## Versioning

`VERSION` and `guidance/catalog.json` carry the guidance version. Consumers always pin the exact 40-character commit SHA; tags/versions are descriptive and review-friendly, never substitutes for the commit pin.

- Patch: editorial clarification with no intended behavioral/routing change.
- Minor: backward-compatible new optional modules or materially improved guidance.
- Major: incompatible module/lock contract changes or changes that consumers must deliberately adapt to.

During `0.x`, any materially behavioral change should be treated as migration-worthy even when represented by a minor bump.


