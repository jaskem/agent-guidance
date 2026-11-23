# Agent Guidance repository instructions

## Choose the entry route

This is a reusable source repository, not a configured personal workspace. It contains no recipient account, operating-guide URL or standing permission to install anything.

- **Install, adopt or connect this workflow:** read [INSTALL.md](INSTALL.md) and follow its implementation route before creating or changing the user's setup. This includes an existing workspace and repository consumers. Installation is a procedure, not a new task-method package.
- **Explain or inspect:** answer the request from the relevant source. Reading this repository alone does not authorize installation, account changes or a workspace scan.
- **Maintain this repository:** follow the repository route below. An installation request is not permission to edit or publish this canonical source.

## Configured user context

Use the current user's operating guide only when its location is supplied through their instructions or their own local configuration. Read it once per session and use its accepted `instructions_version` for Notion calls. Do not search for or fall back to the repository author's private workspace. If no guide is configured, an installation request follows `INSTALL.md`; ordinary work continues from the current request and applicable repository instructions.

Follow an existing guide's accepted context links to the relevant work object or project/task owner; do not copy its subordinate locations into this entrypoint. Reuse verified context and refresh only affected sources. The current user instruction takes precedence; new setup instructions require the user's approval. If a configured guide is unavailable, disclose the missing context and continue independent supported work without inventing instructions or current task state. Keep personal settings and permissions outside the public source.

Read `guidance/playbooks/context-entry.md` for this route. For useful authorized delegation, read `guidance/playbooks/delegation.md`; give workers bounded ownership and verify the combined result. Neither route changes product ownership or creates background agents.

## Repository route

Read `guidance/KERNEL.md` and `guidance/playbooks/work-cycle.md` for the general work route, then `docs/WORKFLOW.md` for this repository's requirements. For changes to vendoring/versioning also read `docs/CONSUMER-CONTRACT.md`.

For skill packages, installation copies or cross-host routing, read `docs/SKILL-WORKFLOW.md`. The packages under `skills/` are task-scoped methods; they do not replace consumer instructions or silently change pinned guidance.

This repository is the canonical owner only for repository-independent AI guidance. Never pull product semantics, repository workflow scenarios, roadmaps, architecture invariants, or consumer-specific rules into shared modules merely to reduce duplication.

A shared guidance change is a behavioral API change for consumers. Keep one normative owner, preserve module IDs unless a deliberate migration says otherwise, assess consumer impact, and prefer simplification over adding overlapping guidance.

Shared files under `guidance/` must remain repository-neutral. Consumer overlays belong in the consumer repository.

Use one bounded objective per batch. Do not migrate consumers while changing the canonical foundation unless that migration is the explicit batch objective.

When real work exposes reusable instruction-system friction, a user correction that may generalise, or a missing/stale/misrouted rule whose repair is outside the active scope, load `guidance/playbooks/instruction-feedback-loop.md`. Use it to preserve evidence and identify the true owner, not to expand the current task.

