# Sources and adaptation

Canonical owner: `jaskem/agent-guidance`, `skills/constraint-driven-development/`. Treat installed packages as versioned distributions of that source. Package version: 1.0.0.

This is an original compact adaptation, reviewed on 2026-11-16 against `addyosmani/agent-skills` commit `39b723ceebf81474d0557c1fecd01eddab585563`:

- [Constraint-driven development](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/constraint-driven-development/SKILL.md)
- [Floor-guard reference](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/constraint-driven-development/references/floor-guard.md)
- [Quality-gate helper](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/constraint-driven-development/scripts/quality-gate.mjs)
- [Definition of Done](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/references/definition-of-done.md)

Retained: a durable quality contract, baseline-based targets, declared control placement, explicit exceptions, review of weakened checks, and deliberate positive/negative/error controls before claiming enforcement.

Intentional differences: preserve existing norm/task ownership instead of requiring `CONSTRAINTS.md`; omit mandatory interviews, fixed thresholds, check-duration limits and compulsory external tools. Separate policy from CI integration and ordinary development. Respect existing authorization and keep unsupported claims open. Treat shallow diff matching as review evidence, not semantic proof. No upstream helper or executable example is bundled or required. Installing this skill does not install scanners or invoke another provider package.

Review exact tool/report versions before adopting an implementation. Third-party scanners and distributed rule packs have their own dependencies and license terms. Propose later upstream changes; do not silently replace accepted local adaptations.

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
