# O15 Terrarium Control Pro — Concept A "Living Demo Theater" (first draft)
Built Oct 25 2026 ~11:40 PM ET. **Local only; nothing committed or pushed.**

## Provenance
- Copy: `briefs/O15-terrarium-PUBLIC_BRIEF.md` (Eng-cleared e84b978). H1, sub, supporting line, buyer open, kit and CTA are word for word from the brief. The six callouts map to differentiators 1–6.
- Structure/craft: copied from C03 `A-living-demo-theater` (393×852 phones, opaque callouts, foldable duo, HA tablet page, per-page Chrome headless PDF → pdfunite → pdftoppm PNG). Art, palette, marks and copy are all new.
- Stage photo: `assets/terrarium-stage-concept.jpg`. It's AI-generated, labelled **Concept photo**, and shows three planted glass enclosures on a walnut wall shelf with a warm basking lamp. There are **no animals**.
- Product mark: `assets/tcp-mark-{white,slate}.svg` (**CONCEPT MARK**), a rounded enclosure frame with an aqua fern sprout and an amber basking lamp.
- Parent: PCB corporate **wordmark** `control-freak-corporate-wordmark-{white,navy}.svg`. It isn't the full lockup, so there's no POOL AUTOMATION tagline.

## Palette / type
Forest-ink dark (#0d1411 / #1d2b25), warm parchment light (#f6f3ec → #dcd6c6). Aqua #2fd3c4 / #109a8e = "on". Basking amber #ffb340 / #ffc27a = day / warmth / Concept tags. Coral #ff6b5e / #e8564a appears only on the example alert. Headlines use Fraunces (serif, italic *Control Freak*) and UI text uses Inter, so it doesn't read like C03 (Space Grotesk, safety-blue) or O04 reef.

## Pages
front (dark phone + 6 callouts + badges Voice & Tap · Away Alerts · No Subscription) · light-mode (light + dark phones) · duo (foldable: gradient strip + day/night curve | 8-outlet Hub, enclosures, alerts, probes) · ha-home ("How many apps…" + HA dashboard + "A weekend away from the shelf…" story) · back (kit, 3 demo scenes, differentiators, example alert, Join the beta). spread.png, brochure.pdf (5 pp), brochure-review.pdf.

## Eng constraints checklist
- [x] Humidity: Eng (James, 2026-10-25) allows an **HA-added** wireless humidity reading (owner Zigbee/Z-Wave/Wi-Fi/ESP32 sensor — HA adds many sensor types; writer brief tip 9a57423) shown "via Home Assistant". Shown once as a row under the phone Probes card: "Humidity 62% · via Home Assistant" + badge "HA-added · owner Zigbee · Z-Wave · Wi‑Fi · ESP32". Wave 1 CF kit still has **no humidity sensor** — not in Pro kit list, not on Power Hub. CF Modbus temp & humidity sensor stays "Later" on back page only.
- [x] Power Hub "8 outlets · on/off"; the kit says on/off; there's no dimming UI.
- [x] Dimming module only appears as "Concept accessory… the Power Hub and controller don't dim."
- [x] Door switch + reservoir float are tagged CONCEPT everywhere (chip, mode, alert, kit, scene).
- [x] Up to three enclosures (1–3); no rack/multi-controller.
- [x] Cutoff wording: "If a probe reads too hot, or is unplugged, its heat outlet turns off and you're told." No fire claims.
- [x] °F only; no prices ("Price to be announced"); no competitors; no species claims (profiles = editable starting points); "never cloud Home Assistant."
- [x] All art labelled Concept (photo, mark, demo UI, device mocks).

## Rebuild
`python3 build.py` (needs google-chrome, poppler-utils, Pillow).

## Eng constraint — probe count vs. enclosure readings (fact-skim fix, 2026-10-25)
- Kit ships **4 probes**: Hot / Cool / Basking / Enclosure 2.
- Enclosure 1 gradient uses 3 (Hot, Cool, Basking); Enclosure 2 uses the 4th.
- **Never show an Enclosure 3 °F reading** (or "all three at setpoint/on schedule") unless a 5th probe is in the story.
- Marketing "1–3 enclosures / up to three" kit copy stays: a third enclosure works with fewer probes per box or extra probes added later.
- Demo now: temps card "example readings · 2 of up to 3" (E1 92 °F, E2 88 °F); H2 "Two enclosures on schedule"; HA col shows "Shelf has room for a third · add a probe later" (no °F); story chip "2 enclosures → kept on schedule".
- Voice: "via Home Assistant" — no "Alexa and Google built in" claims.

## Pages 5–6 · Why Home Assistant + How it all connects (2026-10-26)
Owner request: "Create an infographic page for every product brochure and webpage". The brochure is now seven pages: front, light-mode, duo, ha-home, **why-ha**, **infographic**, back. `infographic.html` → `infographic.pdf`/`infographic.png` comes from `brochures/_infographic/build_infographic.py`, which also splices it into `brochure.pdf` and rebuilds `spread.png` and `brochure-review.pdf`; this folder's build calls it at the end. Words come from the product's PUBLIC_BRIEF (no new claims); the diagram is labelled **Concept illustration · not to scale**, and the buyer's own equipment is drawn dashed and labelled "Your …".

**Why Home Assistant (page 5).** Owner: "Research home assistant benefits and expand the information about it to sell its benefits from multiple angles." `why-ha.html` → `why-ha.pdf`/`why-ha.png`, same builder, same product style. Six angles, worded in the buyer language users actually use about HA (owner: "use social media and forums… value added statements"; research with links in the private repo, `design/research/HA_VOICE_OF_CUSTOMER.md`): One app. No more app juggling; Your brands finally work together; Works when the internet doesn't (home network only, never cloud HA); Ask, don't open (the three owner voice examples, Siri via HomeKit); Peace of mind, all over the house; Nobody can switch it off. The intro answers the top objection users raise (setup is daunting): "everything people love about it, without the setup. Just plug it in." No forum quotes are published. Figures (2.7M+ households, 1,500+ integrations, 1,000+ brands) are cited on the page to home-assistant.io, October 2026; "0 subscriptions with Control Freak" is ours, and is not placed next to the Alexa/Google line. The three idea cards are labelled **Idea · Example** and use the buyer's own devices ("Your lights, speakers and thermostat aren't in the box"). **For Eng/Writer to OK:** the idea-card wording, "without the setup. Just plug it in." and "answers right away".
