import cairosvg, io
from PIL import Image, ImageDraw, ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/sand-box/google/Inter/'+__import__('os').listdir('/usr/share/fonts/truetype/sand-box/google/Inter')[0],22)
def r(fn,w):
    return Image.open(io.BytesIO(cairosvg.svg2png(url=fn,output_width=w))).convert('RGBA')
def sheet(items,out,title):
    W=1400; tiles=[]
    for fn,plate,label,fg in items:
        im=r(fn,1100); t=Image.new('RGB',(W,im.height+160),plate); t.paste(im,((W-im.width)//2,90),im)
        ImageDraw.Draw(t).text((40,30),label,font=F,fill=fg); tiles.append(t)
    H=sum(t.height for t in tiles)+90; S=Image.new('RGB',(W,H),'#e9e6df'); d=ImageDraw.Draw(S); d.text((40,30),title,font=F,fill='#222')
    y=90
    for t in tiles: S.paste(t,(0,y)); y+=t.height
    S.save(out)
NAVYBG='#0b1f3a'; LIGHT='#f4f1ea'
sheet([('control-freak-corporate-lockup-white.svg',NAVYBG,'Full lockup — white (light-on-dark) · control-freak-corporate-lockup-white.svg','#9fb3cc'),
       ('control-freak-corporate-lockup-navy.svg',LIGHT,'Full lockup — navy #0b1f3a (dark-on-light) · control-freak-corporate-lockup-navy.svg','#5b6670')],
      'png/_preview-corporate-lockup.png','Control Freak — corporate PCB lockup (v1.4, 2026-10-25) — vector recreation of James JPG')
sheet([('control-freak-corporate-wordmark-white.svg',NAVYBG,'Wordmark only — white · control-freak-corporate-wordmark-white.svg','#9fb3cc'),
       ('control-freak-corporate-wordmark-navy.svg',LIGHT,'Wordmark only — navy · control-freak-corporate-wordmark-navy.svg','#5b6670'),
       ('control-freak-corporate-wordmark-navy.svg','#ffffff','Wordmark only — navy on white','#5b6670')],
      'png/_preview-corporate-wordmark.png','Control Freak — corporate PCB wordmark (no tagline)')
# side by side with source
src=Image.open('../corporate-logo-2026-10-25/james-new-corporate-logo.jpg').convert('RGB')
v=Image.new('RGB',(1273,880),NAVYBG); m=r('control-freak-corporate-lockup-white.svg',1167); v.paste(m,(55,147),m)
c=Image.new('RGB',(2600,940),'#e9e6df'); c.paste(src,(20,40)); c.paste(v,(1307,40))
d=ImageDraw.Draw(c); d.text((20,8),'Source JPG (James)',font=F,fill='#222'); d.text((1307,8),'Vector recreation (SVG, same scale/position)',font=F,fill='#222')
c.save('png/_compare-source-vs-vector.png')

sheet([('control-freak-corporate-lockup-gold.svg','#0f2e2c','Gold #a8834f on forest #0f2e2c','#c9c2b6'),
       ('control-freak-corporate-lockup-cream.svg',NAVYBG,'Cream #efe9df on navy #0b1f3a','#9fb3cc'),
       ('control-freak-corporate-lockup-forest.svg','#efe9df','Forest #0f2e2c on cream #efe9df','#5b6670'),
       ('control-freak-corporate-wordmark-gold.svg','#0b1f3a','Wordmark gold on navy','#9fb3cc'),
       ('control-freak-corporate-wordmark-cream.svg','#0f2e2c','Wordmark cream on forest','#c9c2b6'),
       ('control-freak-corporate-wordmark-forest.svg','#ffffff','Wordmark forest on white','#5b6670')],
      'png/_preview-corporate-colorways.png','Control Freak corporate PCB mark: theme colorways (same locked geometry)')
