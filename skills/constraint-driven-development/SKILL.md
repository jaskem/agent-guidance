---
name: constraint-driven-development
description: Establish or repair a project's quality requirements and prove how their controls enforce them. Use for missing quality rules, unclear blocking checks, unjustified thresholds or checks weakened to pass. Exclude routine feature work, running existing checks, fixing one test and pipeline configuration with already settled requirements.
---

# Constraint-driven development

## 1. Recover the existing quality contract

Follow the configured operating guide and its active tool-call version once per session; reuse verified context. Resolve the relevant project, task, norm owner and authorized change. Read accepted criteria, existing checks, configuration, baseline results and exceptions before asking questions. Preserve unrelated work and existing ownership; do not create another tracker or require a new constraints file.

Separate task acceptance from the standing quality requirements. Identify the concrete gap: absent rule, unsupported target, ineffective control or unauthorized weakening. Missing access makes that part unknown; continue independently supported work.

## 2. Define only the missing requirements

Choose dimensions from the actual product, risk and request. Reuse accepted targets; otherwise use an applicable standard or a representative measurement with its rationale. Ask only when a consequential quality or cost choice remains unresolved. Keep proposed targets visibly proposed; do not invent a baseline or import a provider's default numbers. A plausible schema, type or unit assumption is not an accepted blocking requirement. Preserve the documented contract and surface any consequential missing specification instead of silently tightening it during a repair.

For each rule record its scope, reason, measurement or check, execution stage, expected failure behavior and owner. Distinguish required, advisory and measured-only rules. Read [control evidence](references/control-evidence.md) for the record and verification cases. A number without an executable or otherwise repeatable check is not enforced.

## 3. Connect rules to proportionate controls

Use existing supported tooling first. Verify tool versions, report formats, dependencies and authority before adding a control. Scope fast checks to relevant changes; place expensive or runtime checks where their required environment exists. Reuse valid results when the relevant revision and conditions have not changed.

Use evidence-driven-development and code-review for substantive code/configuration changes. Use ci-cd-and-automation for a distinct pipeline integration; this method owns what must be enforced, not a second CI procedure. Missing specialist access leaves the dependent work open, not permission to claim its result. Do not install upstream helper scripts merely because they are supplied.

## 4. Prove the control can reject a violation

Exercise the actual check with a safe deliberate violation and a clean control. Test an unavailable tool, malformed/incomplete result or equivalent execution failure: it must not become a pass. For severity thresholds, also test an allowed result below the blocking boundary. Use the environment and command that will make the real decision; a local simulation establishes only its own scope.

Delegate a useful independent check when the host supports it. Supply raw artifacts and the requirement, keep one writer per shared object, and verify the returned evidence yourself. Record exact revision, command/action, inputs and observed outcomes. Restore any controlled test changes and verify the final state.

## 5. Protect the requirement and handle exceptions

Compare the change with the accepted baseline. Investigate removed checks, lower thresholds, skipped tests, removed assertions, new suppressions and exceptions. Judge their semantic effect; a textual match is a finding to inspect, not proof of a violation.

Do not weaken a requirement to make unrelated work pass. Record an authorized exception with scope, reason, owner and expiry or review trigger; preserve the unmet criterion as unmet. For a measured baseline that must not worsen, compare equivalent measurement conditions and account for noise. Changing the measurement method requires an explicit comparable baseline, not a concealed reset.

## 6. Report the actual enforcement state

Update the existing norm and task owner with the rules, controls, evidence and exceptions. Distinguish documented, implemented, verified and actually blocking controls. Confirm the saved state. If merge/release protection or the target environment could not be inspected, state that enforcement remains unverified and name the next check.

Finish with a usable quality contract and demonstrated controls, or precise unresolved portions. Installing this method adds no project tools, thresholds or approval gates by itself.

For provenance when maintaining this package, read [sources](references/sources.md).
