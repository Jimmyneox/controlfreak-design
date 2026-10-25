# controlfreakpool.com

Parent **pool** marketing site (Resort direction). Product industry sites are separate and must not clone this look (`brand/PARENT_BRAND.md` v1.2).

## Status (2026-10-25)

The original GitHub source was lost when James’s GitHub history was disrupted. The live site on Cloudflare is still serving:

- https://controlfreakpool.com/
- `/dealer`, `/app`, `/how-it-works`

## Recovery mirror

`_mirror/` is a pull of the **currently deployed** HTML + assets from the live site (not App Store Connect internals — marketing pages only). Use it as the rebuild base.

| Local | Live |
|---|---|
| `_mirror/index.html` | `/` |
| `_mirror/dealer.html` | `/dealer` |
| `_mirror/app.html` | `/app` |
| `_mirror/how-it-works.html` | `/how-it-works` |
| `_mirror/assets/` | `/assets/` |
| `_mirror/favicon.svg` etc. | site icons |

Missing from the mirror (not on the live host): `RESORT_DIRECTION.md` and any private build tooling / Cloudflare Pages config.

## Rebuild goals (Control Freak Design)

1. Turn `_mirror/` into a proper source tree (clean paths, shared layout, deployable to Cloudflare Pages).
2. Wire **line masters** into chrome/nav/footer; metallic hero only on high-impact parent heroes.
3. Keep App Store–only internals out of this public repo (`PUBLIC.md`).
4. Optional: extract a reusable in-site product demo pattern from the pool site for other products (Design owns pattern; Platform supplies per-product content).

## Visual tokens (from live CSS)

- Ivory `#fbfaf7`, sand `#ebe5da`, mist `#efe9df`
- Lagoon `#0f2e2c` / `#163f3c`
- Brass `#a8834f` / deep `#7d5f33` / light `#d2b789`
- Type: Cormorant Garamond (serif) + Jost (sans), self-hosted SIL OFL

## Source tree (rebuild, 2026-10-25)

```
site/
  _mirror/            recovery reference: untouched pull of live deploy (do not edit)
  src/
    pages/            index, dealer, app, how-it-works (from mirror; chrome brand → partial)
    partials/brand.html   shared logo + wordmark link used in nav + footer
    assets/           mirror assets + controller-408.webp (was missing from mirror)
    assets/brand/     line masters copied from brand/masters/ (forest/cream/gold/currentColor)
    assets/fonts/     woff2 + OFL-cormorantgaramond.txt, OFL-jost.txt
    favicon*, apple-touch-icon.png
  build.py            python3 site/build.py → site/dist/ (deploy dir; gitignored)
```

- Chrome marks: `.logo` CSS-masks `/assets/brand/control-freak-mark-currentColor.svg`, filled with `--brass` `#a8834f` (parent gold). Same geometry as the old `logo-mark-small.svg`. Metallic hero is not used in chrome. Never recolor the line mark to aqua/coral.
- `app.html` has no nav/footer chrome, so it has no mark slot.
- Product demos: a reusable in-site demo pattern comes later.

## Open gaps

- `RESORT_DIRECTION.md`: not recoverable. The tokens above are inferred from the live CSS only.
- Cloudflare Pages config/project name: unknown. Pending a decision from James. Build output dir = `site/dist`, command `python3 site/build.py`.
- Live `/assets/fonts/OFL.txt` (and LICENSE.txt) return 404. The OFL texts were re-added from google/fonts (`ofl/cormorantgaramond`, `ofl/jost`), and the next deploy will serve them.

## Product demo template

Reusable themable in-site demo chrome for all product sites (marketing simulation only): [`demo-template/`](demo-template/README.md).
