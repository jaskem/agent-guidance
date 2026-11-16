# Consumer AGENTS routing fragment

A consumer repository should keep its own small `AGENTS.md`. Conceptually:

```text
Follow the user's configured operating guide once per session, using its accepted version.
Resolve the relevant work/project owner through its current context links.
Always load docs/agent/shared/KERNEL.md.
For substantive work, load the selected docs/agent/shared/playbooks/work-cycle.md.
Use the repository-local workflow for batching/tests/checkpoints.
Route only materially relevant shared roles/playbooks plus any repository-local overlays.
Repository architecture, invariants, roadmap, and product semantics remain local sources of truth.
```

Use one configured guide URL in user-specific entry instructions. Follow its linked index rather than embedding project-specific document links or a second index URL in every repository. Keep stable project/source identity and local file routes for matching the relevant registration; unresolved identity remains explicit. Standalone work does not require a project entry.

Select the general `work-cycle` and relevant `context-entry` modules explicitly when migrating a consumer. Use their pinned local copies; neither this fragment nor a central link upgrades an existing consumer. If a routed module is unavailable, disclose the dependent limit and continue supported work under the applicable instructions.

The shared senior-collaborator stance is already part of `KERNEL.md`; do not gate it on another conditionally loaded model module.

Do not copy this fragment verbatim when repository-specific source ordering or routes need stronger wording.
