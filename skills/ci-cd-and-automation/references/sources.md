# Sources and adaptation

Canonical owner: `jaskem/agent-guidance`, `skills/ci-cd-and-automation/`. Treat installed packages as versioned distributions of that source. Package version: 1.0.0.

This is an original compact adaptation, reviewed on 2026-11-16 against `addyosmani/agent-skills` commit `39b723ceebf81474d0557c1fecd01eddab585563`:

- [CI/CD and automation](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/ci-cd-and-automation/SKILL.md)
- [Constraint-driven development](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/constraint-driven-development/SKILL.md)
- [Security checklist](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/references/security-checklist.md)

Retained: reproducible quality gates, early useful feedback, correctly scoped parallel jobs, CI failure feedback, controlled delivery and verification that failures block the intended action.

Intentional differences: inspect the real provider, event, runtime, lockfile and commands instead of imposing GitHub Actions or Node examples. Separate quality-policy ownership from enforcement, and release acceptance from pipeline success. Omit fixed timing, review-count and rollout requirements. Preserve current task ownership and authorization; inaccessible protection settings remain unknown. Ordinary ChatGPT reminders and scheduled tasks use their host capability rather than this software-pipeline method.

The package bundles no upstream scripts, workflow templates or runtime dependencies. Verify current provider/tool documentation and dependency licenses when implementing a specific pipeline. No other provider skill is required. Propose later upstream changes; do not silently replace accepted local adaptations.

## Upstream license

From the pinned [LICENSE](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/LICENSE):

```text
MIT License

Copyright (c) 2025 Addy Osmani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
