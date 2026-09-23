# Change closure & hygiene playbook

Load this for repository-changing batches. It governs residue caused or exposed by the active change; it is not permission for broad cleanup.

## Closure principle
A change is not complete if the change itself leaves the touched surface misleading, temporary, duplicated, dead, contradictory, or harder to understand without necessity.

## Inspect the touched surface for
- stale or contradictory current-state documentation;
- temporary/debug/experimental paths introduced by the batch;
- dead/unreachable code made obsolete by the change;
- duplication created by the change;
- unused imports/exports/dependencies/configuration;
- obsolete tests, fixtures, examples, or screenshots;
- generated artifacts out of sync with their source;
- TODO/FIXME/HACK markers created by the batch;
- naming/control flow that obscures the new responsibility;
- roadmap/checkpoint text made false by the change.

## Rules
- Fix change-induced residue inside the same batch when needed for a coherent result.
- Do not turn unrelated pre-existing debt into hidden scope.
- A materially important deferred item needs a real reason and durable destination/trigger.
- Do not add a file when an existing owner is clearer; remove a file when its responsibility disappears.
- Comments explain why/invariants/constraints, not obvious narration.
- Dependencies must earn lifecycle cost.
- Tests protect changed behavior or important invariants; do not add volume for its own sake.
- Generated outputs need a deterministic source/regeneration path.

## Final closure question
Could another capable engineer understand the changed responsibility and current state without discovering temporary leftovers or conflicting instructions? If not, closure is incomplete.
