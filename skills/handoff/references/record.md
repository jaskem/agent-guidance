# Handoff record

Use only fields needed to resume reliably:

- Goal and current authorization, including explicit exclusions.
- Canonical project/plan and applicable route links.
- Last verified baseline or exact artifact revision.
- Proven result and the evidence that supports it.
- Relevant delta, pending operations and uncertain write targets.
- First unproven action, genuine blockers and necessary tool context.
- Relevant methods or roles to load, only when needed for the next step.

Mark a provisional checkpoint as evidence, not completion. Keep one active continuation pointer at the established owner. When no checkpoint survived, inspect durable objects and reconstruct only enough to continue; do not recreate a full lost conversation.

An old summary is not current status. A merged PR is not proof of deployment. A timeout is not proof a write failed. Record these distinctions whenever they affect the next action.

## Resuming with agents or uncertain external effects

Retain the exact worker/resource ownership, unfinished branches or external objects, observed operations and last confirmed receipt. A worker being interrupted does not prove its write stopped. Inspect the destination and active ownership before retrying or reassigning.

Tie verification to the revision, environment and behavior it actually covers. Reuse still-valid evidence; rerun only when the state moved, the baseline is absent or the next step depends on an unproven boundary. A generic task status or review ruling does not replace required acceptance.

Record unresolved important findings and the next distinguishing check. Keep necessary evidence durable before deleting a temporary workspace; never assume ignored ledgers and test logs were saved in Git.
