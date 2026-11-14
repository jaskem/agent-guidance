---
name: triage
description: Investigate and organize incoming bug reports or improvement requests into existing tasks with evidence, deduplication and a clear next action. Use for multiple unclear reports, intake or backlog triage; exclude fixing one already scoped bug, product prioritization without evidence and code review.
---

# Triage requests

## 1. Establish intake and owner

Follow the user's configured operating guide once per session and its active tool-call version. Reuse verified context; load the relevant project, current task and source owners, refreshing affected sources after material changes or uncertain writes. If required context is inaccessible, name the gap and continue only independently supported work. Use the routed context-entry playbook when available.

Use available agents without waiting for an explicit user request when this method calls for independent fact-finding or when a bounded parallel task or separate check would improve the result. Follow the routed delegation procedure; give each worker a source/revision, scope, allowed actions and expected evidence. Keep one writer per shared object, use the current host capabilities and let the parent verify and integrate the result. If delegation is unavailable, continue supported work and state any required independence that remains unproven.

Identify the supplied reports or bounded intake period and the existing tracker. Read relevant task fields, statuses, prior decisions and related records. Do not scan unrelated projects or migrate planning. Finish with a bounded intake set and actual destinations, or an explicit access gap.

## 2. Separate and verify reports

Split independently testable outcomes while retaining links to the original request. For each, identify reported versus expected behavior, input/version, effect and available evidence. Search existing work by domain meaning as well as wording. Read a linked external change as evidence; do not treat its author’s description or passing CI as proof that the reported outcome is satisfied. An implemented code path or a similarly named completed task does not prove this report is resolved.

For a bug, use the existing diagnostic method for bounded reproduction when available; otherwise record the attempted action and observed result. Treat source inspection separately from runtime verification. For a request, check accepted scope and prior rejection reasons without silently reasserting an old rejection. Finish with a supported issue, genuine duplicate, already-covered criterion or named missing evidence per report.

## 3. Make work actionable

Use [the intake record](references/intake-record.md). Distinguish impact, confidence and priority; prefer confirmed blocked work over speculative severity. Propose the smallest deliverable and acceptance check. Where reports share a symptom, retain distinct input, version or failure conditions until evidence establishes a common cause; route confirmed independent investigations to bounded agents when useful. Preserve user priority and genuine blockers. Ask only for unavailable information that changes the next action; do not force an interview before checking accessible facts.

Update the existing task when it owns the outcome; create a new task only for an uncovered independent result within authorization. Read the destination before a scoped write, preserve concurrent content and use real identifiers after creation succeeds. Do not close, reject, delete or relabel items merely because a heuristic suggests it. Apply only outcomes justified by evidence and current authority.

## 4. Reconcile intake coverage

Map every supplied report to its owning task, duplicate reference or concrete unresolved question. Verify saved targets, keeping failed writes explicit. Summarize the most consequential findings and next ready work; route implementation to evidence-driven-development or a multi-task plan to implement-spec. Triage alone does not implement fixes or claim product acceptance.

For provenance, read [sources](references/sources.md).
