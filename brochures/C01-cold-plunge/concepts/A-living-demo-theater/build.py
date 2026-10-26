# C01 Cold Plunge Control Pro — Concept A "Living Demo Theater". Rebuild: python3 build.py
# Copy source: briefs/C01-cold-plunge-PUBLIC_BRIEF.md (platform tip 61ff993 + Writer tip d0921fb chip restore).
# Chiller = "switches your chiller's power" only. No prices. PCB corporate wordmark only. No product mark (none exists) — name typography.
import os,subprocess
from PIL import Image
sv=lambda p:f'<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">{p}</svg>'
I={'chl':sv('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M12 7v10M8 9l8 6M16 9l-8 6" stroke="#0007" stroke-width="1.4"/>'),
'flow':sv('<path d="M3 9h12l-3-3M21 15H9l3 3" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>'),
'oz':sv('<circle cx="8" cy="10" r="3"/><circle cx="15" cy="8" r="2.2"/><circle cx="14" cy="15" r="3.4"/>'),
'filt':sv('<path d="M4 4h16l-6 8v7l-4 2v-9z"/>'),
'hl':sv('<path d="M3 13h4l2-5 3 9 2-6 2 2h5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>'),
'air':sv('<path d="M12 2v20M4 6l16 12M20 6L4 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>')}
tl=[('Chiller','chl','Running · flow OK','on'),('Flow','flow','OK · tap “what if”','on'),('Ozone / UV','oz','On with pump','on'),
('Filter · Pro','filt','Clean the filter soon','am'),('Chiller health · Pro','hl','Cooling normally','on'),('Air · winter','air','30 °F · pump on','')]
def tiles(): return '<div class="tiles">'+''.join(f'<button class="tile {k}"><span class="gl">{I[i]}</span><b>{n}</b><em>{c}</em></button>' for n,i,c,k in tl)+'</div>'
RING='''<div class="ring"><svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="34" fill="none" stroke="#8884" stroke-width="7"/><circle cx="40" cy="40" r="34" fill="none" stroke="url(#g)" stroke-width="7" stroke-linecap="round" stroke-dasharray="213.6" stroke-dashoffset="8" transform="rotate(-90 40 40)"/><defs><linearGradient id="g"><stop offset="0" stop-color="#9fd0ff"/><stop offset="1" stop-color="#1f5f9e"/></linearGradient></defs></svg><div class="v"><b>39<u>°F</u></b><span>target 39 °F</span></div></div>'''
TOP=f'''<div class="top"><div class="sb"><b>6:12</b><span>●●● ◔ ▮</span></div>
<div class="tk"><div><small>Plunge · back deck · demo</small><h2>39 °F · ready at 6:30 · flow OK</h2><p>Example readings</p></div><span class="loc"><i></i>Local</span></div>
<div class="rrow">{RING}<div class="kv2" style="flex:1"><div><span>Ready by</span><b>6:30</b></div><div><span>Starts cooling at</span><b>4:50 (example)</b></div><div><span>Water</span><b>39 °F</b></div><div><span>Air</span><b>30 °F</b></div></div></div></div>'''
HUB='<div class="card"><div class="gh">Plunge <span>example readings</span></div>'+tiles()+'<div class="cap">Ozone / UV: only while water is moving</div><div class="cap">Chiller only runs while flow is OK</div></div>'
AL='<div class="card alerts"><div class="gh">Alerts <span>push · text · email · alarm</span></div><div>○ No flow<i>armed</i></div><div>○ Water too warm<i>armed</i></div><div>● Filter<i>clean soon</i></div><div>○ Cold night<i>armed</i></div></div>'
CHIP='<div class="chip alexa">🎙 Ask Alexa if the plunge is ready</div><div class="chip" style="margin-top:4px">Multi-platform integration built in</div>'
MODES='<div class="seg"><span class="on">Plunge</span><span>Warm soak · Pro</span><span>Winter</span></div>'
SCHED='<div class="card"><div class="gh">Coming up <span>example</span></div><div class="kv"><div><span>Starts cooling</span><b>4:50</b></div><div><span>Ready by</span><b>6:30</b></div><div><span>Filtration cycle</span><b>scheduled</b></div><div><span>Heater outlet · Pro</span><b>off · plunge</b></div></div></div>'
def phone(m,h): return f'<div class="phone {m}" style="height:{h}"><div class="island"></div><div class="scr">{TOP}<div class="body">{MODES}{HUB}{AL}{SCHED}{CHIP}</div></div></div>'
def wide():
    return f'''<div class="fold"><div class="cam"></div><div class="scr dark"><div class="wl">{TOP}<div class="body">
<div class="card"><div class="gh">Ready by 6:30 <span>example timeline</span></div><div class="tl"><em style="left:0;width:100%"></em></div><div class="axis"><span>4:50 starts cooling</span><span>6:30 at target</span></div></div>{AL}</div></div>
<div class="wr body">{HUB}{CHIP}</div></div></div>'''
NAME='<div class="lock"><div><b>Cold Plunge<br><span>Control Pro</span></b><small>WORKING NAME · CONCEPT</small></div></div>'
CF='<span class="cf">BROUGHT TO YOU BY <img src="assets/control-freak-corporate-wordmark-{}.svg" alt="Control Freak"></span>'
calls=[('L','2.75in','01','Ready when you are','Set “ready by 6:30”; the controller starts cooling early so the water is at your target when you step in.'),
('L','4.75in','02','Holds your temperature','A water probe keeps the plunge at the target you set, all day.'),
('L','6.75in','03','Works with the chiller you have','Runs a 120 V plug-in chiller from the Power Hub; keep your chiller, and swap in a new one later without changing the rest.'),
('R','2.75in','04','Chiller only runs with water flowing','A flow switch on the pipe stops the chiller running dry.'),
('R','4.75in','05','Clean water on a schedule','Ozone and UV run only while the pump moves water; filtration cycles keep it clear without the pump running all day.'),
('R','6.75in','06','Alerts that reach you','No flow, water too warm, filter, cold night: push, text, email and alarm, including away from home.')]
callhtml=''.join(f'<div class="call {s}" style="top:{t};{"left" if s=="L" else "right"}:.45in"><span class="n">{n}</span><b>{b}</b>{x}</div>' for s,t,n,b,x in calls)
SUB='Set “ready by 6:30.” Cold Plunge Control Pro works back from the water temperature, starts your chiller early, and keeps the water clean and flowing — so you just step in.'
front=f'''<div class="pg front"><div class="bg"></div>
<div class="head"><div><div class="live">▶ WATCH THE DEMO · ON THE SITE</div><h1>Your plunge, <em>ready</em><br>when you are.</h1><p>{SUB}</p></div>{NAME}</div>
<div class="stage">{phone('dark','7.45in')}</div>{callhtml}
<div class="bot"><span>COLD PLUNGE CONTROL PRO · {CF.format('white')}</span><span class="cc" style="position:static">Concept · demo UI · example readings</span></div></div>'''
light=f'''<div class="pg lightpg"><div class="bgl"></div>
<div class="lh"><div class="live">SAME DEMO · LIGHT MODE</div><h1>Sit back — the plunge is <em>ready</em> when you are.</h1><p>{SUB}</p></div>
<div class="duo"><div class="ph1">{phone('light','6.55in')}</div><div class="ph2">{phone('dark','6.55in')}</div></div>
<div class="bot"><span>COLD PLUNGE CONTROL PRO · CONCEPT · DEMO UI NOT FINAL</span><span class="cc" style="position:static">Concept · demo · example readings</span></div></div>'''
duopg=f'''<div class="pg duopg"><div class="bg"></div>
<div class="head"><div><div class="live">CONCEPT · FOLDABLE DEVICE MOCK · DEMO</div><h1>Ready when you are.</h1><p>Set “ready by 6:30”; the controller starts cooling early so the water is at your target when you step in.</p></div>{NAME}</div>
<div class="fstage">{wide()}</div>
<div class="fl"><div><b>Chiller only runs with water flowing</b>A flow switch on the pipe stops the chiller running dry.</div><div><b>Filter reminder (Pro)</b>Tells you to clean the filter before flow drops.</div><div><b>Keeps working when the internet doesn’t</b>Schedules run on the controller. Ethernet, Wi-Fi, and its own Wi-Fi network.</div></div>
<div class="bot"><span>COLD PLUNGE CONTROL PRO · CONCEPT · DEVICE MOCK, NOT A SHIPPING PRODUCT</span><span class="cc" style="position:static">Concept · foldable · example readings</span></div></div>'''
hapg=f'''<div class="pg hapg"><div class="hah"><div><div class="live">HOME ASSISTANT PRE-INSTALLED · ON YOUR HOME NETWORK</div><h1>How many apps do you have to open<br>to control your smart products?</h1><p>Cold Plunge Control Pro ships with Home Assistant and the Control Freak integration already set up, so your plunge and the rest of your smart home meet in one place. Connect the apps and devices you already own and simplify to a single app. Multi-platform integration built in: ask Alexa what the status is, tell Google to adjust the temperature, and receive automated voice alerts to let you know when something is out of balance.</p></div></div>
<div class="tab"><div class="s">
<div class="col"><h6>⌂ Home</h6><div class="gt"><b>Good morning, James</b><span>Example dashboard</span></div><div class="gt bl"><span>Plunge · water</span><div class="big">39 °F</div><span>Ready at 6:30 · flow OK</span></div><div class="voice"><b>“Alexa, is the plunge ready?”</b><span> Example voice reply via Home Assistant: 39 °F, ready at 6:30.</span></div></div>
<div class="col"><h6>◆ Plunge</h6><div class="gt"><b>Chiller · running</b><span>Power switched by the Power Hub</span></div><div class="gt"><b>Flow · OK</b><span>Ozone / UV on with pump</span></div><div class="gt am"><b>Filter · Pro</b><span>Clean the filter soon</span></div><div class="gt"><b>Air · 30 °F</b><span>Winter mode · pump on</span></div></div>
<div class="col"><h6>✦ Your home · via Home Assistant</h6><div class="gt"><b>Deck lights</b><span>Owner device · example</span></div><div class="gt"><b>Thermostat</b><span>Owner device · example</span></div><div class="gt"><b>Alerts</b><span>Push · text · email · alarm</span></div></div></div></div>
<div class="hph">{phone('light','4.9in')}</div>
<div class="story"><h3>A cold night, handled.</h3><span class="ch">Example · winter mode</span><div class="g"><div><b>Winter mode</b>The pump runs when the air nears freezing, protecting outdoor tubs and pipes.</div><div><b>Keeps working</b>Schedules run on the controller.</div><div><b>Alerts that reach you</b>Push, text, email and alarm, including away from home.</div><div><b>Local</b>Home Assistant stays on your home network — never cloud Home Assistant.</div></div></div>
<div class="bot"><span>HA ON YOUR HOME NETWORK · VOICE: ALEXA · GOOGLE · SIRI</span><span class="cc" style="position:static">Concept · example HA dashboard</span></div></div>'''
bars=lambda v,c='#5fb4ff':''.join(f'<i style="height:{x}%;background:{c}"></i>' for x in v)
back=f'''<div class="pg pg2"><div class="live">COLD PLUNGE CONTROL PRO · WHAT IT DOES</div>
<div class="open"><div><h1>Your plunge, ready when you are.</h1><ul class="prob"><li>Most plunges run on the chiller’s own basic thermostat or a Wi-Fi plug. Schedules are unreliable — owners report water still a few degrees warm at the set time.</li><li>A clogged filter slows flow to a trickle and the chiller shuts off — or runs dry and wears out.</li><li>Closed apps go offline after a router change, and a chiller is stranded if its maker disappears.</li></ul>
<p style="margin-top:8px"><b>Self-install:</b> plug the chiller, pump, ozone and UV into the Power Hub, drop in the probes, fit the flow switch on the pipe (Pro includes unions — no pipe cutting), scan the QR code. Price to be announced.</p></div>
<div class="kit"><h4>PRO · BUILDING NOW <em class="cbadge" style="color:#b86e00;border-color:#b86e00">CONCEPT</em></h4><ul><li>Controller with Home Assistant pre-installed and the Control Freak integration</li><li>Power Hub — labelled outlets for chiller, pump, ozone and a spare</li><li>Water and air temperature probes</li><li>Flow switch</li><li>Keyed, colour-coded cables</li><li>Chiller-outlet probe (chiller health)</li><li>Filter pressure sender (filter reminder)</li><li>Plumbing unions — fits without cutting pipes</li><li>Heater outlet for hot/cold tubs</li></ul><div class="nb">Your tub, chiller, pump, ozone and UV aren’t in the box — you keep the ones you have. Starter: coming later.</div></div></div>
<div class="live">TRY IT IN THE SITE DEMO</div>
<div class="scenes scenes4">
<div class="sc"><div class="in"><h4>SET READY-BY</h4><div class="big">Ready by 6:30</div><div class="bar">{bars([95,88,78,66,55,46,40,38,38,38])}</div><div class="note b">Starts cooling at 4:50 (example)</div></div></div>
<div class="sc"><div class="in"><h4>CLOG THE FILTER · PRO</h4><div class="big">Clean the filter soon</div><div class="bar">{bars([30,34,40,50,62,76,88,96],'#ffb340')}</div><div class="note">No flow → chiller stops, alert</div></div></div>
<div class="sc"><div class="in"><h4>COLD NIGHT</h4><div class="big">Air 30 °F · pump on</div><div class="bar">{bars([70,62,55,48,40,34,30,30])}</div><div class="note b">Winter mode runs the pump</div></div></div>
<div class="sc"><div class="in"><h4>HOT / COLD · PRO</h4><div class="big">Warm soak → plunge</div><div class="bar">{bars([40,55,70,85,85,70,55,40],'#ffb340')}</div><div class="note b">Heater outlet on, then back to plunge</div></div></div></div>
<div class="diffs"><div><b>Works with the chiller you have</b>Switches your chiller’s power from the Power Hub — keep your chiller.</div><div><b>Chiller health (Pro)</b>A probe on the chiller outlet shows it’s cooling, and flags early if it slows down.</div><div><b>Keeps working when the internet doesn’t</b>Schedules run on the controller.</div></div>
<div class="what"><div><div class="live" style="color:#d9493d">DEMO · TAP “WHAT IF”</div><div class="alarm"><small>EXAMPLE ALERT</small>No flow · chiller stops · alert sent</div><p style="font:400 8.4px/1.45 Inter;color:#5a6876;margin-top:6px">Concept demo · example readings.</p></div>
<div class="cta"><h3>Join the beta</h3><p>We’re looking for cold plunge owners to test Cold Plunge Control Pro at home before launch.</p><span>Join the interest list →</span></div></div>
<div class="bot" style="left:.5in;right:.5in"><span>COLD PLUNGE CONTROL PRO · {CF.format('navy')}</span><span class="cc" style="position:static;color:#b86e00">Concept · demo · example readings</span></div></div>'''
css=open('style.css').read()+open('ha.css').read()
html=f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,600&display=swap" rel="stylesheet"><style>{css}</style></head><body>{front}{light}{duopg}{hapg}{back}</body></html>'
open('brochure.html','w').write(html)
head=html[:html.index('<body>')+6];parts=[]
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
c.save('spread.png');ims[0].save('brochure-review.pdf',save_all=True,append_images=ims[1:],resolution=110)
# Page 5 "How it all connects" (owner 2026-10-26): render it and splice it in before the back page.
import os as _os, subprocess as _sp
_sp.run(['python3', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../_infographic/build_infographic.py'), 'C01'], check=True)
