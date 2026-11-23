# Spatial, canvas and WebGL scenes

Use an actual spatial renderer only when the task benefits from depth, procedural geometry or many animated primitives. Keep real engineering measurements and physical product claims grounded in their owning source; a pleasing model is not dimensional evidence. A technical model should begin in its agreed assembled state if the interaction explains disassembly.

Separate scene data, state/time, camera, rendering and input. Prefer a shared time source and deterministic seeds for reproducible capture. State what selection changes in the model, material, clipping or annotation; changing only a caption is not a visual demonstration of the selected subject. Avoid accidental camera travel that obscures the explanation.

Inspect bounding volumes, clipping, depth ordering, lighting/material readability, transparency and annotation overlap. Check resize, pixel ratio, pointer coordinates and context/resource disposal. Bound particle counts, texture sizes and resolution from actual performance evidence. Test reduced-motion/static fallback and renderer/context failure. Shader compilation or a nonempty canvas is not visual acceptance.

For timed export use visual-storytelling with a deterministic seek/render contract. Sample frames and decoded output must match the same scene state. For interactive output, exercise user input on the intended runtime and inspect interruption/reversal; screen recording is supplementary evidence, not a substitute for state verification.

Stop owned animation loops, listeners and mixers before disposing their resources. Track geometry, materials, textures and render targets individually; do not dispose shared cached assets while other views still use them. Compare repeated mount/unmount against a stable resource baseline, not an invented requirement that every count become zero. Keep CSS coordinates and framebuffer/pixel-ratio coordinates consistent for shaders and input. A browser installed on a host does not establish GPU or software-renderer availability.
