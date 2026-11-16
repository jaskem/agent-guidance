# Transition cases

Read the relevant case when data, mixed versions or external consumers make a transition consequential. Choose phases from the actual runtime and compatibility requirements.

## Old and new application versions coexist

Map each version's reads and writes against the schema or file format at every phase. Add compatible structures before redirecting consumers; remove old structures only after the accepted retirement criterion is met. Check locks, validation and resource cost: an additive database change is not automatically operationally safe.

For a backfill concurrent with user updates, define the authoritative value and conflict rule. Prevent an older backfill value from overwriting a newer live write. If dual writes are necessary, specify behavior when only one write succeeds and how divergence is detected and repaired. Reverting application code does not reverse transformed data.

## A migration is interrupted after a write

Use a stable unit identity and a checkpoint that represents committed progress. Stop after a representative unit, restart, and verify the result against independent invariants. Include the ambiguous case where a write succeeded but its acknowledgment was lost. Inspect durable state before retrying; a counter of attempted items is not a safe resume point.

Repeated execution must preserve intended effects. For operations that cannot be naturally idempotent, use an appropriate transaction, deduplication record, conditional write or explicit reconciliation step. Verify both final data and side effects; matching row counts alone can hide changed values or duplicate external actions.

## A local application upgrades a user's file

Use representative copies to check version detection, conversion and interruption. Establish whether the previous application can still read the result. Preserve an appropriate pre-conversion copy or atomic replacement path where required; verify that restoration produces a usable file. A single-process offline conversion may need one controlled transition, not a service rollout.

Test disk-full or permission failure around the write boundary when relevant. Avoid claiming crash recovery from a successful in-memory conversion. Do not delete the user's recoverable original merely because the new application opened once.

## A public interface has quiet or offline consumers

Combine known client inventory, dependency search, usage evidence and the existing support policy. A quiet week or zero repository references does not prove that an external client, infrequent job or old exported artifact no longer depends on the interface.

Record coverage gaps and concrete migration examples. Prepare notices or guidance with the existing owner; send them only within the task's authority. Where the accepted policy permits a breaking retirement, document the remaining impact instead of claiming every consumer migrated. Otherwise preserve necessary compatibility until the criterion can be met.

## A transform is lossy or has external effects

Name the information or effects that a reverse transform cannot recover. Choose a verified restore, compensation or forward-repair procedure appropriate to those effects; do not label an untested `down` command as rollback. Restoration from an old backup can discard later valid writes, so define how those are preserved or reconciled.

An authorized sunset can intentionally have no replacement. Establish the accepted loss of capability and any export, retention or support obligation before executing it. A migration recommendation alone does not authorize deletion.
