# Product and UX assumptions

Optional advisory resource for `product-strategy-discovery` and `ux-research`. Use when an unsupported assumption could change a feature choice or interaction model. Skip for an already evidenced decision or an execution-only task with no new uncertainty. The resource does not authorize participant contact, telemetry, experiments, or scope expansion.

## Match the question to evidence

| Uncertainty | Potential evidence | What it does not establish |
| --- | --- | --- |
| Is this a recurring problem? | Existing accounts of actual work, support cases, or observation | How common it is across unobserved users |
| Can people understand and use this design? | Task-based observation with the relevant audience/context | Whether they need the feature |
| Can we deliver it under the constraints? | Focused technical evidence or an authorized prototype | Demand or usability |
| Is the benefit worth its cost and consequences? | Explicit costs, constraints, alternatives, and observed value | A universal score independent of context |

Separate an observation from its interpretation and the proposed decision. Pick an assumption whose failure would alter the choice; use existing evidence first. Define the observation that would support or contradict it before collecting new evidence. Numbers and thresholds must come from the actual decision context, not a generic framework.

## Original illustrative case

A request to add a second navigation sidebar may assume that users cannot find an existing action. Two competing explanations are poor discoverability and unclear terminology. A focused task observation could distinguish them: does the user miss the location, or reach it and misunderstand the label? A preference poll asking which sidebar looks better does not distinguish these explanations. A label change could be the smaller response if the second explanation fits the evidence.

If participants are unavailable, inspect existing evidence or perform an explicitly labelled expert review. Do not invent participant reactions or report an agent's simulated user as observed human evidence. A few observations may expose a failure mode without estimating its population frequency. Contradictory results may justify keeping the assumption unresolved rather than declaring validation.

## Sources and adaptation

Reviewed 2026-09-28. Original synthesis and example; no copied framework, templates, or scripts.

- Primary method reference: Teresa Torres, [Assumption Testing](https://www.producttalk.org/assumption-testing/): selecting risky assumptions, choosing evidence, and considering what results change. This is methodological guidance, not evidence about a particular product's users.
- Community discovery reference: Wondel.ai, [assumption mapping](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/continuous-discovery/references/assumption-mapping.md) and [continuous discovery skill](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/continuous-discovery/SKILL.md).
- Deliberately excluded: fixed interview cadence, mandatory team composition, universal percentages, automatic scoring, and a requirement to research every feature. The existing product/research roles own proportionality and decision output.
