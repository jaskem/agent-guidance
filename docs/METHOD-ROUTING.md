# Task methods and specialist roles

This router owns selection. The [work cycle](../guidance/playbooks/work-cycle.md) owns general execution, result-specific evidence and closure; methods own their bounded procedures. A role supplies a perspective and a tool supplies capability. None adds authority to implement, publish, send or schedule.

## Establish configured context

Start from the user's single configured operating guide once per session. Follow its conditional context route for a standalone object or a known project; a general question requires no project scan. Resolve the actual source and task/document owners using [context-entry](../guidance/playbooks/context-entry.md), preserving the consumer's pinned route. This central pointer does not upgrade a consumer.

Select from the [catalog](../skills/catalog.json), resolve the accepted distribution/version, and actually load the selected method plus necessary references. Installed, enabled, read, applied and verified are distinct states. If installed copies disagree, compare the canonical source, accepted pin and distribution evidence; modification time alone does not decide precedence. Pause only work dependent on an unresolved source or access gap.

## Select the work

Choose by the promised outcome and current uncertainty, not a keyword or available package. Respect an explicitly requested provider and its invocation policy. Otherwise use these canonical methods. A clear authorized request proceeds without restarting discovery.

| Request | Method | Observable finish |
| --- | --- | --- |
| Substantive software change or reported bug | [evidence-driven-development](../skills/evidence-driven-development/SKILL.md) | Requested behavior and applicable checks observed |
| Instruction, routing or skill maintenance | [maintain-agent-instructions](../skills/maintain-agent-instructions/SKILL.md) | Correct owner repaired and recurrence checked |
| Bounded plan or specification | [plan-work](../skills/plan-work/SKILL.md) | Known decisions, open choices and executable scope at existing owner |
| Domain meaning, identity or invariants | [domain-modeling](../skills/domain-modeling/SKILL.md) | Concrete cases reconciled with authoritative domain source |
| An unresolved design question needs concrete evidence | [prototype](../skills/prototype/SKILL.md) | Inspectable experiment answers the question; production status explicit |
| Audit existing interface usability | [audit-ui-ux](../skills/audit-ui-ux/SKILL.md) | Observed findings tied to user tasks and evidence limits |
| Propose visual/interface improvements | [design-ui-improvements](../skills/design-ui-improvements/SKILL.md) | Inspectable proposals preserving accepted identity and useful density |
| Review code, a branch or a PR | [code-review](../skills/code-review/SKILL.md) | Requirements and quality assessed against the complete relevant change |
| Repair source ownership or project navigation | [maintain-project-context](../skills/maintain-project-context/SKILL.md) | Verified owners, current links and explicit coverage gaps |
| Resume or hand off interrupted work | [handoff](../skills/handoff/SKILL.md) | Proven state and first unproven authorized action identified |
| Learn a concept, codebase or workflow | [teach](../skills/teach/SKILL.md) | Verified explanation/example; understanding claimed only if observed |
| Investigate existing architectural friction | [improve-codebase-architecture](../skills/improve-codebase-architecture/SKILL.md) | Traceable structure and bounded before/after alternatives |
| Complete an authorized software plan/task graph | [implement-spec](../skills/implement-spec/SKILL.md) | Integrated acceptance and status per task, or exact blockers |
| Organize incoming reports or backlog | [triage](../skills/triage/SKILL.md) | Deduplicated reports with evidence and one owning task/question |
| Substantive research, comparison or uncertain decision | [research](../skills/research/SKILL.md) | Dated source-backed conclusion, implications and uncertainty |
| Prepare questions for a knowledgeable recipient | [to-questionnaire](../skills/to-questionnaire/SKILL.md) | Decision gaps covered by a usable draft; no implied sending |
| Find a direction through a large uncertain goal | [wayfinder](../skills/wayfinder/SKILL.md) | Ready decisions and evidence dependencies at existing owner |
| Explicitly request an interview or grill a decision | [grill-me](../skills/grill-me/SKILL.md) | Dependency-aware interview retaining known answers |
| Design a public caller or file-format contract | [design-interfaces](../skills/design-interfaces/SKILL.md) | Inputs, outputs, failures, retry and compatibility cases defined |
| Assess a bounded security question | [review-security](../skills/review-security/SKILL.md) | Evidence-backed risks, controls and remaining gaps |
| Investigate measured slowness | [optimize-performance](../skills/optimize-performance/SKILL.md) | Comparable baseline, causal experiment and observed effect |
| Prepare or perform authorized release/distribution | [prepare-release](../skills/prepare-release/SKILL.md) | Package, acceptance, compatibility and recovery evidence |
| Develop substantial written content | [write-content](../skills/write-content/SKILL.md) | Requested material, structure, draft or revision at its intended owner |
| Verify real browser or native user actions | [test-user-flows](../skills/test-user-flows/SKILL.md) | Observed journeys with exact runtime evidence limits |
| Define, change or prove quality constraints | [constraint-driven-development](../skills/constraint-driven-development/SKILL.md) | Applicable norm and validated clean/failing/error behavior of its controls |
| Establish lasting detection and diagnosis signals | [observability-and-instrumentation](../skills/observability-and-instrumentation/SKILL.md) | Useful signals proven on healthy and failure paths |
| Transition or retire a supported system/contract/data version | [deprecation-and-migration](../skills/deprecation-and-migration/SKILL.md) | Consumer compatibility, transition and recovery evidence; retirement status explicit |
| Configure or repair build/test/delivery automation | [ci-cd-and-automation](../skills/ci-cd-and-automation/SKILL.md) | Reproducible event/job behavior and separately verified enforcement |

## Compose without duplicate workflows

1. Use direct handling for a simple answer or small edit. For substantial work choose the method for the requested end result, load it and preserve already accepted decisions.
2. Resolve a decisive knowledge gap with bounded research, diagnosis or a prototype. Return to the original objective after that sub-result; do not stop at research when execution is authorized.
3. Compose only necessary outputs. For example, a decision memo can use research then write-content; an approved software plan can use implement-spec and an authorized release step. Dependencies determine order, not the number of available methods.
4. Resumption identifies the next action; scheduling changes when work will run. Neither replaces the underlying content route. A method never confers new authorization.
5. Keep distinct owners: constraints establish what must hold; CI/CD establishes where checks run and whether failures block; code-review assesses the actual change; prepare-release verifies delivery. Existing checks can simply run without any new constraint or pipeline project.
6. Use observability for lasting signals, not every bug diagnosis; use migration for supported consumers/data transitions, not every refactor. Their software changes still use the applicable implementation and review procedure.

All catalog methods permit implicit relevant selection except grill-me, which remains explicit. An unrelated installed provider is not a second default lifecycle. A provider explicitly requested by the user remains available within its real scope. Provider files are not rewritten.

evidence-driven-development requires code-review; implement-spec requires both, as declared in the catalog. Resolve unavailable dependencies against the accepted canonical release. If that source is inaccessible, name the dependent gap and continue independent work. Other methods are conditional sub-results rather than a mandatory chain.

## Use the appropriate host capability

The method catalog is not a list of every tool. Use the host's required artifact, service or scheduling capability alongside the general cycle, loading its instructions when applicable.

| Result | Handling and finish |
| --- | --- |
| Short answer, summary or minor wording change | Direct handling and proportionate source check; no project/task ceremony |
| Document, report or presentation | write-content when substantial composition is needed, plus the format capability; check content and final rendering, save at the intended destination |
| Spreadsheet, analysis or conversion | Data capability; verify input identity, units, formulas/counts and material edge cases; produce usable saved output |
| Image, diagram or visual design | Appropriate creation/design capability; inspect the result; use exact diagram/plot tools for factual structures and measurements |
| Review of a document, analysis or proposal | Relevant content/data criteria and host capability; report findings against supplied requirements; no code-review or unsolicited edit |
| External app update or send | Resolve exact account/object/recipient and authority; refresh shared target before mutation; system evidence distinguishes draft, saved and sent |
| Later, recurring or conditional task | Actual scheduling capability; verify trigger, timezone, scope and output destination, inspect uncertain creation before retry; no background-agent promise |
| Simple explanation or learning | Direct explanation; teach for a useful bounded lesson, without forcing a quiz or code context |

A scheduler request is not CI/CD merely because both mention automation. Explicit publication or sending can be part of the authorized goal; drafting alone does not authorize either. A status question during work receives a brief answer and the authorized objective continues.

## Select specialist perspectives

The role files remain their single normative owners. Reuse the consumer's pinned copies when routed there; these links identify central source, not a command to override a consumer pin. A role is not a permanent subagent or a second skill package.

| Question or risk | Role |
| --- | --- |
| User problem, intended value, uncertain priority | [product-strategy-discovery](../guidance/roles/product-strategy-discovery.md) |
| Module responsibility, coupling, simpler interfaces | [architecture-engineering](../guidance/roles/architecture-engineering.md) |
| Identity, lifecycle, relations, data compatibility | [domain-data-contracts](../guidance/roles/domain-data-contracts.md) |
| Offline, uncertain writes, recovery and authority | [local-first-sync-recovery](../guidance/roles/local-first-sync-recovery.md) |
| User evidence versus design assumptions | [ux-research](../guidance/roles/ux-research.md) |
| Task route, navigation, status and recovery | [interaction-information-architecture](../guidance/roles/interaction-information-architecture.md) |
| Keyboard, focus, contrast and reflow | [accessibility](../guidance/roles/accessibility.md) |
| Labels, instructions and truthful status | [content-design](../guidance/roles/content-design.md) |
| Visual hierarchy, typography and identity | [visual-design](../guidance/roles/visual-design.md) |
| Repeated UI patterns and component consistency | [design-systems](../guidance/roles/design-systems.md) |
| Acceptance, regression and release evidence | [quality-release](../guidance/roles/quality-release.md) |
| Authorization and sensitive data boundaries | [security-privacy](../guidance/roles/security-privacy.md) |
| Measured slowness and representative workload | [performance](../guidance/roles/performance.md) |
| Diagnostic question and sufficient signals | [observability](../guidance/roles/observability.md) |
| Reproducible tooling and understandable code | [developer-experience](../guidance/roles/developer-experience.md) |

## Preserve local ownership

Follow the existing product plan, terminology, task tracker, decision records and closure workflow. Ownership is project-specific: code may live in a repository while Notion owns tasks and decisions. Resolve each owner separately. A navigation page can link to those sources and give a dated summary; it cannot silently become a second task or product-contract owner. Preserve the distinction between proposed, accepted, implemented, checked and published.

Research, recovery, closure and instruction feedback already have [playbook owners](../guidance/catalog.json). Load the applicable procedure through the consumer route rather than inventing another. Package-specific steps should invoke that role or procedure when available; their self-contained task steps must retain safe handling when a host lacks it.

Choose available subagents autonomously when the selected method asks for them or independent research, execution or verification materially helps the task. The user does not need to mention agents or repeat permission merely for delegation. Preserve the task's actual authority and tool limits. Before delegating, follow the selected [delegation playbook](../guidance/playbooks/delegation.md) through the consumer's local route. If unavailable, retain bounded assignments, non-overlapping writes, explicit evidence and parent verification. Availability of several roles is not authorization to create a standing agent team. A skill call is not a separate agent; a separate agent sharing the author's context is not a fresh-context review. Choose delegation for independent useful work or material review value, not role count or task size alone.
