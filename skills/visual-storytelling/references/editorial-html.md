# Offline editorial HTML

1. Preserve the original source and form a readable working extract. Check headings, tables, code, formulas, footnotes and image meaning against the original where extraction could silently omit them. Note inaccessible or uncertain content. Identify the facts and detail that must survive editing; avoid invented information-retention percentages.

2. Build a prose-first outline around the reader's question. Use tables for comparisons and visual blocks for explanations that benefit from them. Make every visual answer a specific question. Choose reading width, density and aesthetic independently; a narrow text column can coexist with a wider factual figure. An article need not resemble a dashboard or landing page.

3. Build a representative opening and section with actual content. Establish type hierarchy, colour, spacing, links and figure captions; inspect the rendering before extending it. Use semantic HTML, accessible heading order, readable table overflow and meaningful alternate text. Add a contents list only when it helps navigation. Preserve source and figure references.

4. For a self-contained single file, inline CSS, scripts and required media/fonts, or use dependable system fonts. Prefer a small static implementation unless existing tooling makes another approach useful. Do not add an unpinned component framework merely for styling. Keep controls that serve reading usable with keyboard and touch.

5. Open the final delivered file, check desktop and narrow layouts, text clipping, code/formulas, tables and contents links. Test with network blocked when supported; otherwise inspect dependencies and state that offline operation remains untested. A build with inlined CSS/JS alone does not prove embedded images and fonts work offline. Verify any requested print/PDF output separately with its format workflow. Deliver the HTML and editable source, with the actual scope of checks.
