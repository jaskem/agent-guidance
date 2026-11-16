# General workflow implementation — 17 November 2026

## Release scope

Guidance 0.6.0 and skill collection 1.1.0 implement the accepted general-workflow design. The canonical baseline was `69c8d43e779689f210d0d10f2b9140d00b30e777`. The exact published source revision and distribution proofs are recorded at the existing private installation owner after publication. This source report does not itself prove an installed package.

- One configured operating-guide entrypoint routes to the relevant standalone object or project; project links are not duplicated in the entrypoint.
- `guidance/playbooks/work-cycle.md` owns proportionate execution and closure across research, writing, data, design, software, external operations and scheduled work.
- `docs/METHOD-ROUTING.md` selects all 28 methods, direct handling and host capabilities. It distinguishes constraints, pipeline behavior, review, delivery, resumption and scheduling.
- Four Addy-derived packages are added at 1.0.0: constraint-driven-development, observability-and-instrumentation, deprecation-and-migration, ci-cd-and-automation. They retain pinned attribution and the MIT license.
- evidence-driven-development, maintain-agent-instructions, code-review and research advance to 2.1.0. The other 20 package versions remain unchanged. grill-me retains explicit invocation; the other 27 support relevant implicit selection.
- Existing providers remain available when explicitly requested, but do not form a second default lifecycle.

## Source research

The design reviewed repository organization, entrypoints, composition, supporting references, deployment and verification, not only skill names:

- Matt Pocock: `5863806dd4e15c63174bee4e7515a4256792ecfa`.
- Addy Osmani: `39b723ceebf81474d0557c1fecd01eddab585563`.

The prior provider-coverage baseline remains historical evidence. New reviewed provenance is separate in the catalog and changed package references. A source update is not silently adopted.

## Verification and observed behavior

The release verification commands are `python tools/check_foundation.py`, `python tools/check_skills.py` and `python -m unittest discover -s tests -v`, run from the clean committed candidate. Expected suite coverage is 27 test methods: 23 package/routing tests and four consumer-contract tests. The checks reject missing/duplicate/unknown routes and empty acceptance, as well as inconsistent declared package versions. Structural coverage is distinct from correct semantic selection.

The actual personal installation directories for all eight changed packages were validated with the host's bundled validator before saving. Source and remote installation checks are recorded separately.

### Fresh-context route trials

Forty raw Dutch requests were evaluated without revealing expected routes. All 28 method-specific requests selected their intended primary method. Twelve further requests exercised direct answers, document/data/image capabilities, document review, timed work, composition, missing access, ambiguous project selection and uncertain external writes. The agents loaded the selected source methods and prepared their first action and evidence boundaries.

[Recorded requests and observed selections](evidence/workflow-route-trials-2026-11-17.json) retain those observations. These are preparation/selection trials; the forty underlying user tasks were not executed. The tests do not guarantee future host selection.

### Four forward exercises

| Method | Actual exercise and observation | Evidence limit |
| --- | --- | --- |
| constraint-driven-development | A scanner printed ERROR while returning success. Reproduced that failure; repaired its result boundary. Clean returns 0, ERROR returns 1, unavailable/invalid verification returns 2. Thirteen local test methods passed, including preserving an opaque identifier contract. | Local fixture only; no actual scanner service or production merge protection. |
| ci-cd-and-automation | A test-only PR was omitted by a path filter and `python verify.py || true` swallowed failures. Removed those two causes; six local test methods passed and actual shell executions distinguished pass, failure and unavailable tool. | Local trigger/configuration and shell behavior; no provider run or enforcement in that fixture. |
| observability-and-instrumentation | An offline multi-entry importer scenario produced a bounded signal design covering correlation, retries, missing final events and privacy; proposed retention was explicitly unverified. | Proposal exercise; no runtime instrumentation or retention enforcement claimed. |
| deprecation-and-migration | A mixed-version shared-file transition with lossy conversion, partial interruption and an unknown quarterly consumer retained recovery and compatibility obligations, including new transactions after backup. | Proposal exercise; no live migration, restoration or retirement claimed. |

The two executed fixtures used Python 3.12.14; the pipeline fixture also used existing PyYAML 6.0.3 and Bash 5.2.37. Its configured Python 3.13 provider runtime was not executed.

## Review and corrections

An independent review assessed requirements and implementation against the complete baseline delta. It found stale package-version declarations in four supporting source records; these were corrected and a regression guard was added. The scanner trial exposed an unjustified identifier type restriction; the repair and the skill now preserve the documented contract instead of inventing a stronger requirement. The affected tests were repeated.

## Compatibility and continuation

This is a general foundation and skill-distribution batch. It does not change product semantics, project tasks, existing consumer pins, provider plugins or another person's personal skill account. Consumers must deliberately migrate their selected modules before claiming the new vendored work cycle. Notion setup instructions remain 0.0.6.

Next step after source verification: install the eight complete packages, verify reconciled personal and Notion distributions, and activate the existing central guide/catalog with the exact source revision. After distribution closes, project-specific consumer migration belongs to a separate authorized batch.
