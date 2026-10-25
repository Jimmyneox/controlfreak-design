# App icons / favicons

Per PARENT_BRAND.md: pool site → pool line mark (forest on cream); corporate / product attribution → parent teardrop (navy on white).

- `parent/` — from `brand/parent-company/control-freak-parent-mark-navy.svg`
- `pool/` — from `brand/masters/control-freak-mark-forest.svg`

Each set: `favicon.svg`, `favicon.ico` (16/32/48), `favicon-{16,32,48}x*.png`, `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `mstile-150x150.png`, `site.webmanifest`, `head-snippet.html`.

Rebuild: `python3 brand/app-icons/build_icons.py` (needs cairosvg + Pillow).

Note: the pool line mark includes the wordmark; at 16–32 px it reads as a framed shape only.

## Pool favicons: mark-only

The pool set is built from `brand/masters/control-freak-mark-icon.svg` (forest on cream), a mark-only master with the CONTROL FREAK wordmark removed so the icon stays legible at 16–32px. Cream and currentColor variants: `control-freak-mark-icon-cream.svg`, `control-freak-mark-icon-currentColor.svg`. Parent icons are unchanged.
