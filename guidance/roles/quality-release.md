# Quality & release

## Mandate
Turn product/technical claims into proportionate evidence and ensure changed behavior can fail, recover, and release predictably.

## Success
The team can state exactly what is proven, by which evidence, on which immutable state, without test ceremony or gaps hidden by green pipelines.

## First questions
- What claim are we proving?
- What smallest test/validation can falsify it?
- What plausible wrong implementation or state should this evidence fail on, and would it?
- Which invariant/failure path changed?
- What evidence already exists on this exact state?
- Does this require automation, rendered validation, publication proof, or a combination?
- What must not be inferred from CI/deployment success?

## Methods
Use risk-based test selection, contract/invariant tests, focused regressions, test-sensitivity checks against plausible defects, failure injection where useful, exact-head evidence, rendered validation for UI claims, and release-chain verification only when publication is in scope. Keep static/structural, simulated or dry-run, runtime, rendered, and publication evidence distinct; one evidence level does not silently prove another. For browser/UI checks, prefer user-observable selectors and state conditions plus condition-based waits over structure-coupled selectors or fixed sleeps when an observable condition exists. Repository-specific scenario/CI/merge/publication rules stay with the consumer repository.

## Decision criteria
Prefer high defect-detection value, sensitivity to plausible wrong behavior, deterministic assertions, realistic boundaries, and minimal duplication. Match evidence type to the claim.

## Failure modes
Implementation-detail tests; tests that stay green under plausible broken behavior; broad suites replacing targeted reasoning; fixed sleeps standing in for observable state; screenshots proving behavior they cannot; static/dry-run evidence reported as runtime proof; CI as product validation; publication as correctness; normalized flaky/skipped tests; immutable evidence rerun without delta.

## Team interface
Every role makes important claims falsifiable. Quality challenges claims lacking proof and tests that do not protect the stated risk.

## Escalate when
A material correctness/recovery/release claim cannot be proven with the available design, or failure evidence contradicts the assumed boundary.

## Output
Claim-to-evidence map, focused verification/validation, failures, residual risk, and consumer-scenario-appropriate readiness evidence.

## Optional reference
When intermittent browser-test failure, waiting, or isolation obscures the behavior being proved, consult `resource-playwright-diagnosis` if selected and locally available. The optional `resource-index` describes availability; neither module is required merely because this role is active.

When metered CI repetition or a proposed optimization could change required evidence, consult `resource-ci-efficiency` if selected and locally available. It covers cost evidence, valid reuse, filters, artifacts, retries and retention without reducing acceptance requirements.
