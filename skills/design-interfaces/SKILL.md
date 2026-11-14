---
name: design-interfaces
description: Design or revise a caller-facing API, module interface, file format or command contract using concrete consumer cases. Use for inputs, outputs, errors, retries and compatibility; exclude settling domain meaning, routine implementation and unchanged interface explanation.
---

# Design interfaces

## 1. Find the actual boundary

Follow the configured operating guide once per session and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Read current consumers, contracts and the accepted change. Keep domain meaning with its domain owner; identify what callers must know and what the implementation can hide.

If the target, consumer or required behavior is missing, recover it from the named sources. Ask only the material unresolved choice; do not invent an API or reopen an accepted design.

## 2. Work through caller cases

Write the smallest useful set of normal, invalid, repeated, concurrent and interrupted calls. Describe inputs, outputs, observable effects, errors, ordering and compatibility. Read [contract cases](references/contract-cases.md) for stateful mutations or format changes.

Keep language, protocol and storage choices grounded in the actual system. A REST, TypeScript or deep-module example is not a required architecture.

## 3. Compare the consequential choices

Prefer a surface callers can use correctly with few facts to remember. Compare alternatives only where they change misuse, coupling, recovery or consumer cost. Keep existing dependent behavior visible, including observed quirks that consumers use.

Use available subagents on your own initiative when a step calls for independent work or a separate investigation/review can materially improve the result; no explicit user request is needed. Give each a bounded brief and evidence target, keep one writer per shared object, follow current host capabilities, and verify the integrated result yourself.

## 4. Check the contract before implementation

Trace the proposed cases through real callers. Check error handling, authorization, retry safety and upgrade behavior at the actual boundary. Distinguish observed behavior from a proposed promise; use distinguishing examples or contract tests when applicable.

A design request produces a contract or recommendation. Route authorized code changes through the existing implementation/review owner; design alone does not authorize implementation or migration.

## 5. Leave one usable contract

Update the existing contract owner, preserving unrelated content. Return the interface, concrete cases, compatibility effects, accepted decisions and exact remaining gaps. Finish when a caller can identify successful, rejected and uncertain outcomes without learning internal machinery.

For provenance when updating this method, read [sources](references/sources.md).
