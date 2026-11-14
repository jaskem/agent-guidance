---
name: optimize-performance
description: Investigate a reported slowdown, performance regression or explicit budget with representative measurements and a controlled improvement. Use for latency, throughput, responsiveness or resource bottlenecks; exclude speculative optimization and unmeasured speed claims.
---

# Optimize performance

## 1. Define the user-visible symptom

Follow the configured operating guide once per session and reuse verified context. Resolve only the relevant project, work object and existing source/task owner; a standalone request needs no project scan. Identify the operation, representative input, runtime and accepted performance target. Read prior attempts and the current implementation before proposing a change.

If the workload or measuring capability is missing, establish what can be measured and report the gap. A feeling of slowness supplies a question, not a bottleneck or speedup.

## 2. Establish a comparable baseline

Measure the actual operation at a fixed revision with documented inputs and conditions. Repeat enough to reveal variation; distinguish cold/warm state and local, network or hardware boundaries. Read [measurement notes](references/measurement.md) for comparison and diagnostic choices.

Locate the dominant cost with the smallest useful timing, trace or profile. Add bounded diagnostics only when needed; avoid a new telemetry platform by default.

## 3. Run one justified experiment

Choose a change that addresses the measured cause and preserves required outputs, validation, freshness and recovery. State the expected mechanism and what would disprove it. Route authorized implementation through the established development/review owner.

Use available subagents on your own initiative when a step calls for independent work or a separate investigation/review can materially improve the result; no explicit user request is needed. Give each a bounded brief and evidence target, keep one writer per shared object, follow current host capabilities, and verify the integrated result yourself.

## 4. Compare behavior and cost

Re-run the same measurement budget under comparable conditions and report the distribution or stable summary, not a single favorable run. Check relevant correctness and recovery cases alongside time, memory or other affected resources.

Keep a performance claim only when evidence exceeds ordinary variation and applies to the stated boundary. Remove only your own ineffective or regressive experiment and verify the resulting state; preserve unrelated changes.

## 5. Record what was learned

At the existing task or performance record, save revision, workload, method, baseline/result, variation, behavior checks and the keep/revert decision. Include unsuccessful attempts so they are not repeated blindly. Add a proportionate regression guard only when justified. Finish with a measured result or the precise first unproven step, never an invented gain.

For provenance when updating this method, read [sources](references/sources.md).
