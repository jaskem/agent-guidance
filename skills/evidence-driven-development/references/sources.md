# Sources and maintenance

Canonical source: jaskem/agent-guidance, skills/ (use the matching skill name). This package is an original adaptation, not an unchanged Matt Pocock distribution. Keep installed copies aligned with the recorded canonical revision; propose upstream updates rather than silently replacing local decisions.

Reviewed on 2026-11-12: https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa

Relevant upstream files: README.md; skills/productivity/writing-for-agents/SKILL.md and SKILL-MECHANICS.md; skills/engineering/tdd/SKILL.md; diagnosing-bugs/SKILL.md; implement/SKILL.md; code-review/SKILL.md; domain-modeling/SKILL.md; codebase-design/SKILL.md; setup-matt-pocock-skills/SKILL.md; skills/productivity/handoff/SKILL.md.

Retained concepts: small composable procedures, precise context pointers, progressive disclosure, observable completion, behavior-level checks, small usable slices, distinct requirements and quality reviews, and reuse of domain vocabulary.

Adaptations: use the existing repository workflow and destinations; ordinary reversible implementation choices need no repeated confirmation; tests match risk; diagnosis allows necessary code inspection and qualified hypotheses when reproduction is unavailable; handoffs use durable existing records; tools and delegation depend on host capability and authorization; no automatic upstream update. The upstream terminology is inspiration, not a replacement for a product's domain language.

Upstream license: MIT, copyright 2026 Matt Pocock. See [upstream license](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE). This original synthesis does not bundle upstream code or supporting scripts.
