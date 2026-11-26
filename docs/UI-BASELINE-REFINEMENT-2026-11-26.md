# General UI baseline refinement — 2026-11-26

## Scope and signal

The user explicitly requested that recurring design feedback improve the general workflow and skillset, beyond product instructions. Observed signals were poorly fitted table headers and values, inconsistent alignment and color usage, excessive instructions, later preparation actions replacing prior choices, and a header wrapping regression after a typography adjustment.

Baseline: `e03ac76e45ebbe42125b79b4a1260ee3e2259c03`, guidance 0.9.0 / collection 1.4.2. Existing guidance already covered visual inspection, density, readability, color semantics and concise language. This change clarifies decisions, timing and discriminating checks; the incident does not establish that the previous instructions contained none of these requirements.

## Ownership and resulting change

- The general work cycle calls for relevant basic interface decisions before ordinary implementation, without requiring a separate audit or design ceremony.
- Visual design owns content-aware widths, semantic alignment, readable wrapping and deliberate full-value access. Interaction/IA owns preserving valid earlier input and visible dependency invalidation. Design systems owns consistent semantic color/state patterns. Existing content-design guidance remains the owner of concise task language.
- Visual verification owns invalidation of affected layout evidence after labels, type, padding, widths or available space change.
- Four self-contained existing methods apply these criteria at implementation, proposal, audit and flow-verification boundaries. Their main files route to the relevant references, including UI bug fixes.

No new method, palette, pixel minimum, framework recipe, project domain rule or compulsory lifecycle was introduced. Existing expert density, product identity, authority, evidence boundaries, module IDs, consumer pins and setup versions remain intact. This is an additive shared behavior clarification: guidance 0.10.0, collection 1.5.0; evidence-driven-development/design-ui-improvements/audit-ui-ux 2.3.0 and test-user-flows 1.2.0. Existing consumers remain on their configured pins until separately updated.

## Independent comparison

Two fresh-context read-only agents received identical raw tasks and separate complete baseline/candidate snapshots. Neither received an answer key, previous diagnosis or the other output. The trial asked for proposed decisions and checks, explicitly forbidding implementation and runtime claims. A third fresh-context reviewer assessed the actual requirements and complete diff separately. These are reasoning/selection trials, not executed app acceptance.

Raw tasks:

1. Authorized repair of a dense inventory input screen at 900px: nine equal-width columns, 11px text after fitting, isolated final letters in long Dutch headers; code `003047`, long profile name, `12.75 mm` and date `26-11-2026`. Automatic rotation recognition sometimes resets a chosen origin; help paragraphs explain order; established palette. No source/runtime supplied. Ask for actions and acceptance.
2. Proposal-only compact Arabic trading interface with established identity, dense tables, codes/prices/dates, fast comparison and visible expert controls.
3. Only: “Wat betekent kolombreedte?”
4. Verify preserved prior choices and new labels in a delivered native app; only source and an old screenshot are available, no supported current interaction/capture route.

Observed baseline result: content-dependent columns, readable type, meaningful word wrapping, preserved codes/units, appropriate numeric alignment, established identity, preservation/recovery of user choices and real runtime acceptance. The RTL proposal retained density and code direction. The simple question received a direct definition; unavailable runtime acceptance remained not run.

Observed candidate result: the same task/authority boundaries held. Case 1 explicitly separated identifiers/dates from quantities and specified: “Herhaal getroffen layoutchecks na de laatste tekst-/maatwijziging.” The baseline plan specified current layout acceptance but did not state this subsequent-change reinspection trigger. Case 2 preserved RTL, density and identity; case 3 remained a direct answer; case 4 left actual native interaction and final fit unverified.

The narrow comparison metric is presence of an explicit affected-layout reinspection trigger after subsequent text/geometry changes in the case-1 plan: baseline 0, candidate 1. Both runs otherwise produced useful plans; no aggregate score, speed gain, statistical reliability or universal behavior improvement is claimed. Task-local raw briefs and fuller outputs are retained with the existing private maintenance owner.

## Review, checks and recovery

Separate requirements review found the requested coverage reachable. Quality review found no blocking issue and one provenance correction: retain the historical Garden-integration package versions rather than rewriting them to the current release. That correction was applied; current-version declarations and the new dated entry remain separate.

Required verification: foundation checker, skill-package checker, full existing unittest suite, diff whitespace checks and learning evidence preflight; final command results are recorded at the maintenance/distribution owner and PR. Structural checks prove package/catalog integrity; trials prove only the listed observations. Native and Notion distribution readback is recorded separately after source publication.

Rollback: restore the bounded changed source files from the baseline through a reviewed new commit, preserving unrelated work and consumer pins. Preserve previous native complete packages and Notion export archives/attachment Folder IDs before replacing the four distributions; restore only these targets if needed. Do not reset a checkout or delete historical Notion folders. The next relevant real UI task remains a separate observation of actual method use.
