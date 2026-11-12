---
name: maintain-agent-instructions
description: Audit or improve AGENTS.md, instruction routing, reusable skills and their source ownership when the user requests workflow maintenance or an observed recurring instruction defect needs repair. Exclude ordinary product bugs, generic advice and unrelated cleanup.
---

# Maintain agent instructions

## 1. Reconstruct the current route

Follow the user's configured operating guide once per session, including its required tool-call version. Reuse verified context; load project and task owners only when relevant, refreshing them after a project/scope change or material new evidence. Use the routed context-entry playbook when available. If required context is inaccessible, disclose the gap and continue only independent work.

Read the current request, applicable `AGENTS.md` and referenced workflow. Inventory the accessible repositories, instruction files, actual `SKILL.md` packages, installed copies and enabled Notion skills relevant to the task. Record exact source revisions and access gaps. A role document or a folder called skills is not proof of an installed skill. Search/fetch failures are unknown state, not absence.

Load an existing instruction-feedback playbook when routed. Reuse its observation record and owner rules. Do not start a competing maintenance backlog.

## 2. Diagnose useful changes

For each material issue, record observed effect, exact source, responsible owner, minimal repair and a concrete case that would reveal recurrence. Distinguish observed defects from untested improvement hypotheses. Use [design criteria](references/design-criteria.md) to assess triggering, steps, completion, context cost and overlap.

Classify material by responsibility: personal preferences/context, repository routing, product contracts, reusable procedure, reference, or mechanically enforceable check. Keep one normative owner. Check canonical source and pinned consumers before editing a generated or installed copy.

Complete this step when the proposed edit has a traceable reason and one owner. If a source is inaccessible, bound the finding and continue other independent checks.

## 3. Repair the owner

Within the user's requested maintenance scope, make the smallest coherent repair. Prefer code/configuration validation for a mechanically detectable failure. Retain helpful existing instructions; shorten or split only when routing or comprehension improves. Preserve product invariants, existing document destinations and approval boundaries.

For a new skill, give it one responsibility, a discriminating description, ordered steps, observable completion and explicit handling of missing inputs. Put branch-specific detail behind direct relative links. Use supported capability-based tools instead of assuming a CLI, browser or agent is present. Check the complete upstream package, dependencies, license and reviewed revision before importing or adapting it. Never run an upstream installer merely to inspect it.

Use the host's skill-authoring and installation workflow. When GitHub owns the source, validate there and treat personal/Notion installations as versioned distributions. When Notion owns an independent personal skill, edit that owner. Preserve provenance and compare copies before updates. Change a pinned consumer only in an explicit consumer-update batch; use its vendoring tooling rather than editing copied files.

## 4. Verify what changed

Run the existing repository and host checks for the touched surface. Check descriptions, local references, package completeness and invocation metadata. Exercise representative positive, negative and missing-input cases. For substantial revisions use fresh-context forward tests when delegation is available and authorized, following the selected delegation playbook. Without that playbook, keep the trial read-only with a bounded task and raw artifacts, no expected answer, and verify the returned evidence. Without an independent run, label the check a walkthrough.

Structure checks prove structure, not reasoning reliability. Record behavioral observations separately. Resolve findings before installation and verify the saved remote package and enabled state before claiming availability. On uncertain writes, inspect the target before retrying.

## 5. Report and hand off

Update the existing inventory with source revision, actual installation locations, tests, limits and intentional upstream differences. Report what is retained, adapted, installed or deferred, with links. Preserve unresolved cases with a concrete trigger for follow-up. Do not turn successful installation into a claim that every client will automatically load the skill; registries and invocation support vary.

For provenance, read [sources](references/sources.md) when auditing or updating this skill.
