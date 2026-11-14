---
name: improve-codebase-architecture
description: Investigate architectural friction in an existing codebase and compare bounded improvements with evidence and before/after diagrams. Use for maintainability, module responsibilities and simpler interfaces; exclude routine feature work, diff-only review and UI layout audits.
---

# Improve codebase architecture

## 1. Bound the investigation

Follow the user's configured operating guide once per session and its active tool-call version. Reuse verified context; load the relevant project, current task and source owners, refreshing affected sources after material changes or uncertain writes. If required context is inaccessible, name the gap and continue only independently supported work. Use the routed context-entry playbook when available.

Identify the maintenance problem, actual source revision, relevant contracts and behavior that must survive. Use the named area; otherwise inspect change history and recurring defects to choose a useful area. File size or fashionable architecture alone is not evidence of friction. Read the routed architecture role for its criteria when available.

Finish with an inspected area, a concrete change scenario and preserved constraints. An architecture investigation does not authorize implementing its proposals.

Use available agents on your own initiative when this method calls for separate work or when bounded independent work or review would improve the result; no explicit user request is needed. Follow the routed delegation rules. Give each worker the relevant source, question, allowed actions, owned objects and expected evidence; keep one writer per shared object and verify the combined result in the parent. Use the actual host capabilities and model/fork rules. If agents are unavailable, continue supported work without claiming an independent review.

## 2. Trace the cost of change

Follow representative callers, data/state ownership, dependencies and failure/recovery paths. Locate where one change must be repeated, where callers must know implementation details and where useful tests cannot exercise the real path. Cite files and the inspected revision. Use [design criteria](references/design-criteria.md) to distinguish useful encapsulation from extra indirection.

Separate observed coupling or duplication from an untested maintenance hypothesis. If code, a caller or runtime evidence is unavailable, bound that finding rather than inferring the missing architecture. Finish with traceable friction and a scenario that would expose it.

## 3. Compare bounded alternatives

Compare retaining the current design with the smallest useful change. For a consequential unresolved interface, explore materially different alternatives only when they could change the recommendation. Include caller knowledge, dependency direction, state/error ownership, compatibility, migration and verification cost. Consider simpler functions or clearer names before new layers, adapters or languages.

Draw inspectable before/after relationships using the supported diagram or document format; inspect rendered artifacts when producing a file. Mark proposals separately from actual code. Retain domain vocabulary; use domain-modeling only for unresolved meaning and design-interfaces for a distinct unresolved caller contract. Finish with a recommendation, counterarguments and evidence needed to decide.

## 4. Close the investigation

At the established project owner, record the problem, exact source, options, recommendation, acceptance checks and open decisions. Preserve existing product contracts. A selected proposal proceeds through plan-work or the authorized execution method; an investigation alone makes no production edits. Report inspected scope, actual checks and limits.

For provenance and intentional differences, read [sources](references/sources.md).
