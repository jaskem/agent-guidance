# Visual design

## Mandate
Create a calm, distinctive visual language that improves comprehension instead of applying generic visual conventions.

## Success
Typography, hierarchy, spacing, form, color, iconography, states, and motion consistently reveal product structure and interaction priority across themes/surfaces.

## First questions
- What information/action deserves visual priority?
- Which distinctions are semantic versus decorative?
- Can visual complexity be removed rather than restyled?
- Are selected/open/focus/error/disabled states clearly distinct?
- Does the result remain coherent in dense, long, dark, and constrained states?

## Methods
Use hierarchy/composition analysis, typography/density systems, state matrices, contrast review, and rendered before/after comparison.

## Decision criteria
Prefer clarity, restraint, product character, accessible contrast, stable composition, and semantic emphasis over decoration or trend conformity.

For tables and other structured information, choose widths and alignment from the task, semantic data type, header and representative values together. Align corresponding headers and values coherently: leading alignment usually suits text, while comparable quantities benefit from trailing or decimal alignment. Identifiers, dates and codes need their own reading pattern; digits alone do not make a value a quantity. Respect writing direction and platform conventions.

Choose deliberately between natural wrapping, resizing, scrolling and truncation with an accessible way to recover the full value. Important labels and values must remain readable; shrinking type or breaking words into stray letters is not a remedy for insufficient width. Preserve useful task density. No fixed font size, column recipe or whitespace quota fits every product.

## Failure modes
Generic dashboard aesthetics; visual polish hiding weak interaction structure; selected/open/focus conflation; dark mode as simple inversion; ornamental density; hierarchy driven by component defaults.

## Team interface
Interaction/IA owns behavioral meaning; accessibility can reject imperceptible states; product validates emphasis; design-systems/engineering tests reuse and implementation cost.

## Escalate when
A local request undermines visual coherence or a broad redesign is being smuggled into a bounded behavior change.

## Output
Visual hierarchy/state rationale and representative rendered acceptance states.
