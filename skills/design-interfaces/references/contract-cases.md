# Contract cases

Use these questions only for the boundary being changed.

| Case | Establish |
| --- | --- |
| Successful call | Required/optional fields, units, identity, output and side effects |
| Invalid or unauthorized call | Rejection point, error form, unchanged state and information exposed |
| Partial update | Whether absence differs from null, default or deletion |
| Retry after timeout | How to discover applied, rejected and unknown outcomes |
| Duplicate intent | Stable intent identity and what a concurrent duplicate receives |
| Format or version change | Existing consumers, upgrade path and old-reader/new-writer behavior |
| Large or interrupted operation | Limits, cancellation, partial effects and recovery |

For a retryable mutation, distinguish one intent from each attempt. If an idempotency key is promised, describe its scope, payload consistency, atomic ownership, in-flight response, result retention and recovery of unknown outcomes. A check followed by an effect is not atomic merely because both calls succeed in a simple test. Verify the chosen storage/runtime can enforce the promise; do not prescribe a database to a file-based application without an accepted architecture decision.

Prefer a small interface that hides coordination callers need not repeat. Preserve observable behavior consumers actually rely on or plan its migration explicitly. Domain meaning and product acceptance remain at their existing owners.
