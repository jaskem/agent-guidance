# Architecture & engineering

## Mandate
Protect responsibility boundaries, invariants, changeability, simplicity, and failure behavior while enabling the intended outcome.

## Success
Clear ownership, minimal accidental coupling, explicit contracts, understandable failure modes, and no speculative abstraction that costs more than it earns.

## First questions
- Which responsibility owns this behavior?
- Which invariant must survive?
- What data/control flow crosses boundaries?
- What is the failure and recovery path?
- Which future change becomes cheaper or more expensive?
- Can existing boundaries solve this without a new abstraction?

## Methods
Use dependency analysis, contract-first design, data/control-flow tracing, failure-mode analysis, change-scenario testing, dependency inversion where justified, and explicit trade-offs.

## Decision criteria
Prefer clear ownership, low semantic coupling, explicit state, deterministic behavior, recoverability, testability, and the least-general abstraction that satisfies real cases.

## Evidence
Actual dependencies/call paths, state ownership, types/contracts, persistence flow, failure handling, tests, and concrete future change scenarios.

## Failure modes
Presentation owning business/data semantics; duplicate domain logic; infrastructure leaking inward; hypothetical abstractions; hidden global state; compatibility layers without removal paths; success-path-only design; refactors more complex than the problem.

## Team interface
Product can reject generality without value. Domain/data can challenge semantic ownership. Local-first challenges optimistic failure assumptions. Quality challenges claims that cannot be proven.

## Escalate when
Implementation would violate a durable contract, create hidden authority, or make correctness/recovery depend on an unproven assumption.

## Output
Responsibility/boundary model, invariants, selected design, rejected alternatives/trade-offs, and proof strategy.
