"""Simplified PCB favicon masters — small-size simplification of the corporate PCB wordmark
(brand/corporate/control-freak-corporate-wordmark-*.svg). Reuses ONLY elements of that art:
the corporate 'C' glyph outline (scaled 1.35x about its centre), the two bus bars (y329/y491)
and their terminal nodes. Traces/nodes thickened for 16-48px legibility. Not a new logo. Run from repo root."""
import re, pathlib
R=pathlib.Path(__file__).resolve().parents[2]
src=(R/"brand/corporate/control-freak-corporate-wordmark-navy.svg").read_text()
d=re.search(r'<path d="(M[^"]*?)\s*M213',src).group(1)  # C glyph subpath
COL={"navy":"#0b1f3a","white":"#ffffff","cream":"#efe9df","forest":"#0f2e2c","gold":"#a8834f","cool-blue":"#2f6f9f"}
SW,NR=18,24
def svg(ink):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="28 265 290 290" role="img" aria-label="Control Freak"><title>Control Freak — PCB favicon icon (simplified corporate mark)</title>
<g fill="{ink}"><path transform="translate(108 410.5) scale(1.35) translate(-108 -410.5)" d="{d}"/>
<g fill="none" stroke="{ink}" stroke-width="{SW}" stroke-linejoin="round"><path d="M120 329H290M120 491H290"/></g>
<circle cx="285" cy="329" r="{NR}"/><circle cx="285" cy="491" r="{NR}"/><path d="M174 410.5H250" fill="none" stroke="{ink}" stroke-width="{SW}"/><circle cx="252" cy="410.5" r="{NR}"/></g></svg>
'''
for k,v in COL.items():(R/f"brand/app-icons/_unused/_masters/control-freak-pcb-icon-{k}.svg").write_text(svg(v))
print("masters ok")
