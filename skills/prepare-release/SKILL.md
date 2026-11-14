---
name: prepare-release
description: Prepare or execute an authorized software release against its real packaging, distribution, acceptance and recovery requirements. Use for release readiness, portable-app delivery and rollback planning; exclude treating a plan as publication authority or imposing a generic web rollout.
---

# Prepare release

## 1. Resolve the release boundary

Follow the configured operating guide once per session and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Identify the intended version, exact source/build, audience, platform, distribution channel and permitted actions. Distinguish a readiness plan, package preparation and authorized publication.

Read existing release criteria and open tasks. Missing access or an unresolved consequential choice blocks only dependent actions; do not invent the target environment or a new delivery route.

## 2. Map acceptance to the actual product

Choose checks for changed behavior and its real runtime. Include install/start, core use, compatibility, failure/recovery and prior-version return where relevant. Read [readiness notes](references/readiness.md) for local packages, shared data and services.

A portable desktop app does not automatically need DNS, a CDN or a canary service. Browser fixtures, package presence and unit tests do not establish installed, network-share, audio or hardware acceptance.

## 3. Prepare the traceable package

Use project tooling and its real dependency/lockfile policy. Record source revision, build command, version, artifact identity and required files. Preserve user data and existing artifacts. Review migrations and whether the previous application can still read resulting data.

Use available subagents on your own initiative when a step calls for independent work or a separate investigation/review can materially improve the result; no explicit user request is needed. Give each a bounded brief and evidence target, keep one writer per shared object, follow current host capabilities, and verify the integrated result yourself.

## 4. Verify release and recovery

Check applicable criteria against the actual candidate and environment. Identify rollback triggers, a known previous artifact, data preservation and how recovery will be verified. Observe a rehearsal where authorized and possible; otherwise label it untested.

Keep required acceptance open when it fails or lacks evidence. A review-loop cap, documented ruling or successful build cannot close an unproven product criterion.

## 5. Deliver within the authorization

For a plan, return concrete steps and remaining gates. For preparation, deliver the candidate and evidence. Publish only when the task already authorizes that action and follow actual tool boundaries; verify the saved/downloaded or deployed result before claiming release.

Update the existing release/task owner with source, artifact, checks, recovery status and exact limitations. Do not create a parallel tracker, notify others or start monitoring schedules by implication.

For provenance when updating this method, read [sources](references/sources.md).
