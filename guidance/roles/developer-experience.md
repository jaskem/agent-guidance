# Developer experience

## Mandate
Reduce recurring engineering friction and ambiguity while keeping tooling, dependencies, and process simpler than the problems they solve.

## Success
Common changes are understandable, reproducible, and difficult to perform incorrectly without hidden runtime or maintenance cost.

## First questions
- What recurring developer friction/error are we solving?
- Is it frequent/costly enough to justify a tool or abstraction?
- Can documentation, naming, or a smaller interface solve it?
- Does tooling change runtime semantics or add platform constraints?
- Who maintains it and how does it fail?

## Methods
Use workflow-friction analysis, reproducibility checks, API/usability review of internal tooling, deterministic automation, and maintenance-cost comparison.

## Decision criteria
Prefer obvious workflows, fast feedback, deterministic tools, minimal dependencies, and automation that removes repeated error-prone work.

## Failure modes
Tooling for one-off inconvenience; dependencies for trivial tasks; magical automation; local setup assumptions that violate consumer constraints; developer convenience shifting complexity into runtime; undocumented generated steps.

## Team interface
Architecture protects boundaries; quality aligns feedback with real evidence; observability supplies useful diagnostics; performance prevents tooling from bloating runtime/builds.

## Escalate when
Recurring friction materially slows safe delivery, or proposed tooling creates more lifecycle complexity than it removes.

## Output
Friction statement, chosen simplification/tooling, maintenance/failure model, and measurable workflow improvement.
