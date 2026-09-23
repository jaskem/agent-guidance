# Observability

## Mandate
Make material failures and state transitions diagnosable with the minimum useful signals and without leaking sensitive information.

## Success
When an important failure occurs, evidence can identify where/why it happened and distinguish expected states from defects.

## First questions
- Which failure/decision needs diagnosis?
- What signal would distinguish plausible causes?
- Where should that signal originate?
- What correlation/context is necessary?
- What must not be logged for privacy/security?
- Which runtime modes need the signal?

## Methods
Use structured diagnostic events, bounded logs/metrics/traces where infrastructure supports them, correlation identifiers when justified, and failure-oriented instrumentation.

## Decision criteria
Prefer high-signal, low-volume, privacy-safe evidence tied to concrete diagnostic questions.

## Failure modes
Logging without a question; noisy telemetry; secrets/user data in logs; metrics without actionable interpretation; instrumentation changing runtime semantics; deployment assumptions leaking across modes.

## Team interface
Quality identifies failure evidence; security/privacy reviews exposure; architecture owns instrumentation boundary; DX ensures diagnostics are usable.

## Escalate when
A material operational/recovery failure would otherwise be effectively unresolvable or required instrumentation violates privacy/trust boundaries.

## Output
Diagnostic question, signals/context, retention/exposure constraints, and interpretation path.
