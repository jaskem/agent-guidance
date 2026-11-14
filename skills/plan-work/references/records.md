# Plan and task records

Scale detail to the work. Reuse equivalent existing fields rather than adding a new template.

A plan records outcome; existing accepted constraints; proposed choices clearly labelled; observable acceptance; exclusions; unresolved questions and the next safe action. Cite the current source and revision for consequential facts.

A task records one delivered behavior or resolved question, acceptance evidence, true blockers, source plan and owner. Reference actual issue identifiers only after creation succeeds. Keep parent state unchanged unless completion is independently established and updating it is within scope.

Prefer one coherent end-to-end behavior to separate UI, storage and validation tickets that each produce unusable fragments. A research or decision task is legitimate when it resolves a named blocker. Do not turn every small implementation action into a ticket.

If requested output is only a plan, mark implementation as not performed. If code, data or environment are missing, write only what evidence supports; make investigation an explicit first step rather than asserting a cause.

## Specify behavior before task mechanics

For a specification, state the concrete trigger, actor, inputs and intended result; add error, cancellation and recovery behavior when those conditions affect acceptance. Preserve exact values or decision-rich model examples only when they are actually fixed. Mark proposals and unknowns rather than filling a long user-story template.

For a recurring workflow, identify what triggers one run, its allowed sources and actions, the durable output, duplicate or retry behavior and a human decision point only where a real choice or authority boundary requires it. Specifying the workflow does not schedule it.

For dependent tasks, make the consumed and produced interfaces agree. Link each accepted requirement to an owning task and an observation that could fail if the requirement were missing. A likely failure case belongs to its owning behavior rather than an arbitrary extra test ticket. Keep proposed file paths and commands grounded in the current source; recheck them before execution.

A plan can hand directly to authorized execution. Do not add a compulsory design interview, separate execution-method vote or repeated permission gates when the user already delegated that choice.
