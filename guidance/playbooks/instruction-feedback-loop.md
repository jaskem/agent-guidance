# Instruction feedback loop playbook

Load this when real work reveals a reusable defect in instructions, routing, process guidance, or agent-facing enforcement. It exists to preserve high-signal learning without letting meta-work silently expand the active task.

## Trigger

Use this playbook when one or more of these is true:

- a user correction exposes a reusable gap, contradiction, stale rule, or misroute;
- the agent repeatedly redoes proven work, crosses scope, misses a required handoff, or otherwise fails in a way likely caused by guidance rather than the task itself;
- the same workaround or manual recovery appears across sessions or repositories;
- a repository/process defect suggests that guidance is carrying responsibility better owned by code, configuration, schema, CI, or tooling;
- the user explicitly asks to improve the instruction system from observed work.

Do not use it for a one-off content mistake, an ordinary product defect, or a preference already owned by an existing instruction.

## Core rules

- An observation is evidence to review, not an accepted instruction change.
- Protect the active task first. Do not interrupt or broaden a bounded batch merely to improve guidance unless continuing would be unsafe or the current scope explicitly includes the fix.
- Repair the mechanism that owns the failure before adding prose. Prefer code, configuration, schema, validation, automation, or product/process structure when they can prevent the failure more reliably than another instruction.
- Keep one normative owner. Shared guidance receives only repository-independent behavior; consumer-specific workflow, product, domain, and roadmap rules stay with the consumer.
- Promote a finding to cross-cutting guidance only when evidence shows it generalises beyond one local incident.
- Review for removal and simplification as deliberately as for additions. Stale, duplicated, ceremonial, or structurally unenforceable guidance is instruction debt.
- Never let the instruction system modify itself implicitly. Any guidance change remains an explicit, scoped repository change with normal review and verification.

## Observation capture

When the finding is material but cannot or should not be fixed in the active scope, record the smallest durable observation the current environment supports. Reuse an existing issue, checkpoint, backlog, or maintenance mechanism instead of inventing a parallel store.

Capture only what a later reviewer needs:

- **observed effect** — what went wrong or created avoidable friction;
- **evidence** — the concrete correction, repeated behavior, failed control, or repository fact;
- **candidate owner** — code/config/tooling, consumer guidance, shared guidance, or unresolved;
- **scope disposition** — fixed now, deliberately deferred, or needs review;
- **decision impact** — why recurrence would materially affect correctness, scope, evidence quality, user value, recovery, or maintenance cost.

Do not log speculative improvements with no observed consequence. Do not duplicate an already-open observation that describes the same failure mode.

## Review procedure

When the user requests a review, an established maintenance cadence triggers one, or accumulated evidence makes review materially useful:

1. Re-read each candidate against the current repository and instruction route; discard observations that are stale, duplicated, disproven, or already fixed.
2. Cluster by underlying failure mode rather than wording or session.
3. For each cluster, identify the true owning mechanism before proposing guidance.
4. Prefer the smallest structural fix that removes recurrence.
5. If guidance is still the correct owner, edit the single canonical owner and remove or simplify superseded wording elsewhere.
6. Verify the change with the repository's normal guidance/process checks and with at least one concrete failure case the change is meant to prevent.
7. Record the disposition so resolved items leave the active observation set.

## Review questions

Before changing guidance, answer:

- Would this still be correct after the specific incident is forgotten?
- Could a machine-enforced control prevent the failure more reliably?
- Is this rule already owned somewhere else?
- Does the change reduce ambiguity or merely add words?
- What existing instruction can be removed or simplified because of this change?
- What concrete recurrence would demonstrate that the fix worked?

## Output

Keep normal task output unchanged unless the user asked for instruction-system review. For a dedicated review, report only the material observation clusters, their evidence, the selected owner/fix, rejected or deferred items, and the verification needed.

Method inspiration: the observation-and-review approach was informed by Eoghan Henn's Task Observer project (rebelytics/one-skill-to-rule-them-all); this implementation is adapted to this guidance system's canonical-ownership and bounded-scope model.
