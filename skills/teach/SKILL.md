---
name: teach
description: Teach a bounded concept through verified examples, especially the user's own code or workflow. Use for learning, guided code walkthroughs and explaining architecture to others. Exclude routine implementation and simple factual answers needing no lesson.
---

# Teach

## 1. Ground the learning goal

Use the user's question and known preferences to identify one practical outcome, such as explaining a data flow to IT. Read any existing technical guide, learning goal and relevant current source. Do not start a course or interview when the question already supplies the goal.

For project explanations, trace actual files and behavior. State when code or evidence is unavailable; use a labelled generic example rather than implying it describes the project. Check current technical facts with primary sources as appropriate.

## 2. Explain one useful unit

Use the user's language, short sentences and familiar domain concepts. Start with what the component accomplishes, then follow one concrete input through the important transformations to its output. Connect code names to their responsibility. Distinguish intended design, implemented behavior and untested interpretation.

Choose prose, a small table, a diagram or an interactive example based on what makes the concept easier to grasp. Use existing supported artifact tools when needed; a simple explanation does not require an HTML lesson, new framework or repository changes.

## 3. Make understanding observable

For a learning session, offer a small prediction, explanation or safe exercise tied to the goal. Give feedback on the user's actual response. Do not infer mastery from reading, agreement or silence. Avoid forcing a quiz into a direct request for an explanation. Use [learning records](references/learning-records.md) when durable learning notes are appropriate.

## 4. Close at the right size

Answer the requested question and show the source points that substantiate it. Provide a short practical recap the user can reuse when useful. Recommend a next topic only when it follows from the goal or observed difficulty. Persist learning goals or demonstrated insights at the established private destination when authorized; keep product truth in its repository and link it.

Do not modify production code during teaching unless the user also requests an implementation. If a real defect is found, explain it with evidence and preserve it at the existing task owner when authorized.

Read [sources and adaptation](references/sources.md) when maintaining this package.
