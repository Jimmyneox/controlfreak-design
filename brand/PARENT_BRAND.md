# Control Freak — parent brand rules (lockup & co-brand)

**Owner:** Control Freak Pool bot (public site / parent brand: controlfreakpool.com)  
**Audience:** Control Freak Platform (per-product skins, enclosures, apps, brochures, marketing in `controlfreak-platform`)  
**Status:** v1.1 — 2026-10-25 (adopts owner-supplied line masters)  
**Intent:** Each product gets its own identity. All products stay tied by one hero lockup: **“brought to you by Control Freak”** — layered brand, look of corporate scale. Product skins must nest under this parent without fighting the pool brand.

---

## 1. Brand architecture

| Layer | What it is | Who owns it |
|---|---|---|
| **Parent** | Control Freak (company / platform brand) | Control Freak Pool bot + controlfreakpool.com |
| **Product** | Named line (Reef, Basement, Reptile, Plunge, …) with its own mark, accent use, enclosure skin, app theme, brochure | Platform (`design/brand/`, product folders) |
| **Lockup** | Product mark + “brought to you by Control Freak” + parent mark | Shared rules below; Platform implements on skins/materials; parent site uses same |

Products never pretend to be unrelated companies. Buyers should feel “this is a Control Freak product for [hobby],” not “a separate brand that happens to use our board.”

---

## 2. Parent marks (source of truth)

Owner-supplied masters live in Platform at `design/brand/masters/` (mirrored in the parent brand store). Motif: rounded PCB frame + vias, pool ladder into capsule, wave, CONTROL FREAK wordmark.

| Asset | Path | When to use |
|---|---|---|
| **Line master (preferred)** | `masters/control-freak-mark-currentColor.svg` (also `design/brand/mark-core.svg`) | UI, print, web, lockups, favicons — recolor via `currentColor` |
| **Forest** | `masters/control-freak-mark-forest.svg` / `*-forest-on-cream.png` | Flat ink `#0f2e2c` on light / cream grounds |
| **Cream** | `masters/control-freak-mark-cream.svg` / `*-cream-on-forest.png` | Reverse mark on forest / dark grounds |
| **Gold** | `masters/control-freak-mark-gold.svg` / `*-gold-on-forest.png` | Accent / premium reverse only — sparingly |
| **Metallic hero** | `design/brand/hero/control-freak-hero-metallic.png` | **Parent site heroes, press kits, trade-show walls, high-impact ads only.** Never on product marks, app chrome, or co-brand lockups. |

**Adopted for controlfreakpool.com and all parent brand work:** the line masters above. Do not use the older navy/white PNG pair (`mark-core-navy.png` / `mark-core-white.png`) for new work; treat them as legacy until removed.

**Wordmark:** “CONTROL FREAK” stacked (CONTROL over FREAK), all caps, as drawn in the master. Do not write “ControlFreak,” “CF,” or “C.F.” in customer-facing lockups.

Product drafts (Platform until James locks): see `design/brand/PRODUCT_MARKS.md` and `masters/{reef,basement,reptile,plunge}-mark-*.svg`.

---

## 3. Color

### Mark / lockup ink (parent logo)

| Role | Hex |
|---|---|
| Forest | `#0f2e2c` |
| Cream | `#efe9df` |
| Gold | `#a8834f` (accent mark only) |

### Soft-UI / product chrome (unchanged — apps, floating pages)

Align with `design/STYLE.md` and `design/CHATGPT_HANDOFF.md`:

| Role | Hex | Notes |
|---|---|---|
| Navy | `#12355B` | App text, soft-UI outlines |
| Aqua | `#19B3C9` | Soft-UI accent (“on,” active). Gradient `#2CCBE0 → #19B3C9 → #0E8FA6` for buttons |
| Cool grey bg | `#E9EEF4` | Soft-UI surfaces |
| Label slate | `#6F8BAB` | Small uppercase labels + “brought to you by” line on light UI |
| Coral | `#FF6B4A` | Warnings only |

**Rule:** Logo lockups use forest/cream/gold. Soft-UI screens keep navy/aqua. Do not recolor the parent line mark to aqua, coral, or a product accent. On soft-UI pages, place the forest-on-cream (or cream-on-forest) mark on a contrasting plate if needed.

**Product accents:** OK inside a product’s own UI/theme only if system chrome and the lockup stay on the palettes above.

---

## 4. Type

| Use | Face |
|---|---|
| Numbers, headings | Space Grotesk |
| Labels, body | Inter |
| Lockup line (“brought to you by”) | Inter, medium or regular — not Space Grotesk, not all-caps shouting |

Tracking for small labels: ~0.15 em uppercase for chip labels; lockup line uses normal sentence tracking.

---

## 5. The hero lockup — “brought to you by Control Freak”

### Construction (preferred)

Vertical stack, left-aligned or centered as a unit:

1. **Product mark** (or product wordmark) — largest element in the lockup unit  
2. Thin horizontal rule **or** 8–12 px gap (no rule on very small sizes)  
3. **Attribution line:** `brought to you by` in Inter, slate `#6F8BAB` on light / cream-tinted on dark, 40–50% of product-name type size  
4. **Parent:** line mark (`currentColor` / forest / cream) — preferred when space ≥ ~24 px tall for the mark; else the words `Control Freak`

Horizontal variant (footers, brochure strips):  
`[Product mark]  ·  brought to you by  [parent line mark or “Control Freak”]`  
Keep the attribution + parent as one inseparable group; do not put the product mark between “by” and the parent name.

### Required copy

- Exact phrase: **brought to you by Control Freak** (lowercase “brought to you by”; title-case or mark for Control Freak).  
- Acceptable short form in tight chrome only: **by Control Freak** (still with parent mark or wordmark).  
- Do **not** use: “powered by,” “a Control Freak company,” “from the makers of,” or competitor-style “Intel Inside” parodies.

### Clear space

- Around the **parent line mark:** clear space ≥ 1/8 of the mark’s width on all sides (measure from the rounded outer frame).  
- Around the **full lockup unit:** clear space ≥ height of the attribution line.  
- Do not place the lockup over busy photo detail; use a frosted/cream or forest panel if needed.

### Minimum sizes

| Context | Product mark | Parent line mark | Attribution type |
|---|---|---|---|
| Hero / brochure cover | ≥ 14% of page width (≥ 150 px on 1080 px; ≥ 112 px on Letter) | ≥ 28 px tall | ≥ 10 pt print / 12 px screen |
| App splash / about | Product leads | ≥ 24 px tall | ≥ 11 px |
| Favicon / tray | Product or parent alone — drop attribution | 16–32 px | omit line |

Never scale the parent mark smaller than 20 px tall when the attribution line is present.

### Contrast

- Light / cream surface → forest mark + slate attribution.  
- Forest / dark surface → cream (or gold, sparingly) mark + light attribution.  
- Do not put forest on forest, or cream on cream, without a contrasting plate.  
- Never place the metallic hero inside a product lockup.

---

## 6. Where the lockup must appear (Wave 1)

| Touchpoint | Rule |
|---|---|
| Product brochure (cover + back) | Lockup on cover (secondary to product mark) and on back with controlfreakpool.com |
| Hero / infographic / floating pages | Add lockup next to product mark on cover/hero; keep controlfreakpool.com in the footer |
| App (About, splash, settings footer) | Lockup or short form “by Control Freak” + link to controlfreakpool.com |
| Enclosure / faceplate | Product identity may lead; if any parent branding is printed, use the line mark or lockup — not the metallic hero |
| Ads / social for a product | Lockup required once per creative (usually end frame or corner) |
| OEM / private-label builder skins | Builder brand may lead; still include “brought to you by Control Freak” unless a written channel agreement says otherwise |
| controlfreakpool.com | Line mark in chrome/nav/footer; metallic hero only on high-impact parent heroes |

---

## 7. Co-brand don’ts

1. **Don’t fight the pool brand.** Product themes may swap illustration and accent *inside the app*, but parent mark colors and lockup stay on the mark + soft-UI palettes above.  
2. **Don’t invent a second company logo** that competes with Control Freak. Product marks mirror the PCB frame (see `PRODUCT_MARKS.md`) — same weight, vias, rounded outline — not competing badges.  
3. **Don’t recolor, stretch, rotate, add drop shadows, or put effects on** the metallic hero or line masters (except `currentColor` / published forest/cream/gold flats).  
4. **Don’t crop** the ladder, wave, or via pads off the parent mark.  
5. **Don’t put the metallic hero treatment on product marks** (line art only).  
6. **Don’t place competitor marks** next to the lockup.  
7. **Don’t put prices, fake certifications, or UL marks** into lockup artwork.  
8. **Don’t use coral** as a brand/decorative color next to the parent mark.  
9. **Don’t replace the lockup with only the URL** on primary brand surfaces; URL alone is fine in small footnotes *in addition to* the lockup.  
10. **Don’t claim water chemistry / balancing or off-LAN remote access** in parent or product marketing unless the manual supports it.  
11. **Don’t publish third-party soft-UI reference photos** (STYLE.md references are direction only).

---

## 8. Relationship to Platform files

- Masters + grammar: [`brand/masters/README.md`](masters/README.md), [`brand/PRODUCT_MARKS.md`](PRODUCT_MARKS.md)  
- Product soft-UI + floating cards: `design/STYLE.md`  
- Imagery prompts: `design/CHATGPT_HANDOFF.md`  
- This document is the **parent lockup / co-brand source of truth** for controlfreakpool.com and Wave 1 nesting.

---

## 9. Still open (parent bot)

- Official composed lockup packs (stacked + horizontal SVG/PNG, light + dark).  
- Favicon / app-icon set derived from the currentColor master.  
- controlfreakpool.com build using line masters in chrome and metallic hero only on the parent hero.

Until composed lockups ship, compose from `control-freak-mark-*.svg` / PNG + Inter type per §5.

---

## 10. Change control

Parent lockup wording, parent mark files, and §§5–7 don’ts change only via the Control Freak Pool bot / James. Product marks and in-app accents stay with Platform within these rules until James locks product marks.
