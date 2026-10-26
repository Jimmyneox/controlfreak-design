# Site colourways — PCB corporate wordmark / lockup (Wave 1 site chrome)

Masters: `control-freak-corporate-{wordmark,lockup}-<colour>.svg` (+ `png/@1x,@2x`). Lockup carries the POOL AUTOMATION tagline — pool site only; product/hub sites use the **wordmark**.
Colours: white `#ffffff`, navy `#0b1f3a`, forest `#0f2e2c`, cream `#efe9df`, gold `#a8834f`, **ice `#eaf3f8`**, **cool-blue `#2f6f9f`** (ice/cool-blue added 2026-10-26 for C01; `build_corporate.py`).

| Site | Chrome | Wordmark | Favicon set |
|---|---|---|---|
| Hub (light) | white/light | `wordmark-navy` | `brand/app-icons/parent/` |
| Hub on dark / C03 Basement Guard | dark navy/slate | `wordmark-white` (or `navy` on light panels) | `c03-basement/` (C03), `parent/` (hub) |
| O15 Terrarium | cream / forest | `wordmark-forest` on cream; `wordmark-cream` or `-gold` on forest | `o15-terrarium/` |
| C01 Cold Plunge | ice / slate | `wordmark-navy` or `wordmark-cool-blue` on ice; `wordmark-ice` on slate/dark | `c01-cold-plunge/` |
| O04 Reef | per Reef brochure | Coral-teardrop leads (`brochures/O04-reef/approved-mark/`); attribution = `wordmark-navy` (light) / `wordmark-white` (dark) | `o04-reef/` |

Text-led product names for C03/O15/C01 (see `brand/PRODUCT_MARKS.md`). No new product marks.

## Favicon exception — favicons = drops (2026-10-26)
Browser/app icons (favicon.svg/.ico/16/32/48, apple-touch, PWA) use the **teardrop/drop silhouette**: hub = navy parent drop; C03 = white drop, O15 = forest drop, C01 = cool-blue (#2f6f9f) drop (same parent geometry, recolored); O04 = coral-teardrop drop (solid silhouette at 16/32). Flat, transparent, no plates. The corporate **attribution wordmark stays PCB**. Favicon ≠ marketing lockup. Built by `brand/app-icons/build_icons.py`; PCB icon masters moved to `brand/app-icons/_unused/`.
