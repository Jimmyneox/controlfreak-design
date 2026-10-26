# Wave 1 demo objects — photoreal v2 (photo base + overlays)

James bar: "the demo should look real." Each object = photoreal base plate (`base.jpg`, 1024×768, generated text-only, **close-up v3**: tank/tub/pit fills the stage, no room plates) + an SVG overlay stack toggled by root classes. Flat SVG v1 archived in `_flat-svg-v1/`.

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
| C01 `c01-cold-plunge` | **`chromo-on`** = Chromotherapy master (cycles colors 12 s) + optional fixed color `chromo-blue` / `chromo-teal` / `chromo-violet` / `chromo-magenta` / `chromo-warm` / `chromo-white`; `chiller-on` (#mist, #flow, #led-chiller), `power-on` (#display 39°F, #led-power), `temp-neutral` (water tint cold-blue → neutral) | all water layers clipped to `#cWater` ellipse (= `water-mask.png`); `#water-tint` fill for custom temp tint |

Idle composites: O04 `swim-on`; O15/C03 no classes; C01 = `power-on temp-neutral`. Active: all listed classes (O04 also `swim-on`; C01 = `power-on chiller-on chromo-on chromo-violet`).

## Caveats
- Bases are AI-generated plates (brochure-grade, not product photos of our hardware). C03 is a top-down documentary view, not a true cutaway; water-level scaleY is a tint, not a real level change.
- Inline files are ~0.9–1.2 MB each (base64 JPEG); prefer `object.svg` + `base.jpg` or `overlays.svg` over `<img>` for production.
- `mix-blend-mode` overlays need a modern browser; degrade to plain opacity elsewhere.

> **Provenance:** Bases are original generated marketing art; not photographs of customer or third-party installations. James’s reef ref is quality reference only and must not be used as a likeness. (Prior f5aa8d7 bases archived in `_superseded-likeness-f5aa8d7/`.)

## Close-up v3 + swimming fish (James/Chief cue)
- Bases remade as **close-ups**: O04 = inside a rimless reef tank (corals/sand/surface, glass edges at frame), O15 = terrarium interior + frame/lamp clip, C01 = **(v4, see below)**, C03 = sump pit water + pumps/PVC + concrete rim. No living room / skyline / basement plates. Prior room-plate bases archived in `_superseded-roomplate-8c34483/`.
- All four bases are original text-only generations; `_refs/james-reef-demo-look-real.png` was **not** used as a reference.

### How the fish loops work (O04)
- **v4: photoreal fish sprites** (replaces flat vector fish). The O04 base photo has **no fish**; six `<image>` sprites live in `<g id="fish-school">` as `#fish-1` … `#fish-6` (class `fish`, `data-species`). Sprites = transparent PNGs in `o04-reef/fish/`: `clownfish.png`, `blue-tang.png`, `yellow-tang.png`, `chromis.png`, `royal-gramma.png` (original text-only studio generations, cut out with alpha, 480px wide, facing right; left-swimmers are mirrored with `scale(-1,1)`).
- `object.svg` / `overlays.svg` reference `fish/*.png` relatively (serve the `fish/` folder alongside); `object-inline.svg` and `object.html` embed them as data URIs (self-contained).
- Filters: `#fFish` = slight underwater color cast + soft drop shadow; `#fFishFar` = bluer, blurred, .8 opacity for the two distant chromis (`fish-4`, `fish-6`) to give depth.
- CSS `@keyframes`: `cfSwimR` / `cfSwimL` translate each fish across the full width (18–38 s linear loops, staggered negative delays so fish are mid-tank on load), `cfBob` vertical drift/pitch, `cfUndulate` subtle body flex (.7 s). Same `swim-on` / `swim-off` API as before.
- **Default: autoplay ON** — root ships with class `swim-on`. To pause: `o.classList.add('swim-off')` (pauses every animation in the object, incl. caustics/ripples). To stop and hide fish off-stage: remove `swim-on`.
- Respect reduced motion if desired: `if (matchMedia('(prefers-reduced-motion: reduce)').matches) o.classList.add('swim-off')`.
- Other subtle life: C01 surface shimmer (always), C03 expanding ripple rings when `pump1-on`/`pump2-on`, O15 rising mist with `mist-on`.

### Inline required
Class toggles **and** reliable animation require the SVG to be **inlined in the DOM** (`object.html` or `object-inline.svg` contents injected). As `<img src="object.svg">` the page CSS/JS cannot reach it (some browsers also freeze animation). No video assets.

## C01 v4 — spa craft + Chromotherapy (James cue: "water is outside the boundaries")
- **New base** `c01-cold-plunge/base.jpg`: round elevated travertine plunge tub, 3/4 close-up, water **contained inside the vessel** below the rim, two underwater LED fixtures on the inner wall, light mist. Generated with our own pool-site spa photo (`_refs/pool-spa-1248.webp`, from `site/src/assets/photos/spa-1248.webp`) as **style/quality reference only**. James’s reef ref not used. Previous broken rectangle base replaced.
- **Water stays inside the vessel:** every water/LED layer is clipped to `<clipPath id="cWater">` = ellipse `cx 538 cy 422 rx 417 ry 95` (hand-fitted to the water surface) and feathered by `<mask id="mWater">`. Same shape shipped as `c01-cold-plunge/water-mask.png` (1024×768, white = water) for anyone compositing outside the SVG. Only `#chromo-rim` (soft spill onto the *inner* stone wall, masked to the inner bowl) and the rim LCD sit outside the water.
- **Chromotherapy** (feature name for the site/demo button): colored underwater LEDs, like pool app `.m-spa` + `.spa-lit` + tint `#l-spa-c`.
  - `chromo-on` = master. Alone it **cycles** blue → teal → violet → magenta → warm (12 s loop).
  - Add one of `chromo-blue | chromo-teal | chromo-violet | chromo-magenta | chromo-warm | chromo-white` to lock a color (remove to resume cycling).
  - Layers: `#chromo` (multiply + color + screen glows, clipped to water), `#chromo-fixtures` (the two LED lenses glow), `#chromo-rim` (inner-wall spill), `#led-chromo` (dot on the rim LCD). All colored elements share class `.cc`; custom color: `o.querySelectorAll('.cc').forEach(e=>e.style.fill='#ff0')` with `chromo-on` + any `chromo-*` lock (to stop the cycle).
  - `chromotherapy-sheet.png` shows all six locked colors.
```js
const o = stage.querySelector('.c01-cold-plunge');
o.classList.toggle('chromo-on');                         // Chromotherapy button
['blue','teal','violet','magenta','warm','white'].forEach(c=>o.classList.remove('chromo-'+c));
o.classList.add('chromo-teal');                          // color swatch
```
