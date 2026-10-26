# v8: rebuilt toward James's HA tablet ref — airy frosted glass, column layout, bottom dock, °F
M='../approved-mark/'
WW='#F5D9A0'  # restrained warm white/gold "lights on"
def tile(icon,n,s,on=False,pct=None,c=WW):
    bar=f'<i class="sl8"><u style="width:{pct}%;--c:{c}"></u></i>' if (on and pct is not None) else ''
    return f'<div class="g8t{" on" if on else ""}" style="--c:{c}"><span class="ic">{icon}</span><div><b>{n}</b><em>{s}</em></div>{bar}</div>'
def chips():
    L=[('◉','Home'),('🔒','Locked'),('◆','Reef 78 °F'),('☀','Solar 6.1 kWh'),('💧','44%'),('🌡','71 °F')]
    return '<div class="chips8">'+''.join(f'<span><i>{i}</i>{t}</span>' for i,t in L)+'</div>'
def greet(big=True):
    days=[('Sat','62°','74°',(30,80)),('Sun','58°','71°',(20,70)),('Mon','55°','68°',(10,60)),('Tue','60°','76°',(30,90))]
    fc=''.join(f'<div class="fc"><span>{d}</span><em>{lo}</em><i><u style="left:{a}%;right:{100-b}%"></u></i><em>{hi}</em></div>' for d,lo,hi,(a,b) in days) if big else ''
    return f'<div class="col"><div class="hd8">⌂ Home</div><div class="g8 gr"><b>Good evening, James</b></div><div class="g8 wxc"><div class="wxt"><span class="sun">⛅</span><div><small>Partly cloudy, 66 °F</small><small>44% humidity</small></div></div><div class="clk">7:12</div><small class="dt">Sat, Oct 24</small>{fc}</div></div>'
def lights(n=8):
    L=[('💡','Living room','60%',1,60),('💡','Kitchen','80%',1,80),('○','Dining','Off',0,None),('💡','Bedroom','30%',1,30),('○','Office','Off',0,None),('💡','Porch','Sunset → 11 PM',1,100),('○','Hallway','Off',0,None),('💡','Patio','45%',1,45)][:n]
    return '<div class="col"><div class="hd8">✦ Lights</div><div class="lg8">'+''.join(tile(*x) for x in L)+'</div></div>'
def climate():
    rows=''.join(f'<div class="g8 trv"><span class="ic">◎</span><div><b>{n}</b><em>{s}</em></div><div class="pm"><i>−</i><b>{t} °F</b><i>+</i></div></div>' for n,s,t in [('Living room','Heat · 70 °F now',71),('Upstairs','Idle · 69 °F now',68)])
    return f'<div class="col"><div class="hd8">◐ Climate</div>{rows}<div class="lg8 two">{tile("◆","Reef tank","78.2 °F · calm",True,None,"#5EEAD4")}{tile("≋","Living fan","40%",True,40,"#22D3EE")}{tile("▭","Garage","Closed")}{tile("🔒","Front door","Locked",True,None,"#5EEAD4")}</div></div>'
def cams(n=2):
    L=[('Front door','frontdoor','7:12:04 PM'),('Backyard','backyard','7:12:05 PM')][:n]
    return ''.join(f'<div class="hcam" style="background:#000 url(assets/cam-{k}-concept.jpg) center/cover"><span class="rec">● LIVE</span><span class="cts">{ts}</span><b>{t}</b></div>' for t,k,ts in L)
def energy():
    vals=[.3,.25,.2,.22,.35,.55,.7,.5,.45,.4,.48,.62,.8,.72,.5,.38]
    bars=''.join(f'<i style="height:{v*100:.0f}%;background:{"linear-gradient(#F5D9A0,#E9C27A)" if v>.6 else "linear-gradient(#5EEAD4,#22D3EE)"}"></i>' for v in vals)
    return f'<div class="g8 en8"><div class="gh8"><b>Energy today</b><span>12.4 kWh</span></div><div class="bars8">{bars}</div><div class="gh8"><span class="t">● Solar 6.1</span><span class="w">● Peak</span></div></div>'
def right():
    return f'<div class="col"><div class="hd8">▣ Cameras</div>{cams(2)}{energy()}<div class="g8 md8"><div class="art8"></div><div><small>Living room speaker</small><b>Evening Jazz</b><span>⏻ &nbsp;⏮ &nbsp;❚❚ &nbsp;⏭</span></div></div></div>'
def dock(): return '<div class="dock8">'+''.join(f'<span class="{"a" if i==0 else ""}">{x}</span>' for i,x in enumerate(['⌂','◎','♪','◆','✦','◐','☁']))+'</div>'
fold=f'''<div class="fold hafold"><div class="cam"></div><div class="scr"><div class="dash8">
<div class="top8"><b>Home</b>{chips()}</div>
<div class="cols8">{greet()}{lights(8)}{climate()}{right()}</div>{dock()}</div></div></div>'''
ph=f'''<div class="phone haph" style="width:2.55in"><div class="island"></div><div class="scr"><div class="dash8 p">
{greet(False)}<div class="hd8">✦ Lights</div><div class="lg8 two">{''.join(tile(*x) for x in [('💡','Living','60%',1,60),('💡','Kitchen','80%',1,80),('○','Dining','Off'),('💡','Porch','On',1,100)])}</div>
<div class="hd8">▣ Front door</div>{cams(1)}<div class="lg8 two">{tile("◆","Reef tank","78 °F",True,None,"#5EEAD4")}{tile("◐","Climate","71 °F",True,None,"#22D3EE")}</div>{dock()}</div></div></div>'''
hapg=f'''<div class="pg hapg"><div class="hbg"></div>
<div class="head"><div><div class="live">PRE-CONFIGURED HOME ASSISTANT HUB BUILT IN</div><h1>Automate more than just your tank.<br>Automate the rest of your life.</h1><p style="max-width:4.4in;line-height:1.45">Control Freak eliminates app fatigue by bringing all of your smart and internet-connected devices into a single, unified platform—complete observability, one-app control, and cross-brand automation.</p></div><img src="{M}reef-mark-lockup.svg" style="width:1.6in"></div>
<div class="hstage">{fold}</div><div class="hphone">{ph}</div>
<div class="hfl story"><div class="sh"><b>When you pull into the driveway on the way home from work…</b><span class="ch">1 arrival → 4 home automations</span></div><div><b>Garage opens</b>Phone plus car Bluetooth sense you’re home—the door rises as you arrive.</div><div><b>Heated bathroom floor on</b>Warm underfoot by the time you’re upstairs.</div><div><b>Shower water warming</b>Hot water is ready when you step in—no waiting at the tap.</div><div><b>Entry lights if dark</b>Porch and hall come on only when it’s already evening.</div></div>
<div class="bot"><span>HA ON YOUR HOME NETWORK · VOICE VIA HA BRIDGES</span><span class="cc" style="position:static">Concept · example HA dashboard · device mock · concept camera stills</span></div></div>'''
