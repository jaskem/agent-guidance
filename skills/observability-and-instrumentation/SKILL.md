---
name: observability-and-instrumentation
description: Design or implement durable signals that make an operation's health and failures detectable and diagnosable. Use for persistent logging, metrics, tracing, alert rules or a demonstrated diagnostic blind spot; exclude ordinary one-bug diagnosis, temporary debugging and measured performance optimization.
---

# Observability and instrumentation

## 1. Identify the diagnostic gap

Follow the configured operating guide once per session, including its required tool-call version, and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Read the operation, runtime, existing instrumentation and requested scope. Distinguish an assessment or design from an authorized implementation.

Write the concrete questions the signals must answer: whether work succeeded, what failed, which run was affected, or where execution stopped. Identify the healthy result and a known failure that would distinguish useful evidence from noise. Keep immediate bug diagnosis with evidence-driven-development, measured performance work with optimize-performance and release acceptance with prepare-release.

## 2. Choose the smallest useful signal

Map each question to an event, aggregate measure, trace, health check or alert. Reuse the actual platform and existing conventions. A structured local file can be sufficient for an offline application; do not require a collector, dashboard, tracing service or new cloud dependency by default.

Specify event meaning, fields, correlation, units and relevant boundaries. Allowlist useful fields; protect secrets and personal data in logs, spans and exports. Bound label cardinality, output volume, buffering and retention. Make sampling gaps and collection delay explicit. Read [signal cases](references/signal-cases.md) for multiple entry points, offline output, cardinality, missing data or instrumentation failures.

## 3. Add signals at meaningful boundaries

Route authorized code changes through the established development/review owner. Use stable event names and machine-readable fields. Set run identity and entry-point identity where work begins, and preserve them across the relevant calls, queues and processes. Distinguish individual attempts, terminal outcomes and recovery so retries do not misstate success or failure.

For aggregate questions, choose bounded dimensions and useful distributions. For alerts, state the actionable condition, evidence for its threshold and window, first diagnostic query and existing response owner. Reuse established severity and response conventions. Preserve the operation's specified behavior when instrumentation is slow or unavailable.

## 4. Verify emitted evidence

For implemented signals, exercise a representative healthy run and a known failure in an authorized environment. Inspect the actual saved or collected output. Locate the affected operation through its signals and confirm that the selected fields answer the diagnostic questions without relying on source-code inference. Check correlation across relevant boundaries, sensitive fields, counting and missing-data behavior.

For an alert, test both the failure condition and healthy control. Use a safe test sink unless real notification is already authorized. Verify delivery only where exercised; distinguish a passing local rule from an untested remote collector or destination. Do not induce production failures by implication. Record exact inputs, revision, environment, output and any unverified path.

## 5. Leave usable diagnosis

Update the existing code, operational notes or task owner with signal meanings, a working lookup or query, limits and the response path. Remove task-created diagnostic noise that does not serve the agreed questions; preserve useful existing evidence and unrelated work.

For implementation, finish when the healthy and failed cases can be distinguished and the failed case can be located and explained at the stated boundary using the emitted evidence. For a design, deliver that verification procedure and identify the untested parts. Report durable detection and diagnosis only to the extent observed; do not create a parallel tracker or monitoring schedule.

For provenance when updating this method, read [sources](references/sources.md).
