# CI efficiency — 23 November 2026

## Requested result and ownership

The user requested lower GitHub Actions consumption in the standard workflow without weakening task execution, workflow quality or delivered results. The existing work cycle owns the core rule; the optional [CI efficiency reference](../guidance/resources/ci-efficiency.md) supplies detailed decisions. The existing CI/CD method remains the pipeline configuration owner. No new skill, tracker or scheduler is introduced.

The baseline is `ebd5025d136a57daf0aea5395cb86f0cb0bcad90`, guidance 0.8.0, collection 1.4.2. All 211 source blob hashes and the complete tree `3964078ce5585dc5a3da36b3a9512bc718ddb3a4` were verified before editing. Local Git was initialized from those exact source bytes; its snapshot commit is not the original remote commit. Product repositories retain their own owners and pinned versions.

## Historical evidence and privacy limits

The original investigation included account-linked repository and completed-job observations. This revision removes repository identities, run/job identifiers, URLs, job labels, timestamps, measurements and account/access details from the public evidence copy. The [historical sample path](evidence/ci-job-sample-2026-11-23.json) now contains an explicit redaction record with no run data. The removed observations cannot be reproduced or independently checked from these retained files. No replacement run, new measurement or new runtime verification is claimed.

The following are generic decision scenarios, not anonymized measured runs or new test results.

| Scenario | Decision to assess |
| --- | --- |
| Native tests and packaged acceptance | Check duplicated setup and push frequency while preserving their distinct runtime claims. |
| Verification followed by publication | Reuse the exact verified artifact where supported and retain deployed revision and endpoint checks. |
| Development-environment prebuilds | Assess startup benefit, update cadence and the applicable billing category separately. |
| A short foundation workflow | Keep required coverage; elapsed duration alone is no reason to change it. |
| Pull-request and default-branch events | Establish event, trust and revision differences before treating runs as duplicates. |

[GitHub documents](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds) that prebuild workflows consume Actions usage and can update on every push. Their purpose is faster environment startup; changing their cadence must preserve the required development environment and account for startup latency.

No account billing, monthly usage, storage charge or cause of excess usage is established by the retained record. Job elapsed time would not by itself prove billed cost or monthly savings. Visibility changes, paid capacity and self-hosted runners require their own actual authority and operational assessment; this historical record supplies none.

## Implemented decision rules

- Establish changed risks, required checks and applicable existing evidence before spending hosted compute. Prefer suitable local preflight and coherent ready pushes.
- Remove duplicate builds/setup, retry only supported failures, cancel obsolete verification safely and preserve exact tested artifacts through delivery.
- Require dependency coverage before narrowing checks. Unknown/shared/schema/build/platform changes keep full relevant checks. A cache hit or skipped job never qualifies omitted testing.
- Keep required statuses, native/package/security/regression acceptance, source identity and release recovery. Retention follows review and evidence needs.
- Compare equivalent workloads and actual billing before claiming savings. No fixed test quota, obsolete OS multiplier, automatic cleanup or monthly percentage promise.

## Scope and adoption

The original batch changed repository-independent guidance and its routing/catalog/documentation. Existing method packages, skill versions, accepted setup instructions, consumer pins, product workflows, required-status settings, deployment policies and automations were outside that batch. Their current behavior is not reported as optimized.

A recipient can deliberately route their own Guide to an accepted immutable source under their current installation authority. Reading that route makes the decision rule available; it does not mechanically enforce future reasoning or install the optional module into pinned consumers. Each project pipeline optimization and vendored update retains its own owner and scope. Historical authorization and setup choices are not permissions for another recipient.

## Validation and recovery

Use the existing foundation, skill-package and unittest checks on clean tracked source. The separate review and nine task-local synthetic reasoning cases cover ordinary work, adjacent valid retries, unknown dependencies, platform-specific output, required filters, mutation concurrency, missing billing, a simple excluded chat and cache/artifact trust. These are bounded review evidence, not executed GitHub failure/concurrency experiments or a causal savings study. Actual results and activation references belong to the existing maintenance record, not a second registry.

Recovery: revert only the original batch's guidance/routing/version/documentation changes to the accepted baseline above and run the affected repository checks. Restore only affected configured distribution pointers within actual current authority, with readback. Do not reset consumer repositories or change their pins. There is no product deployment to roll back. Historical recovery does not authorize restoring redacted personal evidence into a current public source.

The first product-side opportunity is a separately scoped audit of the exact tested-artifact chain and required checks in the heaviest workflows; preserve active work and verify passing/failing events before adopting a configuration change.
