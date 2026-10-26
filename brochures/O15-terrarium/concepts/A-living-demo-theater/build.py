# O15 Terrarium Control Pro — Concept A "Living Demo Theater". Rebuild: python3 build.py
# Copy source: briefs/O15-terrarium-PUBLIC_BRIEF.md (Eng-cleared e84b978). No CF humidity (HA-added owner sensor reading allowed, Eng), Hub on/off only.
import os,subprocess
from PIL import Image
sv=lambda p,f='currentColor':f'<svg viewBox="0 0 24 24" width="14" height="14" fill="{f}">{p}</svg>'
I={'mat':sv('<rect x="3" y="8" width="18" height="8" rx="2"/><path d="M6 10v4M10 10v4M14 10v4M18 10v4" stroke="#0006" stroke-width="1.4"/>'),
'cer':sv('<path d="M9 3h6v4H9z"/><circle cx="12" cy="13" r="6"/><circle cx="12" cy="13" r="2.5" fill="#0005"/>'),
'bask':sv('<path d="M7 4h10l-2 6H9z"/><circle cx="12" cy="14" r="3"/><path d="M12 18v3M7 17l-2 2M17 17l2 2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'),
'uvb':sv('<rect x="3" y="9" width="18" height="5" rx="2.5"/><path d="M7 17l-1 3M12 17v3M17 17l1 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'),
'day':sv('<circle cx="12" cy="12" r="4.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'),
'mist':sv('<path d="M8 3h8v5H8z"/><path d="M11 8h2v3h-2z"/><circle cx="7" cy="15" r="1.3"/><circle cx="12" cy="17" r="1.3"/><circle cx="17" cy="15" r="1.3"/><circle cx="9.5" cy="20" r="1.1"/><circle cx="14.5" cy="20" r="1.1"/>'),
'fan':sv('<circle cx="12" cy="12" r="2"/><path d="M12 10c-1-4 1-7 4-6-1 3-2 5-4 6zM14 12c4-1 7 1 6 4-3-1-5-2-6-4zM12 14c1 4-1 7-4 6 1-3 2-5 4-6zM10 12c-4 1-7-1-6-4 3 1 5 2 6 4z"/>'),
'spare':sv('<rect x="4" y="4" width="16" height="16" rx="4" opacity=".5"/><path d="M9 9v3M15 9v3M10 16h4" stroke="#0008" stroke-width="2"/>')}
outlets=[('Heat mat','mat','On · holds 92 °F hot side','on'),('Ceramic emitter','cer','Off · night heat','' ),('Basking lamp','bask','On · basking 105 °F','on'),('UVB','uvb','On · day cycle','on'),
('Day light','day','On · until 20:00','on'),('Mister','mist','Next run 18:00',''),('Fan','fan','Off',''),('Spare','spare','Unused','')]
def tiles(): return '<div class="tiles">'+''.join(f'<button class="tile {k}" aria-pressed="{"true" if k=="on" else "false"}"><span class="gl">{I[ic]}</span><b>{n}</b><em>{c}</em></button>' for n,ic,c,k in outlets)+'</div>'
def grad(): return '''<div class="grad"><span class="bar"></span><div class="pts"><div><b>78<u>°F</u></b><span>Cool side</span><em>set 78 °F</em></div><div><b>92<u>°F</u></b><span>Hot side</span><em>set 92 °F</em></div><div><b>105<u>°F</u></b><span>Basking</span><em>set 105 °F</em></div></div></div>'''
TOP='''<div class="top"><div class="sb"><b>9:41</b><span>●●● ◔ ▮</span></div>
<div class="tk"><div><small>Enclosure 1 · living room shelf</small><h2>Two enclosures on schedule</h2><p>Heat holding · lights on a natural day · next mist 18:00</p></div><span class="loc"><i></i>Local</span></div>
'''+grad()+'''<div class="chips"><span class="w">☀ Day · 14:00</span><span>💧 Next mist 18:00</span><span>Reservoir OK <em class="cbadge">CONCEPT</em></span></div></div>'''
ENC='<div class="card"><div class="gh">Enclosures <span>example readings · 2 of up to 3</span></div><div class="temps"><div><b>92<u>°F</u></b><span>Enclosure 1 · hot</span></div><div><b>88<u>°F</u></b><span>Enclosure 2 · hot</span></div></div></div>'
CUT='<div class="card"><div class="gh">Over-temp cutoff <span>armed on every heat outlet</span></div><div class="cap">Too hot or a probe unplugged: heat turns off and you’re told.</div><div class="cap">Heat runs on the controller at home — a Wi-Fi drop changes nothing.</div></div>'
MODES='<div class="seg"><span class="on">Day</span><span>Night</span><span>Away</span><span>Door open <em class="cbadge">CONCEPT</em></span></div>'
HUB='<div class="card"><div class="gh">Power Hub <span>8 outlets · on/off</span></div>'+tiles()+'</div>'
AL='<div class="card alerts"><div class="gh">Alerts <span>push · text · email · alarm</span></div><div>✓ All probes reporting<i>4 of 4</i></div><div>○ Over / under temp · probe unplugged<i>armed</i></div><div>○ Outlet stuck on<i>armed</i></div><div>○ Reservoir empty <em class="cbadge">CONCEPT</em><i>armed</i></div></div>'
PROBES='<div class="card"><div class="gh">Probes <span>4 online</span></div><div class="sens"><div><i></i>Hot side<b>92 °F</b></div><div><i></i>Cool side<b>78 °F</b></div><div><i></i>Basking spot<b>105 °F</b></div><div><i></i>Enclosure 2<b>88 °F</b></div></div><div class="cap" style="margin-top:4px;opacity:.85">💧 Humidity 62% · via Home Assistant<br><em class="cbadge" style="white-space:nowrap">HA-added · owner Zigbee · Z-Wave · Wi‑Fi · ESP32</em></div></div>'
SCHED='<div class="card"><div class="gh">Coming up <span>automatic</span></div><div class="kv"><div><span>Mist · Enclosure 1</span><b>18:00</b></div><div><span>Lights to night</span><b>20:00</b></div><div><span>Seasonal ramp</span><b>−1 °F / week</b></div></div></div>'
CHIP='<div class="chip">⌂ Home Assistant pre-installed · voice control via Home Assistant</div>'
def phone(mode,h):
    return f'<div class="phone {mode}" style="height:{h}"><div class="island"></div><div class="scr">{TOP}<div class="body">{MODES}{CUT}{HUB}{ENC}{AL}{PROBES}{SCHED}{CHIP}</div></div></div>'
def wide():
    return f'''<div class="fold"><div class="cam"></div><div class="scr dark"><div class="wl">{TOP}<div class="body">{MODES}{CUT}
<div class="card"><div class="gh">Day / night · today <span>editable profile</span></div><div class="spark">{''.join(f'<i style="height:{x}%"></i>' for x in [30,30,30,30,30,30,45,70,85,92,96,98,100,100,98,95,90,80,60,40,30,30,30,30])}</div><div class="axis"><span>00:00</span><span>06:00 lights on</span><span>14:00 now</span><span>20:00 night</span></div></div>
{SCHED}</div></div>
<div class="wr body">{HUB}{ENC}{AL}{PROBES}{CHIP}</div></div></div>'''
LOCK='<div class="lock"><img src="assets/tcp-mark-white.svg"><div><b>Terrarium<br><span>Control Pro</span></b><small>CONCEPT MARK</small></div></div>'
CF='<span class="cf">BROUGHT TO YOU BY <img src="assets/control-freak-corporate-wordmark-{}.svg" alt="Control Freak"></span>'
calls=[('L','2.75in','01','One kit for 2–3 enclosures','8 switched outlets and 4 temperature probes, with a thermostat on any outlet — not one thermostat per enclosure.'),
('L','4.75in','02','Heat control stays home','The controller runs heat locally, so a Wi-Fi drop or a server outage changes nothing.'),
('L','6.75in','03','Over-temp cutoff + probe check','If a probe reads too hot, or is unplugged, its heat outlet turns off and you’re told.'),
('R','2.75in','04','Home Assistant, full control','Pre-installed with the Control Freak integration. Setpoints and outlets work from your dashboards.'),
('R','4.75in','05','Day/night + seasonal ramps','Lights and temperatures follow a natural day, with editable profiles to start from.'),
('R','6.75in','06','Misting on schedule','Timed misting from a switched outlet. Reservoir float and door pause are Concept.')]
callhtml=''.join(f'<div class="call {s}" style="top:{t};{"left" if s=="L" else "right"}:.45in"><span class="n">{n}</span><b>{b}</b>{x}</div>' for s,t,n,b,x in calls)
front=f'''<div class="pg front"><div class="bg"></div><span class="cc" style="top:1.8in;right:.5in;z-index:3">Concept photo</span>
<div class="head"><div><div class="live">▶ LIVE DEMO · TRY IT ON THE SITE</div><h1>Put the <em>Control Freak</em><br>on it.</h1><p>Sit back and enjoy your enclosures — the system keeps the heat, light and mist on schedule. Heat, light and misting for up to three enclosures. From one controller. No subscription.</p><div class="badges"><span>VOICE &amp; TAP</span><span>AWAY ALERTS</span><span>NO SUBSCRIPTION</span></div></div>{LOCK}</div>
<div class="stage">{phone('dark','7.45in')}</div>{callhtml}
<div class="bot"><span>TERRARIUM CONTROL PRO · {CF.format('white')}</span><span class="cc" style="position:static">Concept · demo UI · example readings</span></div></div>'''
light=f'''<div class="pg lightpg"><div class="bgl"></div>
<div class="lh"><div class="live">SAME APP · LIGHT MODE</div><h1>Calm, in <em>daylight.</em></h1><p>Glance at the shelf over coffee: cool side, hot side and basking spot against their setpoints, what the lights are doing, when the next mist runs — and every outlet on the Power Hub, on or off.</p></div>
<div class="duo"><div class="ph1">{phone('light','6.55in')}</div><div class="ph2">{phone('dark','6.55in')}</div></div>
<div class="bot"><span>TERRARIUM CONTROL PRO · CONCEPT · DEMO UI NOT FINAL</span><span class="cc" style="position:static">Concept · demo UI · light + dark</span></div></div>'''
duopg=f'''<div class="pg duopg"><div class="bg"></div>
<div class="head"><div><div class="live">CONCEPT · FOLDABLE DEVICE MOCK · DEMO</div><h1>The whole shelf, unfolded.</h1><p>The heat gradient and today’s day/night curve on one side. All eight outlets, the probes and alerts on the other. Tap a setpoint, switch to night or try an alert in the site demo.</p></div>{LOCK}</div>
<div class="fstage">{wide()}</div>
<div class="fl"><div><b>Aqua means on</b>Lit tiles for outlets that are on; muted for off. Every outlet is on/off.</div><div><b>Warm means daytime</b>Basking-light amber marks the day cycle — coral only for a warning.</div><div><b>Runs at home</b>Heat keeps being controlled when Wi-Fi or a cloud app hiccups.</div></div>
<div class="bot"><span>TERRARIUM CONTROL PRO · CONCEPT · DEVICE MOCK, NOT A SHIPPING PRODUCT</span><span class="cc" style="position:static">Concept · foldable layout · dark mode</span></div></div>'''
hapg=f'''<div class="pg hapg"><div class="hah"><div><div class="live">HOME ASSISTANT PRE-INSTALLED · ON YOUR HOME NETWORK</div><h1>How many apps do you open<br>to run your home?</h1><p>Terrarium Control Pro ships with Home Assistant and the Control Freak integration already set up, so your enclosures and the rest of your smart home meet in one place. Connect the devices you already own and simplify to a single app. Use the voice assistant you already have, via Home Assistant, to check status or adjust a setpoint. Home Assistant stays on your home network — never cloud Home Assistant.</p></div><img src="assets/tcp-mark-slate.svg" style="width:.75in"></div>
<div class="tab"><div class="s">
<div class="col"><h6>⌂ Home</h6><div class="gt"><b>Good evening, James</b><span>Away · back Sunday</span></div><div class="gt bl"><span>Enclosure 1 · basking</span><div class="big">105 °F</div><span>Hot 92 · Cool 78 · all at setpoint</span></div><div class="voice"><b>Voice via Home Assistant · “How are the enclosures?”</b><span>“Enclosure 1 and Enclosure 2 are at their setpoints. Next mist at six.”</span></div></div>
<div class="col"><h6>◆ Enclosures</h6><div class="gt"><b>Enclosure 2 · 88 °F</b><span>Heat mat on · day cycle</span></div><div class="gt"><b>Shelf has room for a third</b><span>Add a probe later</span></div><div class="gt"><b>Lights</b><span>Day · night at 20:00</span></div><div class="gt"><b>Mister</b><span>Next run 18:00</span></div></div>
<div class="col"><h6>✦ Home</h6><div class="gt"><b>Front door</b><span>Locked</span></div><div class="gt"><b>Thermostat</b><span>Away · 66 °F</span></div><div class="gt"><b>Living room lights</b><span>Away mode · off</span></div><div class="gt"><b>Alerts</b><span>Push · text · email · alarm</span></div></div></div></div>
<div class="hph">{phone('light','4.9in')}</div>
<div class="story"><h3>A weekend away from the shelf…</h3><span class="ch">2 enclosures → kept on schedule</span><div class="g"><div><b>Heat holds</b>Each heat outlet keeps its own setpoint on the controller — even if the home Wi-Fi drops.</div><div><b>A natural day</b>Lights come on, go to night values and come back, following your profile.</div><div><b>Mist on time</b>The mister outlet runs on its schedule, enclosure by enclosure.</div><div><b>You’re told</b>Too hot or a probe unplugged: heat turns off and an alert reaches you by push, text or email.</div></div></div>
<div class="bot"><span>HA ON YOUR HOME NETWORK · NEVER CLOUD HA · VOICE VIA HA</span><span class="cc" style="position:static">Concept · example HA dashboard · device mock</span></div></div>'''
bars=lambda v,c='#2fd3c4':''.join(f'<i style="height:{x}%;background:{c}"></i>' for x in v)
back=f'''<div class="pg pg2"><div class="live">TERRARIUM CONTROL PRO · WHAT IT DOES</div>
<div class="open"><div><h1>One controller for the whole shelf.</h1><p>Each heat source holding its own setpoint, lights on a natural day, and misting on time — for 1–3 enclosures, without stacking a separate thermostat per enclosure or juggling vendor apps.</p>
<p style="margin-top:8px"><b>Set up in minutes:</b> scan the QR code; keyed, colour-coded plugs only fit their port. Built on a controller we already ship — the same controller as Control Freak’s live pool product, not a one-off board. Profiles are editable starting points. Price to be announced.</p></div>
<div class="kit"><h4>IN THE PRO KIT</h4><ul><li>Controller with Home Assistant pre-installed + Control Freak integration</li><li>Power Hub — 8 switched outlets, on/off (heat mats, ceramic emitters, UVB, day lights, fans, mister)</li><li>4 temperature probes — hot side, cool side, basking spot, second enclosure</li><li>Door switch + mister reservoir float <em class="cbadge" style="color:#b86e00;border-color:#b86e00">CONCEPT</em></li></ul><div class="nb">Concept accessory: a separate dimming module for heat bulbs — the Power Hub and controller don’t dim. Later: temperature &amp; humidity sensor (with Modbus support), extra probes, a second Power Hub.</div></div></div>
<div class="live">TRY IT IN THE SITE DEMO</div>
<div class="scenes">
<div class="sc"><div class="in"><h4>DRAG A SETPOINT</h4><div class="big">Hot side 88 → 92 °F</div><div class="bar">{bars([30,36,44,52,60,68,74,79,82,84,85,85],'#ffb340')}</div><div class="note b">Heat mat on · easing to 92 °F</div><p>Set a new target on the gradient strip and the reading eases toward it.</p></div></div>
<div class="sc"><div class="in"><h4>DAY → NIGHT</h4><div class="big">Lights off · night values</div><div class="bar">{bars([96,98,100,100,96,90,70,45,30,30,30,30])}</div><div class="note b">Day light + UVB off · ceramic emitter on</div><p>Tap the day/night chip: lights and setpoints switch to the night profile.</p></div></div>
<div class="sc"><div class="in"><h4>DOOR OPEN <span style="color:#ffb340">· CONCEPT</span></h4><div class="big">Mist + fan paused</div><div class="wt"><div class="ln"><span>M</span><div class="tr"><em style="left:4%;width:28%"></em><em class="b2" style="left:34%;width:30%"></em><em style="left:66%;width:30%"></em></div><b>✓</b></div><div class="ax"><span>open</span><span>feeding</span><span>closed</span></div></div><div class="note">Concept: door switch pending confirmation</div><p>Open the door to feed and misting and the fan pause; close it and they resume.</p></div></div></div>
<div class="diffs"><div><b>Heat stays local</b>A Wi-Fi drop or server outage changes nothing.</div><div><b>Alerts that reach you</b>Over/under temp, probe unplugged, outlet stuck on — by push, text, email or alarm, including when you’re away.</div><div><b>No subscription</b>Home Assistant on your home network. Voice assistants via Home Assistant.</div></div>
<div class="what"><div><div class="live" style="color:#d9493d">DEMO · TAP “ALERT EXAMPLE”</div><div class="alarm"><small>EXAMPLE ALERT</small>Enclosure 1 hot side over temperature · heat mat switched off · push and text sent</div><p style="font:400 8.4px/1.45 Inter;color:#5a6876;margin-top:6px">Coral appears only for a warning. Everyday state is calm aqua and warm daylight.</p></div>
<div class="cta"><h3>Join the beta</h3><p>We’re looking for keepers with two or more enclosures to test Terrarium Control Pro before launch.</p><span>Join the interest list →</span></div></div>
<div class="bot" style="left:.5in;right:.5in"><span>TERRARIUM CONTROL PRO · {CF.format('navy')}</span><span class="cc" style="position:static;color:#b86e00">Concept · demo · example readings</span></div></div>'''
css=open('style.css').read()+open('ha.css').read()
html=f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,600&display=swap" rel="stylesheet"><style>{css}</style></head><body>{front}{light}{duopg}{hapg}{back}<script>document.addEventListener("click",e=>{{const t=e.target.closest(".tile");if(!t)return;t.classList.toggle("on");t.setAttribute("aria-pressed",t.classList.contains("on"))}})</script></body></html>'
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
_sp.run(['python3', _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../_infographic/build_infographic.py'), 'O15'], check=True)
