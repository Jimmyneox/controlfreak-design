"""Control Freak corporate PCB lockup — vector recreation of James's JPG
(brand/corporate-logo-2026-10-25/james-new-corporate-logo.jpg, 1273x880).
Coordinates are in source-pixel space; node centres were measured from the JPG
(distance-transform peaks), letter x-extents from column runs, cap band y358-463.
Letters: Montserrat (OFL) Black-weight outlines, each glyph fitted to its measured box,
with the two stencil slots cut (O1 top, O2 bottom). Tagline: Montserrat Regular, tracked."""
import os, cairosvg
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
FONT='/usr/share/fonts/truetype/sand-box/google/Montserrat/Montserrat-VariableFont_wght.ttf'
def inst(w): return instantiateVariableFont(TTFont(FONT),{'wght':w})
def glyph_path(f,ch,box):
    gs=f.getGlyphSet(); g=gs[f.getBestCmap()[ord(ch)]]
    bp=BoundsPen(gs); g.draw(bp); x0,y0,x1,y1=bp.bounds
    X0,Y0,X1,Y1=box  # target (y down)
    sx=(X1-X0)/(x1-x0); sy=(Y1-Y0)/(y1-y0)
    sp=SVGPathPen(gs, ntos=lambda v:('%.1f'%v).rstrip('0').rstrip('.'))
    g.draw(TransformPen(sp,(sx,0,0,-sy,X0-x0*sx,Y1+y0*sy)))
    return sp.getCommands()
CAP=(358,463)
RUNS=[('C',59,156),('O',159,265),('N',275,367),('T',374,455),('R',463,548),('O',552,660),('L',669,738),
      ('F',778,846),('R',856,943),('E',951,1018),('A',1022,1121),('K',1127,1217)]
heavy=inst(850)
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from svgelements import Path as SP
def cut(d, rect):
    """Boolean-subtract a stencil slot from a glyph (flattened at 0.25px)."""
    rings=[]
    for sub in SP(d).as_subpaths():
        sp=SP(sub); n=max(32,int(sp.length()/0.6))
        rings.append(Polygon([(p.x,p.y) for p in (sp.point(i/n) for i in range(n))]).buffer(0))
    g=rings[0]
    for r in rings[1:]: g=g.symmetric_difference(r)
    g=g.difference(box(*rect)).simplify(0.15)
    polys=getattr(g,'geoms',[g]); out=[]
    for p in polys:
        for ring in [p.exterior,*p.interiors]:
            c=list(ring.coords)[:-1]; out.append('M'+' '.join('%.1f %.1f'%xy for xy in c)+'Z')
    return ''.join(out)
SLOTR={1:(206.5,350,214.5,384),5:(603,437,611,471)}
WORD=' '.join(cut(glyph_path(heavy,c,(a,CAP[0],b+1,CAP[1])),SLOTR[i]) if i in SLOTR else glyph_path(heavy,c,(a,CAP[0],b+1,CAP[1])) for i,(c,a,b) in enumerate(RUNS))
SLOTS='<rect x="206.5" y="350" width="8" height="34"/><rect x="603" y="437" width="8" height="34"/>'
# tagline: each letter fitted to its measured column run, cap band y724-767
reg=inst(400)
TRUNS=[(184,212),(241,284),(313,356),(388,413),(479,516),(545,579),(610,642),(671,713),(745,786),(816,854),(879,911),(942,947),(980,1022),(1055,1089)]
TAGP=' '.join(glyph_path(reg,c,(x0,724,x1+1,767)) for c,(x0,x1) in zip('POOLAUTOMATION',TRUNS))
SW=10.5  # trace width
NODES=[(331,169),(251,218),(672,219),(406,241),(784,252),(370,284),(1028,284),(137,285),
       (1004,521),(141,531),(902,551),(678,581),(422,596),(299,598),(521,611),(212,617),(375,636)]
R=17.5
TRACES=[
 # bus bars
 'M168 329H1125','M166 491H1125',
 # top-left burst
 'M137 285H182L207 329','M251 218L293 260V329','M264 279V329','M332 169V329','M370 284V329','M406 241V329',
 # top-right traces (vertical off bus, 45deg, horizontal to node)
 'M432 329V292L502 222H672','M480 329V305L529 256H784','M526 329V315L553 288H1028',
 # bottom-left burst
 'M141 530H205L243 492','M266 493V542L212 596V617','M298 493V598','M337 493V655','M373 493V636',
 'M398 493V548L422 572V596','M434 493V535L510 611H521','M467 493V521L524 578H678','M504 493V508L544 548H902','M1004 516H565L541 492',
]
def art(ink, tagline=True, slot_id='s'):
    tr=''.join(f'<path d="{d}"/>' for d in TRACES)
    nd=''.join(f'<circle cx="{x}" cy="{y}" r="{R}"/>' for x,y in NODES)
    body=(f'<g fill="{ink}"><path d="{WORD}"/>{nd}</g>'
          f'<g fill="none" stroke="{ink}" stroke-width="{SW}" stroke-linejoin="miter" stroke-linecap="butt">{tr}</g>')
    if tagline: body+=f'<path fill="{ink}" d="{TAGP}"/>'
    return body
def doc(ink,tagline,label,plate=None):
    vb=(55,147,1167,(784 if tagline else 674)-147) # tight + ~4px pad
    x,y,w,h=vb
    bg=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{plate}"/>' if plate else ''
    st=' style="color:inherit"' if ink=='currentColor' else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="Control Freak{" Pool Automation" if tagline else ""}"{st}><title>Control Freak — corporate PCB {label}</title>'
            f'{bg}{art(ink,tagline)}</svg>')
WHITE,NAVY='#ffffff','#0b1f3a'
FOREST,CREAM,GOLD='#0f2e2c','#efe9df','#a8834f'
ICE,COOLBLUE='#eaf3f8','#2f6f9f'  # C01 Cold Plunge site chrome
out={}
for kind,tg in (('lockup',True),('wordmark',False)):
    for name,ink in (('white',WHITE),('navy',NAVY),('forest',FOREST),('cream',CREAM),('gold',GOLD),('ice',ICE),('cool-blue',COOLBLUE),('currentColor','currentColor')):
        fn=f'control-freak-corporate-{kind}-{name}.svg'; open(fn,'w').write(doc(ink,tg,f'{kind} {name}')); out[(kind,name)]=fn
if __name__=='__main__':
    os.makedirs('png',exist_ok=True)
    for (k,n),fn in out.items():
        if n=='currentColor': continue
        for s in (1,2): cairosvg.svg2png(url=fn,write_to=f'png/{fn[:-4]}@{s}x.png',scale=s*0.5 if s==1 else 1)
    print('\n'.join(out.values()))
