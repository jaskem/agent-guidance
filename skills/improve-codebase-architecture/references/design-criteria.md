# Architecture criteria

An interface includes what callers must know: inputs, ordering, invariants, configuration, errors and meaningful performance limits. A useful module hides substantial complexity behind a small understandable interface. Code length is not a measure of that benefit.

For each candidate ask:
- If removed, would its complexity disappear or spread across callers?
- Which real caller or variation justifies the abstraction?
- Where should state, failure handling and recovery belong?
- Can a caller-visible check distinguish the promised behavior from a plausible wrong result?
- What existing acceptance evidence must remain valid during migration?

Classify computation, local I/O, owned remote services and third-party dependencies before proposing test substitutes. A fake does not qualify real network, filesystem or device behavior. Preserve regression coverage until equivalent coverage is demonstrated; changing module structure is not itself a reason to delete tests.

Use a compact candidate record: observed friction and source; representative change; current/alternative shape; compatibility and recovery; expected benefit versus cost; confidence; acceptance evidence. A diagram is explanatory evidence about the proposal, not proof that it works.
