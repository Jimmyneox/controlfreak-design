# C03 Basement Guard Pro — Concept A "Living Demo Theater" (first draft)
Built Oct 25 2026 ~11:30 PM ET. **Local only; nothing committed or pushed.**

## Provenance
- Copy: `/workspace/controlfreak-design-work/briefs/C03-basement-guard-PUBLIC_BRIEF.md` (authoritative). H1/sub verbatim; *Control Freak* italic like O04.
- Craft reference: `brochures/O04-reef/c-v8-gemini-words/` (real-scale 393×852 phones, Power Hub lit tiles, opaque callouts, foldable duo, HA page, per-page PNG + review PDF). Structure re-written fresh. Nothing reef-specific reused (no reef palette, photos or marks).
- Palette: concrete greys/slate (#11171d → #22303c), safety-blue accent #3d8bff / #1f6fd1, amber #ffb340 for "keep an eye on", red only for the tapped "what if" alert card on the back page.
- Stage photo: `assets/basement-stage-concept.jpg`, an AI-generated **Concept photo** of a dry utility corner (sump lid, two discharge pipes, water heater, ceiling pipes, crawlspace opening). Labelled Concept photo on the art. No flooding.
- Product mark (**Concept**): `assets/bgp-mark-{white,slate}.svg`. Shield outline with a sump-pit cross-section inside it, a safety-blue water line and two pump blocks with discharge risers (lead solid, standby faded). Labelled "CONCEPT MARK" in the lockup.
- Parent: *brought to you by Control Freak* uses the PCB corporate **wordmark** (`brand/corporate/control-freak-corporate-wordmark-{white,navy}.svg`, copied to assets). We used the wordmark and not the full lockup because the lockup's tagline reads "POOL AUTOMATION". No teardrop anywhere.

## Pages
1 front.png (dark phone + 6 callouts) · 2 light-mode.png (light + dark phones) · 3 duo.png (foldable: pit/pumps | Power Hub, sensors, alerts) · 4 ha-home.png (HA dashboard + "When you're away and the forecast turns…" story, Alexa "how's the sump?") · 5 back.png (buyer open, kit list, storm / stagger-weekly test / cold-snap demo tiles, differentiators, what-if alarm, Join the beta CTA). spread.png = all 5.

## Rebuild
`python3 build.py`: writes brochure.html, prints each page with headless Chrome, joins them with pdfunite into brochure.pdf, writes the PNGs at 110 dpi, then spread.png and brochure-review.pdf. Pages are printed one at a time because Chrome shrank the combined document to about 86%.

## Checks
°F only; no prices; no competitor names; no pool/reef/resort wording; no cloud HA (says "never cloud HA"); floats never removed (fail-safe caption says pumps run on their own floats); pumps not included; inverter = one you already own; all art labelled Concept.

## Polish pass 1 (Oct 25 2026, ~11:20 PM ET, local only)
- Front: phone 6.55 → 7.45 in tall (393×852 aspect kept), lifted to 1.9 in; more of the app shows (Alerts + Sensors).
- Duo: foldable is a fixed 6.35 in tall. Left side gets a "Pit level · last 24 h" chart (amber high-water guide) and a Backup card (inverter ready, siren armed, internet not needed for pump rules). Right side gets a Sensors grid (8 online, live dots) and a "Coming up" card (weekly test, lead swap, heat tape) above the HA chip. Both columns now fill to the bottom.
- Back: the weekly-test tile is now a two-lane timeline. A lane = safety-blue glowing pill, B lane = slate pill offset after a wait, ✓ run times, 0 s · wait · 90 s axis. Replaces the old overlaid bars.
- Rebuilt every page PNG, spread.png, brochure.pdf, brochure-review.pdf. Copy, palette, marks and wordmark are unchanged.

## Remaining
- None known. Waiting for James to lock before any push.
