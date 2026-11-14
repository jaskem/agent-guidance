# Review criteria

Select criteria relevant to the tasks; mark unsupported checks untested.

| Lens | Inspect |
| --- | --- |
| Task route | Where to start, current editing context and next action |
| Hierarchy | Distinguishable selection, transport/status, content and secondary tools |
| Density | Grouping by frequency and use; preserve expert throughput |
| Language | Consistent labels, scope, units and understandable state indicators |
| Control | Destructive actions, recovery, save state and pending operations |
| Interaction | Exercise selection, drag, cancellation, zoom, focus and keyboard routes; images cannot prove them |
| Visual system | Typography, spacing, alignment, symbols, tokens and color meaning across states |
| Accessibility | Rendered contrast, non-color cues, focus, accessible names, keyboard and scaling with suitable tools |
| Edge states | Empty/loading/error, dense content, long names, overflow and disabled states |
| Performance | Measure a representative task; a dense image proves neither slowness nor speed |

For dense desktop tools, distinguish navigation, edit commands, object properties and meters/status. Persistent controls can be justified by task frequency. Extra whitespace is a trade-off, not a goal. Mouse/keyboard targets and touch targets have different constraints.

Verify the exact applicable standard, criterion, level, exceptions and units before prescribing accessibility minima. Contrast needs actual foreground/background and rendering context; antialiased edge pixels are insufficient. Static images reveal risks, not full accessibility conformance.

For browser or native semantics inspect meaningful control names, role/state, keyboard activation, focus entry/return, modal behavior and error recovery with available platform tools. Source-level ARIA or a screenshot alone does not establish the rendered accessibility tree or usable interaction. Use test-user-flows for a distinct repeatable journey and retain this audit as the owner of task-based usability interpretation.
