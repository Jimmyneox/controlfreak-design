# Wave 1 site handoff (Design → ECC)

Mirrors `Jimmyneox/controlfreak-platform-public` layout. ECC copies folders as-is; Design does not push to the public repo.
Fixes hub root `favicon.ico` 404 (`root/` → public repo root).

## Favicon drops (copy contents of each folder into the target)

| Handoff folder | Public target | Source set |
|---|---|---|
| `root/` | repo/hub root `/` | `brand/app-icons/parent/` (navy parent teardrop drop, flat/transparent) |
| `products/O04-reef/site/` | `products/O04-reef/site/` | `brand/app-icons/o04-reef/` (coral-teardrop drop; solid silhouette at 16/32) |
| `products/C03-basement-guard/site/` | `products/C03-basement-guard/site/` | `brand/app-icons/c03-basement/` |
| `products/O15-reptile/site/` | `products/O15-reptile/site/` | `brand/app-icons/o15-terrarium/` |
| `products/C01-cold-plunge/site/` | `products/C01-cold-plunge/site/` | `brand/app-icons/c01-cold-plunge/` |

Paste each `head-snippet.html` into that site's `<head>`. Snippets use root-relative `/favicon.ico` etc.; if a product site is served under a sub-path (e.g. `/products/C03-basement-guard/site/`), change the href prefix to relative (`favicon.ico`) or to that path.

## Hero art — **CONCEPT / interim** (locked Living Demo Theater brochure fronts; not final site art)

| Public target | Handoff file | Design source | Tip |
|---|---|---|---|
| `products/O04-reef/site/assets/hero-concept-front.png` (+ `hero-concept-ha-home.png`) | same path here | `brochures/O04-reef/c-v8-gemini-outline/front.png`, `ha-home.png` | 0725816 |
| `products/C03-basement-guard/site/assets/hero-concept-front.png` | same | `brochures/C03-basement-guard/a-gemini-outline/front.png` | 4cf87f3–3e80cac |
| `products/O15-reptile/site/assets/hero-concept-front.png` | same | `brochures/O15-terrarium/concepts/A-living-demo-theater/front.png` | f64b579 |
| `products/C01-cold-plunge/site/assets/hero-concept-front.png` | same | `brochures/C01-cold-plunge/concepts/A-living-demo-theater/front.png` | 95500b3 |

Label as CONCEPT on any review build. No new art was created.

## Chrome wordmarks
See `brand/corporate/SITE_COLOURWAYS.md` (navy/white hub & C03, cream/forest/gold O15, ice/cool-blue/navy C01, coral drop + PCB attribution O04). Product marks: `brand/PRODUCT_MARKS.md`. Beta URL: unchanged (Platform placeholder).

## Favicon exception — favicons = drops (2026-10-26)
Browser/app icons (favicon.svg/.ico/16/32/48, apple-touch, PWA) use the **teardrop/drop silhouette**: hub = navy parent drop; C03 = white drop, O15 = forest drop, C01 = cool-blue (#2f6f9f) drop (same parent geometry, recolored); O04 = coral-teardrop drop (solid silhouette at 16/32). Flat, transparent, no plates. The corporate **attribution wordmark stays PCB**. Favicon ≠ marketing lockup. Built by `brand/app-icons/build_icons.py`; PCB icon masters moved to `brand/app-icons/_unused/`.

## A — Hub product-card marks
`hub/product-cards/` (README table + `preview-dark-32-48.png`). Cream icons for dark hub cards. Favicons stay drops.

## B — Demo physical objects (photoreal v2)
`products/{O04-reef,C03-basement-guard,O15-reptile,C01-cold-plunge}/demo/` — photoreal `base.jpg` + overlay SVG. Inline `object-inline.svg` (or inject `object.html`; or `object.svg`+`base.jpg`; or `overlays/overlays.svg` over an `<img>`). Root `.cf-demo-object` class toggles unchanged from 1559d14 (+ O15 `uvb-on`); `#water` scaleY / C03 `#float`. Full map in `WIRING.md`. Flat v1 archived at `brand/demo-objects/_flat-svg-v1/`.
