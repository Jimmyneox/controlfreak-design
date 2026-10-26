# Wave 1 brochure pages 5–6 ("Why Home Assistant" and "How it all connects")

`build_infographic.py` writes two pages into each locked Wave 1 brochure, which becomes seven pages
(front, light-mode, duo, ha-home, why-ha, infographic, back).

**Page 5, Why Home Assistant** (`why-ha.html`): six benefit angles, four Home Assistant figures
cited to home-assistant.io (October 2026), and three "Idea · Example" automations per product.

**Page 6, How it all connects** (`infographic.html`): a concept diagram of how the
product connects (the buyer's own equipment drawn dashed; the probes and sensors on keyed,
colour-coded leads to the controller; the Power Hub with its labelled outlets; Home Assistant,
phone, voice and alert channels), a numbered legend and three key numbers. Each page reuses
its brochure's palette, type and lockup. Copy comes only from the product's PUBLIC_BRIEF.

    python3 brochures/_infographic/build_infographic.py          # all four
    python3 brochures/_infographic/build_infographic.py O04      # one

Needs Node with Playwright (Chromium) and poppler-utils (`pdfseparate`, `pdfunite`). Each
brochure's own build script calls this at the end, so a rebuild keeps the page.

Site export (public repo): `python3 build_infographic.py --site /path/to/controlfreak-platform-public [codes]`
adds the `#connects` and `#home-assistant` sections to each product site.
