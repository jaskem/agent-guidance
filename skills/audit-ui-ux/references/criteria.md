# Review criteria

Select criteria relevant to the tasks; mark unsupported checks untested.

| Lens | Inspect |
| --- | --- |
| Task route | Where to start, current editing context and next action |
| Hierarchy | Distinguishable selection, transport/status, content and secondary tools |
| Density | Useful information per viewport; column/container widths, row heights, wrapping and scroll cost; grouping by frequency and use; preserve expert throughput |
| Language | Consistent labels, scope, units and understandable state indicators |
| Control | Destructive actions, recovery, save state and pending operations |
| Interaction | Exercise selection, drag, cancellation, zoom, focus and keyboard routes; images cannot prove them |
| Visual system | Typography, spacing, alignment, symbols, tokens and color meaning across states |
| Visual craft | Purposeful containers, content-sized regions, readable hierarchy, consistent spacing/radii, accurate assets and restrained effects; distinguish useful patterns from decorative repetition |
| Accessibility | Rendered contrast, non-color cues, focus, accessible names, keyboard and scaling with suitable tools |
| Edge states | Empty/loading/error, dense content, long names, overflow and disabled states |
| Performance | Measure a representative task; a dense image proves neither slowness nor speed |

For dense desktop tools, distinguish navigation, edit commands, object properties and meters/status. Persistent controls can be justified by task frequency. Extra whitespace is a trade-off, not a goal. Mouse/keyboard targets and touch targets have different constraints.

Verify the exact applicable standard, criterion, level, exceptions and units before prescribing accessibility minima. Contrast needs actual foreground/background and rendering context; antialiased edge pixels are insufficient. Static images reveal risks, not full accessibility conformance.

For browser or native semantics inspect meaningful control names, role/state, keyboard activation, focus entry/return, modal behavior and error recovery with available platform tools. Source-level ARIA or a screenshot alone does not establish the rendered accessibility tree or usable interaction. Use test-user-flows for a distinct repeatable journey and retain this audit as the owner of task-based usability interpretation.

## Inspect space and craft directly

For tables, trees, property panels and schema views, inspect rendered widths against representative content. Look for columns much wider than their values, short objects stretched across the workspace, oversized headers, repeated padding and blank regions that force useful information off-screen. Compare visible rows/columns, wrapping, truncation and scrolling at the same viewport and scale. Retain room for editing, long names, resizing and accessible targets; compactness does not mean shrinking everything.

Inspect headers and values together: widths must accommodate both, corresponding alignment must be coherent, and wrapping must not strand letters or hide meaning. Distinguish readable text and identifiers/dates from quantities that benefit from trailing or decimal alignment; do not right-align every digit-containing field. Where truncation is justified, check full-value access with the available surface. Do not accept tiny text as proof that all columns fit. Recheck affected final states after changes to labels, typography, padding or widths.

Judge instruction text against the task: could clearer order, labels or feedback carry the meaning? Retain necessary domain and recovery help. When interaction is available, inspect whether later edits or automatic results silently replace valid prior choices; distinguish a real domain dependency from accidental resetting. Without interaction evidence, record a risk or untested sequence rather than a demonstrated behavior defect.

Identify the exact region and task consequence. Check whether repeated cards, labels, pills, shadows, gradients or animations communicate grouping, state or meaning. Preserve justified established patterns. Marketing hierarchy and gallery spacing are not defaults for operational tools; maximum density is not the goal of a presentation or product story.

Inspect motion in the actual sequence when claiming behavior. Establish initial state, user trigger, visual change, completion and recovery; confirm that the selected subject remains identifiable. A still image cannot prove timing or interaction. Under reduced motion, relevant content and task completion must remain available.

Treat style recipes and generic design scores as hypotheses. Do not impose universal whitespace percentages, heading ratios, font/card bans or spacing increments. Ground findings in the task, accepted identity, actual rendering and applicable platform requirements.
