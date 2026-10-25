# Control Freak — In-site Product Demo Template

Reusable, themable **marketing simulation** of a phone/app controller, for every Control Freak product site (Wave 1: Reef Control Pro, Basement Guard Pro, Terrarium Control Pro, Sub Zero Control Pro — and all future products). One shell, many skins. No one-off demos.

## Hard rules
- **Marketing simulation only.** All values are fake, client-side, randomised. No backend, no network calls.
- **No** App Store internals, private APIs, real app binaries, screenshots of unreleased builds, or private Platform briefs/specs in this folder.
- Do not claim water chemistry results, cloud HA, or off-LAN remote control. Away-from-home push/text/email/alarm may appear only as a *simulated notification type*.
- Real per-product readouts/controls come later from Platform's marketing-safe demo specs. Until then use `PLACEHOLDER` labels.
- Must **not** look like the pool Resort site (ivory/lagoon/brass, Cormorant + Jost). Each product sets its own visual system via CSS vars.

## Files
| File | Role |
|---|---|
| `demo.html` | Generic shell (neutral default theme) |
| `demo.css` | Structure + `--cfd-*` theme variables |
| `demo.js` | Faux interactivity driven by `window.CFD_CONFIG` |
| `examples/reef-placeholder.html` | Proof of reuse: only CSS vars + placeholder strings change |

Parent lockup: footer `<img>` references `../../lockups/product/brought-to-you-by-control-freak-horizontal-light.svg` (or `-currentColor`/`-dark` variants; parent teardrop + "brought to you by Control Freak"; source mark in `brand/parent-company/`). When deploying a product site, **copy** that SVG next to the demo and update the `src` (relative paths outside the site root won't ship).

## How a product plugs in
1. Copy `demo.css`, `demo.js`, and the markup inside `<div class="cfd-device">` from `demo.html`.
2. Override variables on `.cfd-device` (or `:root`):
   ```css
   .cfd-device { --cfd-accent:#..; --cfd-surface:#..; --cfd-surface-2:#..; --cfd-text:#..; --cfd-muted:#..; --cfd-ok:#..; --cfd-warn:#..; --cfd-radius:..; --cfd-font:..; }
   ```
3. Define `window.CFD_CONFIG` before loading `demo.js`:
   ```js
   window.CFD_CONFIG = {
     product: "PLACEHOLDER Product",
     readouts: [{ label:"Readout A", unit:"", min:0, max:100, value:50, jitter:1 }],
     controls: [{ label:"Control 1", on:false }],
     notify: { label:"Simulated alert", channels:["Push","Text","Email","Alarm"] }
   };
   ```
4. Keep the "SIMULATION" badge visible. Do not remove the disclaimer line.

## Open locally
`python3 -m http.server -d site 8000` from the repo root, then visit
http://localhost:8000/demo-template/demo.html and http://localhost:8000/demo-template/examples/reef-placeholder.html
(Opening the files directly via `file://` also works.)
