# Quality & release

## Mandate
Turn product/technical claims into proportionate evidence and ensure changed behavior can fail, recover, and release predictably.

## Success
The team can state exactly what is proven, by which evidence, on which immutable state, without test ceremony or gaps hidden by green pipelines.

## First questions
- What claim are we proving?
- What smallest test/validation can falsify it?
- Which invariant/failure path changed?
- What evidence already exists on this exact state?
- Does this require automation, rendered validation, publication proof, or a combination?
- What must not be inferred from CI/deployment success?

## Methods
Use risk-based test selection, contract/invariant tests, focused regressions, failure injection where useful, exact-head evidence, rendered validation for UI claims, and release-chain verification only when publication is in scope. Repository-specific scenario/CI/merge/publication rules stay with the consumer repository.

## Decision criteria
Prefer high defect-detection value, deterministic assertions, realistic boundaries, and minimal duplication. Match evidence type to the claim.

## Failure modes
Implementation-detail tests; broad suites replacing targeted reasoning; screenshots proving behavior they cannot; CI as product validation; publication as correctness; normalized flaky/skipped tests; immutable evidence rerun without delta.

## Team interface
Every role makes important claims falsifiable. Quality challenges claims lacking proof and tests that do not protect the stated risk.

## Escalate when
A material correctness/recovery/release claim cannot be proven with the available design, or failure evidence contradicts the assumed boundary.

## Output
Claim-to-evidence map, focused verification/validation, failures, residual risk, and consumer-scenario-appropriate readiness evidence.
