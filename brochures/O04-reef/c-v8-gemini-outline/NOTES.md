# STATUS: LOCKED — James (via Chief), Oct 25, 2026 ~11:08 PM ET

**Locked Reef literature** for O04 Reef Control Pro.
- Craft: Living Demo Theater c-v8
- Voice: Gemini features/benefits outline (`../gemini-features-benefits-2026-10-25/outline.html`)
- HA bottom: driveway arrival story (not bedtime)
- **Local only until James asks to push** — do not publish to origin without his OK.

---

# O04 Reef — C v8 + Gemini OUTLINE voice (text-only)
Built Oct 25 2026 ~11:10 PM ET. Local only; nothing pushed. Sibling of ../c-v8-gemini-words (untouched).
**Craft = c-v8 (via c-v8-gemini-words). Voice = ../gemini-features-benefits-2026-10-25/outline.html** (base features+benefits voice for Reef literature).

## Changes vs c-v8-gemini-words
- Front badges line: LOCAL CONTROL → VOICE & TAP CONTROL · AWAY ALERTS · NO SUBSCRIPTION.
- H1/sub/status/cards 01–06 already matched outline exactly; verified, unchanged.
- Phone chrome (all phones): "Dosing 3-head · daily" → "Continuous Dosing · Ca · Alk · Mg"; top-off "Level OK" → "Water Level Optimal" + low-reservoir alerts via push, Alexa & Google; pH subline → "pH Optimal". °F only.
- Light-mode page → outline deep dive 1: eyebrow "Continuous Biological Stability", H1 "In Perfect Balance", outline body verbatim; legend = Continuous Dosing / pH Optimal / Light or Dark.
- Duo page → outline deep dive 2: eyebrow "Proactive Reservoir Monitoring", H1 "Auto Water Leveling That Talks to You", outline body verbatim; feature cards = Water Level Optimal / Voice Alerts Armed / 8 Smart Outlets Active.
- CSS: appended size overrides for duo/light headers so the longer copy fits (no visual redesign).
- HA page unchanged: outline eyebrow/H1 already present; bottom story stays ARRIVAL (driveway, 1 arrival → 4 home automations, Garage / heated floor / shower / entry lights). Outline bedtime story (EV/TV/pool lights/security) NOT used.
- Brand: coral-teardrop product mark unchanged; PCB corporate not touched.

---
Prior notes (c-v8-gemini-words) follow.

# O04 Reef — C v8 + Gemini words (text-only)
Built Oct 25 2026 ~5:40 PM ET. Local only; nothing pushed or published.

## Provenance
- Base = concepts/C-living-demo-theater v8 (build_c5.py, ha_page.py, style.css, ha.css, assets, refs, brochure.v2.html) copied forward. v8 folder untouched.
- Visual craft unchanged: real-scale phones, Power Hub teal/coral/muted tiles, opaque v8 callouts, sapphire/cyan glow, C reef stage photo (../concepts/img/wide.jpg), airy HA glass dashboard, coral-teardrop mark (../approved-mark/ SVGs).
- Path fixes only: mark path ../../approved-mark → ../approved-mark; CSS image url ../img → ../concepts/img.
- Rebuild: `python3 build_c5.py` (Chrome headless → brochure.pdf → 5 PNGs + spread.png). brochure-review.pdf = 5 PNGs combined (110 dpi).

## Gemini wording applied (text only, from gemini-v2 as identified in merge-gemini-c)
- Front H1 "Put the <em>Control Freak</em> on it." / sub "Sit back and enjoy the reef—the system handles the rest." (no spaces around the dash)
- Status "All Calm in the Reef": phone, foldable, folded mini.
- Six callouts: 8 Smart Outlets / Smart Flow Control / In Perfect Balance / Auto Water Leveling / Heater Fail-Safe (82°F) / Automate Your Tank & Life. Titles and bodies from Gemini; C positions and panels kept.
- HA: eyebrow "Pre-configured Home Assistant hub built in"; H1 "Automate more than just your tank. / Automate the rest of your life."; Gemini app-fatigue paragraph. Small CSS tweak: H1 30px so it fits above the device.
- HA bottom: the C v8 three-tile row is replaced with the arrival story in the same glass tiles (4 columns): "When you pull into the driveway on the way home from work…" · chip "1 arrival → 4 home automations" · Garage opens / Heated bathroom floor on / Shower water warming / Entry lights if dark. No bedroom/EV/TV/backyard/security story.

## Arrival story sources (not on the art)
- Garage on arrival using proximity + vehicle/car Bluetooth: community.home-assistant.io garage-door-on-arrival threads (Proximity integration + companion-app Bluetooth connection sensor patterns).
- Bathroom preheat on presence/zone (approaching home): community.home-assistant.io presence-based / zone-enter heating automations.
- Hot-water recirculation on arrival / on demand, stopped by return-line temperature: community.home-assistant.io recirculation-pump threads.

## NOT taken from merge-gemini-c
- No Gemini section PNGs, no hero crops (gemini-reef-hero.jpg), no merge CSS blocks/backgrounds, no front header badge pills, and no bedtime story. Only the strings were reused, as text.

## Checks
0 °C; no pool/resort; mark SVGs resolve; front H1/sub/status exact.

## Corporate attribution audit — PARENT_BRAND v1.4 (2026-10-25)
- Product mark: coral-teardrop (`../approved-mark/reef-mark-*`), unchanged and stays the Reef Control Pro identity.
- No navy parent teardrop appears anywhere in this candidate (img srcs = reef-mark-drop-white, reef-mark-lockup(-white) only).
- Attribution is text-only: "REEF CONTROL PRO · BROUGHT TO YOU BY CONTROL FREAK" (page-1 footer bar). Nothing to swap; no rebuild done.
- Optional on the next rebuild: add `lockups/product/brought-to-you-by-control-freak-horizontal-dark.svg` (corporate PCB wordmark) to the back-page footer. Never use the PCB mark as the reef logo.

## Pages 5–6 · Why Home Assistant + How it all connects (2026-10-26)
Owner request: "Create an infographic page for every product brochure and webpage". The brochure is now seven pages: front, light-mode, duo, ha-home, **why-ha**, **infographic**, back. `infographic.html` → `infographic.pdf`/`infographic.png` comes from `brochures/_infographic/build_infographic.py`, which also splices it into `brochure.pdf` and rebuilds `spread.png` and `brochure-review.pdf`; this folder's build calls it at the end. Words come from the product's PUBLIC_BRIEF (no new claims); the diagram is labelled **Concept illustration · not to scale**, and the buyer's own equipment is drawn dashed and labelled "Your …".

**Why Home Assistant (page 5).** Owner: "Research home assistant benefits and expand the information about it to sell its benefits from multiple angles." `why-ha.html` → `why-ha.pdf`/`why-ha.png`, same builder, same product style. Six angles, worded in the buyer language users actually use about HA (owner: "use social media and forums… value added statements"; research with links in the private repo, `design/research/HA_VOICE_OF_CUSTOMER.md`): One app. No more app juggling; Your brands finally work together; Works when the internet doesn't (home network only, never cloud HA); Ask, don't open (the three owner voice examples, Siri via HomeKit); Peace of mind, all over the house; Nobody can switch it off. The intro answers the top objection users raise (setup is daunting): "everything people love about it, without the setup. Just plug it in." No forum quotes are published. Figures (2.7M+ households, 1,500+ integrations, 1,000+ brands) are cited on the page to home-assistant.io, October 2026; "0 subscriptions with Control Freak" is ours, and is not placed next to the Alexa/Google line. The three idea cards are labelled **Idea · Example** and use the buyer's own devices ("Your lights, speakers and thermostat aren't in the box"). **For Eng/Writer to OK:** the idea-card wording, "without the setup. Just plug it in." and "answers right away".
