# STATUS: LOCKED — James (via Chief), Oct 25, 2026 ~11:31 PM ET

**Locked Basement Guard Pro literature** for C03.
- Craft: Living Demo Theater Concept A (polished)
- Voice: Gemini features/benefits outline (`../gemini-features-benefits-2026-10-25/outline.html`)
- HA bottom: away/storm story (kept from Concept A)
- Process: Gemini = verbiage (assumed good unless Engineering flags facts); Design = craft/fold
- Pushed with this lock to Jimmyneox/controlfreak-design

---

# C03 Basement Guard Pro — Concept A + Gemini OUTLINE voice (text-only)
Built Oct 25 2026 ~11:30 PM ET. Same pattern as O04 `c-v8-gemini-outline`.
**Craft = concepts/A-living-demo-theater (copied; original untouched). Voice = ../gemini-features-benefits-2026-10-25/outline.html.**

## Changes vs Concept A (all in build.py strings + appended size-only CSS)
- Front badges line: "▶ LIVE DEMO · TRY IT ON THE SITE" → VOICE & TAP CONTROL · AWAY ALERTS · NO SUBSCRIPTION. H1/sub already matched outline exactly.
- Six callouts → outline 01–06 verbatim: Two pumps take turns / Second pump steps in / See the water level / Pumps work if controller doesn't / Pump check-up / Leak and freeze watch. Concept A "06 One hub, whole home" dropped from the front (HA stays on the HA page). Positions/panels are the same.
- Phone chrome (all phones): status subline → "Pit depth 6 in · Pump A lead · B standby · ran 14 times today". Other chips (weekly test, heat tape °F, Power Hub) already match the outline and are unchanged.
- Light-mode page → outline deep dive 1: eyebrow "WHY IT MATTERS · 01 · EQUALIZED WEAR", H1 "Two pumps that actually work as a team.", outline body (lightly trimmed; "frozen in stagnant water" → "idle"; closes with each pump keeping its own factory float).
- Duo page → outline deep dive 2: eyebrow "WHY IT MATTERS · 02 · LOCAL-FIRST · CLOUD-FREE FOUNDATION", H1 "Reliability when internet or power fails.", outline body ("no monthly fees"). The filled Duo layout and feature tiles are unchanged.
- HA page: eyebrow "UNIFIED ECOSYSTEM · HOME ASSISTANT ON YOUR HOME NETWORK"; H1 → "How many apps do you open to run your home?" (removed from the paragraph so it isn't repeated). **Bottom story is still Concept A's away/storm story**; the chip only gained "Storm mode ·". The outline's NWS/geo-fence/arrival cards were NOT used.
- Back: CTA "Join the beta" → "Join Wave 1 Pro early" + outline lines (test early kits with your existing pumps; no credit card required). Kit list, storm/weekly-test/cold-snap tiles and the two-lane timeline are unchanged.
- CSS: appended .lightpg/.duopg header size overrides (H1 27px, body 9.6px, wider) so the longer copy clears the devices. No other visual change.

## Not used
No Gemini PNGs or hero crops; no prices (the $15,400 III stat was already in Concept A); no competitor names; no pool/reef; floats are always kept; °F only.

Rebuild: `python3 build.py`. The prior Concept A notes are in NOTES.conceptA.md.

## Eng fact patch (Oct 25, 2026 ~11:32 PM ET)
Light-mode equalized-wear body only (James rule: Gemini assumed good unless Eng flags unfactual):
- Removed "monitors amp draw" (Wave 1 has no pump energy meters; P2 later).
- Removed circuit-never-trips / dual-startup-surge guarantee; kept stagger benefit.
- Eng wording: "It alternates duty weekly and staggers starts so both pumps never kick on at the same instant."

## Pages 5–6 · Why Home Assistant + How it all connects (2026-10-26)
Owner request: "Create an infographic page for every product brochure and webpage". The brochure is now seven pages: front, light-mode, duo, ha-home, **why-ha**, **infographic**, back. `infographic.html` → `infographic.pdf`/`infographic.png` comes from `brochures/_infographic/build_infographic.py`, which also splices it into `brochure.pdf` and rebuilds `spread.png` and `brochure-review.pdf`; this folder's build calls it at the end. Words come from the product's PUBLIC_BRIEF (no new claims); the diagram is labelled **Concept illustration · not to scale**, and the buyer's own equipment is drawn dashed and labelled "Your …".

**Why Home Assistant (page 5).** Owner: "Research home assistant benefits and expand the information about it to sell its benefits from multiple angles." `why-ha.html` → `why-ha.pdf`/`why-ha.png`, same builder, same product style. Six angles: one app; works with what you already own; your home, your data (on the home network only, never cloud HA); ask, don't open (the three owner voice examples, Siri via HomeKit); automate the whole house; built to last. Figures (2.7M+ households, 1,500+ integrations, 1,000+ brands) are cited on the page to home-assistant.io, October 2026; "0 subscriptions with Control Freak" is ours, and is not placed next to the Alexa/Google line. The three idea cards are labelled **Idea · Example** and use the buyer's own devices ("Your lights, speakers and thermostat aren't in the box"). **For Eng/Writer to OK:** the idea-card wording and "set up and ready, not a weekend project".
