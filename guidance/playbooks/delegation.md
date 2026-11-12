# Delegation

Use this when authorized work could benefit from parallel execution or a separate review. A role supplies specialist criteria, a skill supplies a method, and an agent executes work; none implies a standing team.

## 1. Choose useful separation

Keep small or tightly coupled work with one agent. Delegate only a bounded task that can proceed independently or provide materially different verification. Keep the next blocking decision and final integration with the parent. Check host capability and active authorization; worker tools and permissions must not be assumed from the parent's access. Reuse existing authorization rather than asking again merely because work is delegated. A temporary worker does not authorize persistent agents, schedules or extra service access.

Finish with a concrete benefit and separable result, or continue without delegation. Risk and useful independence matter more than task size or a fixed reviewer count.

## 2. Assign an explicit boundary

Give each worker the minimum relevant source material and a compact assignment:

- desired result and acceptance evidence;
- exact baseline or source/object references, relevant instructions and decisions;
- scope, exclusions and allowed actions;
- owned files, branch/worktree or external object IDs, and whether access is read-only;
- dependencies, expected output and the condition for stopping or returning a blocker.

The parent can pass already verified context with its source, revision/version and observation time. Workers read missing or materially changed context; they need not repeat a whole workspace scan. Do not pass expected findings to an independent reviewer: provide raw requirements, source, diff and artifacts instead.

Assign one writer to a shared resource at a time. Files, branches, task records, document pages, browser tabs and desktops can all collide. Separate code worktrees when appropriate; a separate worktree does not isolate an external page or desktop. Prefer read-only work if ownership cannot be separated. Use existing claims/locks where supported; an assignment is not an enforced lock.

Finish when the worker can identify what it may change, what it must preserve and what result to return. A worker may delegate further only if authorized, within the same scope and resource ownership; it reports the resulting task tree to its parent rather than expanding work silently.

## 3. Coordinate changes and interruptions

Continue independent parent work while workers run. Use bounded waits and meaningful progress reports rather than repeated polling. Re-scope or stop an affected worker when requirements, dependencies or shared state change; verify that an interrupted writer has stopped before another writer takes ownership.

A stalled or failed worker returns established results, partial changes, uncertain operations and the first blocked step. Recover durable evidence before repeating work. For an uncertain write, inspect the exact target before retrying; use the existing interruption-recovery procedure when available. Do not infer failure from a missing final message or success from a worker's status alone.

Finish when every worker result is returned, deliberately stopped or explicitly unresolved. Do not conceal abandoned work behind a completed parent status.

## 4. Integrate and verify

Require a concise return: result, exact source/revision, changed objects, checks actually run, material findings and remaining uncertainty. The parent inspects relevant diffs or saved targets, resolves conflicting findings against the authoritative requirements, and checks the combined result at its current revision. Earlier tests or reviews do not cover later changes automatically.

Distinguish self-review, another agent with shared context, and a reviewer with fresh task-local context. Separate requirements and quality assessments when relevant; neither a different role name nor loading another skill proves independence.

Choose one owner for final task status, integration actions and user-facing delivery. Verify uncertain saves, merges or publication at their actual destination. Report only observed completion, leaving unresolved worker effects explicit. A delegated report is evidence input; the parent remains accountable for final claims.
