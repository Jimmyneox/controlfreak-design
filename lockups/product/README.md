# Product attribution lockups — "brought to you by Control Freak" (PARENT_BRAND v1.4)
**Company mark:** corporate PCB circuit **wordmark** (no POOL AUTOMATION tagline) from `brand/corporate/control-freak-corporate-wordmark-*.svg`.
Navy teardrop packs are retired → `_superseded-teardrop-2026-10/`. The product mark (e.g. Reef coral-teardrop) leads: place it above (stacked) or left (horizontal).

| Variant | Company mark | Attribution | Ground |
|---|---|---|---|
| light | navy #0b1f3a | slate #5b6670 | transparent (light grounds) |
| light-on-plate | navy | slate | cream #f4f1ea plate |
| dark | white | mist #c3cddb | transparent (dark grounds) |
| dark-on-plate | white | mist | navy #0b1f3a plate |
| gold | gold #a8834f | #c9c2b6 | transparent (forest/dark grounds); -on-plate = forest #0f2e2c |
| cream | cream #efe9df | #c9c2b6 | transparent (dark grounds); -on-plate = forest |
| forest | forest #0f2e2c | slate | transparent (light grounds); -on-plate = cream #efe9df |
| currentColor | currentColor | currentColor @72% | inherit |

"brought to you by" = Inter Medium, outlined. PNG @1x/@2x + `png/_contact-sheet.png`. Rebuild: `python3 lockups/product/build_product_lockups.py` (from repo root).
Theme colorways (gold/cream/forest) added 2026-10-25 per James: colors flow with the site theme. For anything else, use currentColor.
