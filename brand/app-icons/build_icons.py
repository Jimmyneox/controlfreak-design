"""Rebuild favicon/app-icon sets from brand masters. Run from repo root."""
import io, re, json, pathlib, cairosvg
from PIL import Image
R = pathlib.Path(__file__).resolve().parents[2]
OUT = R/"brand/app-icons"
M = R/"brand/app-icons/_masters"   # PCB simplified icon masters (make_masters.py)
# tile = solid rounded plate behind the favicon (so dark/light browser chrome both read)
SETS = {
 "parent":          dict(src=M/"control-freak-pcb-icon-navy.svg", ink="#0b1f3a", bg="#FFFFFF", tile="#FFFFFF", name="Control Freak"),
 "o04-reef":        dict(src=R/"brochures/O04-reef/approved-mark/reef-mark-drop.svg", ink="#13788D", bg="#FFFFFF", tile=None, name="Reef Control Pro"),
 "c03-basement":    dict(src=M/"control-freak-pcb-icon-white.svg", ink="#0b1f3a", bg="#0b1f3a", tile="#0b1f3a", name="Basement Guard"),
 "o15-terrarium":   dict(src=M/"control-freak-pcb-icon-forest.svg", ink="#0f2e2c", bg="#efe9df", tile="#efe9df", name="Terrarium Control"),
 "c01-cold-plunge": dict(src=M/"control-freak-pcb-icon-cool-blue.svg", ink="#2f6f9f", bg="#eaf3f8", tile="#eaf3f8", name="Cold Plunge Control Pro"),
 "pool":            dict(src=R/"brand/masters/control-freak-mark-icon.svg", ink="#0f2e2c", bg="#efe9df", tile=None, name="Control Freak Pool"),
}
import sys
if "pool" not in sys.argv: SETS.pop("pool")  # pool set kept as committed; pass 'pool' to rebuild it
def render(svg, size, bg=None, pad=0.0, tile=None):
    inner = round(size*(1-2*pad))
    png = cairosvg.svg2png(bytestring=svg, output_width=inner*4)
    im = Image.open(io.BytesIO(png)).convert("RGBA"); im.thumbnail((inner, inner), Image.LANCZOS)
    c = Image.new("RGBA", (size, size), bg or (0,0,0,0))
    if tile:
        from PIL import ImageDraw
        ImageDraw.Draw(c).rounded_rectangle((0,0,size-1,size-1), radius=round(size*0.18), fill=tile)
    c.alpha_composite(im, ((size-im.width)//2, (size-im.height)//2)); return c
for key, s in SETS.items():
    d = OUT/key; d.mkdir(parents=True, exist_ok=True)
    svg = s["src"].read_bytes()
    # square SVG favicon (transparent) wrapping master
    vb = list(map(float, re.search(rb'viewBox="([^"]+)"', svg).group(1).split()))
    side = max(vb[2], vb[3]); body = re.sub(rb'^.*?<svg[^>]*>|</svg>\s*$', b'', svg, flags=re.S)
    body = re.sub(rb'<title>.*?</title>', b'', body, flags=re.S)
    ox, oy = vb[0]-(side-vb[2])/2, vb[1]-(side-vb[3])/2
    plate = b''
    if s["tile"]:  # pad 10% inside a rounded plate
        p = side*0.12; ox, oy, side = ox-p, oy-p, side+2*p
        plate = b'<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"/>' % (ox,oy,side,side,side*0.18,s["tile"].encode())
    (d/"favicon.svg").write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="%g %g %g %g">' % (ox,oy,side,side) + plate + body + b'</svg>\n')
    fp, ft = (0.10, s["tile"]) if s["tile"] else (0.02, None)
    for n in (16,32,48): render(svg, n, pad=fp, tile=ft).save(d/f"favicon-{n}x{n}.png")
    render(svg, 256, pad=fp, tile=ft).save(d/"favicon.ico", sizes=[(16,16),(32,32),(48,48)])
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
W=len(keys)*190+20; sheet=Image.new("RGB",(W,470),"#ffffff"); dr=ImageDraw.Draw(sheet)
dr.rectangle((0,235,W,470),fill="#202124")
for i,k in enumerate(keys):
    x=20+i*190
    for row,(y0,txt) in enumerate(((10,"#000"),(245,"#ddd"))):
        dr.text((x,y0),k,fill=txt)
        for j,n in enumerate((32,48)):
            im=Image.open(OUT/k/f"favicon-{n}x{n}.png").convert("RGBA")
            sheet.paste(im,(x+j*60,y0+20),im); big=im.resize((n*2,n*2),Image.NEAREST); sheet.paste(big,(x+j*80,y0+80),big)
sheet.save(OUT/"_preview-favicon-sets.png"); print("ok")
