---
name: audit-ui-ux
description: Audit an existing interface from screenshots, a running app or UI source, ranking usability findings against real tasks and available evidence. Use for UI/UX audits and interface critiques; exclude new interface design, implementing fixes and code-only reviews.
---

# Audit UI/UX

For the web-platform branch, load modern-web-guidance before the dependent technical decision when the web-interface audit needs technical HTML/CSS/browser guidance rather than visual observation alone. Use its accepted package and relevant guides; retain this method's outcome, project browser policy and real visual/runtime checks. Backend-only, native-only and purely editorial work do not trigger that branch.

## 1. Fix the target and evidence

Follow the configured operating guide once per session and its active tool-call version. Read the relevant project instructions and existing task owner; reuse verified context and refresh only material changes. Establish the audience, product job, accepted scope and important tasks from supplied context. Preserve unresolved questions and continue independently supported inspection when a source is inaccessible.

Inventory actual screenshots, running surface and source separately. Record version/commit, state, viewport, scale when known and whether data is representative or synthetic. Historical screenshots support a dated baseline, not current behavior. Identify intentionally static fixtures and mockups; absent implementation in such an artifact is an interaction coverage gap, not by itself a defect in the actual product. Finish with a bounded target, task list and evidence inventory.

Use available agents on your own initiative when this method calls for separate work or when bounded independent work or review would improve the result; no explicit user request is needed. Follow the routed delegation rules. Give each worker the relevant source, question, allowed actions, owned objects and expected evidence; keep one writer per shared object and verify the combined result in the parent. Use the actual host capabilities and model/fork rules. If agents are unavailable, continue supported work without claiming an independent review.

## 2. Inspect the interface

Follow the configured visual-verification playbook when available. Discover the actual target runtime and the user's preferred accessible environment before selecting a capture or interaction tool. Prefer the relevant authorized remote desktop for a native/user-machine target; use a cloud browser only for its intended web target or a documented fallback. A failed local browser runner does not establish that visual checks are impossible. Record what the chosen surface proves and which target-specific claims remain untested.

Open the images or running views, rather than inferring their content from filenames. Inspect an overview and readable detail for each selected state. Compare empty, representative and dense/error states when available. Apply [review criteria](references/criteria.md) to the target tasks.

Inspect content fit and space use explicitly: table columns, row heights, oversized headers, stretched objects, wrapping and accidental voids. Assess visual craft as well as task behavior, using the actual rendered interface and representative content.

For screenshots, record visible observations and usability hypotheses. For source, cite exact locations. For interaction claims, exercise the control and record starting state, action and observed result; use test-user-flows for a distinct runtime journey. Classify inaccessible checks as untested and continue independent views. A passing code check, static image or independent reviewer does not establish user validation.

Finish when each selected view has a recorded observation or coverage gap. Retain working patterns that proposed changes should preserve.

## 3. Challenge and prioritize findings

Write each material finding using [the finding record](references/findings.md). Separate the observed condition from its possible user effect and proposed remedy. Seek counterevidence: context menus, shortcuts or deliberate expert density may explain an apparent problem. For an independent exploratory pass, supply the artifact and task context without leaking the intended route or expected findings. Record the actual inferred task, route, hesitation and recovery; keep agent observations separate from human user-research evidence.

Rank by task impact, recurrence and recovery cost. Keep confidence separate from severity. Reserve blocking severity for demonstrated blocked work; a plausible risk becomes a validation task. Prefer a short supported list over exhaustive speculative defects.

Finish when each retained finding has traceable evidence, task consequence, priority, confidence and verification method. Merge repeated symptoms under one actionable owner.

## 4. Deliver the audit

Provide annotated screenshots or precise image locations for visual findings. Keep source images intact; label annotations and proposed designs separately. Use file-native or code-native drawings for exact UI explanations.

Summarize strengths, priority findings and untested coverage at the existing project owner. Distinguish observed defects, recommendations and open questions. Aesthetic preference alone does not establish a defect or justify removing expert controls. Numeric usability or compliance scores require an explicit rubric and sufficient evidence; otherwise report coverage.

Finish with a reviewable audit and next checks. For visual proposals use design-ui-improvements when available; for implementation plans use the existing planning method and tracker. This audit itself makes no production changes.

For provenance or updates, read [sources](references/sources.md).
