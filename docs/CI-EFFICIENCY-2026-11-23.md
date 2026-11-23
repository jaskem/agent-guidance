# CI efficiency — 23 November 2026

## Requested result and ownership

The user requested lower GitHub Actions consumption in the standard workflow without weakening task execution, workflow quality or delivered results. The existing work cycle owns the core rule; the optional [CI efficiency reference](../guidance/resources/ci-efficiency.md) supplies detailed decisions. The existing CI/CD method remains the pipeline configuration owner. No new skill, tracker or scheduler is introduced.

The baseline is `ebd5025d136a57daf0aea5395cb86f0cb0bcad90`, guidance 0.8.0, collection 1.4.2. All 211 source blob hashes and the complete tree `3964078ce5585dc5a3da36b3a9512bc718ddb3a4` were verified before editing. Local Git was initialized from those exact source bytes; its snapshot commit is not the original remote commit. Product repositories retain their own owners and pinned versions.

## Bounded observations

Read-only inventory covered the six accessible repositories owned by the user. A worker inspected at most 30 recent runs in each of the four application/foundation repositories below; the parent inspected the guidance and DXF runs and independently fetched the job timing records listed here. Durations are completed job elapsed seconds, not billed amounts, account totals or an estimate of monthly savings.

| Repository | Observed job time | Evidence and decision |
| --- | --- | --- |
| DXF-viewer | Windows recognition 597 s + Windows package 348 s + Linux release safeguard 15 s; separate Python desktop job 835 s on the same PR update | [Package run](https://github.com/jaskem/DXF-viewer/actions/runs/45165522253), [desktop run](https://github.com/jaskem/DXF-viewer/actions/runs/45165522242). Native and packaged acceptance are distinct evidence; investigate duplicated setup/test work and push frequency before removing checks. |
| project_data_pipeline | App job 1020 s; its UX-shell step 501 s. Separate Pages build/deploy 66 s + 44 s | [App run](https://github.com/jaskem/project_data_pipeline/actions/runs/44749358388), [Pages run](https://github.com/jaskem/project_data_pipeline/actions/runs/44749358475). Candidate: share the exact tested build and preserve deployed revision/HTTPS checks. Pages currently finishes before full app checks; changing this chain requires a bounded product-repository change. |
| taskline | Verification 393 s + publish 25 s; separate Codespaces prebuild 1298 s | [App run](https://github.com/jaskem/taskline/actions/runs/44894133201), [prebuild run](https://github.com/jaskem/taskline/actions/runs/44894132842). Candidate: publish the verified artifact rather than rebuilding; separately inspect prebuild policy and billing category. Official GitHub documentation confirms that prebuild creation uses Actions compute; the actual account charge remains unverified. |
| landscape-core | Schema checks 24 s + foundation 4 s | [Run](https://github.com/jaskem/landscape-core/actions/runs/44893719534). Small measured workload; retain coverage. |
| landscape-platform | Foundation 9 s | [Run](https://github.com/jaskem/landscape-platform/actions/runs/44893725331). Small measured workload; retain coverage. |
| agent-guidance | Recent runs cover PR and main events | [Existing main run](https://github.com/jaskem/agent-guidance/actions/runs/44891141828). Different events/revisions are not automatically duplicates. |

[GitHub documents](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds) that prebuild workflows consume Actions usage and can update on every push. Their purpose is faster environment startup; changing their cadence must preserve the required development environment and account for startup latency.

All six discovered repositories were private. The billing endpoint is outside the GitHub connector's supported operations; the originating browser connection was unavailable. Actual plan, charged SKUs, monthly usage, storage overage and cause of allowance exhaustion remain unverified. A read-only personal-device directory/capability check made no changes; it did not provide billing evidence. No public/private visibility, paid capacity or self-hosted runner change is authorized by these observations.

## Implemented decision rules

- Establish changed risks, required checks and applicable existing evidence before spending hosted compute. Prefer suitable local preflight and coherent ready pushes.
- Remove duplicate builds/setup, retry only supported failures, cancel obsolete verification safely and preserve exact tested artifacts through delivery.
- Require dependency coverage before narrowing checks. Unknown/shared/schema/build/platform changes keep full relevant checks. A cache hit or skipped job never qualifies omitted testing.
- Keep required statuses, native/package/security/regression acceptance, source identity and release recovery. Retention follows review and evidence needs.
- Compare equivalent workloads and actual billing before claiming savings. No fixed test quota, obsolete OS multiplier, automatic cleanup or monthly percentage promise.

## Scope and adoption

Only repository-independent guidance and its routing/catalog/documentation are changed. The existing method packages, skill versions, setup instructions version 0.0.6, consumer pins, product workflows, required-status settings, deployment policies and automations remain unchanged in this batch. Their current behavior is not reported as optimized.

The personal operating guide can point to the reviewed canonical source within this explicit user request. This makes the decision rule available to sessions that read that route; it does not mechanically enforce future reasoning or install the optional module into pinned consumers. Each project pipeline optimization and vendored update remains a separate explicit repository batch.

## Validation and recovery

Use the existing foundation, skill-package and unittest checks on clean tracked source. The separate review and nine task-local synthetic reasoning cases cover ordinary work, adjacent valid retries, unknown dependencies, platform-specific output, required filters, mutation concurrency, missing billing, a simple excluded chat and cache/artifact trust. These are bounded review evidence, not executed GitHub failure/concurrency experiments or a causal savings study. Actual results and activation references belong to the existing maintenance record, not a second registry.

Recovery: revert only this batch's guidance/routing/version/documentation changes to the accepted baseline above, run the affected repository checks, and restore the previous personal guide pointers with readback. Do not reset consumer repositories or change their pins. There is no product deployment to roll back.

The first product-side opportunity is a separately scoped audit of the exact tested-artifact chain and required checks in the heaviest workflows; preserve active work and verify passing/failing events before adopting a configuration change.
