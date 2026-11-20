# Oil UI design-method review — 20 November 2026

## Decision and scope

Recommendation: extend the existing UI methods with the bounded techniques below. Do not install Oil UI unchanged as another default lifecycle. Its core outcomes already have owners in this collection, and several upstream defaults conflict with the accepted workflow and dense operational interfaces.

This is a source review, not an installation, runtime evaluation, verified benchmark or product UI audit. The report records proposals for the parent integration batch; it does not mark them implemented.

- Upstream: [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui/tree/81f2657f41410f04ae47ba77f902fcc0567eaab2).
- Exact main commit: `81f2657f41410f04ae47ba77f902fcc0567eaab2`, verified through the commit endpoint as well as the repository tree. Commit date: 18 November 2026; message: release 0.34.2.
- Main skill metadata: `oil-ui` version `0.34.2`.
- Existing canonical baseline examined: `jaskem/agent-guidance@bfd504878f4c9707cd41b3a68f7d32f6be49b2f2`, including the Garden integration.
- Applied maintenance route: maintain-agent-instructions with bounded source comparison; configured Guide already read, Notion setup version 0.0.6. No Notion mutation was made by this reviewer.
- Owned change: this report only. Source snapshots are temporary review material.

## What is already covered

An Oil UI package was not present in the inspected canonical skill catalog. That does not mean its general capabilities were absent.

| Oil UI outcome | Existing owner and observed coverage |
| --- | --- |
| Visual proposal or new bounded interface design | `design-ui-improvements`: extension/preserve/overhaul modes; task fit, art direction, consequential density/motion/identity choices, inspectable artifacts, acceptance and authorized implementation continuation |
| Critique an existing interface | `audit-ui-ux`: real visual inspection, dense/empty/error states, content fit, column widths, craft, evidence-based priority and coverage gaps |
| Compare alternative layouts or interactions | `prototype`: representative task/data, structurally distinct alternatives, runnable question, actual interaction and recovery evidence |
| Real user-flow verification | `test-user-flows`: actual browser/native actions, expected/actual results, persistence, error recovery and precise environment limits |
| Campaign/product imagery or storyboards | `image-art-direction`: reference roles, fixed/varying attributes, component facts, continuity, matched conditions and inspected native generation |
| Editorial/step/timed narrative | `visual-storytelling`: verified source facts, object continuity, real controls, timing/output distinctions |
| Tokens/components and product identity | Existing design-system role, UI methods, product-owned accepted design sources and `logo-design`; a provider's aesthetic is not a new product contract |
| Honest verification, source ownership and autonomy | General work cycle and package maintenance already distinguish installed/read/applied/proven, preserve accepted consent, and avoid duplicate trackers |

The existing UI criteria explicitly inspect oversized table columns, stretched objects, excessive chrome and repeated padding. Oil UI reinforces task-first first screens; it does not introduce the need to check compactness.

## Concrete useful additions

These are narrower than adopting a new method. Integrate only where the technique is not already explicit, with one normative owner.

| ID | Technique and upstream evidence | Existing owner to extend | Observable acceptance |
| --- | --- | --- | --- |
| OIL-01 | Keep product-reference and interaction-reference evidence separate. A product screenshot supports composition/content/identity; an interaction reference needs trigger → object change → feedback → next state evidence. Read `references/design-direction.md`. | `design-ui-improvements/references/art-direction.md` | A reference records its role, inspected source and which relationships are retained or changed. Static branding cannot be cited as proof of an interaction. |
| OIL-02 | Translate vague feedback such as “premium” or “more refined” into a visible relation: type contrast, grouping, control density, material, motion or hierarchy. Name the main object/action and visible result at the relevant state. Read `references/light-path.md` and `design-direction.md`. | Existing art-direction reference | The next proposal identifies the affected element/relation and the expected visible result, without a mandatory new questionnaire or numeric design dial. |
| OIL-03 | Compare direction skeletons before polishing: same task/content, current baseline first when relevant, comparable viewport and optical scale. For layout-only variants keep the accepted typography/color language fixed. Read `task-explore.md`, `style-explorer.md` and `build_explorer.py`. | `prototype/references/ui.md` and existing visual-handoff reference | Each variant settles a named uncertainty; a color swap is not called a layout alternative. A shrunk preview does not prove text readability. Selection refers to the current candidate/version rather than a stale preview. |
| OIL-04 | Distinguish style borrowing, exact screenshot reconstruction and generated UI inspiration. Record logical viewport, image pixel dimensions, scale/DPR, crop and fixed regions separately. Establish major alignments/ratios before details. Read `layout-and-viewport.md`, `image-ideation.md` and `measure_reference.py`. | New optional reference branch under `design-ui-improvements`, not a separate lifecycle | The requested fidelity is explicit; an unknown pixel-to-CSS scale remains a stated assumption. A generated long image is not treated as the actual desktop viewport. Exact reproduction is judged against the user's reference and real render. |
| OIL-05 | Give each image one job, inspect it in its actual container, and check mobile crops, alpha edges, callout alignment and matched asset quality. For series derive state variants from the accepted base where appropriate. Read `media.md`. | Existing UI visual-handoff plus image-art-direction composition recipes; avoid duplicate normative text | Asset/reference roles and immutable facts are retained; final container/crop is inspected. An attractive isolated asset or filename extension does not prove in-page fit or transparency. |
| OIL-06 | Make motion communicate state continuity. Separate geometry-only change from content replacement, enter/leave/reposition, and scroll-driven progress from once-triggered reveals. Check reverse travel, rapid repeats, interruption and reduced motion. Read `motion.md` and `scroll-narrative.md`. | Optional UI motion reference; visual-storytelling only for narrative-specific details | Business state updates independently of animation completion; the same selected object stays identifiable. Normal-speed feel is observed through actual operation/playback, not inferred from sampled frames. |
| OIL-07 | Offer a bounded fresh exploratory UX pass separate from scripted acceptance: reviewer infers a plausible primary goal from the visible surface, records actual choices and “blocked / wrong turn / hesitation.” Read `ux-review.md` and `ux-reviewer.md`. | Optional branch in `test-user-flows/references/flow-evidence.md` | Report distinguishes reviewer interpretation from product requirements, observed path from expected path, and tool/data problems from product defects. This complements, never replaces, intended-task, persistence and recovery checks. |
| OIL-08 | Preserve successful distinctive choices during refinement; write an explicit “retain” item alongside defects and acceptance targets. Apply a subtraction pass without deleting task evidence or making the page merely emptier. Read `reviewer-manual.md` and `visual-review.md`. | Existing audit finding/visual handoff references | A repair preserves the useful feature it could accidentally erase. Removing a repeated container is judged by task clarity/content fit, not by a quota of fewer cards. |

A small screenshot-reference branch is the strongest missing discrete procedure. It fits the existing UI-design method's responsibility. No new installable core skill is justified by this review. Do not add a second `oil-ui` default to perform the same work.

## Upstream behavior to adapt or exclude

| Topic | Observed upstream instruction | Local treatment |
| --- | --- | --- |
| Autonomy and confirmation | `SKILL.md`, `light-path.md` and `task-explore.md` commonly stop after a direction recommendation; explicit “you decide/directly do” bypasses the pause. | Existing clear implementation authorization already suffices. Ask only about a material unresolved decision; do not require a magic phrase or interrupt ready work. |
| Image-first UI | `SKILL.md` and `image-ideation.md` prefer generating UI images before implementation when native generation exists, including unattended work. | Select imagery when it resolves a visual question or supplies a real asset. Do not make a raster intermediary compulsory for compact data tools, existing-system repairs or deterministic UI layouts. Native image_gen remains the authorized generation/editing capability here. |
| Dense workspaces | `image-ideation.md` prescribes 20–28px module spacing, 22–28px card padding and 44–56px list/table rows as implementation sizes. It also fixes “petite typography and generous open whitespace.” | These values are examples, not defaults. Preserve platform, input method, accepted density and representative content. A touch heuristic cannot determine every expert desktop row height. |
| Color/prompt recipes | The same reference specifies 45–65-word prompts, an 85:10:5-like neutral/anchor/highlight ratio, a single dark focus anchor and 2–3 micro-components. | No universal prompt limit, palette ratio or component count. Use the existing brief and actual data semantics; do not erase meaningful multi-series color or invent focus metrics. |
| Invented evidence | `visual-language.md` proposes irregular-looking example figures; `light-path.md` and `reviewer-manual.md` move demo disclaimers to delivery notes or delete “example/unverified” text. | Synthetic fixtures may be useful but remain clearly scoped. Never present fabricated metrics/testimonials as live evidence. Retain an in-product demo/uncertainty label when needed to prevent deception; avoid implementation chatter in ordinary flows. |
| Novelty and ratings | New designs receive 1–10 scores, novelty anchors, three-second thumbnail/masked tests and mandatory rework for certain generic layouts. | Useful internal diagnostic lenses, not user research or universal release criteria. Readability and task outcomes outrank novelty. Do not score visual quality without actual image inspection and an explicit appropriate rubric. |
| Concept quotas | Expanded concept generation requires at least three internal candidates and an independent gatekeeper; pairwise direction comparisons allow at most one shared visual trait, with some brand exceptions. | Meaningful alternatives only when uncertainty warrants them. A layout comparison may intentionally keep font/color; no fixed agent/candidate quota or reviewer-veto lifecycle. |
| Motion | `motion.md` requires three animations per new interface; `scroll-narrative.md` requires section entrances plus a scroll-driven narrative on all marketing/brand/exhibition pages, with minimum amplitudes and GSAP-related choices. | Retain semantic feedback, continuity and control. Motion amount, dependency and scroll treatment follow the task, accessibility and device budget. A static appropriate page is not a defect. |
| Test/build policy | `light-path.md` says run only type checks/lint; production build/full tests only if the user asks. | Follow actual repository-required checks and proportionate change risk. An upstream design procedure cannot weaken the existing verification contract. |
| Screenshot tooling | `tools.md` says its screenshot helper is mandatory unless a specialized Oil host tool exists, excluding a generic browser as equivalent. | Prefer supported task/host tools. Select missing observations explicitly; no compulsory Chrome/CDP runner or new runtime just to follow a provider. |
| Screenshot helper result | `shoot.mjs` emits readability hints, aesthetic border-count heuristics and tailored contrast floors; some action warnings do not change exit status. `lint()` converts execution errors into a `lintError` finding. | A completed process or no warning is not accessibility conformance or interaction acceptance. Treat hints/errors as scoped evidence, not a proven blocking gate. Confirm applicable standards independently before imposing minima. |
| Reviewer isolation | Oil separates author and reviewer materials and bars the author from reading its review manuals. Its UX reviewer intentionally lacks original task/expected path. | Fresh task-local review can reduce anchoring; it does not confer knowledge or authority. Parent still checks originating requirements and quality. Do not hide relevant acceptance from every reviewer. |
| API/update routing | Optional checker contacts Oil's version service; image runner reads Oil token/config and uses a paid provider API. Pro and companion products are promoted. | Exclude unnecessary updater, account probing, credit discovery, API runner and sales prompts from the integrated method. Installed credentials never authorize service use. Pin reviewed content and use the host's supported installation process. |

The screenshot heuristics are visible source behavior, not an accusation that they are advertised as a complete standards audit. Their exact assumptions make direct adoption inappropriate as our general quality gate.

## Repository inventory and review coverage

The pinned complete tree contains 55 blob files. There is one main skill, not a collection of several independently installable UI skills.

| Material | Coverage in this review |
| --- | --- |
| `SKILL.md`, English `README.md`, root `LICENSE` | Read completely. README benchmark, gallery and Pro claims remain upstream claims; external gallery/benchmark and paid Pro content were not evaluated. |
| All 19 references | Read: design-direction; direction-persuasion; image-ideation; layout-and-viewport; light-path; media; motion; play; reviewer-manual; scroll-narrative; style-explorer; task-explore; task-review; tools; ux-review; ux-reviewer; visual-language; visual-review; workdir. |
| 9 scripts | Inventoried all; statically examined entry/dependency/network behavior and relevant implementation paths for screenshots, lint, serving roots, comparison manifests, image preparation, measurement, media provenance and update/image requests. Large scripts were inspected selectively; this is not an exhaustive code/security audit. |
| `assets/style-explorer.html` | Inspected comparison controls, candidate/viewport behavior, local readiness probe and use of the bundled template/dependencies. Did not render or claim its interactions worked here. |
| 8 test modules | Inventoried test definitions: 284 `test_*` methods in total. Read representative test names/structure; did not execute the tests or claim they pass. |
| `.github/workflows/tests.yml` | Read. Linux core/browser matrices, conditional browser job, manual Windows matrices, ffmpeg/CJK-font setup, and browser-process cleanup check are declared; no CI run was observed. |
| License assets | Read Instrument Serif OFL notice and bundled Alpine.js license/version notices. No font/image binary was executed or redistributed. |
| Multilingual README variants, marketing raster images and external companion repositories | Inventoried, not independently examined as separate design evidence. |

No installer, update check, balance check, generation request or upstream executable was run. No connected browser, paid service or API account was opened.

### Script/dependency map

| Script | Purpose and reviewed dependencies/effects |
| --- | --- |
| `build_explorer.py` | Python 3.10+ standard-library comparison generator. HTML/image candidates and loopback live URLs; native viewport metadata, current-baseline sorting, fingerprints and sandbox/CSP handling. Uses the local HTML template, logo, font and bundled Alpine. |
| `shoot.mjs` | Node 22+ CDP screenshot/action/sequence/recording helper. Requires local Chrome/Chromium/Edge; optional ffmpeg for recording. Uses a temporary browser profile and loopback static server with path/host checks. Reports runtime and visual hints separately. |
| `chrome.mjs` | Shared temporary-profile launch/cleanup; honors CHROME_PATH, uses platform browser discovery and mock keychain/password-store flags. |
| `prep-image.mjs` | Node 22+ plus local browser canvas; crop/resize/encode/alpha handling and responsive snippets. Preserves originals; if transformed encoding is larger, it may copy the original with a warning, so read actual output dimensions rather than assuming the requested transform happened. |
| `measure_reference.py` | Python sampling/annotation/crop helper. Optional Pillow; limited standard-library 8-bit non-interlaced PNG fallback. Measurements describe pixels/ratios, not verified CSS semantics. |
| `curate-media.mjs` | Node 22+; external public collection/media APIs and downloads; optional ffmpeg/ffprobe for contact sheets, probes and posters. Produces per-asset SOURCES.md and use/license records. Rights labels remain source metadata requiring appropriate verification. |
| `oiloil-image.mjs` | Node 22+ optional paid image client. Reads OIL_TOKEN or Oil CLI config, defaults to api.oiloil.org (OIL_IMAGE_API override), sends prompts/references, uses idempotency/status recovery. Not necessary or authorized merely because the method is installed. |
| `check_update.py` | Python standard library; public version request to ui.oiloil.org (OIL_API override), per-install/cache state, optional explicitly approved update through a pinned oil-cli commit. Default check does not replace the skill. |
| `check_update.sh` | Optional shell/Python launcher for the checker, including a missing-Python marker. No relevance to our host-managed distribution. |

The JavaScript helpers primarily use Node built-ins and have no npm dependency installation requirement in this repository. That does not eliminate browser, ffmpeg, network, service-account or font/library dependencies.

## License and provenance

- Root code/docs: [MIT, copyright 2026 oil-oil](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/LICENSE).
- Bundled `assets/vendor/alpine.min.js`: Alpine.js 3.17.4, MIT notice; bundled Vue shared/reactivity notices identify version 3.5.41 and MIT.
- Bundled Instrument Serif: SIL Open Font License 1.1, copyright 2022 The Instrument Serif Project Authors. Preserve the OFL notice if the font is redistributed; it is not covered by replacing its notice with root MIT.
- External retrieved assets retain their own item-specific rights. A museum API or public URL is not permission for every downstream use.
- Integrating concepts through original local procedures avoids introducing a runtime dependency on Oil. If copying or substantially adapting text/code, include the exact root MIT notice and pin in affected package provenance.

## Proposed verification for an integration batch

Exercise concrete cases with current task-local context; structure checks alone do not prove selection or judgment:

1. Dense operational table with over-wide IFC columns: preserve its task and expert controls; do not apply 44–56px rows, large card padding or mandatory image-first generation.
2. User requests two layout alternatives under a locked visual identity: same data, task, viewport and fonts/colors; structural differences and current baseline are visible.
3. User supplies a high-DPR screenshot for faithful reconstruction: identify logical scale or disclose uncertainty, preserve the reference intent, render real code and compare; do not silently reinterpret it as style inspiration.
4. Landing page motion already assembled at initial state: verify forward/reverse/direct-entry and reduced motion; do not force an unrelated animation quota.
5. Fresh exploratory UX pass without a live runtime: report a static/untested boundary; do not imply the route or save succeeded.
6. Screenshot helper returns success with hints, or the lint phase errors: no green acceptance from the exit code alone; classify the exact missing observation.
7. User has clearly authorized execution: complete independent ready work without another direction-approval stop.
8. Ordinary precise spacing/text repair: direct proportional handling, no direction workshop, image generation or new full lifecycle.

These are proposed cases. No fresh behavioral run, accessibility conformance test or measured design/productivity gain is claimed by this review.

## Source links

All links below refer to the reviewed commit:

- [Main skill](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/SKILL.md)
- [Light path](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/light-path.md)
- [Design direction](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/design-direction.md)
- [Reference/image calibration](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/image-ideation.md)
- [Media](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/media.md)
- [Motion](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/motion.md)
- [Scroll narrative](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/scroll-narrative.md)
- [Exploratory UX protocol](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/ux-review.md)
- [Reviewer manual](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/reviewer-manual.md)
- [Tools and evidence boundaries](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/references/tools.md)
- [Scripts](https://github.com/oil-oil/oil-ui/tree/81f2657f41410f04ae47ba77f902fcc0567eaab2/scripts)
- [Declared CI](https://github.com/oil-oil/oil-ui/blob/81f2657f41410f04ae47ba77f902fcc0567eaab2/.github/workflows/tests.yml)

Next technical step: parent chooses and applies the bounded additions at existing owners, reviews their source delta and runs relevant package/behavior/distribution checks. This reviewer has not performed those mutations.
