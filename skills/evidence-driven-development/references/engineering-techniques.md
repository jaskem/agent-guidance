# Select engineering depth

Read only the section relevant to the accepted change. These techniques belong to this package; no provider workflow must be installed or invoked.

## Behavior and test boundaries

Name the incorrect result the check must catch. Derive expected values from the contract or an independently worked example, not from the function under test. Exercise callers through their meaningful interface; choose lower-level tests where an important rule is otherwise hidden. Cover the failure/recovery branch that creates the material risk. Do not force a coverage quota or a test for prose and trivial edits.

Use a substitute only for an understood dependency boundary. A mock assertion proves a call expectation, not that a real file, device, service or browser works. Mentally change a branch, constant or state update to see whether the proposed check could detect a plausible defect. Observe an intended failure before relying on a regression test when practical; setup failures prove no product defect.

## Readability and interfaces

Understand callers, state ownership, error paths and the historical reason before deleting a layer. Prefer clear names, direct control flow and existing platform/library features. Preserve return shape, ordering, side effects, identity, serialization, resource lifetime and error timing. An async-to-sync rewrite or object-to-Map rewrite may change the contract even when normal examples agree. Keep existing coverage until equivalent behavior evidence exists; fewer lines or files alone is not an improvement.

## Migrations and uncertain writes

Find real consumers and supported old/new data versions. Plan compatible reads, idempotent transforms, backup/recovery and an observable transition. Expand/contract fits some services; a local JSON app instead needs its actual file-format, interruption and shared-folder checks. Inspect a write's destination before retrying an uncertain result. Never infer permission to drop a format or consumer from a generic migration recipe.

## Git and CI

Inspect the actual baseline, index and unrelated work. Stage only owned paths or hunks. Use isolation when needed, checking the actual chosen path and ownership before cleanup; a directory name proves neither. Follow the existing package manager, lockfile and scripts policy. Read configured checks and preserve accepted quality floors; do not install an unchecked gate helper or weaken a check to get green. An authorized CI change uses the actual runner and project checks, not a mandatory web-stack example.

## UI implementation

Preserve the accepted design system, task density and domain labels. Represent loading, empty, error, pending, selected and disabled states coherently. Use native semantics or accessible equivalents with keyboard activation, focus entry/return and meaningful names. Keep one source for shared state; optimistic feedback must expose failure and recovery. Verify standards and target-platform scaling before claiming accessibility conformance. Real user-flow evidence belongs to test-user-flows; a screenshot alone cannot qualify interaction.
