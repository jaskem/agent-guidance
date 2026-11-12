# Instructions and skills audit, 2026-11-12

## Scope and evidence

Requested outcome: a reliable instruction/skill workflow, assessment of existing GitHub material, and implemented improvements informed by Matt Pocock's skills. This batch adds optional reusable methods and their checks; it does not change product semantics or migrate pinned consumers.

The connected account exposed six repositories. Complete default-branch trees were read (`truncated: false`); none contained a file named `SKILL.md` before this batch. This proves absence of that package entrypoint in those trees, not absence in other branches, other accounts or the user's computer. The host personal-skill checkout and enabled Notion skill list were also empty at inspection.

| Repository / inspected revision | Retain | Assessment and action |
| --- | --- | --- |
| [agent-guidance](https://github.com/jaskem/agent-guidance/tree/92b9aa78a95134c0e81f61f1e3047bc87fde6f77) | Kernel, 15 roles, four playbooks, optional resources, hash-pinned vendoring | Strong central ownership and reusable methods. Add actual installable packages alongside guidance; preserve IDs and lock contract. |
| [taskline](https://github.com/jaskem/taskline/tree/3f7b3f2363688549d084525144d26090d8700c0b) | Local router, canonical ownership, exact guidance lock | Already pins agent-guidance `92b9aa78...`, v0.4.0. Avoid a redundant migration for this additive skill-only change. |
| [project_data_pipeline](https://github.com/jaskem/project_data_pipeline/tree/89782c36b1f2d1fa76fc6a762d8929938ca76eba) | Root and four scoped AGENTS files, Copilot pointer, BASELINE routing | Good local separation of product contracts, process and generated status. Generic skills must route into this system, not generate another plan or test policy. |
| [DXF-viewer](https://github.com/jaskem/DXF-viewer/tree/3b6b45dfdcda0bd7d5bd91dd9e66fa4807222420) | Compact entrypoint, central concept, reproducibility route | Keep the existing product-plan owner and explicit publication boundary. Installable methods add execution discipline without replacing recognition contracts. |
| [landscape-core](https://github.com/jaskem/landscape-core/tree/4ed144dde82390b085f9b94b9b33558033e2dd97) | Semantic boundary, durable evidence, exact-SHA recovery | Long entrypoint repeats general evidence, strategy and closure themes. Candidate for a separately verified pinned-guidance migration; preserve Core-specific constraints and roadmap authority. |
| [landscape-platform](https://github.com/jaskem/landscape-platform/tree/6f1df6b8b415dd8a9963b952b5f387ad1962aadd) | Core/platform separation, recovery and execution constraints | Similar repeated general process themes. Same migration candidate; this audit does not establish equivalence of a replacement. |

Read in depth: the six root entrypoints, all scoped Flowcraft instructions and BASELINE, Taskline's lock, central workflow/consumer contract/kernel/catalog/tooling/tests, relevant roles and playbooks. This is an instruction-system audit, not a fresh validation of each product's entire roadmap or runtime. Root entrypoint sizes (13/73/44/13/158/168 lines respectively for guidance/Taskline/Flowcraft/DXF/Core/Platform) are context-cost indicators, not defect scores.

## Matt Pocock comparison

Reviewed [mattpocock/skills at 5863806dd4e15c63174bee4e7515a4256792ecfa](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa): full tree, README, CLAUDE.md, license, writing-for-agents and SKILL-MECHANICS, tdd, diagnosing-bugs, implement, code-review, setup, handoff, domain-modeling and codebase-design entrypoints. Referenced upstream helper scripts and supporting method files were not imported. This is a comparison of the selected methods, not an execution audit of every upstream package.

| Upstream idea | Implemented choice | Why |
| --- | --- | --- |
| Small composable skills; precise triggers | Two task-scoped packages | Existing roles remain useful references; converting every role into a skill would increase overlap. |
| Progressive disclosure and clear completion | Short ordered steps with direct branch references | Keep the next action visible and load diagnosis/design detail only when relevant. |
| Vertical slices and red/green feedback | Discriminating behavioral checks and one usable slice at a time | Observe the failure before claiming repair; keep expected values independent. |
| Separate standards and spec reviews | Distinct requirements and quality passes | A correct style can still implement the wrong requirement. Independent reviewers only when authorized and useful. |
| Domain language and deep modules | Reuse current terminology; simplify interfaces | Preserve existing contracts rather than impose GLOSSARY.md or rename domain vocabulary. |
| Interview every change / confirm all test seams | Ask only for material unresolved choices | Existing requirements and test boundaries already authorize routine work. |
| Strict diagnosis gates and fixed hypothesis counts | Reproduce when possible; qualify unavailable evidence | Reading code may be necessary to build the reproducer; uncertainty must remain visible. |
| Handoff in OS temporary folder | Existing durable checkpoint owner | A temporary file is not sufficient for cross-session continuity here. |
| Automatic plugin updates / complete bundle | Pinned, reviewed original adaptations | Avoid hidden behavioral changes, duplicate installers, CLI assumptions and beta/misc features without a demonstrated need. |

Upstream is MIT licensed, copyright 2026 Matt Pocock. The new packages are original synthesis with pinned provenance, not copied upstream packages. Broad upstream statements about reliability are design guidance, not empirical proof of our results.

## Implemented repairs

- **Missing installable packaging:** add `evidence-driven-development` and `maintain-agent-instructions` with names, specific triggers, references and supported host metadata.
- **Possible source conflict:** assign GitHub as source for these engineering packages; treat Notion/personal installs as distributions, with an exact revision and hash record. Product facts remain in their repositories.
- **Unverifiable package completeness:** add offline catalog/metadata/reference checks and negative tests. Add the checker to CI.
- **Unclear applicability:** explicitly exclude planning-only, simple explanations and trivial editorial work from the development method. Retain repository workflow precedence.
- **Overstated confidence:** distinguish structural validation, isolated behavioral trials, installed state, remote CI and live-product evidence.

## Behavioral evidence

Three fresh-context agents received the skill and an isolated raw task, not the intended answer. Fixtures were separate from product repositories; no agent committed or published.

1. **Development trial:** a public `total_cents` function returned 300 for prices [199, 250], although the existing whole-euro test passed. The agent added failing regression checks, observed 300 versus required 449 and 0 versus required 1, removed per-item rounding and reran four passing unittest cases. It preserved integer output/input and separated requirements from quality self-review.
2. **Maintenance trial:** a workflow pointed to absent `docs/DEBUGGING.md` while `docs/DIAGNOSIS.md` existed. The agent changed only the pointer, verified all three routed paths, and preserved product contract, shared kernel and other instructions byte-for-byte. It correctly reported that the shared canonical pin was unavailable rather than inventing it.
3. **Excluded request and missing inputs:** the user requested only a diagnosis plan for intermittent export errors, explicitly forbade changes and had neither code nor example file available. The development-skill agent returned a concise plan, labelled the cause unknown and made no tool calls or file edits. It did not turn a planning request into implementation or require an unnecessary interview.

These are narrow synthetic trials, not proof of performance on the six real projects. Package tests cover a valid distribution, missing reference, escaping reference, unlisted package, conflicting invocation policy and an unpinned upstream revision. Foundation/vendoring tests remain required from a clean committed checkout.

An independent diff review found that the initial checker accepted an invalid YAML description and a misspelled `policy` parent. The repair validates the restricted supported frontmatter syntax and the actual metadata sections/fields. Added negative tests for both cases and a skill name appearing outside the default prompt. Requirements and implementation quality were reviewed separately; installed state and remote checks remain separate evidence.

## Remaining improvements with a concrete trigger

- Core/Platform general-process duplication: perform a separately scoped equivalence review and consumer migration when either instruction router is next maintained; preserve their semantic boundaries and verify required process checks. Do not bulk-rewrite them from this audit.
- Evaluate real skill usefulness on the next substantive DXF/Flowcraft change. Keep one observation in the existing work record if it changes a decision or misses a defect; avoid a new metrics system.
- Other branches and local-computer skill installations were not enumerated. Inspect them only if the user identifies additional sources or a later task reveals a duplicate/conflict.

## Batch record

Base: `92b9aa78a95134c0e81f61f1e3047bc87fde6f77`. Scenarios: F0 method design, F2 process/CI, plus additive package tooling. Consumed shared modules: kernel, developer-experience, architecture-engineering, domain-data-contracts, quality-release, instruction-feedback-loop, change-closure, research-verification, interruption-recovery, resource-index. No consumer files, shared module bytes, shared catalog IDs or lock schema changed. Package version is 1.0.0; shared guidance remains 0.4.0.

Exact final revision, CI, installation and readback evidence belong to the PR and private distribution record. Next technical step after package release: exercise the selected method on the next real authorized repository change and record only material findings at its existing owner.
