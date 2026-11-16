# Sources

This is an original compact adaptation of selected techniques from Addy Osmani's `agent-skills`, reviewed on 2026-11-16. The full primary text and license were inspected at commit `39b723ceebf81474d0557c1fecd01eddab585563`. This pin identifies the reviewed input, not a claim about the latest upstream version.

- [Primary skill](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/deprecation-and-migration/SKILL.md), `skills/deprecation-and-migration/SKILL.md`; inspected text SHA-256 `1896d7db836fc067e2856739664db9ff5bb642526fdff2126d08ec0d588da4b7`.
- [MIT license](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/LICENSE), `LICENSE`; inspected text SHA-256 `6f202f8bd568cd730dbb2b0d1f8e243bc74c2fa1f64dbce9b2c7ea08bd5c9fd7`.

## Intentional differences

- Keep real consumer and data transition as the distinct result, with evidence and visibility limits before retirement. An absence of recent traffic or repository references is insufficient proof of no consumers.
- Choose compatibility phases from the actual runtime. Do not mandate canary percentages, service deployment sequences, compulsory deadlines or an alternative for an explicitly accepted sunset.
- Make interruption, retry/idempotence, uncertain writes, concurrent updates and preservation of original data explicit. A lossy transform needs a justified recovery path, not an automatically required or allegedly reversible `down` command.
- Distinguish planning, authorized execution and retirement without inventing approval rounds. Existing domain, contract, implementation, release and task owners remain authoritative.
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
