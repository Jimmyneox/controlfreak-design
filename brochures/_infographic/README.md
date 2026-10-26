# Wave 1 brochure infographic page ("How it all connects")

`build_infographic.py` writes page 5 of each locked Wave 1 brochure: a concept diagram of how the
product connects (the buyer's own equipment drawn dashed; the probes and sensors on keyed,
colour-coded leads to the controller; the Power Hub with its labelled outlets; Home Assistant,
phone, voice and alert channels), a numbered legend and three key numbers. Each page reuses
its brochure's palette, type and lockup. Copy comes only from the product's PUBLIC_BRIEF.

    python3 brochures/_infographic/build_infographic.py          # all four
    python3 brochures/_infographic/build_infographic.py O04      # one

Needs Node with Playwright (Chromium) and poppler-utils (`pdfseparate`, `pdfunite`). Each
brochure's own build script calls this at the end, so a rebuild keeps the page.
