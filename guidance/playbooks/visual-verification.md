# Visual and interaction verification

Use this when a claim depends on a rendered artifact, interface or live user action. The work cycle owns overall execution and closure; this playbook owns observation-surface selection and evidence limits. Respect the configured consumer version and current host/tool rules.

## 1. Identify what must be observed

Identify the exact artifact or app/build, the requested state or journey, relevant input, and the claim to verify. Distinguish a proposal, local build, deployed page and native application. A historical capture or different runtime is useful comparison evidence, not proof of the current target.

Resolve the user's chosen environment and discover currently available capabilities. Use purpose-built service tools for supported service operations; choose the visual runtime separately. Do not infer a missing capability from one failed runner or assume that an online device exposes every UI operation.

## 2. Select the relevant available surface

| Situation | Route |
| --- | --- |
| User specifies an accessible remote desktop or native target | Inspect that environment and exact target first, using its documented supported capabilities |
| Target runs on the user's computer and authorized Remote Desktop access is available | Prefer that actual runtime for native layout, window, input, display-scale and integration evidence |
| Target is a web page and a connected browser is the chosen relevant surface | Use the applicable browser capability and its interaction rules |
| Target is a generated document, image or video | Inspect the final rendering through the appropriate viewer or format capability; use runtime playback for temporal claims |
| Preferred surface lacks a required operation or cannot reach the target | Record the specific failed capability, then use a supported relevant fallback and bound what it proves |

A cloud browser can supply web evidence when it is the intended environment or a justified fallback. Convenience alone is not a reason to replace an accessible user-selected runtime. When the preferred environment is unavailable, continue supported independent checks and keep target-specific acceptance open. A local browser launch failure calls for capability discovery, not an immediate claim that no visual route exists.

Keep one active controller per live surface. Observe current state before input, use controlled data, preserve the user's open work and inspect the result after an action. Follow required screenshot, handoff and delivery conventions of the actual tool. When only filesystem/process tools are exposed, establish whether a documented capture or automation route is actually available; module presence alone is not capture or input proof. Do not install a new remote-control stack merely to claim coverage.

## 3. Observe at useful scale

Inspect overview and readable detail with representative content. Record viewport or window size and scale when known. Include states that could change the conclusion: dense tables, long labels, empty/error/loading states, selected/disabled controls, small windows, zoom or reduced motion as relevant. Check typography, contrast, alignment, column fit, clipping, wasted space and state consistency rather than judging from source alone.

For interaction, capture starting state, actual action and resulting state. For motion, inspect intermediate and final states plus interruption/reversal or seeking where supported. A screenshot does not prove keyboard behavior, playback smoothness, audio, file writes, synchronization or hardware. Use the relevant task method for those claims; avoid extending a visual test into unrelated product mutation.

## 4. Preserve proportional evidence

Keep build/artifact identity, surface, state/input, expected versus observed result and meaningful evidence at the existing task/artifact owner. Limit retained screenshots to relevant content. Distinguish capture availability, rendered inspection, exercised interactions and measured performance. Mark unrun checks explicitly and recheck only affected states after repairs. A fallback observation must retain its original environment label.

Close when the requested claim is supported on the relevant surface or its remaining boundary is explicit. Successful capture proves a capture route; it does not certify every future app or a complete product journey.
