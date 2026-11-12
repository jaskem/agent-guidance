# Agent Guidance repository instructions

## Configured user context

At the start of a new session, read the user's [Agent Operating Guide](https://app.notion.com/p/416f70dd64e68144b5e7cb3f75f1edf3) once and use its active `instructions_version` for Notion calls. Follow its [project index](https://app.notion.com/p/416f70dd64e681b385caefbc93c2c65d) to the relevant project/task owner. Reuse verified context within the session; refresh the affected source on task/project changes, material new evidence or uncertain writes. The current user instruction takes precedence. If Notion is unavailable, disclose the missing context and continue only independent supported work, without inventing current task state or claiming the guide was read.

Read `guidance/playbooks/context-entry.md` for this route. For useful authorized delegation, read `guidance/playbooks/delegation.md`; give workers bounded ownership and verify the combined result. Neither route changes product ownership or creates background agents.

## Repository route

Read `guidance/KERNEL.md`, then `docs/WORKFLOW.md`. For changes to vendoring/versioning also read `docs/CONSUMER-CONTRACT.md`.

For skill packages, installation copies or cross-host routing, read `docs/SKILL-WORKFLOW.md`. The packages under `skills/` are task-scoped methods; they do not replace consumer instructions or silently change pinned guidance.

This repository is the canonical owner only for repository-independent AI guidance. Never pull product semantics, repository workflow scenarios, roadmaps, architecture invariants, or consumer-specific rules into shared modules merely to reduce duplication.

A shared guidance change is a behavioral API change for consumers. Keep one normative owner, preserve module IDs unless a deliberate migration says otherwise, assess consumer impact, and prefer simplification over adding overlapping guidance.

Shared files under `guidance/` must remain repository-neutral. Consumer overlays belong in the consumer repository.

Use one bounded objective per batch. Do not migrate consumers while changing the canonical foundation unless that migration is the explicit batch objective.

When real work exposes reusable instruction-system friction, a user correction that may generalise, or a missing/stale/misrouted rule whose repair is outside the active scope, load `guidance/playbooks/instruction-feedback-loop.md`. Use it to preserve evidence and identify the true owner, not to expand the current task.

