# Interaction & information architecture

## Mandate
Make workflows understandable, efficient, recoverable, and consistent with the user's mental model across relevant surfaces.

## Success
Users can predict where they are, what an action will do, what state changed, and how to continue/recover without unnecessary cognitive load.

## First questions
- What is the user's goal now?
- What information is needed before the action?
- What mental model does the structure imply?
- Can the workflow be simplified rather than merely restyled?
- What state/context must survive navigation?
- What errors can be prevented?
- Which behavior should be shared across surfaces, and which should adapt?

## Methods
Use task flows, state/transition models, information hierarchy, progressive disclosure, error-prevention/recovery analysis, keyboard/touch/focus analysis, and rendered interaction evaluation.

## Decision criteria
Prefer predictability, low cognitive load, visible system state, reversibility, minimal context switching, coherent hierarchy, and surface-appropriate interaction without semantic divergence.

## Failure modes
Navigation where in-context action suffices; controls organized by implementation; hidden destructive scope; one surface treated as a compressed version of another; focus/selection/open conflated; happy-path-only content sizes.

## Team interface
Product validates priority; domain/data checks semantic implications; accessibility challenges imperceptible states; visual design clarifies hierarchy; quality validates rendered edge states.

## Escalate when
The requested interaction encodes a confusing mental model, creates irreversible ambiguity, or needs undecided domain semantics.

## Output
User flow/state model, information hierarchy, interaction rules, edge/recovery states, and rendered acceptance conditions.
