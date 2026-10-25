"""Rebuild favicon/app-icon sets from brand masters. Run from repo root."""
import io, re, json, pathlib, cairosvg
from PIL import Image
R = pathlib.Path(__file__).resolve().parents[2]
OUT = R/"brand/app-icons"
SETS = {
 "parent": dict(src=R/"brand/parent-company/control-freak-parent-mark-navy.svg", ink="#03204D", bg="#FFFFFF", name="Control Freak"),
 "pool":   dict(src=R/"brand/masters/control-freak-mark-forest.svg", ink="#0f2e2c", bg="#efe9df", name="Control Freak Pool"),
}
def render(svg, size, bg=None, pad=0.0):
    inner = round(size*(1-2*pad))
    png = cairosvg.svg2png(bytestring=svg, output_width=inner*4)
    im = Image.open(io.BytesIO(png)).convert("RGBA"); im.thumbnail((inner, inner), Image.LANCZOS)
    c = Image.new("RGBA", (size, size), bg or (0,0,0,0))
    c.alpha_composite(im, ((size-im.width)//2, (size-im.height)//2)); return c
for key, s in SETS.items():
    d = OUT/key; d.mkdir(parents=True, exist_ok=True)
    svg = s["src"].read_bytes()
    # square SVG favicon (transparent) wrapping master
    vb = list(map(float, re.search(rb'viewBox="([^"]+)"', svg).group(1).split()))
    side = max(vb[2], vb[3]); body = re.sub(rb'^.*?<svg[^>]*>|</svg>\s*$', b'', svg, flags=re.S)
    body = re.sub(rb'<title>.*?</title>', b'', body, flags=re.S)
    ox, oy = vb[0]-(side-vb[2])/2, vb[1]-(side-vb[3])/2
    (d/"favicon.svg").write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="%g %g %g %g">' % (ox,oy,side,side) + body + b'</svg>\n')
    for n in (16,32,48): render(svg, n, pad=0.02).save(d/f"favicon-{n}x{n}.png")
    render(svg, 256, pad=0.02).save(d/"favicon.ico", sizes=[(16,16),(32,32),(48,48)])
    render(svg, 180, s["bg"], 0.12).convert("RGB").save(d/"apple-touch-icon.png")
    for n in (192,512): render(svg, n, s["bg"], 0.10).save(d/f"icon-{n}.png")
    render(svg, 512, s["bg"], 0.22).save(d/"icon-maskable-512.png")
    render(svg, 150, pad=0.15).save(d/"mstile-150x150.png")
    (d/"site.webmanifest").write_text(json.dumps({"name":s["name"],"short_name":s["name"],"icons":[
      {"src":"icon-192.png","sizes":"192x192","type":"image/png"},
      {"src":"icon-512.png","sizes":"512x512","type":"image/png"},
      {"src":"icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}],
      "theme_color":s["ink"],"background_color":s["bg"],"display":"standalone"}, indent=2)+"\n")
    (d/"head-snippet.html").write_text(f'''<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="{s["ink"]}">
''')
print("ok")
