"""Exploratory post-main A ablations and larger-budget A/C strength checks."""
from dataclasses import replace
from pathlib import Path
import json
from .rules import A,C
from .run import play
if __name__=='__main__':
    controls=[replace(A,name='A5_rooted',deployment='rooted'),replace(A,name='A5_target_only',collapse=False),replace(A,name='A5_component_power',power='component'),replace(A,name='A5_formation',formation=True),replace(A,name='A5_reserve3',reserve=3),replace(A,name='A5_reserve7',reserve=7)]
    rows=[]
    for c in controls:
        for seed in range(8):rows.extend([play(c,'deep','tactical',seed),play(c,'tactical','deep',seed)])
        print(c.name,'done',flush=True)
    Path('research/results/r0/A_ablations.json').write_text(json.dumps(dict(protocol='exploratory-post-main',games=rows),separators=(',',':'))+'\n')
    rows=[]
    for c in (A,C):
        for seed in range(8):rows.extend([play(c,'deep6','deep',seed),play(c,'deep','deep6',seed)])
        print(c.name,'deep6 done',flush=True)
    Path('research/results/r0/strength6000.json').write_text(json.dumps(dict(protocol='depth6-6000-vs-depth4-1200',games=rows),separators=(',',':'))+'\n')
