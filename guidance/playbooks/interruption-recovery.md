# Interruption recovery playbook

Load this only when a session/tool call was interrupted, stalled, or resumed without a trustworthy final handoff.

Recovery is a short prelude to the real task, not a new audit campaign.

## Fast path
1. Start from the latest relevant durable checkpoint.
2. Determine only mutable facts needed to know what happened after it: current baseline, active branch/head/PR when relevant, exact checkpoint→head or baseline→current delta, and any action whose completion is genuinely uncertain.
3. Classify interrupted work as **proven**, **possibly completed but unconfirmed**, or **not yet done**.
4. Resume from the first unproven step.
5. If a non-idempotent action may have succeeded, inspect that exact target before retrying it.
6. Do not reopen roadmap history, broad docs, completed CI, or old validation unless the delta can invalidate the next action.
7. If recovery effort approaches the remaining task size, identify the smallest unresolved fact blocking safe continuation and stop expanding the read set.

Preferred handoff: **last proven point → relevant delta/pending state → first unproven action**.

## Valuable uncheckpointed evidence
Create at most one provisional evidence checkpoint at a natural boundary only when a coherent evidence unit is complete, losing it would require material rework, and substantial work remains.

It records evidence, not completion: baseline/head, established facts, minimum reusable references, remaining uncertainty, and first next action.

If no checkpoint survived, salvage durable objects first, then reconstruct only conclusions needed for the next safe action. Re-derive conclusions from facts and constraints rather than recreating lost private reasoning step-by-step.

The goal is bounded evidence debt, not checkpoint administration.
