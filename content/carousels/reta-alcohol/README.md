# Carousel — "Why alcohol hits harder on Reta"

EON Research rebrand of a 7-slide Instagram carousel. Dark theme using the
brand palette in [`/brand/colors.md`](../../../brand/colors.md) (teal `#0D9488`
+ amber gold `#F59E0B`), Inter typeface.

## Output
- `slides/EON-Reta-01.png` … `EON-Reta-07.png` — 2160×2700 (2× Instagram 1080×1350 portrait)

## Slides
1. Hook — "Why alcohol hits way harder on Reta"
2. Slowed digestion — Reta slows gastric emptying
3. What people report — drunk faster / worse hangovers / worse nausea & reflux
4. The research — GLP-1 reduces an alcohol-metabolizing enzyme (npj Metabolic Health and Disease)
5. Lower tolerance — weight loss → less body water → higher BAC
6. Empty stomach — appetite suppression → drinking on an empty stomach
7. CTA — Comment "PEP" for the EON beginner's guide

## Regenerating
```bash
cd content/carousels/reta-alcohol
# Requires: node, playwright, and Inter fonts embedded at ./fonts/inter-embed.css
node render.js   # writes PNGs to ./out
```
The renderer expects `fonts/inter-embed.css` (base64-embedded Inter, weights
400–900). It is not committed here due to size; generate it from the Inter
font files, or point `template.js` at a locally installed "Inter" family.

## Editing copy
All slide text and highlight markup live in `slides.js`
(`<span class="hl">` = amber highlight, `<span class="tl">` = teal/mint highlight).
