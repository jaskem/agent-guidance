---
name: evidence-driven-development
description: Execute an authorized software change, diagnose a reported bug, or review an implementation with observable evidence. Use for substantive repository implementation and bug fixes. Exclude planning-only requests, ordinary factual questions, and trivial editorial edits.
---

# Evidence-driven development

## 1. Establish the work

Read the applicable repository instructions and follow their route to the existing plan, contracts, glossary, decisions, source and tests. Identify repository, branch, exact starting revision and uncommitted work. Preserve unrelated changes. Use the current request as the scope; an audit or planning-only request does not authorize product implementation.

Locate the existing issue, plan or checkpoint before creating another. Write a compact acceptance statement there when the repository requires it; otherwise keep it in the working conversation: input or user action, expected observable result, invariants, and the check that can distinguish success from failure. Resolve ordinary reversible choices from the evidence. Ask only about an unresolved material requirement, authority boundary or domain meaning.

Complete this step when the target behavior and its owning source are identifiable. If a required source is unavailable, continue independent work and mark the dependent claim unverified.

## 2. Choose the branch

- **Reported bug or regression:** read [diagnosis](references/diagnosis.md), then reproduce the reported symptom before claiming a cause or a fix.
- **Feature or refactor:** choose one usable slice through the relevant public interface. Retain existing domain terms and interfaces unless changing them is part of the request. Compare simpler alternatives when the interface or dependency direction changes. Keep detailed internals behind a small understandable interface.
- **Review only:** skip implementation. Pin both ends of the comparison, include relevant staged/unstaged changes when requested, then go to step 4.

## 3. Implement and observe

Use the repository's test framework and risk-based checks. For changed behavior or a regression, add a discriminating failing check where practical, observe why it fails, make the smallest coherent change, and rerun it. Test through the caller-visible interface with expected results from requirements or independently worked examples. A test failure caused by missing setup is not evidence of the bug.

Work one slice at a time. Confirm the slice before extending it. For behavior-preserving refactors, capture the existing behavior and require it to remain unchanged; artificial failing tests are unnecessary. Use direct inspection for low-impact editorial changes. Run the broader checks required by the repository once the changed slices work. Do not invent blanket test or approval requirements.

Keep code, repository plans and decisions in their existing repository owners. Personal memory or a Notion copy may point to them; it must not replace a product contract or claim an unmerged proposal is current behavior.

## 4. Review twice

Assess the actual change separately against:

1. **Requirements:** intended behavior, acceptance checks, missing work and accidental scope expansion.
2. **Implementation quality:** repository conventions, correctness, compatibility, readability, unnecessary coupling and the real failure paths.

Keep findings attributable to their axis. A passing test does not settle either review by itself. Use separate fresh-context reviewers only when delegation is authorized and useful. Give them raw requirements and the exact diff, not your expected verdict. Otherwise perform both passes yourself and state that they were not independent reviews.

Fix material findings within scope. A local pass does not establish remote CI, a merge, deployment, or live behavior.

## 5. Close the actual change

Follow repository closure, merge and release rules within the user's authorization. Clean up temporary diagnostics and change-induced obsolete text. Check uncertain write outcomes before retrying. Record the exact revision, checks and their scope, unresolved items and first unproven next action in the existing durable work record.

Report outcome, evidence and remaining limits briefly. Claim completed behavior only to the extent observed. Do not add another tracker, process gate or handoff store merely because this skill ran.

For provenance and intentional differences from upstream, read [sources](references/sources.md) when auditing or updating this skill.
