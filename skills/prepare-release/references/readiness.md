# Readiness notes

Match the checks to the real distribution contract.

| Environment | Evidence that matters |
| --- | --- |
| Portable Windows app | Exact package/executable, intended Windows runtime, launch without installation where required, dependencies, core flow and previous-version return |
| Local or shared JSON | Required paths/files, schema compatibility, interrupted-write recovery, conflict handling and user-data preservation |
| GitHub/package download | Exact release artifact/version, checksum or identity, download availability and a usable previous artifact |
| Actual online service | Relevant environment, migration, access, service signals and controlled rollout/rollback criteria |

A local folder fixture does not prove behavior on the company's actual shared drive. A browser build does not prove a native executable, plugin host or audio route. Keep each untested boundary visible without blocking unrelated preparation.

For recovery, name the trigger, authorized operator/action, previous artifact, affected data/schema and success check. An old executable is not a complete rollback if new data is unreadable by it. Retain a protected copy or supported compatibility path before an authorized destructive migration.

Use the project's actual release and quality policies. Example percentages, web budgets, fixed review counts and imagined rollback commands are not new requirements. Verify any command against current project tooling before use. Publishing, external notices and recurring monitoring need authority from the task; a readiness method supplies none.
