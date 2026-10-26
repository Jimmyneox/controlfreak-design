"""'brought to you by Control Freak' attribution lockups — company mark = corporate PCB wordmark
(brand/corporate/control-freak-corporate-wordmark-*.svg, PARENT_BRAND v1.4). Run from repo root."""
import re, os, cairosvg
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
INTER='/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf'
f=instantiateVariableFont(TTFont(INTER),{'wght':500,'opsz':14}); gs=f.getGlyphSet(); cm=f.getBestCmap(); upm=f['head'].unitsPerEm
def text(s,size):
    sc=size/upm; x=0; out=[]
    for ch in s:
        g=gs[cm[ord(ch)]]; sp=SVGPathPen(gs, ntos=lambda v:('%.2f'%v).rstrip('0').rstrip('.'))
        g.draw(TransformPen(sp,(sc,0,0,-sc,x,0))); out.append(sp.getCommands()); x+=g.width*sc
    return ' '.join(out), x
T=26; TXT,TW=text('brought to you by',T)
src=open('brand/corporate/control-freak-corporate-wordmark-currentColor.svg').read()
vb=[float(v) for v in re.search(r'viewBox="([^"]+)"',src).group(1).split()]
inner=re.sub(r'(?s)^.*?<title>.*?</title>','',src); inner=re.sub(r'(?s)</svg>\s*$','',inner)
MH=110; MW=MH*vb[2]/vb[3]; CS=MW/8
NAVY,WHITE,SLATE,MIST='#0b1f3a','#ffffff','#5b6670','#c3cddb'
V=[('light',NAVY,SLATE,'#f4f1ea'),('dark',WHITE,MIST,NAVY),('gold','#a8834f','#c9c2b6','#0f2e2c'),('cream','#efe9df','#c9c2b6','#0f2e2c'),('forest','#0f2e2c','#5b6670','#efe9df'),('currentColor','currentColor','currentColor',None)]
def mark(x,y,ink): return f'<svg x="{x:.1f}" y="{y:.1f}" width="{MW:.1f}" height="{MH}" viewBox="{" ".join(map(str,vb))}" style="color:{ink}">{inner}</svg>'
def tx(x,y,ink): op=' opacity=".72"' if ink=='currentColor' else ''
def txt(x,y,ink): return f'<path transform="translate({x:.1f},{y:.1f})" fill="{ink}"{" opacity=\".72\"" if ink=="currentColor" else ""} d="{TXT}"/>'
def doc(w,h,body,plate,label):
    bg=f'<rect width="100%" height="100%" fill="{plate}"/>' if plate else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="brought to you by Control Freak"><title>brought to you by Control Freak — {label}</title>{bg}{body}</svg>'
out=[]; D='lockups/product/'
for n,mi,ti,pl in V:
    for plate in ([False,True] if pl else [False]):
        suf='-on-plate' if plate else ''
        w=max(TW,MW)+2*CS; h=T+14+MH+2*CS
        body=txt((w-TW)/2,CS+T*0.78,ti)+mark((w-MW)/2,CS+T+14,mi)
        fn=f'{D}brought-to-you-by-control-freak-stacked-{n}{suf}.svg'; open(fn,'w').write(doc(w,h,body,pl if plate else None,f'stacked {n}{suf}')); out.append(fn)
        w=TW+28+MW+2*CS; h=MH+2*CS
        body=txt(CS,CS+MH/2+T*0.36,ti)+mark(CS+TW+28,CS,mi)
        fn=f'{D}brought-to-you-by-control-freak-horizontal-{n}{suf}.svg'; open(fn,'w').write(doc(w,h,body,pl if plate else None,f'horizontal {n}{suf}')); out.append(fn)
os.makedirs(D+'png',exist_ok=True)
from PIL import Image, ImageDraw; import io
tiles=[]
for fn in out:
    if 'currentColor' in fn: continue
    for s in (1,2): cairosvg.svg2png(url=fn,write_to=fn.replace(D,D+'png/').replace('.svg',f'@{s}x.png'),scale=s)
    im=Image.open(io.BytesIO(cairosvg.svg2png(url=fn,scale=1.5))).convert('RGBA')
    bgc='#cfcfcf' if 'plate' in fn else '#0b1f3a' if '-dark' in fn else '#0f2e2c' if ('-gold' in fn or '-cream' in fn) else '#efe9df' if '-forest' in fn else '#f4f1ea'
    t=Image.new('RGB',(im.width+80,im.height+80),bgc); t.paste(im,(40,40),im); tiles.append(t)
W=max(t.width for t in tiles)*2+60; rows=[tiles[i:i+2] for i in range(0,len(tiles),2)]
H=sum(max(t.height for t in r)+30 for r in rows)+30; S=Image.new('RGB',(W,H),'#e9e6df'); y=30
for r in rows:
    x=30
    for t in r: S.paste(t,(x,y)); x+=t.width+30
    y+=max(t.height for t in r)+30
S.save(D+'png/_contact-sheet.png'); print('\n'.join(out))
