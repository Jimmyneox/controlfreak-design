---
name: infographic-style
description: Jimmy's house style for Control Freak infographics, distilled from his 58-graphic reference set. It covers geometric modular containers, 2.5D paper-craft depth, a four-part node anatomy, circuit-style connectors and five layout archetypes, with 35–45% open space. Use whenever you build or remake an infographic, a "How it all connects" page, a process or step graphic, a site diagram, or any brochure page that explains a product visually.
---

# Infographic style

Jimmy's style for infographics, first written as a Gemini skill (2026-10-27) from his 58
reference graphics. The patterns don't depend on colour, so each product brings its own
palette, type and lockup.

The reference graphics are third-party work kept on Jimmy's Mac. Use them for direction only.
Never copy, trace or commit them.

## Control Freak rules come first

- **Source of content:** copy and numbers come only from the product's
  `products/<code>/PUBLIC_BRIEF.md`.
  - Cite every number on the page.
  - No prices: Starter / Pro tier names only, and mark Pro-only items "(Pro)".
- **Visual system:** use the product's own brochure palette, type and mark. These come from
  `design/STYLE.md` and `design/PARENT_BRAND.md`.
  - The PCB corporate wordmark is the "brought to you by" lockup.
  - O04 uses the coral-in-teardrop mark.
  - Label every concept visual **Concept**.
- **Required lines:** carry them word for word.
  - "Works with the Control Freak gear you already own…"
  - The product's safety line ("…keep running on the controller, even if Home Assistant
    stops").
- **Banned wording:**
  - "never cloud HA" and "via HA bridges"
  - calling it a "pool add-on", or saying it needs another controller
  - "works with every …"
  - competitor names
- **Units and audience:** °F only. Public repos get no App Store internals, costs, port maps or
  engineering gates.

## Patterns

1. **Geometric containers.** Every step or data point sits in one clean vector shape. Pick one
   family per page and keep it consistent:
   - vertical or horizontal capsules (pills)
   - concentric rings
   - rounded cards
   - hexagons
   - interlocking chevrons
   - isometric 3D platforms
2. **2.5D paper-craft depth.** Lift foreground badges off background cards with soft
   directional shadows (one light source per page). Other depth devices:
   - recessed circular icon wells
   - folded-ribbon tabs
   - paperclips
   - diagonal paper slits

   Use depth, not clutter.
3. **Four-part node anatomy.** Each node holds exactly four things:
   - a zero-padded numeral (`01`, `02`, `03`)
   - one monoline icon, all icons in one set at one stroke weight
   - a bold, tracked-out UPPERCASE header of 1–3 words
   - 12–25 words of micro-copy

   Nothing else goes in a node.
4. **Wayfinding connectors.** Link nodes and hubs with any of these:
   - 45° and 90° circuit-style leader lines ending in dots (they fit the PCB wordmark)
   - dashed orbital arcs
   - S-curve ribbons
   - tapered callout pointers

   Connectors show the real flow, for example sensor → controller → Power Hub → equipment, and
   Home Assistant → phone, voice and alerts.
5. **Five layout archetypes.** Choose by content:
   - **Linear or serpentine step flow:** setup steps, or "what happens when…".
   - **Bilateral hub and spoke:** the controller at the centre, with inputs on one side and
     outputs on the other. This is the default for "How it all connects".
   - **Isometric layered stack:** hardware, then Control Freak core, then Home Assistant, then
     phone and voice.
   - **Folded-ribbon spine:** a timeline or a day in the life.
   - **Modular dashboard grid:** key numbers and features.

   Keep 35–45% of the page as open space.

## Build and check

- Build each infographic as a self-contained HTML page at the brochure's page size. Use inline
  SVG for shapes, icons and connectors. Export to PNG and PDF with Playwright/Chromium.
- **Brochure output:** in each Wave 1 pack, write `infographic.gemini.html` (the file name the
  build expects). `build_infographic.py` exports it to `infographic.png`/`.pdf`, places it as
  page 6, and with `--site` sets the site's `#connects` figure. See
  `design/INFOGRAPHIC_REMAKE.md`.
- **Before you show anyone:**
  - every node follows the four-part anatomy
  - one container family, one icon set, one light source
  - open space is 35–45%
  - text is legible at print size and at 390 px on the site
  - every number is cited
  - none of the banned wording above appears
