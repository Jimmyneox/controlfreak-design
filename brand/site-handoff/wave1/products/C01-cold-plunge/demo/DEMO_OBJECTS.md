# Wave 1 demo physical objects (Living Demo Theater)

One inline SVG per product: `{slug}/object.svg` (root `svg.cf-demo-object`, id = slug). Reference PNGs: `object-idle.png`, `object-active.png` (all state layers on). Overview: `preview-overview.png`.

**Convention:** layers are `<g id>`. Toggle layers have class `state` (hidden, opacity 0); show them by adding a class on the root `<svg>` (CSS is embedded). Water level: scale `#water` via `style.transform = 'scaleY(0.0–1.0)'` (origin = bottom of the water shape).

| Object | Static layers | Toggle (root class → layer) | Continuous |
|---|---|---|---|
| o04-reef | stand, tank-back, lamp, corals, fish, heater, glass | `light-on`→#lamp-on, `heater-on`→#heater-glow, `pump-on`→#pump-active | #water scaleY |
| c03-basement | floor, pit, pump-1, pump-2, float, controller | `pump1-on`→#pump-1-active, `pump2-on`→#pump-2-active, `alarm`→#alarm-glow | #water scaleY (pit level); move #float translateY |
| o15-terrarium | enclosure-back, substrate, plants, rock, animal, lamp, glass | `lamp-on`→#lamp-on, `heat-on`→#heat-glow, `mist-on`→#mist | — |
| c01-cold-plunge | deck, tub, ripples, chiller | `chiller-on`→#chiller-active, `power-on`→#power-led, `temp-neutral`→fades #water-cool to reveal neutral #water | #water-cool opacity for temp tint |

Example: `svg.classList.toggle('light-on', state.light)` beside `site/demo-template/` readouts. Must be inlined (not `<img>`) for JS control.
