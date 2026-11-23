# CI efficiency without weaker evidence

Consult this reference when metered build/test/delivery work is expensive or its triggering is being changed. The work cycle owns execution; the CI/CD method owns configuration and provider evidence. This is decision support, not new authority, a test quota or a mandatory audit for every task.

## Establish the actual cost

Use the account, repository visibility, workflows and a bounded sample of run/job/step timings. Separate compute, artifact/cache storage, prebuilds and other billed products. Provider billing records establish charges; elapsed time and rate estimates are different evidence. Check current official rates rather than remembered minute multipliers. Missing billing access leaves the amount and cause of depletion unknown; continue supported optimization without inventing savings.

## Remove repeat work first

| Opportunity | Quality condition |
| --- | --- |
| Local preflight and coherent pushes | Run relevant cheap checks locally and batch related ready changes where practical. Preserve useful checkpoints and required provider checks on the resulting revision. |
| Reuse successful checks | Relevant source/merge, fixtures, dependencies, tools, configuration, environment and event remain applicable. Documentation changes can affect behavior. Previous PR status does not qualify a different merge or release revision. |
| Cancel obsolete verification | Scope concurrency by workflow and PR/branch; complete required checks on the latest revision. Serialize publishing, migrations and other side effects separately with recovery. Lower parallelism alone does not prove lower total compute. |
| Retry a failure | Diagnose the first relevant error. For a supported transient failure, retry only failed jobs and necessary dependents while preserved outputs remain valid. A code/input fix needs checks on its new revision. Repeated green reruns do not repair a flaky test. |
| Build once | Pass the exact tested immutable artifact to delivery, verifying source/run identity, content hash, expected files and event/trust boundary. A mutable latest name or cached binary is not provenance. Retain native/package acceptance. |
| Cache installation | Include relevant OS/architecture, tool and lockfile inputs in keys; preserve reproducible installs, trust separation and clean-miss behavior. Measure restore/save overhead. A cache hit never skips required tests. |

## Narrow checks only with dependency evidence

Map changed risks and their dependency closure to checks before narrowing events, paths or matrices. Shared code, schemas, contracts, dependencies, build/CI configuration, uncertain impact and cross-platform changes need full relevant coverage. Retain supported-platform and native evidence. Move only demonstrated platform-neutral work to a suitable cheaper runner.

Inspect actual required statuses before filtering. A filtered required workflow may remain pending; skipped jobs or an aggregator ignoring failed/missing dependencies may appear green. Use a supported reporting pattern and verify positive, negative and unknown-selection cases. Keep full relevant end validation at the repository's required merge/release boundary; necessary pre-merge checks cannot be deferred to a schedule for cost reasons.

Run inexpensive blocking checks before expensive dependents when safe. Set timeouts from healthy measured workloads with margin; timeout is failure. Avoid unused tool/browser installs and duplicated setup. Job splitting can shorten waiting without reducing billed work; measure both.

## Retain useful evidence and recovery

Upload required deliverables and diagnostic evidence; choose retention from review, investigation and recovery needs. Short-lived artifacts must not be the sole durable acceptance or recovery source. Do not automatically delete existing evidence. Storage cleanup reduces future retained usage, not historical compute or accrued charges.

Keep private sources private. Public visibility, paid capacity, self-hosted runner installation or executing workflows on a personal computer require their own actual authorization and trust/operations assessment; none is a default cost fix.

After changes compare equivalent workloads using run count, total job duration, runner type, retained bytes and available billing records. Confirm required failures still block and artifact/runtime acceptance remains valid. Record observed savings and limits at the existing owner. Do not add a separate ledger or recurring monitoring workflow just to track this reference.

## Current provider details

Consult the relevant official page when making a provider-specific change; no fixed rates are embedded here.

- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Re-running workflows and jobs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs)
- [Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)
- [Workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts)
