# Consumer contract

## Goal

A consumer must get stable local instructions without runtime dependence on another repository, while shared guidance retains one canonical owner.

## Required consumer surfaces

A migrated consumer has:

- a local `AGENTS.md` that always loads the vendored shared `KERNEL.md` and owns repo-specific routing;
- its own repository workflow and product/architecture sources of truth;
- `.agent-guidance.lock.json` at repository root;
- shared files under a dedicated destination such as `docs/agent/shared/`;
- `tools/verify_agent_guidance.py`, vendored from this repository;
- repository-local overlays outside the shared destination.

## Pinning

The lock must contain:

- `schema_version`;
- canonical `repository`;
- exact lowercase 40-character `commit` SHA;
- optional human-readable `version`/tag;
- destination root;
- selected module IDs, canonical source paths, consumer destination paths, and SHA-256 hashes;
- vendored verifier path/hash.

The commit pin is authoritative. A tag alone is never sufficient.

## Vendoring

Vendoring runs from a **local checkout of the canonical repository at the exact pinned commit**. The canonical checkout must be clean. `tools/vendor_guidance.py` refuses to vendor if HEAD differs from the requested pin.

The tool copies selected module bytes without rewriting them, writes a deterministic lock (sorted keys/modules and final newline), and vendors the verifier. The shared destination is dedicated to generated canonical files; consumer-specific guidance must live elsewhere.

## Drift verification

`tools/verify_agent_guidance.py` runs entirely from the consumer repository. It:

- validates lock shape and exact commit syntax;
- verifies every listed vendored file hash;
- verifies the vendored verifier's own pinned hash;
- rejects duplicate/unsafe destinations;
- rejects unexpected files under the dedicated shared destination.

This is drift/integrity checking, not a security boundary: a deliberate lock+file change is visible repository change and must be reviewed normally.

## Guidance consumption observability

Vendored or catalogued guidance is available guidance, not automatically active guidance.

For substantive work, a consumer must:

- resolve the relevant shared route before relying on specialist guidance;
- load only the selected roles and playbooks whose omission could materially alter the outcome into the current working context;
- avoid treating a module as active merely because it is vendored, listed, or mentioned in historical checkpoint evidence;
- record, in the consumer's existing durable batch record or checkpoint, only the shared modules actually consumed and any material route expansion.

The always-on senior-collaborator behavior is owned by `KERNEL.md`; it must not depend on a separately routed expert model. The retained `expert-operating-model` module is a compatibility module only and adds no behavior beyond the kernel. Consumers should remove it from their selected modules when they explicitly migrate to a canonical commit with this kernel ownership.

This requires no lock-schema change and no separate telemetry system. The durable record is evidence that guidance was reached and made available to the decision process; it is not proof that the guidance was interpreted or applied correctly.

## Update flow

1. Review/merge canonical guidance change.
2. Create a canonical version/tag when appropriate.
3. In one consumer migration/update batch, checkout the exact canonical commit.
4. Run vendoring for that consumer's explicit module selection.
5. Update local routing only where needed.
6. Run local drift verification plus consumer-specific process checks.
7. Review/merge as an explicit consumer PR.

No consumer changes silently when canonical `main` moves.

## Ownership test

Before adding a rule to shared guidance ask: would this still be correct in an unrelated product/runtime repository? If not, it belongs in a consumer overlay or product source of truth.
