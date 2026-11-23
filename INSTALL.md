# Install the workflow in your own environment

This is the implementation entrypoint for an AI agent helping a user adopt this repository. It supports new and existing environments. The user chooses the destination; this source supplies reusable procedures, not personal context, account access or permissions. Read-only inspection does not start installation.

## 1. Establish scope and source

Use the user's current installation request and already supplied destinations. Read their existing operating guide once when configured. Preserve its accepted setup version, preferences, exclusions and owner links. If a required destination is ambiguous, ask one focused question and continue independent preparation. Do not search the author's private accounts or infer a user's preferences from source history.

Select one exact source commit. With Git, resolve the chosen ref using `git rev-parse HEAD` in the selected checkout; for an explicit other ref use a separate checkout at that ref. Verify a clean tracked checkout or read committed blobs at that SHA; never label modified working files as a committed installation. Keep the source fixed throughout installation. Read its `VERSION`, `guidance/catalog.json`, `skills/catalog.json`, [method router](docs/METHOD-ROUTING.md) and [skill workflow](docs/SKILL-WORKFLOW.md). Derive package counts, versions and invocation policies from that snapshot, never from a historical example.

With repository connectors, obtain the commit and fetch dependent files at that same SHA. With a generated bundle, read `BRONNEN.json` and `VERIFICATIE.json`, verify its SHA-256 inventory, and use the recorded commit. A supplied hash inventory proves consistency, not author authenticity; resolve the source using the user's accepted repository. An arbitrary ZIP, unreviewed script or a moving `main` link is not an accepted installation pin.

## 2. Select only the requested destinations

| User's environment | Implementation route | Acceptance |
| --- | --- | --- |
| Durable files or Git, without a required service | [Files installation](docs/INSTALL-FILES.md) | Own Guide, pinned source, index, method access and readback |
| User's chosen Notion workspace | [Notion adapter](distribution/notion-starter/INSTALLATIE.md) | Own verified pages and complete selected native skill packages |
| Native skills supported by the current AI host | [Skill workflow](docs/SKILL-WORKFLOW.md) | Complete packages saved through that host's actual installation mechanism |
| A project repository | [Repository installation](docs/INSTALL-REPOSITORY.md) | Local routing, explicit pin, vendored modules and passing local verifier |

Routes can be combined when requested. A private workspace, paid plan, native skill registry, remote desktop, Git CLI or subagents are not universal prerequisites. Discover actual capabilities; use a supported adapter and report unavailable dependent steps. A host without native skills can read complete pinned method files through its Guide. Call that file-based method access, not native skill installation. Do not install tools, plugins, executables, scheduled tasks or unrelated project migrations merely to imitate the source environment.

## 3. Reconcile the existing setup

Inspect only relevant instructions, navigation, skill packages and their actual owners. Follow pagination and report inaccessible or truncated content. Equal titles do not prove duplicates; a failed search does not prove absence. Preserve personal content, projects, tasks, databases, useful extra skills and local customizations.

At the existing private work/distribution record, compare each affected object: verified identity, function, accepted source, useful unique content, intended change, current authority, recovery and verification. Choose **reuse**, **extend**, **merge**, **replace a bounded obsolete part**, or **decision needed**. Show the compact comparison and execute supported reversible steps already authorized by the installation request; no second blanket permission round. Resolve material conflicts before their dependent writes.

Before changing existing content, save and read back the affected old content and relevant metadata. Refresh the target immediately before the patch and preserve intervening edits. Keep one active general route and one owner per function. Do not recreate databases, remove fields or discard history to match a template. Destructive retirement, sharing changes, sending and new recurring work require their own authority. No permission transfers from another user or historical maintenance record.

For uncertain writes, inspect the exact target and operation identity before retrying. A missing response is not failure. Repeated installation reuses matching objects and packages rather than duplicating them. Without a reliable old base, a difference may be a user's customization; do not overwrite it silently.

## 4. Implement the selected route

Carry out the adapter's steps. Use the [neutral templates](distribution/workflow-starter/templates/Agent-Operating-Guide.md) as inputs, not replacements for a complete existing Guide. Fill required placeholders with verified own locations and the selected source versions. Optional capabilities remain explicitly **not configured** when absent. Keep personal values outside the public source.

Install every base method declared in the selected catalog for a complete base installation, retaining full references, invocation metadata, license notices and original bytes. Compare current installed content before updates. `grill-me` remains explicit-only; other policies come from the catalog and host support. Verify actual package readback where supported. For targeted installation, state the chosen subset rather than claiming the entire collection.

The catalog's external methods are optional integration contracts, not bundled packages or inherited private installations. Reuse only the recipient's verified accepted copy. If absent, use the public or base fallback in the method router and record that limitation. Do not fetch someone else's private adapter, replace custom extensions or activate upstream installers automatically.

Configure one session entrypoint pointing at the user's own Guide or repository-local route. Merge the small entry rule into the host's supported instructions without overwriting other instructions. If account instructions cannot be written through available tools, supply the completed text and mark only that manual step pending. Source files in a temporary directory are not durable installation.

## 5. Verify and hand over

Record the selected commit, guidance/collection/package versions, destinations, changed objects, hashes, recovery references and remaining limits at the existing owner. Confirm:

- The own Guide and all required routes are saved, readable and free of unresolved required placeholders.
- The selected source and complete packages match; extra skills and existing project/task owners are preserved.
- A normal task reaches its method, a simple explanation needs no project scan or full process, and a missing tool blocks only dependent work.
- A second pass reuses the existing setup. Recovery restores only this installation's changes, preserving later user edits.
- A genuinely fresh session can read the saved entrypoint and find the configured index and methods. A same-session walkthrough or structural test is labeled as such. No host-wide guarantee is claimed.

For a new account, fresh-session or native-host acceptance may require the user's own supported action. Complete all other ready steps and name the exact remaining action. An installable repository, a saved Guide, native installation and observed use are different outcomes.

## Optional transfer bundle

When the user needs an archive, a repository maintainer can run `python tools/export_workflow_starter.py --source-ref <exact-commit> --output <chosen-file.zip>` from a checkout containing that commit. The exporter reads one committed snapshot, includes full method archives and source hashes, and does not install anything or call external accounts. The legacy `export_notion_starter.py` command delegates to this generic exporter. Bundle generation does not authorize publication or installation.
