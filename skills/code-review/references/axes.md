# Review axes

## Requirements

Map each applicable acceptance criterion to changed behavior and evidence. Look for omitted paths, wrong defaults, broken existing invariants, unauthorized scope expansion and UI behavior that diverges from accepted decisions. A green unit suite can still accompany a missing requirement. Use examples from the spec independently of implementation-derived expected values.

## Quality

Use repository standards first. Follow material execution paths for error handling, state consistency, compatibility, security/privacy, recovery and data loss. Load specialist roles only for relevant risks. Inspect whether names, boundaries and dependencies make the change understandable to its maintainers.

Possible duplication, scattered edits, misleading names, needless indirection and speculative abstraction are prompts to investigate, not mandatory refactors. A fix must improve the actual project under its constraints. Do not demand new frameworks, languages or a large rewrite merely to satisfy a heuristic.

## Evidence record

Record axis, severity grounded in impact, location, requirement/rule, triggering case and supporting observation. If verification could not run, name the limitation. Prefer a few defensible findings to exhaustive speculative lists.
