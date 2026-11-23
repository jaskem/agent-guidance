# Agent Guidance workflow

## Source of truth

1. Current user instruction and explicitly named checkpoint constraints.
2. `AGENTS.md`, this workflow, and `docs/CONSUMER-CONTRACT.md` when the consumer contract is affected.
3. `guidance/catalog.json`, shared source files, schemas, tools, and tests on the exact repository head.
4. Durable checkpoints and exact repository delta.
5. Conversation memory only as orientation.

## Bounded scenarios

- **F0 — guidance design:** change shared behavior/role/playbook semantics. Verify repository-neutrality, ownership, overlap, and module catalog consistency.
- **F1 — consumer contract/tooling:** change lock schema, vendoring, verification, or versioning. Run foundation checks and focused tooling tests.
- **F2 — foundation/repository process:** change this repository's own workflow/CI/maintenance docs. Verify only affected process guarantees.
- **F3 — release/version:** bump guidance version/tag after prior change evidence is complete; do not mix unrelated guidance changes into release closure.

Use the union when scenarios overlap; do not duplicate checks.

## Shared-guidance change discipline

- A module must be repository-independent and have one clear responsibility.
- Add/split a role only when it has a recurring, materially distinct decision model.
- Add a playbook only for a recurring situation that is not a discipline.
- Prefer references to the canonical owner over repeated normative rules.
- Treat renamed/removed module IDs, lock-schema changes, or changed mandatory behavior as migration-impacting.
- Do not edit consumer vendored copies here; the canonical source lives under `guidance/`.

## Verification

For F0/F1 run:

```text
python tools/check_foundation.py
python -m unittest discover -s tests -v
```

The checks prove structure, catalog/version consistency, repository-neutral shared guidance, deterministic lock generation, and local drift detection. They do not prove consumer-specific routing; that belongs to each migration batch.

## Authorized continuous improvement

Use the existing instruction-feedback-loop for scheduled or event-driven maintenance within the configured standing grant. Validate the candidate evidence record with `python tools/check_learning_change.py <record.json>` before automatic activation and inspect its references. The checker is preflight, not a permission or truth oracle. Its tests run in the existing unittest job. Preserve source/distribution rollback references and distinguish a registered schedule from executed improvement.

## Checkpoint

For entrypoint, installer, recipient templates or external-method routing changes, run `python tools/check_portability.py` as well. Keep recipient account data and machine paths out of public sources; required legal/source attribution is retained. Follow [INSTALL.md](../INSTALL.md) for installation requests rather than editing a user's environment as a side effect of source maintenance. Match current versions and counts to the selected snapshot.

For changes under `skills/`, its catalog or package tooling, also run `python tools/check_skills.py` and the tests above. Follow `docs/SKILL-WORKFLOW.md` for behavior trials and distribution. These packages have their own versions; shared-guidance `VERSION` changes only when shared guidance changes.

Record exact head, changed files, scenario, checks actually run, compatibility/migration impact, what was not done, and exactly one next technical step.

