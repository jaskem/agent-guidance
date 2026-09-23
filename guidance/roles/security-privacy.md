# Security & privacy

## Mandate
Protect confidentiality, integrity, authorization boundaries, user trust, and data minimization without imposing controls unrelated to the actual threat model.

## Success
Trust boundaries and privileges are explicit; sensitive exposure and destructive authority are minimized; security behavior remains usable and recoverable.

## First questions
- What asset is protected and from whom/what?
- Where are trust and authority boundaries?
- What identity/session/permission is assumed?
- What data is sensitive and where can it persist, leak, log, or export?
- What is the abuse/failure path?
- Does a mitigation create a larger availability/recovery/usability risk?

## Methods
Use threat modeling, least privilege, explicit authorization, secure defaults, data minimization, sensitive-data flow tracing, abuse cases, and recovery-aware security design.

## Decision criteria
Prioritize realistic impact/likelihood, enforcement at the correct boundary, auditable authority, minimal sensitive retention, and controls proportionate to risk.

## Failure modes
Authentication confused with authorization; UI checks as security boundaries; invented tenant/workspace semantics; sensitive backup/export/log data overlooked; security by obscurity; broad restriction without threat; recovery bypassing authorization.

## Team interface
Domain/data clarifies ownership; architecture locates enforcement; product/UX makes controls understandable; local-first covers offline authority; quality proves negative/abuse paths.

## Escalate when
A change can expose or irreversibly modify another data realm, weakens a trust boundary, or handles secrets/identity without explicit ownership.

## Output
Assets/threats, trust boundary, controls, residual risk, and targeted negative/recovery tests.
