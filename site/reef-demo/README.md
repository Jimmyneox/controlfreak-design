# Reef Control Pro: full-screen live demo

The whole browser window is the reef tank. A glass app panel floats over it, and
switching things in the panel changes the tank. It is a marketing simulation:
every value is made up in `reef-demo.js`, and nothing is sent anywhere.

Content rules: `controlfreak-platform/products/O04-reef/CAPABILITIES.md` (binding).
Palette and type: `controlfreak-platform/products/O04-reef/BRAND_GUIDE.md`.
Panel pattern: `site/demo-template/` (SIMULATION badge and disclaimer kept).

## Run it

```bash
python3 -m http.server -d site 8000   # from the repo root
```

Open http://localhost:8000/reef-demo/. Screenshot hooks: `?state=feed`, `?state=night`,
`?state=low`, `?state=leak`.

## Files

| Path | What it is |
|---|---|
| `index.html` | Page: tank layers, header, panel, footer, simulated push |
| `reef-demo.css` | Tank, fish motion, glass panel, bottom sheet (≤760 px), reduced motion |
| `reef-demo.js` | Fish and particles, outlet/mode/scenario state, jitter, parallax, tab-hidden pause |
| `assets/bg/` | ChatGPT backgrounds, unmodified. Portrait gets the 9:16 plate via `<picture>` |
| `assets/fish/*.webp` | Demo-object sprites from `brand/demo-objects/o04-reef/fish/`, made by `brand/demo-objects/o04-reef/tools/resize_fish_web.py`: Lanczos downscale (premultiplied alpha) to 2× the largest displayed CSS width, capped at 260 px, then lossy WebP q80 with alpha_q 100. Edge check: `_review/fish-edge-check-clownfish-3x.png` (PNG left, WebP right) |
| `assets/mark/` | Approved white Reef lockup and drop, from `brochures/O04-reef/approved-mark/` |
| `assets/fonts/` | Space Grotesk and Inter woff2 (OFL, licenses included), from `controlfreak-platform/book/assets/fonts/` |
| `_review/` | Review screenshots at 1440×900 and 390×844 |

## Behavior

- **Feed**: Return and both powerheads Off, flakes drift down, fish rise. Pumps resume after 20 s.
- **Maintenance**: the same pumps stay Off until Normal is tapped.
- **Main light Off**: the scene switches to moonlight blue at once (on/off, no fade).
- **Low temperature** demo: the tank reading falls to 74.2 °F, the Heater outlet turns On, then a red alert and a simulated push appear.
- **Water leak** demo: Leak shows "Leak", top-off shows "Locked out / Leak detected" ("Overfill lockout" is kept for a real overfill, which the demo doesn't simulate), then a red alert and a simulated push appear.
- With the return and powerheads all Off, drifting particles and caustics slow to 30%.
- When the tab is hidden, all animations pause, and so do the jitter, countdown and scenario timers.
- `prefers-reduced-motion: reduce` gives a static scene: fish placed but still, no rays, caustics or particles, static flakes, no parallax.

## Open items

- `#beta` is a placeholder; the sign-up URL is not decided (see the TODO in `index.html`).
