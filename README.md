# Agent Guidance

Canonical, repository-independent guidance for AI-assisted product and engineering work across repositories.

This repository owns only guidance that is genuinely reusable across consumers. Product semantics, architecture, workflow scenarios, roadmaps, release rules, and domain-specific expertise stay in their natural repositories.

## Consumer model

Each consumer repository keeps a small local `AGENTS.md` that:

1. loads the vendored `docs/agent/shared/KERNEL.md` on every task;
2. points to its own repository workflow and source-of-truth documents;
3. routes only materially relevant shared roles/playbooks;
4. routes repository-specific roles/playbooks kept outside the shared vendor directory.

Shared guidance is **vendored, not remotely imported at runtime**. Consumers pin an exact canonical commit and optional human-readable version in `.agent-guidance.lock.json`. The vendored files and verifier are byte-hashed. Updating guidance is an explicit consumer repository change/PR.

## Canonical source

- `guidance/KERNEL.md` — small always-on cross-repository behavior.
- `guidance/EXPERT-OPERATING-MODEL.md` — senior multidisciplinary decision behavior for substantive work.
- `guidance/roles/` — reusable decision lenses.
- `guidance/playbooks/` — reusable situation procedures.
- `guidance/catalog.json` — machine-readable module catalog and guidance version.
- `schemas/consumer-lock.schema.json` — consumer pin/lock contract.
- `tools/vendor_guidance.py` — deterministic vendoring from an exact local canonical checkout.
- `tools/verify_consumer.py` — local hash/drift verification with no network dependency.

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

## Bootstrap

The first durable commit should be tagged `v0.1.0` after foundation verification. Consumer migration happens in separate repository-specific batches.
