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
