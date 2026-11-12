# Agent Guidance repository instructions

Read `guidance/KERNEL.md`, then `docs/WORKFLOW.md`. For changes to vendoring/versioning also read `docs/CONSUMER-CONTRACT.md`.

For skill packages, installation copies or cross-host routing, read `docs/SKILL-WORKFLOW.md`. The packages under `skills/` are task-scoped methods; they do not replace consumer instructions or silently change pinned guidance.

This repository is the canonical owner only for repository-independent AI guidance. Never pull product semantics, repository workflow scenarios, roadmaps, architecture invariants, or consumer-specific rules into shared modules merely to reduce duplication.

A shared guidance change is a behavioral API change for consumers. Keep one normative owner, preserve module IDs unless a deliberate migration says otherwise, assess consumer impact, and prefer simplification over adding overlapping guidance.

Shared files under `guidance/` must remain repository-neutral. Consumer overlays belong in the consumer repository.

Use one bounded objective per batch. Do not migrate consumers while changing the canonical foundation unless that migration is the explicit batch objective.

When real work exposes reusable instruction-system friction, a user correction that may generalise, or a missing/stale/misrouted rule whose repair is outside the active scope, load `guidance/playbooks/instruction-feedback-loop.md`. Use it to preserve evidence and identify the true owner, not to expand the current task.

