---
name: evidence-driven-development
description: Execute an authorized software change or diagnose a reported bug with observable evidence. Use for substantive repository implementation and bug fixes. Route review-only requests to code-review; exclude planning-only requests, ordinary factual questions, and trivial editorial edits.
---

# Evidence-driven development

For the web-platform branch, load modern-web-guidance before the dependent technical decision when the change implements or diagnoses HTML, CSS, browser APIs or client-side JavaScript. Use its accepted package and relevant guides; retain this method's outcome, project browser policy and real visual/runtime checks. Backend-only, native-only and purely editorial work do not trigger that branch.

## 1. Establish the work

Follow the user's configured operating guide once per session, including its required tool-call version. Reuse verified context; load project and task owners only when relevant, refreshing them after a project/scope change or material new evidence. Use the routed context-entry playbook when available. If required context is inaccessible, disclose the gap and continue only independent work.

Read the applicable repository instructions and follow their route to the existing plan, contracts, glossary, decisions, source and tests. Identify repository, branch, exact starting revision and uncommitted work. Preserve unrelated changes. Use the current request as the scope; an audit or planning-only request does not authorize product implementation.

Locate the existing issue, plan or checkpoint before creating another. Write a compact acceptance statement there when the repository requires it; otherwise keep it in the working conversation: input or user action, expected observable result, invariants, and the check that can distinguish success from failure. Resolve ordinary reversible choices from the evidence. Ask only about an unresolved material requirement, authority boundary or domain meaning.

Complete this step when the target behavior and its owning source are identifiable. If a required source is unavailable, continue independent work and mark the dependent claim unverified.

Use available agents on your own initiative when this method calls for separate work or when bounded independent work or review would improve the result; no explicit user request is needed. Follow the routed delegation rules. Give each worker the relevant source, question, allowed actions, owned objects and expected evidence; keep one writer per shared object and verify the combined result in the parent. Use the actual host capabilities and model/fork rules. If agents are unavailable, continue supported work without claiming an independent review.

## 2. Choose the branch

Before executing the selected branch, actually load its method or reference and note its decisive check in the existing work context. Dispatch useful separable investigation early through the configured delegation procedure. For a changed interface, use audit-ui-ux for a distinct assessment, design-ui-improvements for unresolved visual proposals, motion-design for substantial interactive animation and test-user-flows for live acceptance. These are conditional results, not a mandatory design cascade. Follow the configured visual-verification procedure for the relevant runtime; a cloud preview does not prove native user-machine behavior.

- **Reported bug or regression:** read [diagnosis](references/diagnosis.md), then reproduce the reported symptom before claiming a cause or a fix.
- **Feature or refactor:** choose one usable slice through the relevant public interface. Retain domain terms and interfaces unless their change is authorized. Use [engineering techniques](references/engineering-techniques.md) for behavior-preserving simplification, migrations, CI and UI work; load only the relevant section. Keep complexity behind an understandable interface.
- **Distinct assessment:** use design-interfaces for an unresolved caller contract, review-security for a bounded security assessment, optimize-performance for a measured performance investigation and test-user-flows for real user-route evidence. They contribute their specific result; this method retains ownership of an authorized code change.
- **Review only:** load the `code-review` method and follow its review-only route; do not start implementation.

## 3. Implement and observe

Use the repository's test framework and risk-based checks. For changed behavior or a regression, add a discriminating failing check where practical, observe why it fails, make the smallest coherent change, and rerun it. Test through the caller-visible interface with expected results from requirements or independently worked examples. A test failure caused by missing setup is not evidence of the bug.

Work one slice at a time. Confirm the slice before extending it. For behavior-preserving refactors, capture the existing behavior and require it to remain unchanged; artificial failing tests are unnecessary. Use direct inspection for low-impact editorial changes. Run the broader checks required by the repository once the changed slices work. Do not invent blanket test or approval requirements.

Keep code, plans, task status and decisions with their verified owners. A repository may own code while Notion owns tasks; do not create a parallel tracker or silently migrate ownership. Context summaries must not replace a product contract or claim an unmerged proposal is current behavior.

## 4. Load the review owner

Load the separately installed `code-review` method for the actual change. Its package owns requirements and implementation-quality review; use the repository's applicable roles and acceptance sources through that method. An available name is not proof that its instructions were read.

If the method is unavailable, resolve its exact canonical source from the current distribution record and read that revision. If the source cannot be reached, continue independent repository checks and report the shared review as incomplete; do not silently replace it with a second review procedure. Fix material findings within the authorized implementation scope, then rerun affected checks. A review-only request does not authorize applying its findings.

## 5. Close the actual change

Follow repository closure, merge and release rules within the user's authorization. Clean up temporary diagnostics and change-induced obsolete text. Check uncertain write outcomes before retrying. Record the exact revision, checks and their scope, unresolved items and first unproven next action in the existing durable work record.

Report outcome, evidence and remaining limits briefly. Claim completed behavior only to the extent observed. Do not add another tracker, process gate or handoff store merely because this skill ran.

For provenance and intentional differences from upstream, read [sources](references/sources.md) when auditing or updating this skill.
