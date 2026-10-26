# C03 Basement Guard Pro — Concept A "Living Demo Theater". Rebuild: python3 build.py
import os,subprocess,math
from PIL import Image
I={'pump':'<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><rect x="7" y="11" width="10" height="10" rx="2.5"/><path d="M11 3h2v8h-2z"/><path d="M11 3h6v2h-6z"/><circle cx="12" cy="16" r="2" fill="#0006"/></svg>',
'heat':'<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h18M3 16h18"/><path d="M6 8c1 2.5-1 5.5 0 8M12 8c1 2.5-1 5.5 0 8M18 8c1 2.5-1 5.5 0 8"/></svg>',
'dehu':'<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><rect x="5" y="3" width="14" height="18" rx="3"/><path d="M8 7h8v2H8z" fill="#0006"/><path d="M12 12c2 2.4 2.6 3.4 2.6 4.4a2.6 2.6 0 0 1-5.2 0c0-1 .6-2 2.6-4.4z" fill="#0006"/></svg>',
'spare':'<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><rect x="4" y="4" width="16" height="16" rx="4" opacity=".5"/><path d="M9 9v3M15 9v3M10 16h4" stroke="#0008" stroke-width="2"/></svg>'}
outlets=[('Pump A','pump','Lead · last run 7 min ago','on'),('Pump B','pump','Standby · waits its turn','sbt'),('Heat tape','heat','Off · on below 35 °F',''),('Dehumidifier','dehu','On schedule · 48% RH','on'),('Spare','spare','Unused','')]
def tiles(): return '<div class="tiles">'+''.join(f'<button class="tile {k}" aria-pressed="{"true" if k=="on" else "false"}"><span class="gl">{I[ic]}</span><b>{n}</b><em>{c}</em></button>' for n,ic,c,k in outlets)+'</div>'
def ring(light=False,sz=74):
    r=30;C=2*math.pi*r;p=6/18
    trk='#22303c22' if light else '#ffffff22'
    def tick(frac,col):
        a=math.radians(-90+360*frac);x1,y1=37+26*math.cos(a),37+26*math.sin(a);x2,y2=37+35*math.cos(a),37+35*math.sin(a)
        return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="1.6" stroke-linecap="round"/>'
    return f'''<div class="ring"><svg viewBox="0 0 74 74"><defs><linearGradient id="rg" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#1f6fd1"/><stop offset="1" stop-color="#6fb0ff"/></linearGradient></defs><circle cx="37" cy="37" r="{r}" fill="none" stroke="{trk}" stroke-width="5"/><circle cx="37" cy="37" r="{r}" fill="none" stroke="url(#rg)" stroke-width="5" stroke-linecap="round" stroke-dasharray="{C*p:.1f} {C:.1f}" transform="rotate(-90 37 37)"/>{tick(8/18,'#9fb3c6')}{tick(14/18,'#ffb340')}</svg><div class="v"><b>6<u>in</u></b><span>↘ falling · 0.2 in/min</span></div></div>'''
def phone(mode,h):
    lt=mode=='light'
    return f'''<div class="phone {mode}" style="height:{h}"><div class="island"></div><div class="scr">
<div class="top"><div class="sb"><b>9:41</b><span>●●● ◔ ▮</span></div>
<div class="tk"><div><small>Basement · after the storm</small><h2>Both pumps healthy</h2><p>Pit depth 6 in · Pump A lead · B standby · ran 14 times today</p></div><span class="loc"><i></i>On site</span></div>
<div class="pitrow">{ring(lt)}<div class="pk"><div><span>Pump starts</span><b>8 in</b></div><div><span>High-water line</span><b style="color:#ffb340">14 in</b></div><div><span>High-water float</span><b style="color:#30d158">Clear</b></div><span class="pill">Lead this week · Pump A</span></div></div></div>
<div class="body">
<div class="card"><div class="gh">Pumps <span>swaps lead every Monday</span></div><div class="pumps"><div class="pu"><b><i></i>Pump A<em class="tag">LEAD</em></b><span>Last run 7 min ago · 38 s</span></div><div class="pu sb2"><b><i></i>Pump B<em class="tag">STANDBY</em></b><span>Weekly test passed Sun</span></div></div>
<div class="cap">Never starts both pumps at once — the second waits its turn.</div><div class="cap">If the controller is ever off, both pumps still run on their own floats.</div></div>
<div class="card amb"><small>Pump health</small><b style="display:block;font:600 10px Inter;margin-top:2px">Keep an eye on Pump A</b><span class="am">Pump A emptied the pit slower than usual — plan a replacement.</span></div>
<div class="two"><div class="card"><small>Leak</small><div class="dry">✓</div><b>Dry · Dry</b><span class="ok">Water heater · Washer</span></div><div class="card"><small>Heat tape</small><b>Off</b><span>On below 35 °F crawlspace</span></div></div>
<div class="card"><div class="gh">Temperatures <span>example readings</span></div><div class="temps"><div><b>58<u>°F</u></b><span>Basement</span></div><div><b>41<u>°F</u></b><span>Crawlspace</span></div><div><b>22<u>°F</u></b><span>Outdoor</span></div></div></div>
<div class="card"><div class="gh">Power Hub <span>5 labelled outlets</span></div>{tiles()}</div>
<div class="card alerts"><div class="gh">Alerts <span>push · text · email · alarm</span></div><div>✓ Weekly pump test — both OK<i>push</i></div><div>◐ Slow pump-down · Pump A<i>push · email</i></div><div>○ High water · leak · freezing pipes<i>armed</i></div></div>
<div class="card"><div class="gh">Sensors <span>8 online</span></div><div class="sens"><div><i></i>Pit level<b>6 in</b></div><div><i></i>High-water float<b>Clear</b></div><div><i></i>Leak · water heater<b>Dry</b></div><div><i></i>Leak · washer<b>Dry</b></div><div><i></i>Basement<b>58 °F</b></div><div><i></i>Water heater area<b>64 °F</b></div></div></div>
<div class="card"><div class="gh">Coming up <span>automatic</span></div><div class="kv"><div><span>Weekly pump test</span><b>Sun 10 AM</b></div><div><span>Lead swaps to Pump B</span><b>Mon</b></div><div><span>Heat tape</span><b>On below 35 °F</b></div></div></div>
<div class="chip">⌂ Home Assistant pre-installed · Ask Alexa how the sump is doing</div>
</div></div></div>'''
def wide():
    return f'''<div class="fold"><div class="cam"></div><div class="scr dark">
<div class="wl"><div class="top"><div class="sb"><b>9:41</b><span>●●● ◔ ▮</span></div><div class="tk"><div><small>Basement · after the storm</small><h2>Both pumps healthy</h2><p>Pit depth 6 in · Pump A lead · B standby · ran 14 times today</p></div><span class="loc"><i></i>On site</span></div>
<div class="pitrow">{ring()}<div class="pk"><div><span>Pump starts</span><b>8 in</b></div><div><span>High-water line</span><b style="color:#ffb340">14 in</b></div><div><span>High-water float</span><b style="color:#30d158">Clear</b></div><div><span>Runs today</span><b>A 14 · B 0</b></div></div></div></div>
<div class="body"><div class="seg"><span class="on">Storm</span><span>Weekly test</span><span>Swap lead</span><span>Cold snap</span></div>
<div class="card"><div class="gh">Pumps <span>swaps lead every Monday</span></div><div class="pumps"><div class="pu"><b><i></i>Pump A<em class="tag">LEAD</em></b><span>Last run 7 min ago · 38 s</span></div><div class="pu sb2"><b><i></i>Pump B<em class="tag">STANDBY</em></b><span>Weekly test passed Sun</span></div></div>
<div class="cap">Never starts both pumps at once — the second waits its turn.</div><div class="cap">If the controller is ever off, both pumps still run on their own floats.</div></div>
<div class="card amb"><small>Pump health</small><span class="am" style="font-size:7.5px;margin-top:2px">Pump A emptied the pit slower than usual — plan a replacement.</span></div>
<div class="card"><div class="gh">Pit level · last 24 h <span>storm passed 3 AM</span></div><div class="spark">{''.join(f'<i style="height:{x}%"></i>' for x in [22,24,23,26,30,38,52,66,74,70,58,46,38,32,28,26,25,24,24,23,22,22,21,22])}</div><div class="axis"><span>6 PM</span><span>Midnight</span><span>6 AM</span><span>Now</span></div></div>
<div class="card"><div class="gh">Backup <span>if the power goes out</span></div><div class="kv"><div><span>Inverter hook-up</span><b style="color:#30d158">Ready</b></div><div><span>Siren in the house</span><b>Armed</b></div><div><span>Internet</span><b>Not needed for pump rules</b></div></div></div></div></div>
<div class="wr body"><div class="card"><div class="gh">Power Hub <span>5 labelled outlets</span></div>{tiles()}</div>
<div class="two"><div class="card"><small>Leak</small><div class="dry">✓</div><b>Dry · Dry</b><span class="ok">Water heater · Washer</span></div><div class="card"><small>Heat tape</small><b>Off</b><span>On below 35 °F crawlspace</span></div></div>
<div class="card"><div class="gh">Temperatures <span>example readings</span></div><div class="temps"><div><b>58<u>°F</u></b><span>Basement</span></div><div><b>41<u>°F</u></b><span>Crawlspace</span></div><div><b>22<u>°F</u></b><span>Outdoor</span></div></div></div>
<div class="card alerts"><div class="gh">Alerts <span>push · text · email · alarm</span></div><div>✓ Weekly pump test — both OK<i>push</i></div><div>◐ Slow pump-down · Pump A<i>push · email</i></div><div>○ High water · leak · freezing pipes<i>armed</i></div></div>
<div class="card"><div class="gh">Sensors <span>8 online</span></div><div class="sens"><div><i></i>Pit level<b>6 in</b></div><div><i></i>High-water float<b>Clear</b></div><div><i></i>Leak · water heater<b>Dry</b></div><div><i></i>Leak · washer<b>Dry</b></div><div><i></i>Basement<b>58 °F</b></div><div><i></i>Water heater area<b>64 °F</b></div></div></div>
<div class="card"><div class="gh">Coming up <span>automatic</span></div><div class="kv"><div><span>Weekly pump test</span><b>Sun 10 AM</b></div><div><span>Lead swaps to Pump B</span><b>Mon</b></div><div><span>Heat tape</span><b>On below 35 °F</b></div></div></div>
<div class="chip">⌂ Home Assistant pre-installed · Ask Alexa how the sump is doing</div></div></div></div>'''
LOCK='<div class="lock"><img src="assets/bgp-mark-white.svg"><div><b>Basement<br><span>Guard Pro</span></b><small>CONCEPT MARK</small></div></div>'
CF='<span class="cf">BROUGHT TO YOU BY <img src="assets/control-freak-corporate-wordmark-{}.svg" alt="Control Freak"></span>'
calls=[('L','2.75in','01','Two pumps take turns','Plug in the two pumps you already own. The lead pump swaps weekly so both wear evenly, and the two never start at the exact same moment.'),
('L','4.75in','02','Second pump steps in','If torrential rain causes the water to keep rising, the second pump is brought in automatically after a brief stagger — and you get a reassuring note.'),
('L','6.75in','03','See the water level','Know exact pit depth in inches and how fast it’s rising on a live ring gauge, moving far beyond simplistic “alarm / no alarm” binary switches.'),
('R','2.75in','04','Pumps work if controller doesn’t','Pump outlets stay continuously powered even if the controller is off, and each pump keeps its own float switch. Your basement is never worse off than with plain pumps.'),
('R','4.75in','05','Pump check-up','Spots a slow pump-down or a pump that didn’t empty the pit before you face a crisis. With automated weekly self-tests, you replace a tired pump on your own schedule.'),
('R','6.75in','06','Leak and freeze watch','Monitors the perimeter with water heater and washer leak sensors, high-water float backups, and temperature probes that automatically trigger plug-in heat tape.')]
callhtml=''.join(f'<div class="call {s}" style="top:{t};{"left" if s=="L" else "right"}:.45in"><span class="n">{n}</span><b>{b}</b>{x}</div>' for s,t,n,b,x in calls)
front=f'''<div class="pg front"><div class="bg"></div><span class="cc" style="top:1.8in;right:.5in;z-index:3">Concept photo</span>
<div class="head"><div><div class="live">VOICE &amp; TAP CONTROL · AWAY ALERTS · NO SUBSCRIPTION</div><h1>Put the <em>Control Freak</em><br>on your basement.</h1><p>Two pumps, one watchful hub. Basement Guard Pro keeps an eye on the pit, the pipes and the floor — so you can stop listening for the pump every time it rains.</p></div>{LOCK}</div>
<div class="stage">{phone('dark','7.45in')}</div>{callhtml}
<div class="bot"><span>BASEMENT GUARD PRO · {CF.format('white')}</span><span class="cc" style="position:static">Concept · demo UI · example readings</span></div></div>'''
light=f'''<div class="pg lightpg"><div class="bgl"></div>
<div class="lh"><div class="live">WHY IT MATTERS · 01 · EQUALIZED WEAR</div><h1>Two pumps that actually work as a team.</h1><p>Most homes with dual pumps have a primary unit doing all the heavy lifting while a backup pump sits idle for years — often failing the single time it is called upon. Basement Guard Pro manages your existing equipment with equalized wear. It alternates duty weekly and staggers starts so both pumps never kick on at the same instant. If the lead pump falls behind heavy storm inflow, the second pump smoothly engages to double capacity. Each pump keeps its own factory float.</p></div>
<div class="duo"><div class="ph1">{phone('light','6.55in')}</div><div class="ph2">{phone('dark','6.55in')}</div></div>
<div class="bot"><span>BASEMENT GUARD PRO · CONCEPT · DEMO UI NOT FINAL</span><span class="cc" style="position:static">Concept · demo UI · light + dark</span></div></div>'''
duopg=f'''<div class="pg duopg"><div class="bg"></div>
<div class="head"><div><div class="live">WHY IT MATTERS · 02 · LOCAL-FIRST · CLOUD-FREE FOUNDATION</div><h1>Reliability when internet or power fails.</h1><p>Real storm weather knocks out connectivity and utility power. A basement system that relies on a remote cloud server to make switching decisions is a liability. All logic, pump rotation, high-water thresholds and the indoor siren run locally on the box in your basement. If the hub is unplugged, your pumps run directly on their own floats. When you’re away, status reaches your phone over secure networking — with no monthly fees.</p></div>{LOCK}</div>
<div class="fstage">{wide()}</div>
<div class="fl"><div><b>Lit when it’s working</b>Safety-blue tiles for outlets that are on, slate for standby, muted for off.</div><div><b>Amber means “keep an eye on”</b>Never a siren for something you can plan for.</div><div><b>Runs in the basement</b>Pump rules and the siren keep working when the internet doesn’t.</div></div>
<div class="bot"><span>BASEMENT GUARD PRO · CONCEPT · DEVICE MOCK, NOT A SHIPPING PRODUCT</span><span class="cc" style="position:static">Concept · foldable layout · dark mode</span></div></div>'''
haph=phone('light','4.9in')
hapg=f'''<div class="pg hapg"><div class="hah"><div><div class="live">UNIFIED ECOSYSTEM · HOME ASSISTANT ON YOUR HOME NETWORK</div><h1>How many apps do you open<br>to run your home?</h1><p>Basement Guard Pro ships with Home Assistant and the Control Freak integration already set up, so your sump, leak sensors and the rest of your smart home meet in one place. Connect the devices you already own and simplify to a single app.</p></div><img src="assets/bgp-mark-slate.svg" style="width:.75in"></div>
<div class="tab"><div class="s">
<div class="col"><h6>⌂ Home</h6><div class="gt"><b>Good evening, James</b><span>Away · weekend at the lake</span></div><div class="gt bl"><span>Sump pit</span><div class="big">6 in</div><span>Pump A lead · B standby · both healthy</span></div><div class="voice"><b>“Alexa, how’s the sump?”</b><span>“The pit is at 6 inches and both pumps are healthy.”</span></div></div>
<div class="col"><h6>◆ Basement</h6><div class="gt"><b>Leak · Water heater</b><span style="color:#1a9e45;opacity:1">Dry</span></div><div class="gt"><b>Leak · Washer</b><span style="color:#1a9e45;opacity:1">Dry</span></div><div class="gt"><b>Crawlspace 41 °F</b><span>Heat tape off · on below 35 °F</span></div><div class="gt am"><b>Pump A check-up</b><span>Slower pump-down — plan a replacement</span></div></div>
<div class="col"><h6>✦ Home</h6><div class="gt"><b>Front door</b><span>Locked</span></div><div class="gt"><b>Thermostat</b><span>Away · 62 °F</span></div><div class="gt"><b>Dehumidifier</b><span>On schedule · 48% RH</span></div><div class="gt"><b>Lights</b><span>Away mode · off</span></div></div></div></div>
<div class="hph">{haph}</div>
<div class="story"><h3>When you’re away and the forecast turns…</h3><span class="ch">Storm mode · 1 storm → 4 things handled</span><div class="g"><div><b>Pumps take turns</b>The lead pump works the storm; the second waits its turn and only steps in if it’s needed.</div><div><b>You get a note</b>Push, text or email wherever you are — the siren at home sounds even if the internet is down.</div><div><b>Ask, don’t open</b>“Alexa, how’s the sump?” through Home Assistant — no extra vendor app.</div><div><b>Morning summary</b>“Pit at 6 in · Pump A ran 14 times · both pumps healthy.”</div></div></div>
<div class="bot"><span>HA ON YOUR HOME NETWORK · NEVER CLOUD HA · VOICE VIA HA BRIDGES</span><span class="cc" style="position:static">Concept · example HA dashboard · device mock</span></div></div>'''
bars=lambda v,c='#3d8bff':''.join(f'<i style="height:{x}%;background:{c}"></i>' for x in v)
back=f'''<div class="pg pg2"><div class="live">BASEMENT GUARD PRO · WHAT IT DOES</div>
<div class="open"><div><h1>Stop listening for the pump.</h1><p>Plug the two pumps you already own into the Power Hub, drop in the level sensor, scan the QR code. <b>No rewiring.</b> From then on the pumps take turns, the pit level is a number you can see, and leaks and cold pipes get noticed early — whether you’re upstairs or a state away.</p>
<p style="margin-top:8px">Built for homeowners with a basement sump, second-home and rental owners who can’t pop downstairs, and Home Assistant users who’d rather not build it by hand. Water and freezing claims average <b>$15,400</b> (Insurance Information Institute) — a little attention goes a long way.</p></div>
<div class="kit"><h4>IN THE RECOMMENDED PACKAGE</h4><ul><li>Controller with Home Assistant + Control Freak integration</li><li>Power Hub — labelled outlets for two sump pumps, heat tape, a dehumidifier and a spare</li><li>Pit level sensor (depth + rate of rise)</li><li>High-water float (second check)</li><li>Leak sensors — water heater + washer</li><li>Temperature probes — basement, crawlspace, water heater area, outdoor</li><li>Siren for inside the house</li><li>Backup inverter hook-up (for one you already own)</li><li>Keyed, colour-coded cables</li></ul><div class="nb">Your sump pumps aren’t in the box — keep the ones you have. Every sensor is its own cart line; the full package costs less than buying lines separately. Optional: UPS, partner 12 V battery backup pump.</div></div></div>
<div class="live">TRY IT IN THE SITE DEMO</div>
<div class="scenes">
<div class="sc"><div class="in"><h4>SIMULATE A STORM</h4><div class="big">Level rises, Pump A runs</div><div class="bar">{bars([20,28,38,50,62,70,64,52,40,30,22,18])}</div><div class="note b">Second pump stepped in · after a short delay</div><p>Still rising? Pump B joins in — never at the same moment — and the level falls back.</p></div></div>
<div class="sc"><div class="in"><h4>STAGGER · WEEKLY TEST</h4><div class="big">A → wait → B</div><div class="wt"><div class="ln"><span>A</span><div class="tr"><em style="left:4%;width:30%"></em></div><b>✓ 38 s</b></div><div class="ln"><span>B</span><div class="tr"><em class="b2" style="left:48%;width:30%"></em></div><b>✓ 41 s</b></div><div class="ax"><span>0 s</span><span>wait</span><span>90 s</span></div></div><div class="note b">Both pumps OK · lead swaps Monday</div><p>Each pump runs briefly in turn and reports back. Swap the lead with one tap.</p></div></div>
<div class="sc"><div class="in"><h4>COLD SNAP</h4><div class="big">Crawlspace 41 → 34 °F</div><div class="bar">{bars([80,74,68,60,54,47,40,34,30,28,27,27],'#8fa3b8')}</div><div class="note">Heat tape switched on · below 35 °F</div><p>The plug-in heat tape comes on by itself and you see why.</p></div></div></div>
<div class="diffs"><div><b>Pump check-up</b>Spots a slow pump-down or a pump that didn’t empty the pit, so you replace on your schedule.</div><div><b>Alerts that reach you</b>Push, text, email and alarm — including away (cloud via Tailscale) — plus a siren in the house.</div><div><b>Keeps working offline</b>Pump rules and the siren run on the box in the basement. No subscription.</div></div>
<div class="what"><div><div class="live" style="color:#c0392b">DEMO · TAP “WHAT IF”</div><div class="alarm"><small>EXAMPLE ALERT</small>Water by the water heater · siren on · push, text and email sent</div><p style="font:400 8.4px/1.45 Inter;color:#5a6876;margin-top:6px">Red appears only when you tap a “what if” in the demo. Everyday state is calm blue and slate.</p></div>
<div class="cta"><h3>Join Wave 1 Pro early</h3><p>We’re looking for homeowners to test Basement Guard Pro in their own basements before launch — test early kits with your existing pumps. No credit card required.</p><span>Join the interest list →</span></div></div>
<div class="bot" style="left:.5in;right:.5in"><span>BASEMENT GUARD PRO · {CF.format('navy')}</span><span class="cc" style="position:static;color:#b86e00">Concept · demo · example readings</span></div></div>'''
css=open('style.css').read()+open('ha.css').read()
html=f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet"><style>{css}</style></head><body>{front}{light}{duopg}{hapg}{back}<script>document.addEventListener("click",e=>{{const t=e.target.closest(".tile");if(!t)return;t.classList.toggle("on");t.setAttribute("aria-pressed",t.classList.contains("on"))}})</script></body></html>'
open('brochure.html','w').write(html)
# Chrome shrinks the combined doc; print each page alone then join (pdfunite)
head=html[:html.index('<body>')+6]
parts=[]
for i,pg in enumerate([front,light,duopg,hapg,back]):
    fn=f'_p{i}.html';open(fn,'w').write(head+pg+'</body></html>')
    subprocess.run(['/usr/bin/google-chrome','--headless','--disable-gpu','--no-pdf-header-footer','--virtual-time-budget=6000',f'--print-to-pdf=_p{i}.pdf','file://'+os.path.abspath(fn)],capture_output=True)
    subprocess.run(['pdfseparate','-f','1','-l','1',f'_p{i}.pdf',f'_q{i}.pdf']);parts.append(f'_q{i}.pdf')
subprocess.run(['pdfunite',*parts,'brochure.pdf']);subprocess.run('rm -f _p*.html _p*.pdf _q*.pdf',shell=True)
names=['front','light-mode','duo','ha-home','back']
subprocess.run('rm -f pg-*.png; pdftoppm -png -r 110 brochure.pdf pg',shell=True)
for i,n in enumerate(names,1): os.replace(f'pg-{i}.png',f'{n}.png')
ims=[Image.open(f+'.png').convert('RGB') for f in names]
c=Image.new('RGB',(ims[0].width*5+80,ims[0].height),'#888')
for i,im in enumerate(ims): c.paste(im,(i*(im.width+20),0))
c.save('spread.png')
ims[0].save('brochure-review.pdf',save_all=True,append_images=ims[1:],resolution=110)
# Page 5 "How it all connects" (owner 2026-10-26): render it and splice it in before the back page.
import os as _os, subprocess as _sp
_sp.run(['python3', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../_infographic/build_infographic.py'), 'C03'], check=True)
