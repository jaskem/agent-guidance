---
name: prototype
description: Build a bounded prototype to answer an unresolved UI, interaction, state or data-model question. Use when alternatives need a concrete demonstration. Exclude ordinary production implementation, cosmetic tweaks and already-decided behavior.
---

# Prototype

## 1. Name the question

Follow the user's configured operating guide once per session, including its required tool-call version. Reuse verified context; load project and task owners only when relevant, refreshing them after a project/scope change or material new evidence. Use the routed context-entry playbook when available. If required context is inaccessible, disclose the gap and continue only independent work.

Read the current goal, accepted design constraints and relevant project route. State the single question the prototype will answer and how the user can judge it. Choose [UI comparison](references/ui.md) or [logic exploration](references/logic.md). If the choice is unclear, inspect the existing app and ask only when the answer changes the artifact.

Use the host's supported preview or site workflow and existing project tools. Do not require the user to install a local runtime. Load routed interaction, visual, accessibility or domain guidance only where its omission could change the answer.

## 2. Build a safe, runnable experiment

Mark the artifact as a prototype. Use representative non-sensitive fixtures and isolated state. Existing app data may be read when authorized; prototype controls must not mutate production records. Preserve the surrounding design context when it affects judgment.

Keep implementation limited to the question. Use a clear start/reset path. A prototype may omit production robustness, but must actually run and expose the behavior needed to judge the question. Verify its controls and relevant states; do not represent a screenshot as proof of interaction.

## 3. Capture the result

Present the artifact with the question, concrete comparison or scenarios and any known limitation. If human preference is needed, wait for that decision instead of inventing a winner. Record the chosen option and reason only after it is established; an agent recommendation remains a recommendation.

Save the artifact and result in the existing durable project or artifact destination and link them from the owning task. Do not rely on an OS temporary path as the sole handoff. Integrate validated behavior only when authorized, using the production workflow and its checks. A prototype is not a production release.

Read [sources and adaptation](references/sources.md) when maintaining this package.
