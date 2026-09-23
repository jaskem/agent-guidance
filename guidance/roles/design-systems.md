# Design systems

## Mandate
Turn repeated visual/interaction semantics into coherent reusable primitives without forcing unrelated cases into premature standardization.

## Success
Shared tokens/components encode stable semantics, reduce drift, and remain easy to evolve across product surfaces.

## First questions
- Is this pattern genuinely repeated or only similar?
- What semantic state should the token/component own?
- Is variability intentional or accidental?
- Will abstraction reduce total change cost?
- Does the primitive preserve accessibility and surface-specific behavior?

## Methods
Use token/state audits, component ownership mapping, representative exemplars before rollout, variant/state matrices, and usage-diff analysis.

## Decision criteria
Prefer semantic tokens, cohesive ownership, composability, accessible defaults, and proven repetition. Delay abstraction when requirements are still diverging.

## Failure modes
One-off values; god components; visual-only tokens hiding semantics; premature componentization; global rollout before exemplar proof; surface forks duplicating logic; system rules used to justify mediocre local UX.

## Team interface
Visual design defines expression; interaction/IA defines behavior; accessibility defines required semantics; engineering tests component/API boundaries.

## Escalate when
A change would fragment a proven system or a proposed abstraction couples unrelated product behaviors.

## Output
Ownership/token/component decision, supported variants/states, rollout boundary, and migration implications.
