---
name: handoff
description: Prepare a durable handoff or resume interrupted work from verified state. Use for transfer, continuation, stalled sessions or uncertain prior writes. Exclude unrelated new tasks and routine progress messages.
---

# Handoff

## 1. Choose prepare or resume

Follow the user's configured operating guide once per session, including its required tool-call version. Reuse verified context; load project and task owners only when relevant, refreshing them after a project/scope change or material new evidence. Use the routed context-entry playbook when available. If required context is inaccessible, disclose the gap and continue only independent work.

Use available agents without waiting for an explicit user request when this method calls for independent fact-finding or when a bounded parallel task or separate check would improve the result. Follow the routed delegation procedure; give each worker a source/revision, scope, allowed actions and expected evidence. Keep one writer per shared object, use the current host capabilities and let the parent verify and integrate the result. If delegation is unavailable, continue supported work and state any required independence that remains unproven.

Read the current instruction and the latest relevant durable work record. Follow the existing interruption-recovery procedure when routed. Preserve its checkpoint destination and scope boundaries; personal context does not replace current project evidence.

For preparing a handoff, inspect the state needed by the next task. For resuming, compare the recorded baseline with current head, branch, PR, checks or exact external target as relevant. Restrict reconstruction to facts that can change the next action. A current working directory or old task-complete marker does not prove project identity, current integration or acceptance.

## 2. Separate proof from uncertainty

Classify relevant work as established, possibly completed but unconfirmed, or not done. If a non-idempotent write may have succeeded, read its exact target before retrying. Missing history is unknown state, not evidence of failure. Do not repeat completed work or reopen unrelated history.

Use [handoff record](references/record.md). Link existing plans, decisions, commits, artifacts and checks instead of copying their contents. Preserve active worker ownership and in-flight effects; confirm a writer has stopped before handing its resource to another agent. Include the first unproven action and any prerequisite that actually blocks it. Retain explicit user scope limits and meaningful rejected alternatives.

## 3. Save or continue

Prepare a durable record at the verified project checkpoint/task owner, which may be Notion even when code lives in a repository. A chat response can be the requested handoff, but do not claim durable external storage unless it succeeded. Link evidence at its source and update the existing task; do not create a second ledger.

For resuming, act on the first unproven authorized step after the minimum necessary verification. If blocked, report the exact missing fact or capability and continue independent work. Recovery is a prelude to the task, not a new audit campaign or reason to stop after one checkpoint.

## 4. Confirm the boundary

Report the last verified point, remaining uncertainty and next action. Distinguish source saved, installed, merged, deployed and tested. Verify ambiguous save results before retrying. Preserve necessary reports and test receipts at their established owner before cleaning temporary workspaces; repository history alone may not contain ignored evidence. Exclude secrets, full transcripts and private reasoning from the handoff.

Read [sources and adaptation](references/sources.md) when maintaining this package.
