---
name: code-review
description: Review a code change against its originating requirements and repository quality rules using a fixed comparison. Use for requested PR, branch or implementation review. Exclude ordinary explanation and unchanged codebase surveys.
---

# Code review

For the web-platform branch, load modern-web-guidance before the dependent technical decision when the reviewed change makes substantive web-platform or browser-compatibility choices. Use its accepted package and relevant guides; retain this method's outcome, project browser policy and real visual/runtime checks. Backend-only, native-only and purely editorial work do not trigger that branch.

## 1. Fix the review scope

Follow the user's configured operating guide once per session, including its required tool-call version. Reuse verified context; load project and task owners only when relevant, refreshing them after a project/scope change or material new evidence. Use the routed context-entry playbook when available. If required context is inaccessible, disclose the gap and continue only independent work.

Resolve the repository, actual changed files and comparison baseline from the request, PR or existing task. Pin the base and reviewed head. Inspect local changes when relevant. Do not guess an arbitrary baseline or claim an unobserved diff. An empty change can be reported directly.

Read the applicable router and originating requirements, accepted decisions and relevant standards. Resolve references before asking the user. If requirements cannot be found, perform the supported quality review and mark requirements coverage unavailable; do not invent a spec. If the change itself is unavailable, identify that blocker and avoid findings about unseen code.

## 2. Review two independent questions

Use [review axes](references/axes.md). Requirements review checks missing, incorrect and unrequested behavior. Quality review checks correctness, maintainability and applicable repository rules. Inspect the real call paths and existing tests; passing tests are evidence for their cases, not proof the requirements are met.

Use available agents on your own initiative when this method calls for separate work or when bounded independent work or review would improve the result; no explicit user request is needed. Follow the routed delegation rules. Give each worker the relevant source, question, allowed actions, owned objects and expected evidence; keep one writer per shared object and verify the combined result in the parent. Use the actual host capabilities and model/fork rules. If agents are unavailable, continue supported work without claiming an independent review. Choose a separate fresh-context review for an important independent question, not merely because a diff is large. Supply raw evidence rather than expected findings. Assess both review axes even with one reviewer; distinguish self-review, shared-context agent review and a genuinely fresh-context review.

## 3. Substantiate findings

For each material finding cite the changed location, relevant requirement or rule, concrete failure scenario and impact. Distinguish observed failures, code-supported risks and unverified hypotheses. Check whether a proposed finding is already handled elsewhere before reporting it. Treat design heuristics as judgments, not automatic violations. Prefer executable checks for mechanically detectable defects.

Do not edit code during a review-only request. Use [review feedback](references/review-feedback.md) when assessing comments or proposed fixes. When fixes are authorized, preserve the review baseline, apply bounded fixes through the execution workflow, then recheck affected findings and changed head. Do not approve a different revision using earlier evidence.

## 4. Report actionable results

Keep requirements and quality findings identifiable. Lead with material blockers and next action; avoid a wall of style observations. Report the inspected scope, checks actually run and gaps. State no findings only for the inspected scope. Distinguish reviewed, tested, merged and published states.

Read [sources and adaptation](references/sources.md) when maintaining this package.
