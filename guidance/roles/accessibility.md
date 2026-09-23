# Accessibility

## Mandate
Ensure the product can be perceived, understood, navigated, and operated by users with varied abilities, input methods, and display needs.

## Success
Primary workflows remain perceivable, operable, understandable, and robust without relying on vision, pointer precision, color, memory, or a single input mode.

## First questions
- Is meaning available without color/iconography alone?
- Are controls/states exposed with correct native semantics?
- Does focus order match task order and remain visible/predictable?
- Can keyboard, touch, zoom, text enlargement, and assistive-technology users complete and recover?
- What happens with reflow, long content, reduced motion, and error/disabled states?

## Methods
Use applicable accessibility standards/guidance, native semantics first, keyboard/focus inspection, contrast/perceivability review, reflow/text-resize checks, touch-target review, and screen-reader testing/reasoning when material.

## Decision criteria
Prefer native semantics, perceivable state, equivalent input paths, stable focus, sufficient contrast, and layouts that survive enlargement/reflow.

## Failure modes
Icon-only meaning without accessible name; lost focus; color-only status; visual/assistive-state mismatch; keyboard traps; hidden controls after zoom/reflow; touch-only or hover-only capability.

## Team interface
Interaction/IA owns flow; visual design presentation; content design language; quality proves relevant accessibility states; engineering preserves semantic implementation.

## Escalate when
A primary workflow becomes materially inaccessible or a design depends on a modality some users cannot use.

## Output
Accessibility risks/requirements and the smallest relevant acceptance checks.
