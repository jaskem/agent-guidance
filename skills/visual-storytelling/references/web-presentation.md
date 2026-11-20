# Step-driven web presentation

1. Separate factual material from narration. Use the original to verify numbers, definitions and visual details; use the script to organise cadence and spoken emphasis. Map each step to a clear idea and observable visual state. Advance the explanation through meaningful object or relationship changes rather than repeating the script as title cards.

2. Choose stage dimensions and scaling for the audience and delivery context. Preserve safe space and readable text at the actual viewing size. Define theme tokens for repeated visual decisions. Use focused reveal when it helps understanding; avoid fixed rules for the number of steps, diagrams or animation types.

3. Keep one ordered state model for chapters and steps and one matching narration collection. Derive progress and audio mapping from it. Use stable identities for data and objects carried forward. Prevent interaction with embedded controls from also advancing the whole stage. Keep navigation discoverable and keyboard/touch usable; recording controls may hide only if they remain accessible to the presenter.

4. Implement back, forward, restart and direct navigation without stale state or duplicate playback. Define the expected transition state on a seek. If persisting position, validate it against the current content version. Inspect representative states and actual transitions; verify focus and reduced-motion behaviour where applicable.

5. Add audio only within the requested scope and actual available service. Keep provider, text and resulting files traceable; do not assume keys or install a provider by default. Time visuals to measured audio length. Estimated silent timing is a preview fallback, not synchronisation proof. Verify autoplay restrictions, missing-audio behaviour and controls.

6. Deliver the working web experience. If video was requested, verify the actual recording/encoding route and inspect its output; a browser preview or a URL is not an exported film. State any remaining recording, audio or playback gap precisely.
