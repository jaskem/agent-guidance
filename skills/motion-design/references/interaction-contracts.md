# Motion behavior contracts

For each important transition, record trigger, source state, animated object, destination, semantic change, interruption rule and fallback. Use a concise state table or diagram only when it clarifies branching. Preserve object identity and hierarchy; an element should appear to come from the control or location that explains it.

| Situation | Design and verification question |
| --- | --- |
| Toggle or selection | Does another activation reverse from the current visual state, and does actual selection match the view? |
| Open/close or route transition | When is focus moved/restored, when is content interactive, and what happens if removal interrupts exit? |
| Scroll-progress scene | Can the same state be reached forward, backward and by direct position? Is the initial state correct before scroll? |
| Scroll-triggered reveal | Is it intentionally once-only or repeatable? Does reverse scrolling preserve usable content? |
| Drag/direct manipulation | Does the object follow input without delayed business state, and settle/cancel predictably? |
| Loading or asynchronous work | Does progress reflect known state; can retry/cancel work without waiting for ornament? |
| High-frequency actions | Is repeated motion restrained enough for sustained work, with immediate useful feedback? |

Separate a continuous cyclic movement from an object entering or settling. A constant-rate loop may use linear timing; it is not universally wrong. Motion curves and durations are starting hypotheses chosen from distance, frequency and purpose, then inspected. Avoid blanket prohibitions on fades, keyboard-triggered feedback or any single property; keep response immediate and content usable.

Reduced-motion handling is a complete alternate experience: remove unnecessary travel, parallax, zoom, smooth scrolling or pinning while retaining meaning and state changes. Check the live preference change and clean up prior JS/canvas timelines. Do not rely only on CSS to stop independently scheduled effects or on near-zero global durations that can break callbacks. Do not hide content behind an animation that never runs. Validate pause/stop controls and flashing constraints when applicable rather than claiming compliance from one preference branch.
