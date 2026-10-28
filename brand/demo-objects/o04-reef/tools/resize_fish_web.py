"""Lanczos-downscale the O04 fish sprites (premultiplied alpha) and save lossy WebP with alpha."""
import subprocess, sys
from pathlib import Path
from PIL import Image

SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2]); TMP = Path(sys.argv[3])
# Largest displayed CSS width = largest size factor in reef-demo.js x 190px clamp max; target 2x, capped at 260px.
MAX_S = {"blue-tang": 1.35, "yellow-tang": 1.1, "clownfish": 0.85, "royal-gramma": 0.68, "chromis": 0.48}
for sp, s in MAX_S.items():
    im = Image.open(SRC / f"{sp}.png").convert("RGBA")
    w = min(260, round(2 * s * 190))
    h = round(im.height * w / im.width)
    small = im.convert("RGBa").resize((w, h), Image.LANCZOS).convert("RGBA")  # premultiplied: no dark/bright halo
    png = TMP / f"{sp}-{w}.png"; small.save(png)
    dst = OUT / f"{sp}.webp"
    subprocess.run(["cwebp", "-quiet", "-q", "80", "-alpha_q", "100", "-m", "6", "-sharp_yuv", str(png), "-o", str(dst)], check=True)
    print(sp, f"{w}x{h}", dst.stat().st_size, "bytes")
