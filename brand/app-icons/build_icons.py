"""Rebuild favicon/app-icon sets from brand masters. Run from repo root."""
import io, re, json, pathlib, cairosvg
from PIL import Image
R = pathlib.Path(__file__).resolve().parents[2]
OUT = R/"brand/app-icons"
# FAVICONS = DROPS (James 2026-10-26). Teardrop/drop silhouettes only; PCB C+traces masters in _unused/ are NOT used.
P = R/"brand/_superseded/parent-teardrop-2026-10"
D = R/"brochures/O04-reef/approved-mark"
def cc(color):  # recolor the currentColor parent drop master (same geometry)
    return (P/"control-freak-parent-mark-currentColor.svg").read_bytes().replace(b'currentColor', color.encode())
# tile=None everywhere: flat transparent favicons. bg only used for apple-touch / PWA icons.
SETS = {
 "parent":          dict(svg=(P/"control-freak-parent-mark-navy.svg").read_bytes(), ink="#03204D", bg="#FFFFFF", name="Control Freak"),
 "o04-reef":        dict(svg=(D/"reef-mark-drop.svg").read_bytes(), ink="#13788D", bg="#FFFFFF", name="Reef Control Pro", simple=True),
 "c03-basement":    dict(svg=(P/"control-freak-parent-mark-white.svg").read_bytes(), ink="#0b1f3a", bg="#0b1f3a", name="Basement Guard"),
 "o15-terrarium":   dict(svg=(P/"control-freak-parent-mark-forest.svg").read_bytes(), ink="#0f2e2c", bg="#efe9df", name="Terrarium Control"),
 "c01-cold-plunge": dict(svg=cc("#2f6f9f"), ink="#2f6f9f", bg="#eaf3f8", name="Cold Plunge Control Pro"),
 "pool":            dict(svg=(R/"brand/masters/control-freak-mark-icon.svg").read_bytes(), ink="#0f2e2c", bg="#efe9df", name="Control Freak Pool"),
}
import sys
if "pool" not in sys.argv: SETS.pop("pool")  # pool set kept as committed; pass 'pool' to rebuild it
def solid(im, color):
    """Fill interior holes -> solid drop silhouette (for 16/32 legibility)."""
    from PIL import ImageDraw
    a = im.getchannel("A").point(lambda v: 255 if v > 0 else 0)
    m = Image.new("L", (a.width+2, a.height+2), 0); m.paste(a, (1,1))
    ImageDraw.floodfill(m, (0,0), 128)
    m = m.crop((1,1,a.width+1,a.height+1)).point(lambda v: 0 if v == 128 else 255)
    out = Image.new("RGBA", im.size, color); out.putalpha(m); return out
def render(svg, size, bg=None, pad=0.0, tile=None, simple=None):
    inner = round(size*(1-2*pad))
    hi = max(inner*8, 512)
    png = cairosvg.svg2png(bytestring=svg, output_height=hi)
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    if simple: im = solid(im, simple)
    im.thumbnail((inner, inner), Image.LANCZOS)
    c = Image.new("RGBA", (size, size), bg or (0,0,0,0))
    if tile:
        from PIL import ImageDraw
        ImageDraw.Draw(c).rounded_rectangle((0,0,size-1,size-1), radius=round(size*0.18), fill=tile)
    c.alpha_composite(im, ((size-im.width)//2, (size-im.height)//2)); return c
for key, s in SETS.items():
    d = OUT/key; d.mkdir(parents=True, exist_ok=True)
    svg = s["svg"]
    # square SVG favicon (transparent) wrapping master
    vb = list(map(float, re.search(rb'viewBox="([^"]+)"', svg).group(1).split()))
    side = max(vb[2], vb[3]); body = re.sub(rb'^.*?<svg[^>]*>|</svg>\s*$', b'', svg, flags=re.S)
    body = re.sub(rb'<title>.*?</title>', b'', body, flags=re.S)
    ox, oy = vb[0]-(side-vb[2])/2, vb[1]-(side-vb[3])/2
    plate = b''
    p = side*0.07; ox, oy, side = ox-p, oy-p, side+2*p   # drop ~86% of canvas
    (d/"favicon.svg").write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="%g %g %g %g">' % (ox,oy,side,side) + plate + body + b'</svg>\n')
    fp = 0.07
    sm = s["ink"] if s.get("simple") else None   # O04: solid drop at 16/32
    ims = {n: render(svg, n, pad=fp, simple=(sm if n <= 32 else None)) for n in (16,32,48)}
    for n, im in ims.items(): im.save(d/f"favicon-{n}x{n}.png")
    ims[48].save(d/"favicon.ico", sizes=[(16,16),(32,32),(48,48)], append_images=[ims[16], ims[32]])
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
# preview sheet: every set at 32/48 (1:1 and 4x nearest) on light + dark strips
from PIL import ImageDraw
keys=[k for k in ("parent","o04-reef","c03-basement","o15-terrarium","c01-cold-plunge","pool") if (OUT/k/"favicon-48x48.png").exists()]
W=len(keys)*230+20; sheet=Image.new("RGB",(W,470),"#ffffff"); dr=ImageDraw.Draw(sheet)
dr.rectangle((0,235,W,470),fill="#202124")
for i,k in enumerate(keys):
    x=20+i*230
    for row,(y0,txt) in enumerate(((10,"#000"),(245,"#ddd"))):
        dr.text((x,y0),k,fill=txt)
        for j,n in enumerate((16,32,48)):
            im=Image.open(OUT/k/f"favicon-{n}x{n}.png").convert("RGBA")
            sheet.paste(im,(x+j*55,y0+20),im); big=im.resize((n*2,n*2),Image.NEAREST); sheet.paste(big,(x+[0,40,110][j],y0+80),big)
sheet.save(OUT/"_preview-favicon-sets.png"); print("ok")
