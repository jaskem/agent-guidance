---
name: deprecation-and-migration
description: Plan or execute a verified transition of real consumers and data away from an existing system, API, schema or file format. Use for compatibility changes, deprecation, backfills and justified retirement; exclude routine refactoring or dependency updates without a consumer/data transition, isolated bug fixes and release packaging.
---

# Deprecation and migration

## 1. Establish the transition and authority

Follow the configured operating guide once per session, including its required tool-call version, and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Read the current contract, accepted reason for change, target behavior and affected runtime. Identify which planning, implementation, data mutation, publication and retirement actions the current task authorizes; continue already-authorized work without extra approval rounds.

Compare the actual value and maintenance cost of keeping the current system with the transition's cost and risks. A recommendation does not authorize execution or removal. Keep unresolved domain meaning with its owner and unresolved caller-contract design with design-interfaces; use the existing implementation/review owner for code changes.

## 2. Find consumers and preservation requirements

Inventory real callers, deployed versions, scripts, jobs, integrations and persisted data using available source and runtime evidence. Include infrequent or offline consumers where relevant. Record the observation window and blind spots; an empty search or quiet log is not proof of no consumers.

Work through representative before/after cases, including observable quirks callers depend on. State what must remain equivalent, what intentionally changes and what happens to data. Identify the usable replacement or accepted sunset outcome, consumer guidance and the evidence required for retirement. Keep existing task and contract ownership; do not make a parallel migration tracker.

## 3. Design compatible and recoverable steps

Map old/new readers, writers and stored states across the proposed phases. Choose an additive transition, adapter, staged cutover or controlled conversion only when the actual runtime requires it. Do not impose a service rollout on a local application. Read [transition cases](references/transition-cases.md) for mixed versions, interrupted writes, local files, quiet consumers or lossy transforms.

Define data invariants, batch boundaries, retry/idempotence behavior, committed progress and conflict handling. Specify a safe stop point and recovery from partial or uncertain outcomes. Separate reversible code changes from irreversible data effects; justify a tested restore, compensation or forward-repair path where a reverse migration cannot preserve data. Name evidence needed before each consequential step.

## 4. Exercise and execute the authorized transition

For a plan, produce concrete steps and checks without mutating consumer data. For execution, rehearse relevant conversion and recovery on representative disposable data where practical, then migrate a bounded consumer or data slice. Verify behavior and data against the agreed invariants before extending the change. Check effects and values, not just counts or command exit status.

Exercise interruption and repeat execution at the meaningful write boundary. On an uncertain write result, inspect durable state before retrying. Preserve needed backups or original artifacts under the existing retention policy. Stop dependent work when compatibility or recovery fails, record the current state and continue only independent authorized work. Use prepare-release for the actual distribution boundary rather than treating a migration rehearsal as a release.

## 5. Retire only on demonstrated grounds

Retire the old path only within the task's authority and when the accepted consumer, data, compatibility and support criteria are met. Record remaining impact explicitly where an accepted policy permits a breaking retirement; otherwise keep necessary compatibility while evidence or migration is incomplete. Do not claim zero consumers beyond the evidence's coverage.

Remove only obsolete code, configuration and current guidance covered by the retirement, retaining required history and recovery material. Verify the resulting consumer behavior and data, including supported old versions where they remain in scope. Update the existing owners with revision, migrated scope, checks, recovery status and exact remaining consumers or unknowns. Finish with a verified transition, justified retirement or a precise unproven next step; a successful deploy alone proves none of these.

For provenance when updating this method, read [sources](references/sources.md).
