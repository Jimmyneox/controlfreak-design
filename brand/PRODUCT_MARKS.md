# Product-line marks

Co-brand with [PARENT_BRAND.md](PARENT_BRAND.md) (“brought to you by Control Freak” =
**PCB corporate wordmark-only**, never the retired navy teardrop).

## Locked product marks

| Product | Id | Locked mark | Canonical assets | Tip |
|---|---|---|---|---|
| Reef Control Pro | O04 | **Coral-in-teardrop** (not PCB-family) | [`brochures/O04-reef/approved-mark/reef-mark-drop.svg`](../brochures/O04-reef/approved-mark/reef-mark-drop.svg) (+ `-white`, `-currentColor`; lockups `reef-mark-lockup*.svg`; JPG ref `reef-control-freak-coral-teardrop.jpg`) | **0725816** (still on main) |

O04 brochure literature: [`brochures/O04-reef/c-v8-gemini-outline/`](../brochures/O04-reef/c-v8-gemini-outline/) tip **0725816**. Soft-UI brochure looks are rejected — do not revive.

## Site marks — confirmed 2026-10-26 (matches locked brochures)

| Product | Id | Site / chrome mark | Favicon set |
|---|---|---|---|
| Reef Control Pro | O04 | Coral-teardrop product mark + PCB corporate wordmark attribution | `brand/app-icons/o04-reef/` (coral drop) |
| Basement Guard Pro | C03 | **Text-led product name + PCB corporate wordmark only** | `brand/app-icons/c03-basement/` (PCB simplified icon) |
| Terrarium Control Pro | O15 | **Text-led product name + PCB corporate wordmark only** | `brand/app-icons/o15-terrarium/` (PCB simplified icon) |
| Cold Plunge Control Pro | C01 | **Text-led product name + PCB corporate wordmark only** | `brand/app-icons/c01-cold-plunge/` (PCB simplified icon) |

No new product marks for C03/O15/C01 unless James cues. The PCB-family drafts below stay unused. Coral-teardrop = O04 only. Colourways: `brand/corporate/SITE_COLOURWAYS.md`.

## Wave 1 drafts (unlocked — PCB-family grammar until James locks)

Other Wave 1 products may still draft as PCB-family mirrors of the parent mark (same rounded PCB frame, vias, corner traces; only top motif / bottom cue / wordmark change). These are **not** locked marks.

| Product | Id | Draft motif (replaces ladder) | Bottom cue | Wordmark |
|---|---|---|---|---|
| Basement Guard Pro | C03 | House + water drop | Wave or drip line | BASEMENT |
| Terrarium Control Pro | O15 | Terrarium box + heat lamp | Warm wave / ground | REPTILE |
| Cold Plunge Control Pro | C01 | Tub / plunge silhouette | Cold wave | PLUNGE |

Hydro already has a soft mark; remake into this family as **HYDRO** (sprout in capsule) when Wave 2 skins start.

## Deliverables per *PCB-family* draft product

- `masters/<slug>-mark-currentColor.svg`
- `masters/<slug>-mark-navy.svg` (or forest to match parent flat set)
- `masters/<slug>-mark-cream.svg`
- PNG exports navy-on-cream and cream-on-dark (replace older `mark-*-navy.png` when ready)

O04 does **not** use this PCB-family deliverable set — use `approved-mark/` coral-teardrop only.

## Don’ts

- Don’t invent a second company logo that competes with Control Freak.
- Don’t put the metallic hero treatment on product marks (line art only).
- Don’t use a PCB-family fish silhouette (or any PCB capsule draft) as the O04 Reef product mark — coral-teardrop is locked.
- Don’t use the PCB corporate mark as a product logo.
- Don’t drop PCB vias or the rounded board outline on **PCB-family** drafts.

## Favicon exception — favicons = drops (2026-10-26)
Browser/app icons (favicon.svg/.ico/16/32/48, apple-touch, PWA) use the **teardrop/drop silhouette**: hub = navy parent drop; C03 = white drop, O15 = forest drop, C01 = cool-blue (#2f6f9f) drop (same parent geometry, recolored); O04 = coral-teardrop drop (solid silhouette at 16/32). Flat, transparent, no plates. The corporate **attribution wordmark stays PCB**. Favicon ≠ marketing lockup. Built by `brand/app-icons/build_icons.py`; PCB icon masters moved to `brand/app-icons/_unused/`.

## Hub product-card marks vs favicons (2026-10-26)
- **Favicons = drops** (unchanged since 0202420).
- **Hub product cards = product-identifying marks** in `brand/product-card-marks/` (tank / basement-sump / terrarium / plunge tub) — not drops.
- O04 literature/site product mark remains the coral teardrop; only the hub card uses the new tank/reef icon.
- PCB wordmark stays attribution-only.
- C03/O15/C01 remain text-led for product naming; these are hub-card icons only, not locked product logos competing with Control Freak.
