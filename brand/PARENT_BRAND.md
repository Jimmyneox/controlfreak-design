# Control Freak — brand architecture & lockup rules

**Owner (change control):** Control Freak Pool bot  
**Production:** Control Freak Design (`Jimmyneox/controlfreak-design`)  
**Audience:** Design, Platform, and anyone shipping company / pool / product surfaces  
**Status:** **v1.4 — 2026-10-25** (corporate logo = PCB circuit wordmark lockup **everywhere**; navy teardrop **retired**)  
**Supersedes:** v1.3 (parent = navy teardrop; pool = ladder/wave PCB line mark)

**James brand lock (via Chief, 2026-10-25 ~10:40 PM ET):** The PCB circuit **CONTROL FREAK** wordmark from James's new JPG (`brand/corporate-logo-2026-10-25/james-new-corporate-logo.jpg`) is the **corporate logo everywhere**, and **controlfreakpool.com uses it as the site corporate mark**. The navy teardrop is replaced.

### What changed in v1.4
- **Corporate / parent logo everywhere** = PCB circuit wordmark lockup (`brand/corporate/`).
- **Navy teardrop = RETIRED** as parent/corporate. Do not use for corporate, press, or "brought to you by". Archived at `brand/_superseded/parent-teardrop-2026-10/`.
- **"Brought to you by Control Freak"** lockups now use the corporate PCB wordmark (`lockups/product/`, rebuilt 2026-10-25).
- **controlfreakpool.com** site chrome (nav/footer/favicon source) = corporate PCB mark.
- Forest/cream/gold **ladder + wave** line marks are **superseded** for site chrome and company use → legacy/archive only (§3).
- **Reef coral-in-teardrop stays the Reef Control Pro product mark** — unchanged. The PCB corporate mark is never the reef product logo.

---

## 1. Brand architecture

| Layer | What it is | Marks | Who owns production |
|---|---|---|---|
| **Corporate (parent)** | Control Freak the company, across all divisions and on controlfreakpool.com | **PCB circuit CONTROL FREAK wordmark** — full lockup with **POOL AUTOMATION** tagline, or wordmark-only (`brand/corporate/`) | Design produces; Pool owns rules |
| **Pool division** | Pool automation line + **controlfreakpool.com** (Resort: ivory / lagoon / brass) | Same corporate PCB mark (full lockup with POOL AUTOMATION is the natural pool-site lockup). Metallic hero badge: see §3 | Design; Pool launch/ops |
| **Product lines** | Reef, Basement, Reptile, Plunge, … — own app, site, colors, industry look | **Product mark leads** (e.g. Reef coral-teardrop) + **"brought to you by Control Freak"** with corporate PCB wordmark | Platform (UX/content) + Design |

**Do not conflate:** the corporate PCB mark is the company attribution, never a product's identity. Product marks are never the company logo.

---

## 2. Corporate mark (PCB circuit wordmark)

Source: James's JPG (white logo on navy pool photo). Digitized as clean vectors — no photo/raster embedded.

| Asset | Path | Use |
|---|---|---|
| Full lockup, white | `brand/corporate/control-freak-corporate-lockup-white.svg` | Light-on-dark: site hero/nav on dark, press, decks |
| Full lockup, navy `#0b1f3a` | `brand/corporate/control-freak-corporate-lockup-navy.svg` | Dark-on-light |
| Full lockup, currentColor | `brand/corporate/control-freak-corporate-lockup-currentColor.svg` | UI / CSS-colored |
| Wordmark only (no tagline) — white / navy / currentColor | `brand/corporate/control-freak-corporate-wordmark-{white,navy,currentColor}.svg` | Non-pool corporate contexts, product attribution, tight chrome |
| PNGs + preview sheets | `brand/corporate/png/` | Review / quick use |
| Source JPG (provenance) | `brand/corporate-logo-2026-10-25/james-new-corporate-logo.jpg` (copy in `brand/corporate/`) | Reference only |

**Which lockup:** use the **full lockup (POOL AUTOMATION)** on controlfreakpool.com and pool materials. Use the **wordmark-only** version for multi-division corporate use and all product "brought to you by" lockups (a reef/reptile product shouldn't say "pool automation").

**Color (flexible, James 2026-10-25):** ink flows with the site theme. Published flats: **white**, **navy `#0b1f3a`**, **forest `#0f2e2c`**, **cream `#efe9df`**, **gold `#a8834f`**, plus **`currentColor`**. Themes may recolor with currentColor or use these flats (`control-freak-corporate-{lockup,wordmark}-{white,navy,forest,cream,gold,currentColor}.svg`). Geometry is locked; only the ink changes. Use one ink per lockup (don't tint traces/nodes separately), and keep contrast readable (e.g. gold on forest, cream on navy, forest on cream).

**Construction notes:** horizontal bold-sans wordmark with stencil slots (top of first O, bottom of second O); bus traces above/below; left radiating burst ending in solid nodes; right traces with 45° bends ending in nodes. Don't redraw, rearrange nodes, stretch, or drop traces.

**Min size:** full lockup ≥ 120 px wide (tagline legibility); wordmark-only ≥ 72 px wide; below that use text "Control Freak". Clear space ≥ height of the letter C on all sides.

---

## 3. Legacy / superseded marks

| Mark | Status | Path |
|---|---|---|
| **Navy teardrop + horizontal wordmark** (former parent, v1.1–v1.3) | **RETIRED 2026-10-25.** Not for corporate, press, attribution, or favicons. | `brand/_superseded/parent-teardrop-2026-10/` |
| Teardrop "brought to you by" packs | **RETIRED** | `lockups/product/_superseded-teardrop-2026-10/` |
| Forest/cream/gold **PCB frame + ladder + wave** line marks (`brand/masters/control-freak-mark-*.svg`) + `lockups/pool/` | **Superseded for site chrome and company use** by the corporate PCB mark. Legacy/archive only; don't use in new work unless James re-assigns them. | Left in place (not moved) so old references don't break |
| Metallic hero badge (`brand/hero/…`) | Ladder/wave family — legacy. Don't use as the site corporate mark; any hero use needs a James OK. | — |
| Legacy Platform PNGs `mark-core-navy.png` / `mark-core-white.png` | Don't use | — |

Product PCB-family drafts (`PRODUCT_MARKS.md`, `masters/{reef,basement,reptile,plunge}-mark-*.svg`) stay Platform drafts until James locks them; they aren't the corporate mark.

---

## 4. Color summary

| Role | Hex |
|---|---|
| Corporate navy (mark on light) | `#0b1f3a` |
| Corporate white (mark on dark) | `#ffffff` |
| Forest | `#0f2e2c` |
| Cream | `#efe9df` |
| Gold | `#a8834f` |
| Any theme ink | `currentColor` variants |
| Attribution text on light / dark | slate `#5b6670` / mist `#c3cddb` |

**Pool site (Resort)** — ivory / lagoon / brass stays the controlfreakpool.com palette. The corporate mark sits on it in navy or white.  
**Product visual systems:** full freedom for industry palettes. The required shared element is the attribution lockup (§5).

---

## 5. "Brought to you by Control Freak" lockup

### Construction
1. Product mark (largest; e.g. Reef coral-teardrop)  
2. Gap or thin rule  
3. `brought to you by` (Inter Medium; slate on light, mist on dark)  
4. **Corporate PCB wordmark** (wordmark-only, no tagline)

Packs: `lockups/product/brought-to-you-by-control-freak-{stacked,horizontal}-{light,dark}[-on-plate].svg` + `-currentColor`, PNGs in `lockups/product/png/`. Rebuild with `python3 lockups/product/build_product_lockups.py`.

### Copy
- Exact: **brought to you by Control Freak**  
- Tight chrome: **by Control Freak** (text-only when the mark would be < 72 px wide)  
- Don't use "powered by" or "a Control Freak company" unless James adds them.

### Clear space & mins
- Clear space around company mark ≥ 1/8 mark width  
- Corporate wordmark ≥ 72 px wide with the attribution line; otherwise text-only

---

## 6. Where marks appear

| Surface | Mark |
|---|---|
| Corporate / multi-division / press / decks | Corporate PCB lockup (wordmark-only, or full lockup for pool topics) |
| **controlfreakpool.com** nav, footer, favicon source | **Corporate PCB mark** (full lockup with POOL AUTOMATION; wordmark-only in tight nav) |
| Pool marketing / print | Corporate PCB full lockup |
| Product apps, sites, brochures (e.g. O04 Reef) | **Product mark leads** + "brought to you by Control Freak" with corporate PCB wordmark |
| OEM / private-label | Builder may lead; still include "brought to you by Control Freak" unless a written deal says otherwise |

---

## 7. Don'ts

1. Don't use the navy teardrop as the company/parent/attribution mark (retired).  
2. Don't use the PCB corporate mark as a product logo (e.g. as the reef mark), and don't swap a product mark for it.  
3. Don't use the ladder/wave line marks for site chrome or company use in new work.  
4. Don't clone controlfreakpool.com's Resort look onto other industry sites.  
5. Don't put App Store–only internals in the public `controlfreak-design` repo (`PUBLIC.md`).  
6. Don't recolor, stretch, crop, or re-arrange the corporate mark outside the published flats.  
7. Don't claim water chemistry/balancing or general off-LAN remote control unless the manual supports it. Away-from-home **alerts** (push/text/email/alarm) are allowed per James Oct 25; HA integration stays local-only.  
8. Don't publish unfinished product marks until James locks them.

---

## 8. Open work

| Item | Owner |
|---|---|
| Corporate PCB SVG masters | **Locked by James 2026-10-25** ("They look great"); colorways white/navy/forest/cream/gold/currentColor |
| Product attribution packs → corporate PCB | **Done 2026-10-25** (`lockups/product/`) |
| controlfreakpool.com chrome → corporate PCB mark | Design — site source not in this local work tree; swap nav/footer/favicon when the site build is touched (no deploy without OK) |
| Favicon / small-size mark | **Done 2026-10-26.** Parent favicons = **PCB simplified icon** (corporate C + bus bars + nodes; `brand/app-icons/_masters/control-freak-pcb-icon-*.svg`), navy on white. **Teardrop favicon retired.** Sets in `brand/app-icons/` (see README) |
| O04 brochure attribution | Text-only "BROUGHT TO YOU BY CONTROL FREAK" in c-v8; no teardrop present. Optional: add corporate wordmark to the back-page footer on the next rebuild |

---

## 9. Change control

Corporate / pool / product mark rules and this file change only via Control Freak Pool / James. **Pool owns the rules; Design produces assets;** Platform owns product marks until James locks them. v1.4 was locked by James via Chief on 2026-10-25.

## Favicon exception — favicons = drops (2026-10-26)
Browser/app icons (favicon.svg/.ico/16/32/48, apple-touch, PWA) use the **teardrop/drop silhouette**: hub = navy parent drop; C03 = white drop, O15 = forest drop, C01 = cool-blue (#2f6f9f) drop (same parent geometry, recolored); O04 = coral-teardrop drop (solid silhouette at 16/32). Flat, transparent, no plates. The corporate **attribution wordmark stays PCB**. Favicon ≠ marketing lockup. Built by `brand/app-icons/build_icons.py`; PCB icon masters moved to `brand/app-icons/_unused/`.
