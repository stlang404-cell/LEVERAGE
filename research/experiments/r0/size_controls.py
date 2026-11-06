"""Canonical 5x5 counterparts to the four-seed 6x6/7x7 sweeps."""
from pathlib import Path
import json
from .rules import B,C
from .run import play,write_result
if __name__=='__main__':
    for c in (B,C):
        rows=[]
        for seed in range(4):rows.extend([play(c,'deep','tactical',seed),play(c,'tactical','deep',seed)])
        print(write_result(dict(protocol='canonical-size-control',games=rows),Path('research/results/r0')/(c.candidate+'_canonical_control.json')),flush=True)
