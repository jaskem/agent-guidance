# Sources

This is an original compact adaptation of selected techniques from Addy Osmani's `agent-skills`, reviewed on 2026-11-16. The full primary text, linked checklist and license were inspected at commit `39b723ceebf81474d0557c1fecd01eddab585563`. This pin identifies the reviewed input, not a claim about the latest upstream version.

- [Primary skill](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/observability-and-instrumentation/SKILL.md), `skills/observability-and-instrumentation/SKILL.md`; inspected text SHA-256 `e7fcb0820306d46268de9594d676ad98e35040858926c412b7000faa52a61f87`.
- [Observability checklist](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/references/observability-checklist.md), `references/observability-checklist.md`; Git blob `ad40d7aa3fca5d2091fa45be234c14aee22c3588`.
- [MIT license](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/LICENSE), `LICENSE`; inspected text SHA-256 `6f202f8bd568cd730dbb2b0d1f8e243bc74c2fa1f64dbce9b2c7ea08bd5c9fd7`.

## Intentional differences

- Make verified, durable detection and diagnosis the result. Ordinary bug diagnosis, temporary probes, performance optimization and release readiness keep their existing owners.
- Choose signals for concrete questions and the actual runtime. Do not mandate production services, OpenTelemetry, a dashboard, every signal type or supplier-specific thresholds, sampling rates, severity counts and launch gates.
- Preserve event/run/entry-point identity, field allowlisting and bounded cardinality while adding explicit healthy controls, missing-data limits, local/offline cases and telemetry-failure behavior.
- Preserve current user, project and host authority. An instrumentation task does not imply production fault injection, notifications, new monitoring schedules or a parallel tracker.
- Use original workflow text and examples; copy no upstream scripts or executable examples. No provider package must be invoked.

## Attribution and license

The selected upstream material is licensed under MIT. Retain its notice below.

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
