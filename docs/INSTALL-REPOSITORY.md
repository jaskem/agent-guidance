# Install in a project repository

Use this adapter from [INSTALL.md](../INSTALL.md). Follow the [consumer contract](CONSUMER-CONTRACT.md); project semantics, tasks and architecture remain at their existing owners. Updating this source does not update an existing consumer pin.

1. Verify the exact target repository and its current `AGENTS.md`, workflow, source owners, selected modules and any `.agent-guidance.lock.json`. Read only the relevant project context. A request for personal installation is not permission to migrate every project.
2. Reuse an existing lock and overlays when current. For a requested update compare the accepted base, local copy and proposed source; preserve local customizations outside the dedicated generated destination. Back up affected instructions and lock before writes. Review the selected module list; do not drop old selected modules silently.
3. Use a clean local source checkout at the selected exact commit. Read the vendor tool before executing it. A ZIP lacking Git metadata is not that checkout; use an authorized Git checkout or leave this adapter pending while other routes proceed. Resolve values from the actual target, source commit and catalog version; angle-bracket values below are placeholders, not a runnable command.

```text
python <source-checkout>/tools/vendor_guidance.py --source-root <source-checkout> --source-commit <40-character-commit> --consumer-root <target-repository> --module kernel --module work-cycle --module context-entry
```

4. Add only the selected required roles/playbooks using additional `--module` arguments. Reuse current module selection on an update. The default dedicated destination is `docs/agent/shared`; the verifier is `tools/verify_agent_guidance.py`. The tool can delete stale generated modules when updating a selection, so inspect the existing lock and destination before execution. Keep product overlays outside it.
5. Merge the filled [repository entry template](../distribution/workflow-starter/templates/Repository-AGENTS.md) into the existing `AGENTS.md`. Use the actual local kernel path and project workflow. If the user has a personal Guide, resolve it through their host/local configuration, never a public hardcoded private link. Keep method access at the user's accepted source/distribution; shared-module vendoring does not install native skills.
6. Run `python tools/verify_agent_guidance.py --root .` in the consumer and the target's relevant process checks. Inspect the lock's source commit, hashes and exact files. Verify routing in a new task context when possible; a passing hash verifier does not prove interpretation. Follow the target's normal authorized commit/PR route and report reviewed, published and installed states separately.

No remote runtime import is required for vendored modules. If a needed method or host capability is unavailable, retain the project pin and report that dependent gap. Recovery reverts this consumer installation's bounded changes and verifies the restored lock; it does not reset unrelated project work.
