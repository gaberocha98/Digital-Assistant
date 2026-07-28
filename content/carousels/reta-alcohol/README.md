# Carousel — Why alcohol hits harder on retatrutide

Remake of an Instagram carousel (@joeknowspeps original), rebuilt as an
on-brand, evidence-forward 7-slide set. **Loose reinterpretation** — copy
rewritten in our own voice, structure improved, hook and CTA added.

## Files
- `slides.html` — source layout for all 7 slides (1080×1080 each)
- `render.mjs` — Playwright script that exports each slide to PNG @2x (2160×2160)
- `slides/slide-01.png` … `slide-07.png` — ready-to-post images

## Rebuild
```bash
cd content/carousels/reta-alcohol
ln -sf /opt/node22/lib/node_modules node_modules   # or: npm i playwright
node render.mjs
```

## Slide flow (8 slides)
1. Cover / hook — "Why alcohol hits way harder on retatrutide"
2. Mechanism 1 — slowed gastric emptying
3. What people report — faster drunk, worse hangovers, nausea/reflux
4. Mechanism 2 — reduced alcohol-metabolizing enzyme (GLP-1 research)
5. Mechanism 3 — weight loss lowers tolerance (less body water → higher BAC)
6. Mechanism 4 — appetite loss → drinking on a near-empty stomach
7. Practical takeaways (added value beyond the original)
8. CTA + disclaimer

> Mechanisms 1–4 and the CTA mirror the 7-slide source; slide 7 (practical
> takeaways) is added value. Swap `eonresearch.bio`, the "E" logo mark, and
> the "Comment PEPTIDES" keyword for your real brand assets before posting.

## Suggested caption
Two drinks now hitting like four? If you're on retatrutide (or any GLP-1),
you're not imagining it. Here's what's actually happening in your body —
and how to drink smarter for the version of you that exists now. 🔬

Save this for your next night out, and send it to the friend who needs it.

*Educational only — not medical advice. Always talk to your prescriber.*

#retatrutide #GLP1 #peptides #tirzepatide #weightloss #alcohol #metabolichealth
