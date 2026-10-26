# Wave 1 demo objects — photoreal v2 (photo base + overlays)

James bar: "the demo should look real." Each object = photoreal base plate (`base.jpg`, 1024×768, generated; O04 matched to `_refs/james-reef-demo-look-real.png`) + an SVG overlay stack toggled by root classes. Flat SVG v1 archived in `_flat-svg-v1/`.

## Files per object (`{slug}/`)
| file | use |
|---|---|
| `base.jpg` | idle photo plate |
| `object.svg` | wrapper, links `base.jpg` (relative) — use when serving files side by side |
| `object-inline.svg` | same, base embedded as data URI — **inline this into the DOM** (self-contained) |
| `object.html` | self-contained fragment (`<div class="cf-demo-stage">` + inline SVG) for injection |
| `overlays/overlays.svg` | overlay layers only (base hidden) — to stack over your own `<img>` |
| `object-idle.png` / `object-active.png` | composites |

viewBox `0 0 1024 768`. CSS lives in the SVG `<style>` (scoped by `.cf-demo-object`), transitions .6s, caustic shimmer + LED pulse animations built in.

## Wiring (API compatible with 1559d14)
Toggle classes on root `svg.cf-demo-object`:
```js
const o = stage.querySelector('.cf-demo-object');
o.classList.toggle('pump-on', true);
o.querySelector('#water').style.transform = `scaleY(${level})`; // 0..1, bottom-anchored
```

| object | classes | extras |
|---|---|---|
| O04 `o04-reef` | `light-on` (#light-beam, #light-glow, #status-light), `heater-on` (#heater-glow, #status-heater), `pump-on` (#flow caustics, #status-pump) | `#water` = cyan tint layer, scaleY |
| C03 `c03-basement` | `pump1-on` (#pump1-glow, #ripple1, #led-pump1), `pump2-on` (…2), `alarm` (#alarm-wash red pulse, #led-alarm) | `#water` (pit tint) scaleY; `#float` translateY (px, negative = up) |
| O15 `o15-terrarium` | `lamp-on` (#lamp-beam, #lamp-glow), `heat-on` (#heat-haze), `mist-on` (#mist rising) | **new** `uvb-on` (#uvb bar) |
| C01 `c01-cold-plunge` | `chiller-on` (#chill-glow, #frost, #flow, #led-chiller), `power-on` (#display, #led-power), `temp-neutral` (water tint cold-blue → neutral teal) | `#water-tint` inside `#water`; set `style.fill` for custom temp tint |

Idle composites: O04/O15/C03 no classes; C01 = `power-on temp-neutral`. Active: all listed classes (C01 = `chiller-on power-on`).

## Caveats
- Bases are AI-generated plates (brochure-grade, not product photos of our hardware). C03 is a top-down documentary view, not a true cutaway; water-level scaleY is a tint, not a real level change.
- Inline files are ~0.9–1.2 MB each (base64 JPEG); prefer `object.svg` + `base.jpg` or `overlays.svg` over `<img>` for production.
- `mix-blend-mode` overlays need a modern browser; degrade to plain opacity elsewhere.
