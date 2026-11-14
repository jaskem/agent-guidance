# Logic exploration

Expose a small state model through domain-language actions and a readable current-state view. Keep the logic separable from the display when practical. Provide reset and scenarios for the normal path, a meaningful edge case and an invalid transition.

Prefer a self-contained browser artifact if it fits the question. Avoid a new framework, backend or real database solely for the demo. If persistence is the question, use a clearly isolated fixture destination and make recovery behavior visible.

Check that actions change the intended state and illegal transitions are visibly handled. Show assumptions and uncertainty next to the result. A plausible model is a candidate until checked against domain evidence and accepted decisions.

Keep the experiment's initial state, transition, expected outcome and observed outcome distinguishable. Derive expected states from the proposed rule, not by calling the implementation to generate both sides. Expose cancellation, invalid input and failure/recovery when they bear on the question. Label fixtures and simulated boundaries; they do not qualify real persistent or concurrent writes.
