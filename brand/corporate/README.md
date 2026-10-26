# Corporate PCB mark — Control Freak (PARENT_BRAND v1.4, 2026-10-25)

Corporate logo **everywhere** (James lock via Chief, 2026-10-25). Vector recreation of
`../corporate-logo-2026-10-25/james-new-corporate-logo.jpg` (copy: `source-james-new-corporate-logo.jpg`).

| File | What |
|---|---|
| `control-freak-corporate-lockup-{white,navy,forest,cream,gold,currentColor}.svg` | Full lockup: CONTROL FREAK + circuit traces + POOL AUTOMATION |
| `control-freak-corporate-wordmark-{white,navy,forest,cream,gold,currentColor}.svg` | Wordmark + circuit traces only (no tagline) |
| `png/*@1x/@2x.png` | Rasters (@1x = half of source scale, @2x = source scale) |
| `png/_preview-corporate-lockup.png`, `png/_preview-corporate-wordmark.png` | Preview sheets on navy / cream / white plates |
| `png/_preview-corporate-colorways.png` | Theme colorways: gold/forest, cream/navy, forest/cream |
| `png/_compare-source-vs-vector.png` | Source JPG vs vector side by side |

**How it was made (`build_corporate.py`):** this isn't an auto-trace. Node centres (17) were measured from the JPG, and
trace centrelines were rebuilt as clean polylines (10.5 px strokes, 45° bends, butt caps) in source-pixel coordinates.
Letters are Montserrat (OFL) heavy-weight outlines, each glyph fitted to its measured box in the JPG, with the two stencil slots
boolean-cut into the paths (top of first O, bottom of second O). Tagline: Montserrat Regular, each letter placed at its
measured position. No raster embedded; the pool photo background is excluded. **Locked by James 2026-10-25.** Inks: white `#ffffff`, navy `#0b1f3a`, forest `#0f2e2c`, cream `#efe9df`, gold `#a8834f`, plus currentColor. Colors are flexible and follow the site theme; geometry is locked.
Traces are stroked paths. If a tool needs fills only, expand strokes in Figma/Illustrator.
Rebuild: `python3 build_corporate.py && python3 preview_sheet.py` (needs fonttools, shapely, svgelements, cairosvg).
