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
