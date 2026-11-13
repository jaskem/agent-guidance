---
name: audit-ui-ux
description: Audit an existing interface from screenshots, a running app or UI source, ranking usability findings against real tasks and available evidence. Use for UI/UX audits and interface critiques; exclude new interface design, implementing fixes and code-only reviews.
---

# Audit UI/UX

## 1. Fix the target and evidence

Read the applicable project instructions and existing task owner. Establish the audience, product job, accepted scope and two or three important tasks from supplied context. Preserve unresolved questions; proceed with supported inspection when answers are unavailable.

Inventory actual screenshots, running surface and source separately. Record version/commit, state, viewport, scale when known and whether data is representative or synthetic. Historical screenshots support a dated baseline, not current behavior. Finish with a bounded target, task list and evidence inventory.

## 2. Inspect the interface

Open the images or running views, rather than inferring their content from filenames. Inspect an overview and readable detail for each selected state. Compare empty, representative and dense/error states when available. Apply [review criteria](references/criteria.md) to the target tasks.

For screenshots, record visible observations and usability hypotheses. For source, cite exact locations. For interaction claims, exercise the control when available and record starting state, action and observed result. Classify inaccessible checks as untested. A passing code check, static image or independent reviewer does not establish user validation.

Finish when each selected view has a recorded observation or coverage gap. Retain working patterns that proposed changes should preserve.

## 3. Challenge and prioritize findings

Write each material finding using [the finding record](references/findings.md). Separate the observed condition from its possible user effect and proposed remedy. Seek counterevidence: context menus, shortcuts or deliberate expert density may explain an apparent problem.

Rank by task impact, recurrence and recovery cost. Keep confidence separate from severity. Reserve blocking severity for demonstrated blocked work; a plausible risk becomes a validation task. Prefer a short supported list over exhaustive speculative defects.

Finish when each retained finding has traceable evidence, task consequence, priority, confidence and verification method. Merge repeated symptoms under one actionable owner.

## 4. Deliver the audit

Provide annotated screenshots or precise image locations for visual findings. Keep source images intact; label annotations and proposed designs separately. Use file-native or code-native drawings for exact UI explanations.

Summarize strengths, priority findings and untested coverage at the existing project owner. Distinguish observed defects, recommendations and open questions. Aesthetic preference alone does not establish a defect or justify removing expert controls. Numeric usability or compliance scores require an explicit rubric and sufficient evidence; otherwise report coverage.

Finish with a reviewable audit and next checks. For visual proposals use design-ui-improvements when available; for implementation plans use the existing planning method and tracker. This audit itself makes no production changes.

For provenance or updates, read [sources](references/sources.md).

