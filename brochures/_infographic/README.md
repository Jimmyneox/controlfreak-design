# Wave 1 brochures: "Why Home Assistant" page and splice

`build_infographic.py` writes page 5, **Why Home Assistant** (`why-ha.html` → `why-ha.pdf`/`why-ha.png`),
into each locked Wave 1 brochure and rebuilds `brochure.pdf`:

front, light-mode, duo, ha-home, **why-ha**, infographic, back

The page has six benefit angles, four Home Assistant figures cited to home-assistant.io (October 2026),
the owner's "Works with the Control Freak gear you already own" line, and three "Idea · Example"
automations per product, in each brochure's own palette, type and lockup.

**The "How it all connects" infographic is not made here any more** (owner, 2026-10-26): Gemini is
remaking it (controlfreak-platform `design/INFOGRAPHIC_REMAKE.md`). This script never writes
`infographic.*`. If a brochure folder has an `infographic.pdf`/`.png`, the splice places it as page 6;
if not, the brochure is six pages.

    python3 brochures/_infographic/build_infographic.py          # all four
    python3 brochures/_infographic/build_infographic.py O04      # one

Site export (public repo) writes only the `#home-assistant` section on each product site; it doesn't touch
`#connects` or `how-it-connects.svg`:

    python3 brochures/_infographic/build_infographic.py --site /path/to/controlfreak-platform-public [codes]

Needs Node with Playwright (Chromium) and Python with Pillow and pypdf. Each brochure's own build
script calls this at the end, so a rebuild keeps the pages.
