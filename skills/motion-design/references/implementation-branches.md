# Choose the smallest suitable implementation

These are design/verification prompts, not executable API recipes. Read the actual installed version and current primary documentation before coding. Prefer existing dependencies and inspect the real target; upstream examples may depend on deprecated or internal APIs.

| Branch | Ownership and failure checks |
| --- | --- |
| Native CSS or Web Animations | Use for local state feedback where supported. Feature-detect newer entry/exit, discrete display and intrinsic-size behavior; provide an ordinary usable fallback. Keep final layout/state real rather than visually transformed only. |
| Layout changes / FLIP | Batch before measurements, layout mutation and after measurements; avoid interleaved read/write thrashing. Verify nested transforms, scroll offsets and text/border scale distortion. Keep reading order and actual hit targets aligned with the visual result. |
| React presence/shared layout | Preserve stable keys and an owner that remains mounted for exit. Choose overlap/wait/layout-removal from desired behavior, avoid uncontrolled layout identity reuse, and inspect nested scale effects. A remounting route wrapper cannot reliably own cross-route exit. Do not adopt private router internals as a generic solution. |
| GSAP or another timeline engine | Use scoped timeline/context ownership. Revert split text and clean up affected triggers/listeners on unmount or preference change. Wait for relevant font/image readiness and recalculate layout-bound timelines after real geometry changes. Do not globally kill unrelated effects. |
| Scroll orchestration | Distinguish native scroll, smooth-scroll driver and animation clock. If a driver is needed, use one synchronized clock with correct time units; account for nested scrollers, anchors, resize and content loading. Preserve a usable native/reduced-motion route without unnecessary pinning. |
| View transitions | Keep named identities unique, navigation semantics correct and ordinary navigation functional when unsupported. Exercise actual entry/back/forward routes; static DOM snapshots do not prove cross-page continuity. |
| SVG | Inspect viewBox, transform origins, actual path geometry and optical bounds. Path drawing or morphing must preserve meaningful final shapes; confirm compatibility instead of assuming arbitrary paths can interpolate. |
| Lottie or another exported animation | Check asset load/error state, segment playback, themes, input response and accessible meaning. Pause irrelevant offscreen loops where appropriate; inspect the real renderer and fallback rather than assuming vector export is cheap or faithful. |

Test lifecycle as well as appearance: repeated mounting, route exit, rapid toggles, live preference changes and slow asset readiness can reveal duplicate handlers or stale measurements. Use representative workload to identify main-thread, layout/paint and rendering costs. Transform/opacity often avoid some layout work but do not guarantee a frame rate, low GPU cost or correct semantics.
