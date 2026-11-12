---
name: handoff
description: Prepare a durable handoff or resume interrupted work from verified state. Use for transfer, continuation, stalled sessions or uncertain prior writes. Exclude unrelated new tasks and routine progress messages.
---

# Handoff

## 1. Choose prepare or resume

Read the current instruction and the latest relevant durable work record. Follow the repository's existing interruption-recovery procedure when routed. Preserve its checkpoint destination and scope boundaries. Use the available operating guide to locate personal context, not to replace current project evidence.

For preparing a handoff, inspect the state needed by the next task. For resuming, compare the recorded baseline with current head, branch, PR, checks or exact external target as relevant. Restrict reconstruction to facts that can change the next action.

## 2. Separate proof from uncertainty

Classify relevant work as established, possibly completed but unconfirmed, or not done. If a non-idempotent write may have succeeded, read its exact target before retrying. Missing history is unknown state, not evidence of failure. Do not repeat completed work or reopen unrelated history.

Use [handoff record](references/record.md). Link existing plans, decisions, commits, artifacts and checks instead of copying their contents. Include the first unproven action and any prerequisite that actually blocks it. Retain explicit user scope limits and meaningful rejected alternatives.

## 3. Save or continue

Prepare a durable record at the existing project checkpoint/issue location, or the established private document destination when no repository owns the work. A chat response can be the requested handoff, but do not claim durable external storage unless it succeeded. Keep Notion as a dated pointer to repository-owned state rather than a second task ledger.

For resuming, act on the first unproven authorized step after the minimum necessary verification. If blocked, report the exact missing fact or capability and continue independent work. Recovery is a prelude to the task, not a new audit campaign or reason to stop after one checkpoint.

## 4. Confirm the boundary

Report the last verified point, remaining uncertainty and next action. Distinguish source saved, installed, merged, deployed and tested. Verify ambiguous save results before retrying. Exclude secrets, full transcripts and private reasoning from the handoff.

Read [sources and adaptation](references/sources.md) when maintaining this package.
