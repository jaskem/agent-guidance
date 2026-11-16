# Quality rules and control evidence

Reuse equivalent fields in the existing source of truth. Keep the normative requirement there and link its implementation; do not maintain competing copies of a checklist.

| Record | Include |
| --- | --- |
| Requirement | ID, applicable surface, desired invariant or metric, rationale and accepted/proposed status |
| Measurement | Input and environment, baseline identity, units, variation and comparison method |
| Control | Actual command or repeatable action, tool/version, checked scope and execution stage |
| Decision | Blocking/advisory/measured-only, allowed results and behavior on execution failure |
| Exception | Affected rule/scope, reason, owner, expiry or review trigger and remaining risk |
| Evidence | Revision, actual input, observed output, interpretation, limits and next unproven check |

## Distinguishing controls

Exercise the decision path, not merely report generation. A scanner can produce findings while returning a successful exit; a wrapper can accidentally discard a failed exit. Check both the report and the final decision used by the caller.

| Case | Required observation |
| --- | --- |
| Known relevant violation | The rule identifies it and the decision rejects it |
| Clean control | The valid case passes without weakening the rule |
| Allowed severity or boundary value | The configured threshold is preserved |
| Missing tool, malformed report or incomplete scope | The result is explicitly unavailable/failed, never clean |
| Configured required gate | The intended merge/release boundary actually requires the relevant result |

Use safe fixtures or an authorized isolated branch; never introduce a defect into production to demonstrate a gate. A successful fixture checks the mechanism, not all possible production behavior. Read branch or release protection separately; a failed CI job alone does not prove publication is blocked.

## Guarding the bar

Inspect changes to the norm source and the mechanisms that implement it, including filtering, ignored paths, suppression comments, skipped/deleted tests and weakened assertions. Include the intended comparison scope, staged and unstaged work and relevant new files when reviewing a local change. Preserve unrelated work.

Determine whether a removed assertion lost coverage or moved to an equivalent check. Distinguish a legitimate scoped exception from a hidden bypass. Keep tools that cannot decide semantics advisory until a responsible review resolves the case; do not present a regex guard as comprehensive enforcement.

For a ratchet, keep the measured baseline separate from an aspirational target. Repeated measurements may be necessary for noisy metrics. An improved number under changed inputs is not automatically a valid new baseline, and an exception does not establish that the original requirement passed.
