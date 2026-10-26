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
