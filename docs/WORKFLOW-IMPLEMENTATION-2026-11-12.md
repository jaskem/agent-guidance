# Workflow implementation — 2026-11-12

## Scope and source

Implement the accepted workflow plan using small task methods and the existing specialist roles. Baseline: `jaskem/agent-guidance@4eff666f08534e7f2912bfcf0d597a97f40cf10f`. The reviewed upstream remains `mattpocock/skills@5863806dd4e15c63174bee4e7515a4256792ecfa`. This is an original adaptation, not a bulk plugin import or automatic upstream updater.

Scenario: F0/F2 for optional methods and their router, plus F1 for package dependency validation. Consumed central route: `AGENTS.md`, `guidance/KERNEL.md`, `docs/WORKFLOW.md`, `docs/SKILL-WORKFLOW.md`. Roles remain unchanged; the routing table identifies when to load them rather than claiming all were active in every exercise.

## Implemented source changes

- Six methods cover planning, domain modeling, prototypes, change review, durable handoff and learning through project code.
- `evidence-driven-development` 1.1.0 delegates review to `code-review`; the two-axis review method has one owner. Review-only tasks route directly there.
- The method router connects each task to its finish criterion and the existing 15 role sources, with consumer instructions and version pins retaining authority.
- The catalog declares required method dependencies. Offline checks reject missing and cyclic dependencies; this does not prove runtime invocation.
- The shared `guidance/` files, version 0.4.0, consumer lock schema and vendoring contract are unchanged. Existing consumers do not receive changed guidance merely because these optional methods were added.

## Ownership and rollout

Repository plans, product decisions, tasks and checkpoints remain with their existing owners. Notion provides private navigation and dated summaries. Personal installations and Notion Skills distribute the canonical packages; their verification records must name a published source revision. A locally validated package is a candidate until source publication and installation verification succeed.

Consumer routing changes are separate PRs and preserve local workflows. This source release neither merges consumer PRs nor proves product behavior. Installation order must satisfy the catalog dependency: make `code-review` available before activating the changed development method. Keep the previous version available for recovery.

## Validation record

- Clean committed source: foundation check passed with guidance version 0.4.0 and 25 modules; skill package check passed; all 15 unittest cases passed (11 package checks and 4 vendoring checks). The two added failure cases reject an unknown required method and a dependency cycle.
- Host validation: six new packages and the changed development package passed the host validator in the actual personal-skill workspace. Installation is verified separately after publication.
- Requirements and quality integration review: the implementing agent inspected all six new method bodies and branch-specific references; a separate parent integrator read the central diff and review/handoff/prototype methods. No blocking defect was found in those scopes. The parent review shared session context, so it is not described as a blind independent release review.

| Behavior exercise | Observed result | Boundary |
| --- | --- | --- |
| Planning-only CSV request without code | Produced three behavior slices, left duplicate policy explicitly undecided, did not invent technology or write files | Fresh-context case, not an implementation test |
| Domain identifiers equal in a sample | Kept product identity separate from row ordering; used a labelled hypothetical reorder counterexample | No schema/code migration |
| Review with green tests | Pinned fixture base `23dfe11` and head `ddb2135`; existing two tests passed, but reproduced 5000 giving 495 instead of required 0 and negative input giving 495 instead of ValueError | Correctly separated a pre-existing omitted requirement; no review-only edit |
| Existing DXF route baseline | Found current main `3b6b45d` and open/unmerged PR #7; corrected unsupported live-publication note and proposed next code lesson | Existing route already handled this case; no superiority claim |
| New handoff plus teaching on DXF | Corrected the same stale publication premise, traced client save through portable server/storage, distinguished JSON/D1 and untested two-PC operation; offered an exercise without claiming mastery | Read-only source-backed pilot; prompts differed, so not a controlled A/B study |

Additional exclusion/missing-input trials in the fresh-context worker returned a simple CSV explanation without planning ceremony, explained an established identifier without a domain-design workflow, and requested the missing repository/diff instead of inventing review findings.

Prototype: an isolated two-variant experiment exercised the actual handler script against a simulated DOM. Six transitions passed (left, reset, variant B, right, skip, variant A). This was a direct experiment by the author, not an independent rendered-browser evaluation. Real Chromium attempts failed first because the bundled executable was unavailable and then because system-browser socket startup returned EPERM. No rendered UI, keyboard accessibility or visual acceptance is claimed; an end-to-end browser pilot remains a concrete limitation before claiming such quality. The remote PR identifies the exact tested release head; the distribution record identifies the merged source and verified host copies. These exercises do not measure general reliability, speed improvement, automatic selection by every host, or product live behavior.

## Project-context extension

Source baseline: `8b99d6e859c8b6b6192738c33a4d63859dc792e8`. Scenario F2, optional package and routing only. All baseline tracked blobs were compared with the remote main tree before editing. The shared modules, VERSION, eight existing methods and consumer pins are unchanged.

Added `maintain-project-context` 1.0.0 for a distinct recurring operation: reconcile project homes and portfolio navigation with verified owners. Initial planning, single-task handoff and instruction maintenance retain their own methods. The package separates enumeration coverage, exact source identity, project-specific task ownership, dated evidence, scoped patches and uncertain-write readback. Matt Pocock's writing-for-agents (including skill mechanics) and chief-of-staff source were read at the existing pinned upstream revision. Only the bounded wiki/source-pointer ideas are adapted; no mandatory delegation, strategic expansion or schedules are imported.

A fresh-context agent executed the method on supplied Aster/Haven artifacts, without expected answers. It kept two same-name Aster homes with different source IDs separate; preserved local-code/Notion-task ownership; marked a deployment claim unsupported; refused to equate a complete empty Spaces listing with ChatGPT Projects coverage; required exact readback after a Haven timeout; and preserved a concurrent release-checklist note. It answered an unrelated repository-definition question directly. These are read-only behavior trials with supplied artifacts, not live Notion write or exhaustive reasoning tests. The agent identified missing operating guide/index inputs rather than inventing them.

Requirements and quality were checked separately by the author against the accepted scope and full package. The package is self-contained, uses capability-based source discovery and has no runtime dependencies. Existing structural regression tests cover its catalog registration, local references and metadata; no text-matching tests were added. Host validation passed in the actual installation workspace. Foundation/package checks and all 15 unit tests are required on the clean committed source and in PR CI before publication. Installation and Notion readback remain distinct downstream evidence recorded privately.

Compatibility: additive optional method; existing project owners and consumer routes remain authoritative. Next technical step after source publication: verify complete personal and enabled Notion distributions against the released package.

## Context entry and bounded delegation

Source baseline: published `b20f7d4b98d6d8577610c624644d80d36e33968a`. The edited kernel, catalog, VERSION and this record matched current GitHub main blobs before editing. Scope: F0 shared behavior and F3 version closure after structural inspection; the integrating release also updates skill routing separately. All 15 role modules remain unchanged.

Added two provider-neutral playbooks with distinct triggers: `context-entry` for a configured guide/project/task route, and `delegation` for authorized parallel work or useful separate review. The kernel owns the compact principles and routes to these selected modules. Context handling reads a required guide once per session, locates each project's real owners, refreshes only potentially invalidating changes and treats unavailable access as a limit. Delegation assigns scoped source/resource ownership, covers shared external editors and interrupted workers, preserves authorization, and makes the parent verify integration at the actual result revision. A temporary worker is not a scheduled or persistent agent.

The existing 25 module IDs remain stable; two playbooks bring the catalog to 27 modules. Guidance version is 0.5.0. No lock/schema/tool change or implicit module expansion was introduced. The kernel route is a consumer-visible behavior change: each migration must explicitly select the new playbooks, preserve local authority rules and verify exact pinned bytes. A consumer that has not migrated retains its existing pin and must not be described as updated. This foundation edit itself changes no consumer or external context configuration.

Validation during authoring: foundation check passed before version closure; the current dirty worktree ran 11 skill structural tests successfully, while the vendoring test class correctly skipped because it requires a clean committed source. The final integrator must run the full clean-checkout suite and behavioral examples before release claims. These checks do not prove automatic loading by every host, live agent coordination, external service access or universal consultation of context.

Integration review preserved the 15 roles and all existing module IDs. Nine independently invocable skills now have the same short configured-context entry, with task ownership resolved separately from code. The review method selects another reviewer by risk and independent value rather than change size alone. Skill versions: evidence-driven-development 1.1.1; maintain-agent-instructions 1.0.2; the other seven 1.0.1. The configured personal guide is linked only from the repository-local router; shared modules remain provider-neutral.

Fresh-context read-only trials used raw artifacts without expected answers. The delegation/context trial handled five cases: a simple question reused an already-read guide without project scanning; two read-only assessments received bounded source assignments; a second worker could not take an unacknowledged writer's page or desktop; a timeout required exact-target inspection and revision-delta review while preserving a newer user decision; inaccessible Notion prevented an unsupported completion claim while allowing independent source inspection. A separate direct-skill trial followed Notion task ownership for planning, avoided a project scan for a simple CSV explanation, and resolved an uncertain saved change by exact ID without repeating it. These are artifact-based behavioral observations, not live concurrency, browser, network or production tests.

All nine candidate packages passed host validation in the actual personal-skills checkout. Source publication, clean-checkout structural/15-test verification and personal/Notion roundtrip are separate release gates; their exact revisions and completion evidence belong to the PR and distribution record. No text-matching tests were added to simulate behavioral proof.

Next rollout step after source publication: verify the nine updated distributions and explicitly update the configured consumer routes, including the existing Taskline vendoring pin. No claim is made that instructions force every ChatGPT host to load context or change the account's custom-instruction setting.
