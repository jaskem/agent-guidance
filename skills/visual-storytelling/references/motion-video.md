# Deterministic motion and MP4

1. Resolve duration, aspect ratio, required content and audio scope from the request and accepted decisions. Choose a visual grammar and narrative structure. Storyboard the change each shot explains and the subject/position/direction inherited by the next shot. Reuse accepted identity; use alternatives only for a consequential unresolved direction.

2. Define one timeline for picture, narration and sound events. Use real speech timestamps when claiming speech synchronisation; label sentence-level alignment accurately and never invent word timings. Record the source of music, effects and narration separately. Keep audio optional when the requested result permits it.

3. Make each frame computable from time: use a pure render(t), deterministic randomness and explicit asset readiness. Avoid hidden previous-frame state, wall-clock time or uncontrolled animation during capture. Use the same scene implementation for preview and export. Derive layout from output dimensions and adapt composition for another aspect ratio rather than cropping blindly.

4. Confirm a functioning browser renderer and encoder such as ffmpeg/ffprobe, or a supported equivalent. Tool names, installed packages and an upstream script are not evidence the pipeline works. Do not run an upstream installer merely to check capability. Build a small actual render before expensive production; check that repeated and out-of-order timestamps agree.

5. Inspect composition stills and continuous motion around state changes and shot joins. Check subject continuity, readable text, speed, intended pauses and loop seams. For sound, distinguish measured loudness/peaks from actual listening. Encode the requested film when supported; inspect the final file's decode, dimensions, fps, duration, frame count and intended audio tracks. Assess black frames against the design intent.

6. Deliver the actual encoded film and editable timeline/source with rebuild details. A contact sheet or source page does not prove video export; an encoded file does not prove complete playback review. State exact untested audio, rendering or export limits and the next required check.
