# Wave 1 brochures: "Why Home Assistant" page and splice

`build_infographic.py` writes page 5, **Why Home Assistant** (`why-ha.html` → `why-ha.pdf`/`why-ha.png`),
into each locked Wave 1 brochure and rebuilds `brochure.pdf`:

front, light-mode, duo, ha-home, **why-ha**, infographic, back

The page has six benefit angles, four Home Assistant figures cited to home-assistant.io (October 2026),
the owner's "Works with the Control Freak gear you already own" line, and three "Idea · Example"
automations per product, in each brochure's own palette, type and lockup.

**The "How it all connects" infographic is not made here any more** (owner, 2026-10-26): Gemini is
remaking it (controlfreak-platform `design/INFOGRAPHIC_REMAKE.md`). When a brochure folder has
Gemini's `infographic.gemini.html`, the build exports it as-is to `infographic.pdf`/`.png` and the splice
places it as page 6 (brief: controlfreak-platform `design/INFOGRAPHIC_REMAKE.md`). Without that file the
script never writes `infographic.*`; an existing `infographic.pdf` is still placed, and with none the
brochure is six pages.

    python3 brochures/_infographic/build_infographic.py          # all four
    python3 brochures/_infographic/build_infographic.py O04      # one

Site export (public repo) writes the `#home-assistant` section on each product site. When Gemini's art
exists it also copies `infographic.png` to `assets/how-it-connects.png` and points the `#connects` figure at
it; otherwise `#connects` is left alone:

    python3 brochures/_infographic/build_infographic.py --site /path/to/controlfreak-platform-public [codes]

Needs Node with Playwright (Chromium) and Python with Pillow and pypdf. Each brochure's own build
script calls this at the end, so a rebuild keeps the pages.
