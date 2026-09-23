# Consumer AGENTS routing fragment

A consumer repository should keep its own small `AGENTS.md`. Conceptually:

```text
Always load docs/agent/shared/KERNEL.md.
Use the repository-local workflow for batching/tests/checkpoints.
For substantive decisions, load docs/agent/shared/EXPERT-OPERATING-MODEL.md.
Route only materially relevant shared roles/playbooks plus any repository-local overlays.
Repository architecture, invariants, roadmap, and product semantics remain local sources of truth.
```

Do not copy this fragment verbatim when repository-specific source ordering or routes need stronger wording.
