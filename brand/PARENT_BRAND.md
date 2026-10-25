# Control Freak — brand architecture & lockup rules

**Owner (change control):** Control Freak Pool bot  
**Production:** Control Freak Design (`Jimmyneox/controlfreak-design`)  
**Audience:** Design, Platform, and anyone shipping company / pool / product surfaces  
**Status:** v1.3 — 2026-10-25 (**parent company ≠ pool division**; product lockups = parent teardrop, confirmed)**  

**James (2026-10-25):** The navy **teardrop + horizontal CONTROL FREAK wordmark** is the **parent company** logo. The forest/cream/gold **PCB + ladder + wave** line mark (and metallic hero badge) is the **pool division** mark — not the parent company mark. Product apps/sites stay industry-specific and are not reskins of controlfreakpool.com.

---

## 1. Brand architecture (three layers)

| Layer | What it is | Marks | Who owns production |
|---|---|---|---|
| **Parent company** | Control Freak (the company) across all divisions | Navy teardrop + horizontal **CONTROL FREAK** wordmark (`brand/parent-company/`) | Design digitizes; Pool owns rules |
| **Pool division** | Pool automation product line + **controlfreakpool.com** (Resort: ivory / lagoon / brass) | PCB frame + ladder + wave line mark (forest/cream/gold) + metallic hero for high-impact pool marketing | Design on `controlfreak-design`; Pool launch/ops |
| **Product lines** | Reef, Basement, Reptile, Plunge, … — each with its **own** app, **website**, colors, look & feel for that industry | Product mark (Platform until James locks) + **“brought to you by Control Freak”** lockup | Platform (UX/content) + Design (public design as assigned) |

**Do not conflate:** pool line marks are not the company logo. Company logo is not the pool site badge.

Buyers should feel “a Control Freak company product for [hobby],” not “the pool website with a different logo,” and not “an unrelated brand.”

---

## 2. Parent company mark

| Asset | Path | Use |
|---|---|---|
| **Parent lockup (source JPG)** | `brand/parent-company/control-freak-parent-lockup-navy.jpg` | Owner-supplied: navy teardrop (drop + S-curve ending in a node) + horizontal CONTROL FREAK wordmark on white |
| **SVG / reverse masters** | *Design to digitize into* `brand/parent-company/` (navy, reverse/cream, currentColor) | UI, print, corporate lockups, product “brought to you by” **if James confirms** |

**Wordmark:** horizontal **CONTROL FREAK** (single line), all caps, as in the parent JPG — not the stacked pool-division wordmark.

**Color (parent company):** navy ink matching the supplied art (approx. deep navy on white; exact hex from digitization). Do not recolor the teardrop to forest/gold/aqua/product accents.

---

## 3. Pool division marks

Motif: rounded PCB frame + vias, pool ladder into capsule, wave, stacked CONTROL / FREAK wordmark.

| Asset | Path | When to use |
|---|---|---|
| **Line master** | `brand/masters/control-freak-mark-currentColor.svg` (also `mark-core.svg`) | Pool site chrome, pool print, pool favicons |
| **Forest / cream / gold flats** | `brand/masters/control-freak-mark-{forest,cream,gold}.svg` + PNG pairs | Pool division ink: forest `#0f2e2c`, cream `#efe9df`, gold `#a8834f` |
| **Metallic hero** | `brand/hero/control-freak-hero-metallic.png` | **Pool** high-impact only: controlfreakpool.com heroes, pool press, pool trade-show — never on product co-brand lockups as the “company” mark |

**controlfreakpool.com** uses pool-division line marks in nav/footer; metallic hero only on high-impact pool heroes. That remains correct under this split.

Legacy Platform PNGs `mark-core-navy.png` / `mark-core-white.png`: do not use for new work.

Product PCB-family drafts (Platform until James locks): `PRODUCT_MARKS.md` and `masters/{reef,basement,reptile,plunge}-mark-*.svg` — these mirror **pool-division** grammar for product lines, not the parent teardrop.

---

## 4. Color summary

### Parent company
| Role | Notes |
|---|---|
| Navy | As in parent JPG / digitized SVG |

### Pool division mark ink
| Role | Hex |
|---|---|
| Forest | `#0f2e2c` |
| Cream | `#efe9df` |
| Gold | `#a8834f` (accent only) |

### Pool site (Resort) — controlfreakpool.com only
Ivory / lagoon / brass as on the live site. Do **not** default non-pool product sites to Resort.

### Soft-UI (optional product kit)
Navy `#12355B`, aqua `#19B3C9`, grey `#E9EEF4`, slate `#6F8BAB`, coral `#FF6B4A` warnings only — only where a product still uses that Platform kit. Not required for new industry sites.

**Product visual systems:** full freedom for industry palettes. Mandatory shared element is the company attribution lockup (§5), not pool colors.

---

## 5. “Brought to you by Control Freak” lockup

### Construction
1. Product mark (largest)  
2. Gap or thin rule  
3. `brought to you by` (Inter; slate on light)  
4. **Control Freak company identifier** — mark preferred when ≥ ~24 px tall  

Horizontal footer variant allowed; keep attribution + company mark as one group.

### Which mark? (**confirmed James 2026-10-25 — A**)

Product “brought to you by Control Freak” lockups use the **parent company teardrop + horizontal wordmark** — not the pool-division PCB line mark.

Pool line marks stay on **controlfreakpool.com** chrome and pool-only materials. Do not ship the forest/cream/gold PCB lockup pack as the company / product attribution lockup.

Design digitizes the parent JPG → SVG under `brand/parent-company/` and rebuilds product lockup packs from those masters.

### Copy
- Exact: **brought to you by Control Freak**  
- Tight chrome: **by Control Freak**  
- Don’t use: “powered by,” “a Control Freak company” as a substitute slogan unless James adds it  

### Clear space & mins
- Clear space around company mark ≥ 1/8 mark width  
- Lockup unit clear space ≥ attribution line height  
- Parent/company mark ≥ 28 px on heroes, ≥ 24 px in app, never < 20 px with the line present  

---

## 6. Where marks appear

| Surface | Mark |
|---|---|
| Corporate / multi-division / press about the company | Parent teardrop lockup |
| controlfreakpool.com chrome & pool marketing | Pool line mark; metallic hero on pool heroes only |
| Product apps, product websites, product brochures | Product identity + “brought to you by Control Freak” + **company mark per James A/B** |
| OEM / private-label | Builder may lead; still include “brought to you by Control Freak” unless a written deal says otherwise |

---

## 7. Don’ts

1. Don’t call the PCB+ladder mark the parent company logo.  
2. Don’t call the teardrop the pool badge or put it in place of the pool metallic hero on pool heroes without a deliberate redesign.  
3. Don’t clone controlfreakpool.com’s Resort look onto other industry sites.  
4. Don’t put App Store–only internals in the public `controlfreak-design` repo (`PUBLIC.md`).  
5. Don’t recolor, stretch, or crop either official mark family outside published flats.  
6. Don’t claim water chemistry/balancing or general off-LAN remote control unless the manual supports it. Away-from-home **alerts** (push/text/email/alarm) are allowed per James Oct 25; HA integration stays local-only.  
7. Don’t publish unfinished product marks until James locks them.

---

## 8. Open work

| Item | Owner |
|---|---|
| Digitize parent JPG → SVG / reverse | Design (in progress) |
| Product lockups = parent teardrop (A) | **Confirmed** — Design rebuilding packs |
| Pool site rebuild from `site/_mirror/` + pool line marks in chrome | Design (local commit held for push OK) |
| Composed lockup packs (parent company for products; pool-only packs separate) | Design after parent SVG digitize |
| Favicons | Pool site → pool line mark; corporate / product attribution → parent teardrop once digitized |

---

## 9. Change control

Parent/company vs pool-division rules and this file change only via Control Freak Pool / James. Design produces assets; Platform owns product marks until James locks them.
