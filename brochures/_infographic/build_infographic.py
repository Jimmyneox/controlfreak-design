"""Wave 1 brochures: the "Why Home Assistant" page, and the brochure splice.

    python3 brochures/_infographic/build_infographic.py            # all four
    python3 brochures/_infographic/build_infographic.py O04 C01    # some
    python3 brochures/_infographic/build_infographic.py --site /path/to/controlfreak-platform-public [codes]

For each locked Wave 1 brochure this writes why-ha.html, renders it to why-ha.pdf and why-ha.png
(Playwright for Node, Chromium), then rebuilds brochure.pdf as front, light-mode, duo, ha-home,
why-ha, infographic (when the folder has an infographic.pdf), back, plus spread.png and
brochure-review.pdf. --site writes the matching #home-assistant section on each product site.

The "How it all connects" infographic is no longer made here (owner, 2026-10-26): Gemini remakes
it (controlfreak-platform design/INFOGRAPHIC_REMAKE.md). If a brochure folder has Gemini's
infographic.gemini.html, the build exports it to infographic.pdf/.png and places it as page 6,
and --site copies that PNG to the site and points the #connects figure at it. Without that file
nothing here writes infographic.* or the sites' #connects section.
"""
from __future__ import annotations

import html
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
BRO = HERE.parent

FONTS = ("https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=IBM+Plex+Mono:wght@400;600"
         "&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;600;700"
         "&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap")


P = {
    "O04": dict(
        folder="O04-reef/c-v8-gemini-outline", name="Reef Control Pro", serif=False,
        acc="#2fd3c4", acc2="#ff9a6e", bg="background:radial-gradient(ellipse 80% 45% at 30% 0%,#2fd3c433,transparent 70%),radial-gradient(ellipse 70% 40% at 80% 100%,#ff8a6522,transparent 70%),linear-gradient(180deg,#04121f 0,#0a2a3d 55%,#06202f 100%)",
        lock='<img src="../approved-mark/reef-mark-lockup-white.svg" style="width:1.8in">',
        cf=None, foot="REEF CONTROL PRO · BROUGHT TO YOU BY CONTROL FREAK",
    ),
    "C03": dict(
        folder="C03-basement-guard/a-gemini-outline", name="Basement Guard Pro", serif=False,
        acc="#3d8bff", acc2="#ffb340", bg="background:url(assets/basement-stage-concept.jpg) center 70%/cover;filter:brightness(.42) blur(2px)",
        lock='<div class="lock"><img src="assets/bgp-mark-white.svg"><div><b>Basement<br><span>Guard Pro</span></b><small>CONCEPT MARK</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="BASEMENT GUARD PRO",
    ),
    "O15": dict(
        folder="O15-terrarium/concepts/A-living-demo-theater", name="Terrarium Control Pro", serif=True,
        acc="#2fd3c4", acc2="#ffb340", bg="background:radial-gradient(ellipse 70% 40% at 25% 0%,#ffb34026,transparent 70%),radial-gradient(ellipse 80% 50% at 70% 100%,#2fd3c41f,transparent 70%),linear-gradient(180deg,#0d1612 0,#16261f 55%,#0f1a15 100%)",
        lock='<div class="lock"><img src="assets/tcp-mark-white.svg"><div><b>Terrarium<br><span>Control Pro</span></b><small>CONCEPT MARK</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="TERRARIUM CONTROL PRO",
    ),
    "C01": dict(
        folder="C01-cold-plunge/concepts/A-living-demo-theater", name="Cold Plunge Control Pro", serif=True,
        acc="#5fb4ff", acc2="#ffb340",
        bg="background:radial-gradient(ellipse 90% 40% at 50% 104%,#f6c58a33,transparent 60%),linear-gradient(180deg,#0a1320 0,#14263d 55%,#2a4a6c 100%)",
        lock='<div class="lock"><div><b>Cold Plunge<br><span>Control Pro</span></b><small>WORKING NAME · CONCEPT</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="COLD PLUNGE CONTROL PRO",
    ),
}


# ---------------------------------------------------------------- "Why Home Assistant" page
# Facts about Home Assistant itself: home-assistant.io and analytics.home-assistant.io, read
# 2026-10-26 ("Over 2.7 million households", "1500+ integrations", "Works with over 1000
# brands", "local control and privacy first", "a non-profit and can't be sold or acquired").
# Control Freak specifics stay inside DECISIONS / PUBLIC_BRIEF: HA pre-installed with the CF
# integration, local on the controller on the home network (not a cloud service), Alexa and Google through the voice
# bridge and Siri through HomeKit on HA, away alerts through the apps, no subscription.
HA_SOURCE = "Home Assistant figures: home-assistant.io, October 2026."
# Owner decision 2026-10-26 (DECISIONS db07edb): verbatim on every Wave 1 product.
# Writer line, cleared by Engineering with conditions (controlfreak-platform PUBLIC_BRIEFs 0783797,
# DECISIONS 5f2d9af). Verbatim per product; no claim beyond it (e.g. nothing about power loss).
SAFETY_LEAD = "Safety rules don’t depend on Home Assistant"
SAFETY = {
    "O04": "Control Freak’s own safety rules — heater cutoff, top-off lockout and leak shutoff — keep running on the controller, even if Home Assistant stops.",
    "C03": "Control Freak’s own safety rules — pump switching, high-water and leak alarms, and the freeze heat-tape switch — keep running on the controller, even if Home Assistant stops.",
    "O15": "Control Freak’s own safety rules — over-temperature cutoff and the unplugged-probe check — keep running on the controller, even if Home Assistant stops.",
    "C01": "Control Freak’s own safety rules — the no-flow chiller stop, temperature hold and freeze protection — keep running on the controller, even if Home Assistant stops.",
}
CF_GEAR = ("Works with the Control Freak gear you already own: every Control Freak product is a complete kit on "
           "its own. If a Control Freak controller you already have has a free port or relay, Home Assistant can "
           "put it to work for this product too.")
HA_STATS = [("2.7M+", "households run Home Assistant"), ("1,500+", "integrations"),
            ("1,000+", "brands it works with"), ("0", "subscriptions with Control Freak")]


def ha_angles(thing: str, own: str) -> list[tuple[str, str, str]]:
    # Headlines and wording follow what Home Assistant users say they love (private repo:
    # design/research/HA_VOICE_OF_CUSTOMER.md). Language only; no quotes are published.
    return [
        ("apps", "One app. No more app juggling.",
         f"How many apps do you open today? Home Assistant puts {own} and the rest of your smart home in one place, so you have one app to check and one to control."),
        ("plug", "Your brands finally work together",
         "Home Assistant works with over 1,000 brands through 1,500+ integrations. Lights, plugs, thermostats, locks, speakers and cameras you already own can finally talk to each other."),
        ("lock", "Works when the internet doesn’t",
         "It runs on the controller on your home network, not in someone else’s cloud, so it responds fast and keeps working when the internet doesn’t. Your data stays home."),
        ("voice", "Ask, don’t open",
         "Ask Alexa what the status is, tell Google to adjust the temperature, or use Siri through HomeKit, and get automated voice alerts when something is out of balance."),
        ("bolt", "Peace of mind, all over the house",
         f"Anything {own} knows can set off something else: lights, speakers, thermostats and alerts on every phone. A few ideas are below."),
        ("shield", "Yours to keep",
         "Your setup lives in your home, not on a company’s server. Home Assistant is free and open source, and Control Freak adds no subscription."),
    ]


HA = {
    "O04": dict(h1="Your reef, and every smart thing in your home, in one app.",
                angles=ha_angles("reef", "your tank"),
                ideas=[("Water under the stand", "Hallway lights flash and every speaker says where."),
                       ("Feeding time", "A button by the tank starts Feed mode; pumps pause, then resume."),
                       ("Reef sunset", "As the reef lights ramp down, the living-room lamps dim with them.")]),
    "C03": dict(h1="Your basement, and every smart thing in your home, in one app.",
                angles=ha_angles("basement", "your sump"),
                ideas=[("Pump B steps in", "The kitchen light turns amber so you notice, even with your phone down."),
                       ("Leak by the water heater", "Every speaker in the house says where the water is."),
                       ("Crawlspace near freezing", "You get a text, and your thermostat gets a nudge.")]),
    "O15": dict(h1="Your enclosures, and every smart thing in your home, in one app.",
                angles=ha_angles("enclosures", "your shelf"),
                ideas=[("Lights to night", "When the enclosures switch to night, the room lamp dims too."),
                       ("Humidity, your way", "Add your own wireless humidity sensor; it shows beside the temperatures."),
                       ("Over-temperature cutoff", "Speakers announce which enclosure, and your phone gets a push.")]),
    "C01": dict(h1="Your plunge, and every smart thing in your home, in one app.",
                angles=ha_angles("plunge", "your plunge"),
                ideas=[("Alarm set for 6:00", "Ready-by follows your morning: the water is at target by 6:30."),
                       ("“Alexa, is the plunge ready?”", "Hear the water temperature before you head outside."),
                       ("Out of the plunge", "The bathroom floor heat comes on, so you warm up after.")]),
}

ICON = {
    "apps": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><path d="M17.5 14v7M14 17.5h7"/>',
    "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15.5" r="1.4"/>',
    "voice": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "shield": '<path d="M12 2 4 5v6c0 5 3.5 9 8 11 4.5-2 8-6 8-11V5z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
}


def ha_page(c: dict, h: dict, code: str) -> str:
    head_font = "'Fraunces'" if c["serif"] else "'Space Grotesk'"
    cards = "".join(f'<div class="hc"><span class="ic"><svg viewBox="0 0 24 24">{ICON[i]}</svg></span><b>{html.escape(t)}</b><p>{html.escape(d)}</p></div>'
                    for i, t, d in h["angles"])
    stats = "".join(f'<div class="st"><b>{n}</b><span>{html.escape(t)}</span></div>' for n, t in HA_STATS)
    ideas = "".join(f'<div class="id"><small>IDEA · EXAMPLE</small><b>{html.escape(t)}</b><p>{html.escape(d)}</p></div>' for t, d in h["ideas"])
    cf = (f'<span class="cfw2">BROUGHT TO YOU BY <img src="{c["cf"]}" alt="Control Freak"></span>' if c["cf"] else "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(c['name'])} · why Home Assistant</title>
<link href="{FONTS}" rel="stylesheet"><style>
@page{{size:8.5in 11in;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{-webkit-print-color-adjust:exact;print-color-adjust:exact;--acc:{c['acc']};--acc2:{c['acc2']}}}
.pg{{width:8.5in;height:11in;position:relative;overflow:hidden;font-family:Inter;color:#fff;background:#0b141e}}
.bg{{position:absolute;inset:-10px;{c['bg']}}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,#0b141ecc 0,#0b141e80 35%,#0b141eb0 70%,#0b141ef0 100%)}}
.head{{position:absolute;top:.45in;left:.5in;right:.5in;display:flex;justify-content:space-between;align-items:flex-start;gap:24px;z-index:2}}
.live{{font:600 9px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-bottom:8px}}
h1{{font:700 28px/1.08 {head_font};letter-spacing:-.02em;max-width:5.4in}}
.sub{{font:400 12px/1.5 Inter;color:#dbe7ef;max-width:5.2in;margin-top:10px}}
.lock{{display:flex;align-items:center;gap:9px;color:#fff;flex:none}}.lock img{{width:.62in}}
.lock b{{font:700 17px/1 {head_font};letter-spacing:-.01em;display:block}}.lock b span{{color:var(--acc)}}
.lock small{{display:block;font:600 6.5px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-top:4px}}
.cc{{font:600 8px Montserrat;letter-spacing:.2em;text-transform:uppercase;padding:4px 8px;border:1px solid currentColor;border-radius:2px;color:var(--acc2)}}
.grid{{position:absolute;left:.5in;right:.5in;top:2.2in;display:grid;grid-template-columns:1fr 1fr;gap:12px;z-index:2}}
.hc{{padding:14px 16px;border-radius:16px;background:#ffffff12;border:1px solid #ffffff26;min-height:1.28in}}
.hc .ic,.gear .ic{{display:inline-flex;width:30px;height:30px;border-radius:9px;background:var(--acc);align-items:center;justify-content:center;margin-bottom:8px}}
.hc svg,.gear svg{{width:18px;height:18px;fill:none;stroke:#0b141e;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
.hc b{{font:600 14px/1.2 {head_font};display:block;margin-bottom:5px}}.hc p{{font:400 10.5px/1.45 Inter;color:#cfdce6}}
.stats{{position:absolute;left:.5in;right:.5in;top:6.86in;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;z-index:2}}
.st{{padding:10px 14px;border-radius:14px;background:#ffffff14;border:1px solid #ffffff2a}}
.st b{{font:700 26px/1 {head_font};color:var(--acc);white-space:nowrap;display:block}}.st span{{font:600 8px/1.35 'IBM Plex Mono';letter-spacing:.12em;text-transform:uppercase;color:#dbe7ef;display:block;margin-top:6px}}
.ideas{{position:absolute;left:.5in;right:.5in;top:7.95in;z-index:2}}
.ideas h2{{font:600 9px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-bottom:8px}}
.ideas .row{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}
.id{{padding:12px 14px;border-radius:14px;background:#ffffff0f;border:1px dashed #ffffff40}}
.id small{{font:600 7px 'IBM Plex Mono';letter-spacing:.18em;color:var(--acc2)}}.id b{{display:block;font:600 12.5px/1.25 {head_font};margin:5px 0 3px}}.id p{{font:400 10px/1.4 Inter;color:#cfdce6}}
.strip{{position:absolute;left:.5in;right:.5in;bottom:1.0in;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.gear{{display:flex;gap:10px;align-items:center;padding:8px 12px;border-radius:14px;background:#ffffff12;border:1px solid #ffffff2e;border-left:3px solid var(--acc)}}
.gear .ic{{flex:none;margin:0}}.gear p{{font:400 9.5px/1.4 Inter;color:#e3edf4}}.gear b{{font-weight:600;color:#fff}}
.src{{position:absolute;left:.5in;right:.5in;bottom:.72in;font:400 8.5px Inter;color:#9fb1bf;z-index:2}}
.bot{{position:absolute;bottom:.35in;left:.5in;right:.5in;display:flex;justify-content:space-between;align-items:center;font:600 8px 'IBM Plex Mono';letter-spacing:.2em;color:#c4ccd3;z-index:2;gap:12px}}
.bot .l{{display:flex;align-items:center;gap:14px}}.cfw2{{display:flex;align-items:center;gap:8px}}.cfw2 img{{height:22px}}
</style></head><body><div class="pg"><div class="bg"></div><div class="shade"></div>
<div class="head"><div><div class="live">WHY HOME ASSISTANT · PRE-INSTALLED · ON YOUR HOME NETWORK</div><h1>{html.escape(h['h1'])}</h1>
<p class="sub">{html.escape(c['name'])} comes with Home Assistant already installed and the Control Freak integration already connected. You get everything people love about it, without the setup. Just plug it in.</p></div>{c['lock']}</div>
<div class="grid">{cards}</div>
<div class="stats">{stats}</div>
<div class="ideas"><h2>IDEAS YOU CAN BUILD IN HOME ASSISTANT · EXAMPLES WITH YOUR OWN DEVICES</h2><div class="row">{ideas}</div></div>
<div class="strip"><div class="gear"><span class="ic"><svg viewBox="0 0 24 24">{ICON["shield"]}</svg></span><p><b>{html.escape(SAFETY_LEAD)}</b> — {html.escape(SAFETY[code])}</p></div><div class="gear"><span class="ic"><svg viewBox="0 0 24 24">{ICON["plug"]}</svg></span><p><b>{html.escape(CF_GEAR.split(": ",1)[0])}:</b> {html.escape(CF_GEAR.split(": ",1)[1])}</p></div></div>
<p class="src">{HA_SOURCE} Home Assistant is a trademark of the Open Home Foundation. Your lights, speakers and thermostat aren’t in the box.</p>
<div class="bot"><div class="l"><span>{html.escape(c['foot'])}</span>{cf}</div><span class="cc">Concept · example automations</span></div>
</div></body></html>"""


RENDER = r"""
const { chromium } = require('playwright');
const [url, pdf, png] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 110 / 96 });
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: pdf, preferCSSPageSize: true, printBackground: true });
  await p.screenshot({ path: png });
  await b.close();
})();
"""

ORDER = ["front", "light-mode", "duo", "ha-home", "why-ha", "infographic", "back"]   # infographic: if present


def splice(folder: Path) -> None:
    """Rebuild brochure.pdf as front, light-mode, duo, ha-home, why-ha, [infographic], back: the
    brochure's own five pages plus why-ha.pdf, and infographic.pdf when the folder has one.
    This script no longer makes the infographic (owner, 2026-10-26: Gemini remakes it); it only
    places whatever infographic.pdf/.png the folder holds."""
    pdf = folder / "brochure.pdf"
    # pypdf, not pdfseparate/pdfunite: those copy every shared font and image once per page.
    src = PdfReader(pdf)
    n = len(src.pages)
    assert n in (5, 6, 7), f"{folder}: unexpected {n} pages"
    base = list(src.pages[:4]) + [src.pages[n - 1]]   # the brochure's own five pages (earlier inserts dropped)
    w = PdfWriter()
    order = [n for n in ORDER if n != "infographic" or (folder / "infographic.pdf").exists()]
    inserts = list(PdfReader(folder / "why-ha.pdf").pages)
    if "infographic" in order:
        inserts += list(PdfReader(folder / "infographic.pdf").pages)
    for pg in base[:4] + inserts + [base[4]]:
        w.add_page(pg)
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    with open(f"{pdf}.tmp", "wb") as f:
        w.write(f)
    os.replace(f"{pdf}.tmp", pdf)
    # the brochure's own page PNGs stay; why-ha.png comes from this build
    ims = [Image.open(folder / f"{n}.png").convert("RGB") for n in order]
    h = max(i.height for i in ims)
    ims = [i.resize((round(i.width * h / i.height), h)) for i in ims]
    gap = 20
    spread = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), h), "#ffffff")
    x = 0
    for i in ims:
        spread.paste(i, (x, 0)); x += i.width + gap
    spread.save(folder / "spread.png")
    ims[0].save(folder / "brochure-review.pdf", save_all=True, append_images=ims[1:], resolution=110)


def build(code: str) -> None:
    c = P[code]
    folder = BRO / c["folder"]
    (folder / "why-ha.html").write_text(ha_page(c, HA[code], code), encoding="utf-8")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(RENDER); js = f.name
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", js, "file://" + str(folder / "why-ha.html"), str(folder / "why-ha.pdf"),
                    str(folder / "why-ha.png")], check=True, env=env)
    gemini = folder / "infographic.gemini.html"
    if gemini.exists():   # Gemini's remake (INFOGRAPHIC_REMAKE.md): export it as-is, never edit it
        subprocess.run(["node", js, "file://" + str(gemini), str(folder / "infographic.pdf"),
                        str(folder / "infographic.png")], check=True, env=env)
    os.unlink(js)
    splice(folder)
    print("built", folder.relative_to(BRO))


SITE = {"O04": "O04-reef", "C03": "C03-basement-guard", "O15": "O15-reptile", "C01": "C01-cold-plunge"}

HA_SITE_CSS = """
/* Why Home Assistant (Design build_infographic.py, 2026-10-26) */
.whyha .grid.angles{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.whyha .card .ic{display:inline-flex;width:34px;height:34px;border-radius:10px;align-items:center;justify-content:center;background:var(--accent,var(--teal));margin-bottom:10px}
.whyha .card .ic svg{width:20px;height:20px;fill:none;stroke:var(--onaccent,#0b141e);stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.whyha .hastats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-top:24px}
.whyha .hastats div{padding:14px 18px;border-radius:18px;border:1px solid var(--line)}
.whyha .hastats b{display:block;font-family:var(--display);font-size:2rem;line-height:1.1;color:var(--accent,var(--teal))}
.whyha .hastats span{color:var(--muted);font-size:.8rem;text-transform:uppercase;letter-spacing:.1em}
.whyha h3.ideas{margin:32px 0 0;font-size:.75rem;text-transform:uppercase;letter-spacing:.16em;color:var(--accent,var(--teal))}
.whyha .idea{border-style:dashed}
.whyha .gear{display:flex;gap:14px;align-items:flex-start;margin-top:16px;border-left:3px solid var(--accent,var(--teal))}
.whyha .gear .ic{flex:none;margin:0}.whyha .gear p{margin:0}
.whyha .idea small{display:block;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
"""


def site_ha(code: str, root: Path) -> None:
    """Add the "Why Home Assistant" section to the product site, styled with the site's own cards."""
    c, h = P[code], HA[code]
    d = root / "products" / SITE[code] / "site"
    cards = "".join(f'<div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON[i]}</svg></span>'
                    f'<h3>{html.escape(t)}</h3><p>{html.escape(x)}</p></div>' for i, t, x in h["angles"])
    stats = "".join(f"<div><b>{n}</b><span>{html.escape(t)}</span></div>" for n, t in HA_STATS)
    ideas = "".join(f'<div class="card idea"><small>Idea · example</small><h3>{html.escape(t)}</h3><p>{html.escape(x)}</p></div>'
                    for t, x in h["ideas"])
    sec = (f'<section id="home-assistant"><div class="wrap whyha">\n'
           f'  <div class="eyebrow">Why Home Assistant · pre-installed · on your home network</div><h2>{html.escape(h["h1"])}</h2>\n'
           f'  <p class="lead">{html.escape(c["name"])} comes with Home Assistant already installed and the Control Freak integration already connected. You get everything people love about it, without the setup. Just plug it in.</p>\n'
           f'  <div class="grid angles">{cards}</div>\n  <div class="hastats">{stats}</div>\n'
           f'  <div class="card gear"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON["shield"]}</svg></span><p><b>{html.escape(SAFETY_LEAD)}</b> — {html.escape(SAFETY[code])}</p></div>\n'
           f'  <div class="card gear"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON["plug"]}</svg></span><p><b>{html.escape(CF_GEAR.split(": ",1)[0])}:</b> {html.escape(CF_GEAR.split(": ",1)[1])}</p></div>\n'
           f'  <h3 class="ideas">Ideas you can build in Home Assistant · examples with your own devices</h3>\n'
           f'  <div class="grid angles">{ideas}</div>\n'
           f'  <p class="small" style="margin-top:18px">{HA_SOURCE} Home Assistant is a trademark of the Open Home Foundation. Your lights, speakers and thermostat aren’t in the box. Concept · example automations.</p>\n'
           f'</div></section>\n\n')
    idx = d / "index.html"
    t = idx.read_text(encoding="utf-8")
    if '<section id="home-assistant">' in t:
        a = t.index('<section id="home-assistant">'); b = t.index("</section>", a) + len("</section>\n\n")
        t = t[:a] + t[b:]
    anchor = '<section id="connects">' if '<section id="connects">' in t else '<section id="demo">'
    t = t.replace(anchor, sec + anchor, 1)
    idx.write_text(t, encoding="utf-8")
    css = d / "styles.css"
    st = css.read_text(encoding="utf-8")
    if "/* Why Home Assistant (Design" in st:   # the HA block is appended last; replace it
        st = st[:st.index("/* Why Home Assistant (Design")].rstrip("\n") + "\n"
    css.write_text(st.rstrip("\n") + "\n" + HA_SITE_CSS, encoding="utf-8")
    print("site ha", d.relative_to(root))


def site_gemini(code: str, root: Path) -> None:
    """Use Gemini's infographic art on the product site, when the brochure folder has it: copy the
    exported infographic.png to the site and point the #connects figure at it. Without
    infographic.gemini.html the site's #connects section is left exactly as it is."""
    folder = BRO / P[code]["folder"]
    if not (folder / "infographic.gemini.html").exists() or not (folder / "infographic.png").exists():
        return
    d = root / "products" / SITE[code] / "site"
    shutil.copyfile(folder / "infographic.png", d / "assets" / "how-it-connects.png")
    idx = d / "index.html"
    t = idx.read_text(encoding="utf-8")
    if '<section id="connects">' in t:
        a = t.index('<section id="connects">'); b = t.index("</section>", a)
        t = t[:a] + t[a:b].replace("assets/how-it-connects.svg", "assets/how-it-connects.png") + t[b:]
        idx.write_text(t, encoding="utf-8")
    print("site gemini art", d.relative_to(root))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--site":       # --site /path/to/controlfreak-platform-public [codes]
        root = Path(args[1])
        for code in (args[2:] or list(P)):
            site_ha(code, root)
            site_gemini(code, root)
    else:
        for code in (args or list(P)):
            build(code)
