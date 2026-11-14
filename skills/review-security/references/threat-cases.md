# Threat cases

Choose credible cases from the real trust boundaries, not every category by default.

| Boundary | Concrete checks |
| --- | --- |
| Imported/local/shared files | Malformed content, bounded resource use, archive traversal, filename/path confusion and parser behavior |
| Delete/move/overwrite | Resolved permitted root, refusal to target the root itself, authenticated ownership/authority and safe handling of links or path races |
| Identity or authorization | Actor may perform this operation on this object; a hidden button is not an authorization guard |
| Service or browser data | Validate shape and encode at the effect boundary; avoid command/query/markup injection |
| Model/tool output | Treat returned text as data; constrain actions and their arguments through actual authority |
| Dependencies | Actual install boundary, chosen manager, lockfile, install scripts, advisory reachability and upgrade behavior |
| Diagnostics and retention | Secrets/personal data exposure, purpose, minimal useful fields and working deletion where required |

A path marker can be forged by anyone able to write it. Establish expected ownership outside attacker-controlled content; an exists-check and later operation can race when ancestors are mutable. A read-only inspection or safe fixture may reveal a risk without proving the production protection works.

Record a finding as source/revision, entry point, prerequisite, demonstrated or reasoned effect, affected asset and smallest repair. Rank unverified hypotheses separately. Do not run forced dependency remediation, broad cleanup or destructive probes merely because a checklist mentions them.
