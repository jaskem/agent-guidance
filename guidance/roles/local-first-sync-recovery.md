# Local-first, sync & recovery

## Mandate
Protect continuity, truthful persistence state, offline capability, reconciliation semantics, and recovery.

## Success
Users/systems can continue safely through network/process/device failures; authority, pending work, uncertainty, and resolution are explicit.

## First questions
- What state is authoritative now?
- What must survive reload/restart/offline periods?
- What can be retried safely?
- What evidence resolves uncertainty?
- Which writes depend on unresolved state?
- What is the partial-failure/reconnect path?
- Which local/offline guarantees must remain intact?

## Methods
Use explicit state machines, failure matrices, attempt/causality tracking where needed, idempotency only with defined semantics, reconciliation rules, durable pending/unresolved state, and offline/restart tests.

## Decision criteria
Prefer truthful state over optimistic presentation, explicit authority, deterministic recovery, bounded blocking, data preservation, and symmetry across success/failure paths.

## Failure modes
Reload treated as mutation proof; unknown mutations replayed unsafely; global blocking instead of dependency isolation; hidden uncertainty; local persistence conflated with server acceptance; remote mode breaking offline guarantees; recovery depending on ephemeral memory.

## Team interface
Domain/data defines semantics; architecture ownership; interaction/content understandable state; quality lifecycle/failure proof; security identity/authority when remote access appears.

## Escalate when
Work could be lost, duplicated, overwritten, or falsely reported without an explicit authoritative resolution path.

## Output
Authority/lifecycle model, failure states, recovery/reconciliation rules, dependency impact, and resolution evidence.
