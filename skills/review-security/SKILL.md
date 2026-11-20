---
name: review-security
description: Assess a bounded security risk in code, local file operations, authentication, integrations or dependencies and report evidence-backed findings. Use for threat and abuse-case reviews; exclude general safety guarantees, unrelated scans and unrequested remediation.
---

# Review security

For the web-platform branch, load modern-web-guidance before the dependent technical decision when the assessment concerns browser APIs, client-side sanitization or other web-platform security. Use its accepted package and relevant guides; retain this method's outcome, project browser policy and real visual/runtime checks. Backend-only, native-only and purely editorial work do not trigger that branch.

## 1. Bound the review

Follow the configured operating guide once per session and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Fix the reviewed revision, changed surface, runtime and authorization. Identify assets, input authors and trust boundaries before selecting checks.

If code, environment or ownership is unavailable, state the review boundary and continue independent analysis. Do not infer safety from an internal network, local execution or a green audit.

## 2. Trace credible misuse

Follow relevant input to its effects. Include local/shared filenames, paths, overwrites, archives and imported data where present; include identity, access, network and model/tool output where used. Read [threat cases](references/threat-cases.md) for concrete branches.

Rank plausible cases by impact and reachability. Use the system's accepted security requirements; do not apply a web-service checklist to unrelated desktop software.

## 3. Verify the important claims

Inspect the implementation and use controlled distinguishing checks on the authorized target. Record the entry point, preconditions, relevant guard and resulting effect. Preserve existing work and data; avoid destructive probes, secret exposure and unapproved external disclosure.

Use available subagents on your own initiative when a step calls for independent work or a separate investigation/review can materially improve the result; no explicit user request is needed. Give each a bounded brief and evidence target, keep one writer per shared object, follow current host capabilities, and verify the integrated result yourself.

## 4. Assess fixes and residual risk

Separate confirmed defects, credible but unverified risks, and controls actually observed. For dependencies, examine the exact lockfile/advisory, reachable path and fix cost; an audit matches known advisories and is not a trust guarantee.

Recommend the smallest effective repair and its regression evidence. Execute repairs only within the authorized scope through the existing implementation/review owner. Keep independent work moving when one finding lacks access or a decision.

## 5. Report the bounded result

Return material findings with source/revision, evidence, affected asset, impact, preconditions and a concrete next action. Record accepted deferrals at the existing task owner with rationale and review trigger. State what was not tested; no findings in this scope does not mean the whole system is secure.

For provenance when updating this method, read [sources](references/sources.md).
