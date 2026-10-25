#!/usr/bin/env python3
"""Build site/dist from site/src. Usage: python3 site/build.py"""
import re,shutil,pathlib
R=pathlib.Path(__file__).parent; S=R/'src'; D=R/'dist'
shutil.rmtree(D,ignore_errors=True); shutil.copytree(S,D,ignore=shutil.ignore_patterns('pages','partials'))
def part(mo):
    a=dict(re.findall(r'(\w+)="([^"]*)"',mo.group(2))); t=(S/'partials'/f'{mo.group(1)}.html').read_text().rstrip('\n')
    a['cls']=f' class="{a["cls"]}"' if a.get('cls') else ''
    return re.sub(r'\{\{(\w+)\}\}',lambda m:a.get(m.group(1),''),t)
for p in (S/'pages').glob('*.html'):
    (D/p.name).write_text(re.sub(r'\{\{> (\w+)((?: \w+="[^"]*")*)\}\}',part,p.read_text())); print('built',p.name)
