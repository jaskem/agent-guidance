# Focused Playwright diagnosis

Optional advisory resource for `quality-release`. Use when intermittent failure, waiting, or test isolation obscures a browser-behavior claim. Skip for unrelated unit tests, ordinary edits with sufficient evidence, or a proven result without an invalidating change. Consumer verification and retry rules remain authoritative.

## Distinguish explanations

| Observation | Candidate explanation, not a conclusion | Smallest useful discriminator |
| --- | --- | --- |
| Action completes but the expected result is absent | Rendering is delayed, or the operation failed | Inspect the existing trace and assert the specific resulting state |
| Failure occurs with concurrent workers | Shared account/data mutation or a product race | Identify the shared resource and ownership before changing worker count |
| Failure depends on an earlier test | Leaked fixture, storage, or server state | Compare setup/cleanup boundaries for that pair |
| Failure occurs only in CI | Environment, dependency, or timing difference | Compare versions and captured failure artifacts before adding retries |

These are diagnostic hypotheses. A test passing alone does not establish whether the product or test is correct.

## Choose the observable boundary

Playwright supports retrying assertions for observable page state. Prefer a stable user-facing locator and the outcome being claimed over an immediate boolean read or an arbitrary delay. Browser-context isolation does not by itself isolate a shared server account. Check both boundaries when relevant.

Original illustrative case: a save test clicks Save, sleeps, and checks a green icon. If the claim is persistence across reload, the icon alone is insufficient. Observe completion, reopen/reload within the supported lifecycle, and inspect the saved value. If the claim is only immediate feedback, do not turn it into a persistence test. A mocked success response can exercise UI behavior but cannot prove the real storage boundary.

## Limits and local adaptation

Use the installed Playwright version and official API documentation for exact syntax. This page adds no runner configuration, fixed repetition count, timeout increase, quarantine policy, or instruction to rerun a full suite. Repetition is useful only for a specified unresolved hypothesis within the consumer's verification budget. Do not replace the integration boundary being proved with a mock merely to obtain green results.

## Sources

Reviewed 2026-09-28. Original synthesis and example; no upstream files or scripts are copied.

- Primary: [Playwright best practices](https://playwright.dev/docs/best-practices) and [assertions](https://playwright.dev/docs/test-assertions). Live documentation: check compatibility with the installed version when API details matter.
- Community discovery/diagnostic reference: Currents.dev, [assertions and waiting](https://github.com/currents-dev/playwright-best-practices-skill/blob/283d5cbc5d11aac1abda058b16ad22c317d54dc0/playwright-best-practices/core/assertions-waiting.md) and [flaky tests](https://github.com/currents-dev/playwright-best-practices-skill/blob/283d5cbc5d11aac1abda058b16ad22c317d54dc0/playwright-best-practices/debugging/flaky-tests.md).
- Deliberately excluded: upstream burn-in counts, broad test commands, generic retry/quarantine defaults, and blanket mocking advice.
