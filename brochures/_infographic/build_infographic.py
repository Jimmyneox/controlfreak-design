"""Wave 1 brochure infographic page: "How it all connects".

    python3 brochures/_infographic/build_infographic.py            # all four
    python3 brochures/_infographic/build_infographic.py O04 C01    # some

For each locked Wave 1 brochure this writes infographic.html, renders it to infographic.pdf and
infographic.png in that brochure's folder (Playwright for Node, Chromium), then splices the page
into brochure.pdf just before the back page and rebuilds brochure-review.pdf and spread.png.
The page reuses each brochure's palette, type, stage background and lockup, so it reads as one
more page of the same brochure. Words come from that product's PUBLIC_BRIEF (Platform); the
diagram is a concept illustration, not to scale. Owner request 2026-10-26: "Create an
infographic page for every product brochure and webpage".
"""
from __future__ import annotations

import html
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
BRO = HERE.parent

# Keyed plug colours (design/CHATGPT_HANDOFF.md, brand reference)
BLUE, YELLOW, ORANGE, PURPLE, GREEN, GREY = "#3d8bff", "#ffc93c", "#ff9440", "#b38bff", "#3fd68a", "#aab4bf"

FONTS = ("https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=IBM+Plex+Mono:wght@400;600"
         "&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;600;700"
         "&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap")


# ---------------------------------------------------------------- shared diagram pieces

def controller(x: int, y: int) -> str:
    return f'''<g transform="translate({x} {y})">
  <rect x="0" y="0" width="150" height="96" rx="16" fill="#141c26" stroke="#ffffff33" stroke-width="1.5"/>
  <rect x="14" y="14" width="122" height="44" rx="8" fill="#22303f"/>
  <circle cx="28" cy="27" r="4" fill="var(--acc)"/>
  <text x="75" y="44" text-anchor="middle" class="cfw">CONTROL FREAK</text>
  <g fill="#3a4c60"><circle cx="35" cy="76" r="7"/><circle cx="60" cy="76" r="7"/><circle cx="85" cy="76" r="7"/><circle cx="110" cy="76" r="7"/></g>
  <line x1="138" y1="2" x2="146" y2="-40" stroke="#141c26" stroke-width="7" stroke-linecap="round"/>
</g>'''


def hub(x: int, y: int, labels: list[str], w: int = 470) -> str:
    n = len(labels)
    step = (w - 30) / n
    cells = []
    for i, lab in enumerate(labels):
        cx = 15 + step * i + step / 2
        lines = lab.split("|")
        txt = "".join(f'<tspan x="{cx:.0f}" dy="{0 if k == 0 else 12}">{html.escape(t)}</tspan>'
                      for k, t in enumerate(lines))
        cells.append(f'<rect x="{cx - 17:.0f}" y="12" width="34" height="40" rx="8" fill="#e9eef4" stroke="#c5cdd8" stroke-width="1.5"/>'
                     f'<path d="M{cx - 6:.0f} 22 v9 M{cx + 6:.0f} 22 v9" stroke="#12355b" stroke-width="2.6" stroke-linecap="round"/>'
                     f'<circle cx="{cx:.0f}" cy="40" r="2.6" fill="#12355b"/>'
                     f'<text y="80" class="olab">{txt}</text>')
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="{w}" height="64" rx="16" fill="#f4f7fa"/>'
            + "".join(cells) + "</g>")


def lead(d: str, col: str) -> str:
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'


def plug(x: float, y: float, col: str) -> str:
    return f'<rect x="{x - 9}" y="{y - 6}" width="18" height="12" rx="3" fill="{col}" stroke="#0b1a26" stroke-width="1.2"/>'


def num(x: float, y: float, n: int) -> str:
    return (f'<g class="num"><circle cx="{x}" cy="{y}" r="12" fill="var(--acc)"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text></g>')


def home_side(x: int, y: int, extra: str = "") -> str:
    """Home network column: HA, phone, voice and alert channels."""
    return f'''<g transform="translate({x} {y})">
  <path d="M-80 214 C -80 120 -40 46 0 46 M-80 214 C -60 170 -10 160 34 160" fill="none" stroke="var(--acc)" stroke-width="2" stroke-dasharray="3 6" stroke-linecap="round"/>
  <text x="-74" y="236" class="sm">HOME NETWORK</text>
  <rect x="0" y="0" width="118" height="92" rx="16" class="glass"/>
  <path d="M38 64 V 42 l 21 -16 l 21 16 V 64 Z" fill="none" stroke="#fff" stroke-width="2.6" stroke-linejoin="round"/>
  <circle cx="59" cy="50" r="4.5" fill="var(--acc)"/>
  <text x="59" y="84" text-anchor="middle" class="sm">HOME ASSISTANT</text>
  <rect x="34" y="112" width="52" height="96" rx="11" fill="#0b141e" stroke="#ffffff66" stroke-width="2"/>
  <rect x="40" y="122" width="40" height="10" rx="3" fill="var(--acc)" opacity=".55"/>
  <rect x="40" y="138" width="18" height="16" rx="3" fill="#ffffff2a"/><rect x="62" y="138" width="18" height="16" rx="3" fill="#ffffff2a"/>
  <rect x="40" y="158" width="18" height="16" rx="3" fill="#ffffff2a"/><rect x="62" y="158" width="18" height="16" rx="3" fill="var(--acc)" opacity=".7"/>
  <text x="59" y="226" text-anchor="middle" class="sm">YOUR PHONE</text>
  <g transform="translate(-6 244)">
    <rect width="130" height="24" rx="12" class="chip"/><text x="65" y="16" text-anchor="middle" class="ch">Alexa · Google</text>
    <rect y="32" width="130" height="24" rx="12" class="chip"/><text x="65" y="48" text-anchor="middle" class="ch">Push · text · email · alarm</text>
  </g>{extra}
</g>'''


def scene_label(x: float, y: float, text: str, anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="slab">{html.escape(text)}</text>'


# ---------------------------------------------------------------- product scenes (viewBox 1000 x 640)

def reef_svg() -> str:
    s = []
    # display tank and stand
    s.append('<rect x="40" y="40" width="400" height="200" rx="8" class="water"/>')
    s.append('<path d="M40 76 Q 240 66 440 76" class="wline"/>')
    s.append('<g class="coral"><path d="M110 240 c -4 -40 -26 -54 -16 -84 M110 240 c 6 -36 28 -48 22 -76 M196 240 c 0 -30 -18 -40 -8 -64 M300 240 c -6 -46 14 -58 6 -86 M300 240 c 10 -28 30 -34 34 -58 M380 240 c -2 -26 12 -36 4 -54"/></g>')
    s.append('<rect x="60" y="240" width="360" height="150" rx="6" class="stand"/>')
    # sump inside stand
    s.append('<rect x="84" y="296" width="250" height="78" rx="6" class="water"/>')
    s.append('<path d="M84 312 H 334" class="wline"/>')
    s.append('<path d="M330 296 V 220 H 418 V 60" class="pipe"/>')  # return line
    # reservoir (yours)
    s.append('<rect x="350" y="318" width="56" height="56" rx="6" class="yours"/>')
    s.append(scene_label(378, 412, "Your reservoir", "middle"))
    s.append(scene_label(52, 30, "Display tank"))
    s.append(scene_label(96, 290, "Sump"))
    # sensors
    s.append('<rect x="120" y="318" width="8" height="40" rx="4" class="probe"/><rect x="146" y="318" width="8" height="40" rx="4" class="probe"/>')
    s.append('<rect x="186" y="314" width="10" height="46" rx="5" class="probe"/>')  # pH
    s.append('<rect x="250" y="312" width="16" height="10" rx="3" class="probe"/><rect x="250" y="330" width="16" height="10" rx="3" class="probe"/>')  # level
    s.append('<ellipse cx="240" cy="404" rx="22" ry="7" class="probe"/>')  # leak puck on floor
    s.append('<rect x="452" y="250" width="70" height="44" rx="10" class="probe"/><g fill="#0b1a26"><circle cx="469" cy="272" r="7"/><circle cx="487" cy="272" r="7"/><circle cx="505" cy="272" r="7"/></g>')  # doser
    s.append('<path d="M469 250 C 469 230 330 240 300 296 M487 250 C 487 236 320 248 290 296 M505 250 C 505 240 316 252 280 296" class="tube"/>')
    s.append(scene_label(487, 310, "Doser (Pro)", "middle"))
    # controller + leads
    s.append(controller(600, 214))
    s.append(lead("M600 232 H 560 V 190 H 160 V 318", BLUE) + plug(592, 232, BLUE))
    s.append(lead("M600 252 H 548 V 202 H 191 V 314", PURPLE) + plug(592, 252, PURPLE))
    s.append(lead("M600 272 H 536 V 214 H 258 V 312", YELLOW) + plug(592, 272, YELLOW))
    s.append(lead("M600 292 H 540 V 430 H 240 V 411", YELLOW) + plug(592, 292, YELLOW))
    s.append(lead("M600 304 H 525 V 272 H 522", GREEN) + plug(592, 306, GREEN))
    # hub
    s.append('<path d="M675 310 V 470" stroke="#141c26" stroke-width="9" stroke-linecap="round"/>')
    s.append(hub(440, 470, ["Return", "Power-|head 1", "Power-|head 2", "Heater", "Chiller|/ fan", "Main|light", "Refug.|light", "Skimmer"], 520))
    s.append('<path d="M460 502 H 430 V 250" class="power" />')
    s.append(home_side(850, 40))
    s += [num(140, 300, 1), num(206, 300, 2), num(282, 300, 3), num(272, 404, 4), num(536, 248, 5), num(965, 500, 6), num(990, 70, 7)]
    return "".join(s)


def basement_svg() -> str:
    s = []
    s.append('<rect x="20" y="70" width="520" height="2" fill="#ffffff55"/>')  # ground line
    s.append(scene_label(28, 60, "Ground level"))
    s.append('<rect x="20" y="380" width="520" height="3" fill="#ffffff66"/>')  # basement floor
    s.append(scene_label(28, 400, "Basement floor"))
    # sump pit
    s.append('<path d="M90 380 V 560 H 250 V 380" class="pit"/>')
    s.append('<rect x="92" y="470" width="156" height="88" class="water"/><path d="M92 470 H 248" class="wline"/>')
    s.append('<rect x="108" y="510" width="40" height="46" rx="6" class="yours"/><rect x="190" y="510" width="40" height="46" rx="6" class="yours"/>')
    s.append(scene_label(128, 584, "Pump A", "middle") + scene_label(210, 584, "Pump B", "middle"))
    s.append('<path d="M128 510 V 300 H 60 V 90 M210 510 V 320" class="pipe"/>')
    s.append('<rect x="160" y="420" width="12" height="80" rx="5" class="probe"/>')  # level sensor
    s.append('<ellipse cx="176" cy="444" rx="10" ry="6" class="probe2"/>')  # high-water float
    # water heater + washer
    s.append('<rect x="300" y="250" width="70" height="130" rx="30" class="yours"/>' + scene_label(335, 242, "Water heater", "middle"))
    s.append('<rect x="400" y="290" width="90" height="90" rx="8" class="yours"/><circle cx="445" cy="335" r="24" fill="none" stroke="#ffffff55" stroke-width="2"/>' + scene_label(445, 282, "Washer", "middle"))
    s.append('<ellipse cx="335" cy="388" rx="20" ry="6" class="probe2"/><ellipse cx="445" cy="388" rx="20" ry="6" class="probe2"/>')
    # pipe with heat tape and temp probes
    s.append('<path d="M290 140 H 520" class="pipe"/><path d="M300 140 l 10 -6 l 10 12 l 10 -12 l 10 12 l 10 -12 l 10 12 l 10 -12 l 10 12 l 10 -6" fill="none" stroke="#ff9440" stroke-width="2"/>')
    s.append(scene_label(300, 128, "Pipes · heat tape"))
    s.append('<rect x="420" y="150" width="30" height="8" rx="4" class="probe"/><rect x="250" y="210" width="30" height="8" rx="4" class="probe"/>')
    s.append('<path d="M520 92 V 40" stroke="#ffffff55" stroke-width="2"/><rect x="510" y="30" width="30" height="8" rx="4" class="probe"/>' + scene_label(548, 38, "Outdoor"))
    # siren
    s.append('<path d="M40 190 l 22 -14 v 44 l -22 -14 z" fill="#e9eef4"/><path d="M70 186 q 8 12 0 24 M78 180 q 12 18 0 36" fill="none" stroke="var(--acc)" stroke-width="2.2" stroke-linecap="round"/>' + scene_label(30, 240, "Siren"))
    s.append(controller(600, 214))
    s.append(lead("M600 232 H 560 V 410 H 166 V 420", ORANGE) + plug(592, 232, ORANGE))
    s.append(lead("M600 252 H 570 V 444 H 186", YELLOW) + plug(592, 252, YELLOW))
    s.append(lead("M600 272 H 552 V 400 H 445 V 382", YELLOW) + lead("M552 400 H 335 V 382", YELLOW) + plug(592, 272, YELLOW))
    s.append(lead("M600 292 H 540 V 154 H 450 M540 154 V 100 H 525 V 38 M540 214 H 280", BLUE) + plug(592, 292, BLUE))
    s.append(lead("M600 306 H 586 V 120 H 62 V 176", GREY) + plug(592, 306, GREY))
    s.append('<path d="M675 310 V 470" stroke="#141c26" stroke-width="9" stroke-linecap="round"/>')
    s.append(hub(440, 470, ["Pump A", "Pump B", "Heat|tape", "Dehumid-|ifier", "Spare"], 400))
    s.append(home_side(850, 40))
    s += [num(150, 430, 1), num(196, 452, 2), num(170, 600, 3), num(390, 400, 4), num(465, 154, 5), num(46, 168, 6), num(990, 70, 7)]
    return "".join(s)


def terrarium_svg() -> str:
    s = []
    s.append('<rect x="20" y="330" width="540" height="12" rx="4" class="stand"/>' + scene_label(28, 362, "Shelf"))
    # enclosure 1 (hot side left)
    s.append('<rect x="40" y="110" width="300" height="220" rx="8" class="glassbox"/>')
    s.append('<path d="M40 300 q 75 -14 150 -2 t 150 0 V 330 H 40 Z" fill="#8a6a3c55"/>')
    s.append('<path d="M70 300 q 30 -40 80 -36" fill="none" stroke="#c49a5c" stroke-width="10" stroke-linecap="round"/>')  # basking log
    s.append('<g class="coral"><path d="M290 300 c -4 -40 -20 -50 -12 -80 M300 300 c 6 -30 24 -40 18 -66 M270 300 c -8 -24 -22 -30 -16 -52"/></g>')
    s.append('<path d="M74 100 a 30 26 0 0 1 60 0 Z" fill="#e9eef4"/><path d="M90 108 l -8 18 M104 110 v 20 M118 108 l 8 18" stroke="#ffb340" stroke-width="2.4" stroke-linecap="round"/>')
    s.append('<rect x="170" y="92" width="150" height="9" rx="4.5" fill="#e9eef4"/><rect x="170" y="104" width="150" height="7" rx="3.5" fill="#b38bff99"/>')
    s.append(scene_label(104, 64, "Basking lamp", "middle") + scene_label(200, 84, "UVB · day light"))
    s.append('<rect x="50" y="342" width="140" height="8" rx="4" fill="#ff944088"/>' + scene_label(50, 382, "Heat mat"))
    s.append('<rect x="250" y="114" width="14" height="8" rx="3" fill="#e9eef4"/><g stroke="var(--acc)" stroke-width="2" stroke-dasharray="1 5" stroke-linecap="round"><line x1="254" y1="126" x2="244" y2="150"/><line x1="258" y1="126" x2="258" y2="154"/><line x1="262" y1="126" x2="272" y2="150"/></g>' + scene_label(282, 136, "Mister"))
    # enclosure 2
    s.append('<rect x="370" y="190" width="170" height="140" rx="8" class="glassbox"/>' + scene_label(380, 180, "Enclosure 2"))
    s.append('<path d="M370 312 q 40 -8 85 0 t 85 0 V 330 H 370 Z" fill="#8a6a3c55"/>')
    # probes
    s.append('<rect x="90" y="250" width="26" height="7" rx="3.5" class="probe"/><rect x="230" y="250" width="26" height="7" rx="3.5" class="probe"/>')
    s.append('<rect x="120" y="230" width="26" height="7" rx="3.5" class="probe"/><rect x="430" y="270" width="26" height="7" rx="3.5" class="probe"/>')
    s.append(scene_label(64, 246, "Hot") + scene_label(232, 244, "Cool") + scene_label(112, 222, "Basking") + scene_label(432, 264, "Probe"))
    # door switch + reservoir float (Concept)
    s.append('<rect x="184" y="160" width="10" height="20" rx="3" class="probe2"/>')
    s.append('<rect x="440" y="378" width="70" height="56" rx="8" class="yours"/><ellipse cx="475" cy="420" rx="10" ry="6" class="probe2"/>' + scene_label(440, 452, "Mister reservoir"))
    s.append(controller(600, 214))
    s.append(lead("M600 232 H 560 V 200 H 103 V 250 M560 200 H 243 V 250 M200 200 H 133 V 230 M560 200 V 266 H 456", BLUE) + plug(592, 232, BLUE))
    s.append(lead("M600 260 H 575 V 150 H 189 V 160 M575 260 V 420 H 485", YELLOW) + plug(592, 260, YELLOW))
    s.append('<path d="M675 310 V 470" stroke="#141c26" stroke-width="9" stroke-linecap="round"/>')
    s.append(hub(440, 470, ["Heat mat", "Ceramic|emitter", "Basking|lamp", "UVB", "Day|light", "Mister", "Fan", "Spare"], 520))
    humid = ('<g transform="translate(-10 316)"><rect width="138" height="40" rx="10" fill="none" stroke="#ffffff88" stroke-width="1.5" stroke-dasharray="4 4"/>'
             '<text x="69" y="17" text-anchor="middle" class="ch">Your humidity sensor</text>'
             '<text x="69" y="31" text-anchor="middle" class="ch2">wireless · via Home Assistant</text></g>')
    s.append(home_side(850, 20, humid))
    s += [num(78, 262, 1), num(166, 178, 2), num(965, 500, 3), num(222, 60, 4), num(510, 384, 5), num(990, 50, 6)]
    return "".join(s)


def plunge_svg() -> str:
    s = []
    s.append('<rect x="20" y="380" width="540" height="3" fill="#ffffff55"/>' + scene_label(28, 402, "Deck"))
    # tub
    s.append('<path d="M40 180 H 300 V 380 H 40 Z" class="yours"/><rect x="48" y="214" width="244" height="160" class="water"/><path d="M48 214 H 292" class="wline"/>')
    s.append(scene_label(52, 170, "Your tub"))
    s.append('<rect x="120" y="250" width="34" height="8" rx="4" class="probe"/>' + scene_label(110, 244, "Water"))
    # plumbing loop to pump, filter, ozone/UV, chiller
    s.append('<path d="M292 350 H 330 V 450 H 520 V 300 H 470 M300 230 H 330 V 300 H 380" class="pipe"/>')
    s.append('<rect x="340" y="420" width="56" height="56" rx="12" class="yours"/>' + scene_label(368, 496, "Pump", "middle"))
    s.append('<rect x="420" y="420" width="44" height="60" rx="10" class="yours"/>' + scene_label(442, 498, "Filter", "middle"))
    s.append('<rect x="380" y="276" width="90" height="48" rx="8" class="yours"/>' + scene_label(425, 268, "Ozone / UV", "middle"))
    s.append('<rect x="380" y="130" width="140" height="100" rx="14" class="yours"/><g stroke="#ffffff44" stroke-width="2"><line x1="396" y1="150" x2="504" y2="150"/><line x1="396" y1="162" x2="504" y2="162"/><line x1="396" y1="174" x2="504" y2="174"/></g>' + scene_label(450, 122, "Your chiller", "middle"))
    s.append('<path d="M470 230 V 300" class="pipe"/>')
    # sensors
    s.append('<rect x="300" y="340" width="20" height="20" rx="4" class="probe2"/>')  # flow switch
    s.append('<rect x="476" y="236" width="26" height="7" rx="3.5" class="probe"/>')  # chiller-outlet probe
    s.append('<rect x="468" y="430" width="16" height="16" rx="4" class="probe3"/>')  # filter pressure
    s.append('<rect x="230" y="100" width="26" height="7" rx="3.5" class="probe"/>' + scene_label(214, 92, "Air"))
    s.append(controller(600, 214))
    s.append(lead("M600 232 H 560 V 76 H 243 V 100 M560 76 V 60 M300 76 H 137 V 250", BLUE) + plug(592, 232, BLUE))
    s.append(lead("M600 254 H 548 V 360 H 320", YELLOW) + plug(592, 254, YELLOW))
    s.append(lead("M600 276 H 536 V 240 H 502", BLUE) + plug(592, 276, BLUE))
    s.append(lead("M600 298 H 540 V 438 H 484", ORANGE) + plug(592, 298, ORANGE))
    s.append('<path d="M675 310 V 470" stroke="#141c26" stroke-width="9" stroke-linecap="round"/>')
    s.append(hub(440, 520, ["Chiller", "Pump", "Ozone|/ UV", "Heater|(Pro)", "Spare"], 400))
    s.append('<path d="M675 470 V 520" stroke="#141c26" stroke-width="9" stroke-linecap="round"/>')
    s.append(home_side(850, 40))
    s += [num(160, 238, 1), num(310, 322, 2), num(516, 254, 3), num(496, 420, 4), num(860, 550, 5), num(990, 70, 6)]
    return "".join(s)


# ---------------------------------------------------------------- products

P = {
    "O04": dict(
        folder="O04-reef/c-v8-gemini-outline", name="Reef Control Pro", serif=False,
        acc="#2fd3c4", acc2="#ff9a6e", bg="background:radial-gradient(ellipse 80% 45% at 30% 0%,#2fd3c433,transparent 70%),radial-gradient(ellipse 70% 40% at 80% 100%,#ff8a6522,transparent 70%),linear-gradient(180deg,#04121f 0,#0a2a3d 55%,#06202f 100%)",
        lock='<img src="../approved-mark/reef-mark-lockup-white.svg" style="width:1.8in">',
        cf=None, foot="REEF CONTROL PRO · BROUGHT TO YOU BY CONTROL FREAK",
        eyebrow="HOW IT ALL CONNECTS · THE WHOLE TANK ON ONE CONTROLLER",
        h1="One controller under the stand.",
        sub="The probes, top-off, leak sensor and doser plug into the controller; the pumps, heater and lights plug into the Power Hub. Keyed, colour-coded plugs only fit their own port — scan the QR code and you’re set up.",
        svg=reef_svg,
        legend=[("Temperature probes", "Two in the kit, room for more. The heater stands down above your limit."),
                ("pH probe (Pro)", "pH right on the home screen, with trends."),
                ("Top-off sensors and pump", "Tops up evaporation with an overfill lockout. Just add a reservoir."),
                ("Leak sensor", "Water on the floor under the stand is caught early."),
                ("3-head doser (Pro)", "Ca, Alk and Mg in small, steady doses."),
                ("Power Hub", "8 smart outlets. Return and powerheads stay on if the controller loses power."),
                ("Home Assistant, pre-installed", "One app for the reef and the home. Voice through Alexa and Google; alerts when you’re away.")],
        stats=[("8", "smart outlets in one Power Hub"), ("3", "dosing heads (Pro): Ca · Alk · Mg"), ("0", "subscriptions")]),
    "C03": dict(
        folder="C03-basement-guard/a-gemini-outline", name="Basement Guard Pro", serif=False,
        acc="#3d8bff", acc2="#ffb340", bg="background:url(assets/basement-stage-concept.jpg) center 70%/cover;filter:brightness(.42) blur(2px)",
        lock='<div class="lock"><img src="assets/bgp-mark-white.svg"><div><b>Basement<br><span>Guard Pro</span></b><small>CONCEPT MARK</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="BASEMENT GUARD PRO",
        eyebrow="HOW IT ALL CONNECTS · PIT, PIPES AND FLOOR",
        h1="Two pumps, one watchful hub.",
        sub="Plug the two pumps you already own into the Power Hub, drop in the level sensor, scan the QR code. No rewiring — and your pumps keep their own float switches.",
        svg=basement_svg,
        legend=[("Pit level sensor", "Pit depth in inches and how fast it’s rising — not just “alarm / no alarm.”"),
                ("High-water float", "A second check if the water keeps rising."),
                ("Your two pumps", "They take turns every week; the second steps in if the water keeps rising. Pump outlets stay on if the controller is ever off."),
                ("Leak sensors", "By the water heater and the washer."),
                ("Temperature probes", "Basement, crawlspace, water heater area and outdoor. Heat tape switches on when it gets cold."),
                ("Siren", "Sounds in the house whether or not the internet is up."),
                ("Home Assistant, pre-installed", "Alerts by push, text, email and alarm — including when you’re away.")],
        stats=[("2", "pumps take turns, weekly"), ("4", "temperature probes"), ("0", "subscriptions")]),
    "O15": dict(
        folder="O15-terrarium/concepts/A-living-demo-theater", name="Terrarium Control Pro", serif=True,
        acc="#2fd3c4", acc2="#ffb340", bg="background:radial-gradient(ellipse 70% 40% at 25% 0%,#ffb34026,transparent 70%),radial-gradient(ellipse 80% 50% at 70% 100%,#2fd3c41f,transparent 70%),linear-gradient(180deg,#0d1612 0,#16261f 55%,#0f1a15 100%)",
        lock='<div class="lock"><img src="assets/tcp-mark-white.svg"><div><b>Terrarium<br><span>Control Pro</span></b><small>CONCEPT MARK</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="TERRARIUM CONTROL PRO",
        eyebrow="HOW IT ALL CONNECTS · UP TO THREE ENCLOSURES",
        h1="One controller for the whole shelf.",
        sub="Heat, light and misting for up to three enclosures. From one controller. No subscription.",
        svg=terrarium_svg,
        legend=[("Temperature probes (4 in Pro)", "Hot side, cool side, basking spot and a second enclosure — a thermostat on any outlet. Too hot or a probe unplugged: heat turns off and you’re told."),
                ("Door switch", "Pauses misting and fans while you’re feeding. Concept."),
                ("Power Hub", "8 on/off outlets: heat mat, ceramic emitter, basking lamp, UVB, day light, mister, fan and a spare."),
                ("Day/night cycles", "Lights and temperatures follow a natural day, with seasonal ramps."),
                ("Mister reservoir float", "Stops misting before the reservoir runs dry. Concept."),
                ("Home Assistant, full control", "Setpoints and outlets from your dashboards. Add humidity with your own wireless sensor.")],
        stats=[("8", "switched outlets"), ("4", "temperature probes in Pro"), ("2–3", "enclosures from one kit")]),
    "C01": dict(
        folder="C01-cold-plunge/concepts/A-living-demo-theater", name="Cold Plunge Control Pro", serif=True,
        acc="#5fb4ff", acc2="#ffb340",
        bg="background:radial-gradient(ellipse 90% 40% at 50% 104%,#f6c58a33,transparent 60%),linear-gradient(180deg,#0a1320 0,#14263d 55%,#2a4a6c 100%)",
        lock='<div class="lock"><div><b>Cold Plunge<br><span>Control Pro</span></b><small>WORKING NAME · CONCEPT</small></div></div>',
        cf="assets/control-freak-corporate-wordmark-white.svg", foot="COLD PLUNGE CONTROL PRO",
        eyebrow="HOW IT ALL CONNECTS · TUB, CHILLER AND PUMP",
        h1="Ready when you are, from one controller.",
        sub="Keep your tub, chiller, pump, ozone and UV. The Power Hub switches their power, and the probes and flow switch watch the water — so you just step in.",
        svg=plunge_svg,
        legend=[("Water and air probes", "Holds your temperature, all day. Winter mode runs the pump when the air nears freezing."),
                ("Flow switch", "The chiller only runs with water flowing."),
                ("Chiller-outlet probe (Pro)", "Shows the chiller is cooling, and flags early if it slows down."),
                ("Filter pressure sender (Pro)", "Tells you to clean the filter before flow drops."),
                ("Power Hub", "Switches your chiller’s power. Ozone and UV run only while the pump moves water. Heater outlet for hot/cold tubs (Pro)."),
                ("Home Assistant, pre-installed", "Alerts by push, text, email and alarm. Ask Alexa if the plunge is ready.")],
        stats=[("2", "probes: water and air"), ("1", "flow switch · no dry runs"), ("0", "subscriptions")]),
}


def page(c: dict) -> str:
    head_font = "'Fraunces'" if c["serif"] else "'Space Grotesk'"
    legend = "".join(f'<div class="li"><span class="n">{i}</span><div><b>{html.escape(t)}</b><p>{html.escape(d)}</p></div></div>'
                     for i, (t, d) in enumerate(c["legend"], 1))
    stats = "".join(f'<div class="st"><b>{n}</b><span>{html.escape(t)}</span></div>' for n, t in c["stats"])
    cf = (f'<span class="cfw2">BROUGHT TO YOU BY <img src="{c["cf"]}" alt="Control Freak"></span>' if c["cf"] else "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(c['name'])} · how it all connects</title>
<link href="{FONTS}" rel="stylesheet"><style>
@page{{size:8.5in 11in;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{-webkit-print-color-adjust:exact;print-color-adjust:exact;--acc:{c['acc']};--acc2:{c['acc2']}}}
.pg{{width:8.5in;height:11in;position:relative;overflow:hidden;font-family:Inter;color:#fff;background:#0b141e}}
.bg{{position:absolute;inset:-10px;{c['bg']}}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,#0b141ecc 0,#0b141e66 30%,#0b141e99 70%,#0b141ef0 100%)}}
.head{{position:absolute;top:.45in;left:.5in;right:.5in;display:flex;justify-content:space-between;align-items:flex-start;gap:24px;z-index:2}}
.live{{font:600 9px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-bottom:8px}}
h1{{font:700 30px/1.05 {head_font};letter-spacing:-.02em;text-shadow:0 2px 20px #0008;max-width:5.3in}}
.sub{{font:400 12px/1.5 Inter;color:#dbe7ef;max-width:5.1in;margin-top:10px}}
.lock{{display:flex;align-items:center;gap:9px;color:#fff;flex:none}}.lock img{{width:.62in}}
.lock b{{font:700 17px/1 {head_font};letter-spacing:-.01em;display:block}}.lock b span{{color:var(--acc)}}
.lock small{{display:block;font:600 6.5px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-top:4px}}
.cc{{position:absolute;font:600 8px Montserrat;letter-spacing:.2em;text-transform:uppercase;padding:4px 8px;border:1px solid currentColor;border-radius:2px;color:var(--acc2);z-index:3}}
.panel{{position:absolute;left:.4in;right:.4in;top:2.15in;height:4.9in;border-radius:22px;background:#0b141e8c;border:1px solid #ffffff22;backdrop-filter:blur(6px);z-index:2;padding:.12in .15in}}
svg.dg{{width:100%;height:100%}}
.cfw{{font:700 11px 'Space Grotesk';letter-spacing:.18em;fill:#e9eef4}}
.olab{{font:600 10px Inter;fill:#e9eef4;text-anchor:middle}}
.slab{{font:600 10px 'IBM Plex Mono';letter-spacing:.08em;fill:#dbe7efcc;text-transform:uppercase}}
.sm{{font:600 9px 'IBM Plex Mono';letter-spacing:.14em;fill:#dbe7ef}}
.ch{{font:600 10px Inter;fill:#fff}}.ch2{{font:500 9px Inter;fill:#dbe7efcc}}
.chip{{fill:#ffffff1a;stroke:#ffffff44}}.glass{{fill:#ffffff1a;stroke:#ffffff44;stroke-width:1.5}}
.water{{fill:color-mix(in srgb,var(--acc) 22%,transparent);stroke:#ffffffaa;stroke-width:2}}
.wline{{fill:none;stroke:var(--acc);stroke-width:2}}
.stand{{fill:#ffffff14;stroke:#ffffff66;stroke-width:2}}
.pit{{fill:#ffffff10;stroke:#ffffff99;stroke-width:3}}
.glassbox{{fill:#ffffff12;stroke:#ffffffaa;stroke-width:2.5}}
.yours{{fill:#ffffff14;stroke:#ffffff88;stroke-width:2;stroke-dasharray:6 4}}
.pipe{{fill:none;stroke:#ffffff77;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}}
.tube{{fill:none;stroke:#3fd68a99;stroke-width:1.6}}
.power{{fill:none;stroke:#141c26;stroke-width:5;stroke-dasharray:8 6;opacity:.0}}
.coral path{{fill:none;stroke:#ff8a65;stroke-width:6;stroke-linecap:round;opacity:.8}}
.probe{{fill:#e9eef4;stroke:#0b1a26;stroke-width:1}}.probe2{{fill:#ffc93c;stroke:#0b1a26;stroke-width:1}}.probe3{{fill:#ff9440;stroke:#0b1a26;stroke-width:1}}
.num text{{font:700 13px 'Space Grotesk';fill:#0b141e}}
.legend{{position:absolute;left:.5in;right:.5in;top:7.2in;display:grid;grid-template-columns:1fr 1fr;gap:9px 22px;z-index:2}}
.li{{display:flex;gap:10px;align-items:flex-start}}
.li .n{{flex:none;width:22px;height:22px;border-radius:50%;background:var(--acc);color:#0b141e;font:700 12px/22px 'Space Grotesk';text-align:center}}
.li b{{font:600 12px/1.25 {head_font};display:block}}.li p{{font:400 10px/1.4 Inter;color:#cfdce6;margin-top:2px}}
.stats{{position:absolute;left:.5in;right:.5in;bottom:.78in;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;z-index:2}}
.st{{display:flex;align-items:center;gap:12px;padding:10px 16px;border-radius:16px;background:#ffffff14;border:1px solid #ffffff2a}}
.st b{{font:700 34px/1 {head_font};color:var(--acc);white-space:nowrap}}.st span{{font:600 8.5px/1.35 'IBM Plex Mono';letter-spacing:.14em;text-transform:uppercase;color:#dbe7ef}}
.bot{{position:absolute;bottom:.35in;left:.5in;right:.5in;display:flex;justify-content:space-between;align-items:center;font:600 8px 'IBM Plex Mono';letter-spacing:.2em;color:#c4ccd3;z-index:2;gap:12px}}
.bot .l{{display:flex;align-items:center;gap:14px}}
.cfw2{{display:flex;align-items:center;gap:8px}}.cfw2 img{{height:22px}}
</style></head><body><div class="pg"><div class="bg"></div><div class="shade"></div>
<div class="head"><div><div class="live">{html.escape(c['eyebrow'])}</div><h1>{html.escape(c['h1'])}</h1><p class="sub">{html.escape(c['sub'])}</p></div>{c['lock']}</div>
<span class="cc" style="top:2.25in;right:.55in">Concept illustration · not to scale</span>
<div class="panel"><svg class="dg" viewBox="0 0 1010 640" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Concept diagram: how {html.escape(c['name'])} connects">{c['svg']()}</svg></div>
<div class="legend">{legend}</div>
<div class="stats">{stats}</div>
<div class="bot"><div class="l"><span>{html.escape(c['foot'])}</span>{cf}</div><span class="cc" style="position:static">Concept · diagram · example layout</span></div>
</div></body></html>"""


# ---------------------------------------------------------------- "Why Home Assistant" page
# Facts about Home Assistant itself: home-assistant.io and analytics.home-assistant.io, read
# 2026-10-26 ("Over 2.7 million households", "1500+ integrations", "Works with over 1000
# brands", "local control and privacy first", "a non-profit and can't be sold or acquired").
# Control Freak specifics stay inside DECISIONS / PUBLIC_BRIEF: HA pre-installed with the CF
# integration, local on the home network (never cloud HA), Alexa and Google through the voice
# bridge and Siri through HomeKit on HA, away alerts through the apps, no subscription.
HA_SOURCE = "Home Assistant figures: home-assistant.io, October 2026."
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
         "It runs on the controller on your home network, not in someone else’s cloud, so it answers right away and keeps working when the internet doesn’t. Your data stays home."),
        ("voice", "Ask, don’t open",
         "Ask Alexa what the status is, tell Google to adjust the temperature, or use Siri through HomeKit, and get automated voice alerts when something is out of balance."),
        ("bolt", "Peace of mind, all over the house",
         f"Anything {own} knows can set off something else: lights, speakers, thermostats and alerts on every phone. A few ideas are below."),
        ("shield", "Nobody can switch it off",
         "Your setup lives in your home, not on a company’s server. Home Assistant is open source, and run by a non-profit that can’t be sold. Control Freak adds no subscription."),
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


def ha_page(c: dict, h: dict) -> str:
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
.grid{{position:absolute;left:.5in;right:.5in;top:2.2in;display:grid;grid-template-columns:1fr 1fr;gap:16px;z-index:2}}
.hc{{padding:14px 16px;border-radius:16px;background:#ffffff12;border:1px solid #ffffff26;min-height:1.28in}}
.hc .ic{{display:inline-flex;width:30px;height:30px;border-radius:9px;background:var(--acc);align-items:center;justify-content:center;margin-bottom:8px}}
.hc svg{{width:18px;height:18px;fill:none;stroke:#0b141e;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
.hc b{{font:600 14px/1.2 {head_font};display:block;margin-bottom:5px}}.hc p{{font:400 10.5px/1.45 Inter;color:#cfdce6}}
.stats{{position:absolute;left:.5in;right:.5in;top:7.0in;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;z-index:2}}
.st{{padding:10px 14px;border-radius:14px;background:#ffffff14;border:1px solid #ffffff2a}}
.st b{{font:700 26px/1 {head_font};color:var(--acc);white-space:nowrap;display:block}}.st span{{font:600 8px/1.35 'IBM Plex Mono';letter-spacing:.12em;text-transform:uppercase;color:#dbe7ef;display:block;margin-top:6px}}
.ideas{{position:absolute;left:.5in;right:.5in;top:8.12in;z-index:2}}
.ideas h2{{font:600 9px 'IBM Plex Mono';letter-spacing:.2em;color:var(--acc2);margin-bottom:8px}}
.ideas .row{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}
.id{{padding:12px 14px;border-radius:14px;background:#ffffff0f;border:1px dashed #ffffff40}}
.id small{{font:600 7px 'IBM Plex Mono';letter-spacing:.18em;color:var(--acc2)}}.id b{{display:block;font:600 12.5px/1.25 {head_font};margin:5px 0 3px}}.id p{{font:400 10px/1.4 Inter;color:#cfdce6}}
.src{{position:absolute;left:.5in;right:.5in;bottom:.72in;font:400 8.5px Inter;color:#9fb1bf;z-index:2}}
.bot{{position:absolute;bottom:.35in;left:.5in;right:.5in;display:flex;justify-content:space-between;align-items:center;font:600 8px 'IBM Plex Mono';letter-spacing:.2em;color:#c4ccd3;z-index:2;gap:12px}}
.bot .l{{display:flex;align-items:center;gap:14px}}.cfw2{{display:flex;align-items:center;gap:8px}}.cfw2 img{{height:22px}}
</style></head><body><div class="pg"><div class="bg"></div><div class="shade"></div>
<div class="head"><div><div class="live">WHY HOME ASSISTANT · PRE-INSTALLED · ON YOUR HOME NETWORK</div><h1>{html.escape(h['h1'])}</h1>
<p class="sub">{html.escape(c['name'])} comes with Home Assistant already installed and the Control Freak integration already connected. You get everything people love about it, without the setup. Just plug it in.</p></div>{c['lock']}</div>
<div class="grid">{cards}</div>
<div class="stats">{stats}</div>
<div class="ideas"><h2>IDEAS YOU CAN BUILD IN HOME ASSISTANT · EXAMPLES WITH YOUR OWN DEVICES</h2><div class="row">{ideas}</div></div>
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

ORDER = ["front", "light-mode", "duo", "ha-home", "why-ha", "infographic", "back"]


def splice(folder: Path) -> None:
    """Rebuild brochure.pdf as front, light-mode, duo, ha-home, why-ha, infographic, back: the
    brochure's own five pages plus why-ha.pdf and infographic.pdf."""
    pdf = folder / "brochure.pdf"
    # pypdf, not pdfseparate/pdfunite: those copy every shared font and image once per page.
    src = PdfReader(pdf)
    n = len(src.pages)
    assert n in (5, 6, 7), f"{folder}: unexpected {n} pages"
    base = list(src.pages[:4]) + [src.pages[n - 1]]   # the brochure's own five pages (earlier inserts dropped)
    w = PdfWriter()
    for pg in base[:4] + list(PdfReader(folder / "why-ha.pdf").pages) + list(PdfReader(folder / "infographic.pdf").pages) + [base[4]]:
        w.add_page(pg)
    w.compress_identical_objects(remove_identicals=True, remove_orphans=True)
    with open(f"{pdf}.tmp", "wb") as f:
        w.write(f)
    os.replace(f"{pdf}.tmp", pdf)
    # the brochure's own page PNGs stay; the infographic PNG comes from this build
    ims = [Image.open(folder / f"{n}.png").convert("RGB") for n in ORDER]
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
    (folder / "infographic.html").write_text(page(c), encoding="utf-8")
    (folder / "why-ha.html").write_text(ha_page(c, HA[code]), encoding="utf-8")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(RENDER); js = f.name
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    for n in ("infographic", "why-ha"):
        subprocess.run(["node", js, "file://" + str(folder / f"{n}.html"), str(folder / f"{n}.pdf"),
                        str(folder / f"{n}.png")], check=True, env=env)
    os.unlink(js)
    splice(folder)
    print("built", folder.relative_to(BRO))


SITE = {"O04": "O04-reef", "C03": "C03-basement-guard", "O15": "O15-reptile", "C01": "C01-cold-plunge"}

SVG_CSS = """.cfw{font:700 11px 'Space Grotesk',sans-serif;letter-spacing:.18em;fill:#e9eef4}
.olab{font:600 10px Inter,sans-serif;fill:#e9eef4;text-anchor:middle}
.slab{font:600 10px 'IBM Plex Mono',monospace;letter-spacing:.08em;fill:#dbe7efcc;text-transform:uppercase}
.sm{font:600 9px 'IBM Plex Mono',monospace;letter-spacing:.14em;fill:#dbe7ef}
.ch{font:600 10px Inter,sans-serif;fill:#fff}.ch2{font:500 9px Inter,sans-serif;fill:#dbe7efcc}
.chip{fill:#ffffff1a;stroke:#ffffff44}.glass{fill:#ffffff1a;stroke:#ffffff44;stroke-width:1.5}
.water{fill:ACC33;stroke:#ffffffaa;stroke-width:2}.wline{fill:none;stroke:ACC;stroke-width:2}
.stand{fill:#ffffff14;stroke:#ffffff66;stroke-width:2}.pit{fill:#ffffff10;stroke:#ffffff99;stroke-width:3}
.glassbox{fill:#ffffff12;stroke:#ffffffaa;stroke-width:2.5}
.yours{fill:#ffffff14;stroke:#ffffff88;stroke-width:2;stroke-dasharray:6 4}
.pipe{fill:none;stroke:#ffffff77;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}
.tube{fill:none;stroke:#3fd68a99;stroke-width:1.6}.power{opacity:0}
.coral path{fill:none;stroke:#ff8a65;stroke-width:6;stroke-linecap:round;opacity:.8}
.probe{fill:#e9eef4;stroke:#0b1a26;stroke-width:1}.probe2{fill:#ffc93c;stroke:#0b1a26;stroke-width:1}.probe3{fill:#ff9440;stroke:#0b1a26;stroke-width:1}
.num text{font:700 13px 'Space Grotesk',sans-serif;fill:#0b141e}"""

SITE_CSS = """
/* How it all connects (Design build_infographic.py, 2026-10-26) */
.connects figure{position:relative;margin:24px 0 0;border-radius:24px;overflow:hidden;border:1px solid var(--line);background:#0b141e}
.connects figure img{display:block;width:100%;height:auto}
.connects figure .tag{z-index:1;left:auto;right:14px}
.connects figcaption{padding:10px 18px 14px}
.connects ol{list-style:none;padding:0;margin:24px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px 28px;counter-reset:c}
.connects li{display:flex;gap:12px;align-items:flex-start;counter-increment:c}
.connects li::before{content:counter(c);flex:none;width:26px;height:26px;border-radius:50%;background:var(--accent,var(--teal));color:var(--onaccent,#0b141e);font-weight:800;text-align:center;line-height:26px;font-size:.85rem}
.connects li b{display:block}.connects li span{color:var(--muted);font-size:.93rem}
.connects .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:24px}
.connects .stats div{display:flex;align-items:center;gap:14px;padding:14px 18px;border-radius:18px;border:1px solid var(--line)}
.connects .stats b{font-family:var(--display);font-size:2.2rem;line-height:1;color:var(--accent,var(--teal));white-space:nowrap}
.connects .stats span{color:var(--muted);font-size:.85rem;text-transform:uppercase;letter-spacing:.1em}
"""


def site(code: str, root: Path) -> None:
    """Write the product site's diagram SVG and its "How it all connects" section."""
    c = P[code]
    d = root / "products" / SITE[code] / "site"
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1010 615" role="img" aria-label="Concept diagram: how {html.escape(c["name"])} connects">'
           f'<style>{SVG_CSS.replace("ACC", c["acc"])}</style><rect width="1010" height="615" fill="#0b141e"/>'
           f'<g style="--acc:{c["acc"]}">{c["svg"]().replace("var(--acc)", c["acc"])}</g></svg>')
    (d / "assets" / "how-it-connects.svg").write_text(svg, encoding="utf-8")
    legend = "".join(f"<li><div><b>{html.escape(t)}</b><span>{html.escape(x)}</span></div></li>" for t, x in c["legend"])
    stats = "".join(f"<div><b>{n}</b><span>{html.escape(t)}</span></div>" for n, t in c["stats"])
    sec = (f'<section id="connects"><div class="wrap connects">\n'
           f'  <div class="eyebrow">How it all connects</div><h2>{html.escape(c["h1"])}</h2>\n'
           f'  <p class="lead">{html.escape(c["sub"])}</p>\n'
           f'  <figure><span class="tag">Concept</span><a href="assets/how-it-connects.svg" target="_blank" rel="noopener"><img src="assets/how-it-connects.svg" alt="Concept diagram of how {html.escape(c["name"])} connects: sensors on colour-coded leads to the controller, the Power Hub with labelled outlets, and Home Assistant, phone, voice and alerts" loading="lazy"></a>'
           f'<figcaption class="small">Concept illustration, not to scale. Your own equipment is drawn dashed. Tap to open full size.</figcaption></figure>\n'
           f'  <ol>{legend}</ol>\n  <div class="stats">{stats}</div>\n</div></section>\n\n')
    idx = d / "index.html"
    t = idx.read_text(encoding="utf-8")
    if '<section id="connects">' in t:
        a = t.index('<section id="connects">'); b = t.index("</section>", a) + len("</section>\n\n")
        t = t[:a] + t[b:]
    t = t.replace('<section id="demo">', sec + '<section id="demo">', 1)
    idx.write_text(t, encoding="utf-8")
    css = d / "styles.css"
    st = css.read_text(encoding="utf-8")
    if "How it all connects (Design" not in st:
        css.write_text(st.rstrip("\n") + "\n" + SITE_CSS, encoding="utf-8")
    print("site", d.relative_to(root))

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
           f'  <h3 class="ideas">Ideas you can build in Home Assistant · examples with your own devices</h3>\n'
           f'  <div class="grid angles">{ideas}</div>\n'
           f'  <p class="small" style="margin-top:18px">{HA_SOURCE} Home Assistant is a trademark of the Open Home Foundation. Your lights, speakers and thermostat aren’t in the box. Concept · example automations.</p>\n'
           f'</div></section>\n\n')
    idx = d / "index.html"
    t = idx.read_text(encoding="utf-8")
    if '<section id="home-assistant">' in t:
        a = t.index('<section id="home-assistant">'); b = t.index("</section>", a) + len("</section>\n\n")
        t = t[:a] + t[b:]
    t = t.replace('<section id="connects">', sec + '<section id="connects">', 1)
    idx.write_text(t, encoding="utf-8")
    css = d / "styles.css"
    st = css.read_text(encoding="utf-8")
    if "Why Home Assistant (Design" not in st:
        css.write_text(st.rstrip("\n") + "\n" + HA_SITE_CSS, encoding="utf-8")
    print("site ha", d.relative_to(root))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--site":       # --site /path/to/controlfreak-platform-public [codes]
        root = Path(args[1])
        for code in (args[2:] or list(P)):
            site(code, root)
            site_ha(code, root)
    else:
        for code in (args or list(P)):
            build(code)
