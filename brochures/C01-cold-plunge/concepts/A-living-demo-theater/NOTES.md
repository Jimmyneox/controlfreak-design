# C01 Cold Plunge Control Pro: Concept A "Living Demo Theater" (first draft)
Built Oct 26 2026 ~12:30 AM ET. **This is local only. Nothing has been committed or pushed.** Rebuild with `python3 build.py` (needs google-chrome, poppler-utils and Pillow).

## Provenance
- Copy comes from `briefs/C01-cold-plunge-PUBLIC_BRIEF.md` (platform tip 61ff993). It also folds in **Writer tip d0921fb**: the restored demo chip **"Ask Alexa if the plunge is ready"**. The H1, sub, callouts (diffs §4), kit (§5), problem (§3), demo tiles and interactions (§6), CTA (§8), and the HA buyer-open with the multi-platform STYLE line (§1) are all taken from the brief.
- Structure and build come from O15 `A-living-demo-theater`: 393×852 phones, callouts, foldable duo, HA tablet page, per-page Chrome PDF → pdfunite → pdftoppm.
- There is **no stage photo**. The dawn sky and water come from CSS gradients only, so there is no tub, chiller or person imagery anywhere.
- **No product mark.** No C01 mark exists yet. The coral-teardrop belongs to O04 and is NOT used here. The product name is set in type ("Cold Plunge Control Pro", tagged WORKING NAME · CONCEPT).
- Parent attribution uses only the PCB corporate **wordmark**: `assets/control-freak-corporate-wordmark-{white,navy}.svg`, copied from `brand/corporate/` (v1.4). There is no POOL AUTOMATION lockup.

## Palette / type
- Ice white #f4f7fa, slate #1e2b38 / #1b2a3c, and deep cool blue #1f5f9e / #5fb4ff, with a dawn gradient.
- Amber #ffb340 marks "keep an eye on" (filter tile, filter scene).
- Red appears only on the tapped "what if" example alert.
- Type: Fraunces for headlines, Inter for UI, IBM Plex Mono for eyebrows.

## Pages
- **front:** H1/sub, dark demo phone and 6 callouts.
- **light-mode:** light and dark phones.
- **duo:** foldable mock with the ready-by timeline.
- **ha-home:** "How many apps…", HA dashboard and "A cold night, handled".
- **back:** problem, Pro kit (Starter coming later), 4 demo scenes, an example alert and Join the beta.
- Also built: spread.png, brochure.pdf and brochure-review.pdf.

## Concept labels
- The demo UI is labelled "Concept · demo UI · example readings" on every page, and the phone header says "demo · Example readings".
- The foldable is labelled "device mock, not a shipping product".
- The HA dashboard is labelled "example". Owner devices (deck lights, thermostat) are marked "Owner device · example" under "Your home · via Home Assistant". They are not kit contents.
- The kit card is tagged CONCEPT.

## Eng hard-false watchouts (please skim)
1. Chiller: the page only says "switches your chiller's power" and "Power switched by the Power Hub". It never says "sets chiller temperature" or "works with every chiller". Callout 03 quotes §4 verbatim ("Runs a 120 V plug-in chiller from the Power Hub…").
2. "Chiller only runs while flow is OK" and "No flow → chiller stops, alert" match flow-switch interlock §4/§6.
3. Ozone/UV: "only while water is moving" (§6).
4. Ready-by example: starts cooling at 4:50, ready at 6:30, 39 °F. These are example readings.
5. Pro-only items are tagged Pro: filter reminder, chiller health, and heater outlet / hot-cold.
6. Winter mode: example air at 30 °F with the pump on.
7. Voice: the chip says "Ask Alexa if the plunge is ready" (d0921fb). The HA tile has the example voice reply "via Home Assistant" with the quoted line "Alexa, is the plunge ready?". The STYLE line is taken verbatim on the HA page. "Standard bridges" does not appear.
8. "Keeps working when the internet doesn't · Ethernet, Wi-Fi, and its own Wi-Fi network" is taken from §4.
9. Alerts go by push, text, email and alarm, including away from home. The Tailscale detail is omitted.
10. Kit list is exactly §5 Starter + Pro. Tub, chiller, pump, ozone and UV are listed as not in the box. There are no prices ("Price to be announced"). Starter is shown as "coming later".
11. There are no health/recovery claims, competitors, testimonials or retired names.
12. **Design paraphrases for Eng/Writer to OK:**
    - light-page H1 "Sit back — the plunge is ready when you are." (from the §7 voice line)
    - back diff "Switches your chiller's power from the Power Hub — keep your chiller."
    - HA story heading "A cold night, handled."
    - phone "Coming up" row "Filtration cycle · scheduled"
    - mode segment "Plunge / Warm soak · Pro / Winter"

## Page 5 · How it all connects (2026-10-26)
Owner request: "Create an infographic page for every product brochure and webpage". The brochure is now six pages: front, light-mode, duo, ha-home, **infographic**, back. `infographic.html` → `infographic.pdf`/`infographic.png` comes from `brochures/_infographic/build_infographic.py`, which also splices it into `brochure.pdf` and rebuilds `spread.png` and `brochure-review.pdf`; this folder's build calls it at the end. Words come from the product's PUBLIC_BRIEF (no new claims); the diagram is labelled **Concept illustration · not to scale**, and the buyer's own equipment is drawn dashed and labelled "Your …".
