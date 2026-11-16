---
name: ci-cd-and-automation
description: Configure or repair a software build, test or delivery pipeline and verify its triggering, results and enforcement. Use for CI/CD setup, missing jobs, incorrect filters, runner failures or ineffective required checks. Exclude merely running existing tests, defining quality thresholds, release-only preparation and ordinary ChatGPT reminders or scheduled tasks.
---

# CI/CD and automation

## 1. Establish the pipeline boundary

Follow the configured operating guide and its active tool-call version once per session; reuse verified context. Resolve the relevant repository, work item, configuration owner, current revision and permitted actions. Inspect the real provider, workflow events, branches, runner, dependency/lockfile policy, checks, artifacts and available protection settings. Preserve existing changes and task ownership.

Separate a configuration request from authorized deployment or scheduling. Existing permission persists; the method adds none. If the provider or settings are inaccessible, continue supported configuration analysis and identify the exact unverified behavior.

## 2. Map requirements to jobs and events

Use accepted quality rules and release requirements. Read [pipeline evidence](references/pipeline-evidence.md) for event, trust and result boundaries. Identify which changes need which checks, their dependencies, environment and outputs. Verify that filters and conditional jobs cover the relevant path; a fast pipeline that omits required work is not complete.

Place inexpensive checks early and independent jobs in parallel when useful. Reuse results only for the same relevant revision and conditions. Choose budgets from the actual workload and project needs, not fixed web-stack timings. Use constraint-driven-development only when the quality requirements themselves need a distinct decision or repair.

## 3. Make the smallest coherent change

Use the project's actual package manager, lockfile, wrappers and runner-supported commands. Verify version-specific syntax against the provider's official documentation when needed. Scope permissions and secrets to the job and event that require them; do not give untrusted code privileged credentials to make a run succeed.

Use evidence-driven-development and code-review for substantive code/configuration changes; this method owns pipeline behavior. Do not replace unavailable specialist evidence with a completion claim. Delegate bounded independent checks when useful, provide raw configuration/run artifacts, keep one writer per shared object, and verify the integrated result.

Keep build, check, artifact and deployment decisions explicit. Preserve an applicable recovery route for delivery changes. Use prepare-release for a distinct release acceptance or publication task rather than duplicating that procedure.

## 4. Observe actual execution

Validate configuration locally with available project tooling, then inspect a run on the intended provider, revision and event where authorized. Confirm required jobs actually executed, dependencies and artifact identities agree, and the final result represents their outcomes. A valid YAML file or local test run does not establish runner behavior.

Use an authorized isolated branch or safe fixture to check a deliberate failure as well as a passing case. Confirm failed checks, missing outputs and tool errors cannot be swallowed by wrappers, conditions or aggregation. Restore test-only changes and verify the final candidate. If no live run is possible, report configuration-level evidence and the first unproven runtime check.

## 5. Verify the decision boundary

Inspect whether the appropriate status checks are actually required for the intended merge or release, including relevant branches and events. Distinguish a failed job from an enforced block. If protection settings cannot be read, mark enforcement unknown rather than inferring it from workflow configuration.

For delivery, trace the source revision through the built artifact to the intended destination. Execute publication only within existing authorization and verify the observed result. Missing release acceptance stays open; pipeline success alone does not qualify a release.

## 6. Close with reproducible evidence

Update the existing work owner with configuration revision, event, run/job identifiers, commands, artifact identity, observed checks, protection evidence and limits. Confirm the saved state. Finish with demonstrated pipeline behavior or explicit unverified portions and next actions.

Do not create a parallel tracker, send notifications or schedule recurring execution merely because this method ran. Route ordinary reminders and ChatGPT scheduled tasks to the host's scheduling capability.

For provenance when maintaining this package, read [sources](references/sources.md).
