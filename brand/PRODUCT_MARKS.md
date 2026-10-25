# Product-line marks (PCB family)

Each product mark **mirrors** the parent Control Freak mark: same rounded PCB frame,
same via pads and corner traces, same stroke language. Only the **top motif**, optional
**bottom cue**, and **wordmark** change. Co-brand with
[PARENT_BRAND.md](../PARENT_BRAND.md) (“brought to you by Control Freak”).

## Wave 1 set (first to ship)

| Product | Id | Top motif (replaces ladder) | Bottom cue | Wordmark |
|---|---|---|---|---|
| Reef / aquarium | O04 | Fish silhouette in the capsule | Soft wave (keep) | REEF |
| Basement guard | C03 | House + water drop | Wave or drip line | BASEMENT |
| Reptile / vivarium | O15 | Terrarium box + heat lamp | Warm wave / ground | REPTILE |
| Cold plunge | C01 | Tub / plunge silhouette | Cold wave | PLUNGE |

Hydro already has a soft mark; remake into this family as **HYDRO** (sprout in capsule) when Wave 2 skins start.

## Deliverables per product

- `masters/<slug>-mark-currentColor.svg`
- `masters/<slug>-mark-navy.svg` (or forest to match parent flat set)
- `masters/<slug>-mark-cream.svg`
- PNG exports navy-on-cream and cream-on-dark (replace older `mark-*-navy.png` when ready)

## Don’ts

- Don’t invent a second company logo that competes with Control Freak.
- Don’t put the metallic hero treatment on product marks (line art only).
- Don’t drop PCB vias or the rounded board outline.
