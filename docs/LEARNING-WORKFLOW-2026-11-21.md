# Continuous workflow improvement — 21 November 2026

## Accepted objective and boundaries

The user requested automatic refinement of the workflow, updates to skills, discovery of missing skills and an effective, reliable implementation. Learning here means changing versioned guidance, checks and reusable skills from evidence; it does not retrain the underlying model.

The [instruction feedback loop](../guidance/playbooks/instruction-feedback-loop.md) owns the procedure. The configured personal operating guide owns the maintenance grant and cadence; the existing distribution/work record owns observations, decisions, installation evidence and last successful maintenance checkpoint. This document records this implementation, not another task tracker or runtime policy.

Source baseline: workflow commit `cb16682b0c38e59de3fbf1c59626d6f3120930c0`, tree `7f4d58e3e87b0340dc3513367ab78c7bd70a735b`. Local baseline tree was compared with the published source before editing. Shared guidance becomes 0.8.0; collection 1.4.1 records the existing online adapter patch 1.0.1 while all 32 procedure packages retain their versions. Setup remains 0.0.6. Project pins are not upgraded in this batch.

## Implemented mechanisms

- Real work supplies a compact, deduplicated observation only for a material reusable error, user correction, repeated workaround or demonstrated capability gap. Ordinary product defects retain their product owner; successful tasks need no extra maintenance ceremony.
- A separately registered weekly maintenance run inspects new observations and changed relevant sources. It uses a bounded source/candidate budget, checks existing coverage before discovery and can return no change. Existing memory/setup and cleanup schedules retain their scopes.
- A candidate is prepared separately, compared with baseline and representative regressions, reviewed independently and activated only within the actual standing grant. Unknown or missing evidence leaves it pending. New permissions, setup versions, product contracts and consumer pin changes retain their own authority.
- [The learning evidence checker](../tools/check_learning_change.py) validates a compact JSON record and returns eligible, manual_review or blocked. It has no network, installation or mutation path. It checks the evidence contract; it cannot prove assertions true or replace host permission checks, source review or observed execution.
- Source/installed content and invocation settings are verified separately. The previous known-good content/reference and restore procedure remain available. A demonstrated regression stops further promotion and triggers authorized restoration with readback.

## Evidence contract

A record supplied to the checker includes identity/kind, true owner and authorization reference; observed effect/evidence; exact base/candidate references and outcomes; positive, excluded, missing-input and regression checks; independent resolved review; risks; and a restore reference/procedure. A pass-to-pass change additionally needs a finite measured benefit with the expected direction. New or refreshed external content needs exact source revision, license and complete content review; a new skill also needs a demonstrated distinct outcome and comparison with existing routes.

The exact field shape is exercised by `valid_record` in `tests/test_learning_change.py`; its synthetic references are test fixtures, not actual evidence or authorization. Run `python tools/check_learning_change.py <record.json>` from the canonical checkout. Exit 0 means the record meets preflight requirements, 2 means an actual decision/authority boundary remains, and 1 means required evidence is invalid/missing or prohibited. Referenced proof must still be inspected. The existing work record remains the durable owner; JSON input/output is a verification artifact, not a competing registry.

## Initial pilot and acceptance

The bounded initial pilot addresses unnecessary index retrieval in the accepted online Modern Web Guidance adapter. An earlier task fetched an unnecessarily large README before selecting known guide paths. The candidate gives the already-declared path map priority, keeps the exact upstream pin and narrows index output; backend-only scope and missing-source fallback remain unchanged. Its baseline/candidate trials, review, gate and actual distribution outcome are retained in the existing private work record. The paired table trial returned the same two full guides with 140,251 versus 12,260 fetched source characters. Parent and reviewer independently re-fetched those immutable payloads. Both proposals retained the task constraints; adjacent valid, excluded and constrained missing-source cases were reviewed. This is one bounded payload comparison based on agent returns, not complete execution logs or time/token/UI/long-term evidence. The initial incomplete record was blocked; after actual supporting checks/review and durable evidence capture, preflight returned eligible. The saved rollback content was byte-verified; no live restore is claimed. Inconclusive evidence must not be described as proven improvement.

Acceptance covers foundation/package checks, the new checker's fail-closed/decision cases, source and distribution comparison, behavioral trials and a real scheduler registration. Future scheduled execution and long-term reliability remain unobserved until those runs occur. A registered schedule does not mean all clients can access the same context or enforce this protocol.

## Primary sources inspected

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): outcome-based evaluation, representative tasks, regression coverage and calibrated grading. Source principles inform the protocol; no vendor eval service is required.
- [Google SRE: Canarying Releases](https://sre.google/workbook/canarying-releases/): small reversible changes, separate evaluation and production observation, explicit stop/restore behavior. This implementation does not claim traffic splitting where the host cannot provide it.
- [Anthropic: Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise): complete skill inspection, coexistence/trigger evaluation, exact versions and recovery. Vendor-specific controls are not assumed to exist here.

No universal success score, automatic trust in source popularity, quota for new skills or removal of local user customizations is introduced. Real benefit is evaluated per task/outcome, including whether a smaller skillset or simpler rule performs better.
