# Agent Guidance repository instructions

Read `guidance/KERNEL.md`, then `docs/WORKFLOW.md`. For changes to vendoring/versioning also read `docs/CONSUMER-CONTRACT.md`.

This repository is the canonical owner only for repository-independent AI guidance. Never pull product semantics, repository workflow scenarios, roadmaps, architecture invariants, or consumer-specific rules into shared modules merely to reduce duplication.

A shared guidance change is a behavioral API change for consumers. Keep one normative owner, preserve module IDs unless a deliberate migration says otherwise, assess consumer impact, and prefer simplification over adding overlapping guidance.

Shared files under `guidance/` must remain repository-neutral. Consumer overlays belong in the consumer repository.

Use one bounded objective per batch. Do not migrate consumers while changing the canonical foundation unless that migration is the explicit batch objective.
