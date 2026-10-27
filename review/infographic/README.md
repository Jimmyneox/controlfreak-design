# Wave 1 "How it all connects" — review images (not for merge)

Review-only branch for Jimmy and the PM (2026-10-27). Nothing here ships; delete the branch after review.

- **v1-*.png** — bilateral hub and spoke: sensors → controller → Power Hub → your equipment, Home Assistant → phone, voice, alerts (infographic-style skill).
- **v2-*.png** — leads with the 3 problem → fix pairs from controlfreak-platform `design/INFOGRAPHIC_PROBLEM_FIX.md` @ 849f68e around a hub with a dotted orbit, then a compact "how it all connects" circuit row. Layout ideas from the reference sample (ref-02 orbit + capsule cards, ref-08 icon wells, ref-06 outline numerals); colours are each product's own palette. (v2 C03 shows no pump alternation; v3 restores it.)
- **v3-current-*.png / v3-proposed-*.png**: v2 refined with the impeccable skill.
  - No coloured side-tab borders and no eyebrow kicker.
  - All text is 11px or larger, with 0.6in page margins.
  - Flow chips are sized to their labels.
  - C03 keeps the weekly pump alternation.
  - Each product is rendered twice: in its current brochure palette and in a proposed palette.
- **v3-palette-swatches.png**: current vs proposed palettes. The proposals use the product-palette method and come from each product's world:
  - O04: dark actinic dusk with coral.
  - C03: light concrete with safety yellow.
  - O15: dark bark with moss and terracotta.
  - C01: light ice with glacial slate and cedar.

  Signature hues are at least 48° apart (OKLCH 35/91/139/240), and every text pair passes WCAG AA. Locked marks (the O04 coral teardrop and the PCB wordmark) keep their colours.
- **v1-O15.png** is refreshed: node 06 is now "Your equipment" (dashed = gear you own) and keeps the natural-day fact.

All versions carry the safety line and the "Works with the Control Freak gear you already own…" line word for word, three cited numbers, and Concept labels.

## v4 (O04 first, for direction)

Jimmy rejected v1 and v2: page 6 must look like the brochure pages around it, and like his references (3D, not flat).

- **v4-O04.png**: a light reef page built from the pack's own fonts, CSS, lockup and light-mode phone.
  - The hub is a concept 3D render (three.js) of the controller + Power Hub, sitting on a raised platform inside a dotted orbit.
  - The three problem → fix pairs are raised capsules with bevelled icon wells and extruded numerals.
  - A folded-ribbon flow, slab stat cards, and the safety and gear lines word for word.
  - No orange, per Jimmy: the accent is violet, from the reef's actinic light and purple corals.
- **v4-O04-in-context.png**: page 5, the new page 6 and page 7, side by side.
