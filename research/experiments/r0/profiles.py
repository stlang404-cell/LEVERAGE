"""Untuned alternate evaluator sensitivity; canonical even seeds match main subsets."""
from pathlib import Path
import json
from .rules import CORE
from .run import play
if __name__=='__main__':
    rows=[]
    for c in CORE:
        for seed in range(0,8 if c.candidate=='B' else 16,2):
            rows.extend([play(c,'deep','tactical',seed,profile='material'),play(c,'tactical','deep',seed,profile='material')])
        print(c.name,'alternate evaluator done',flush=True)
    Path('research/results/r0/profiles.json').write_text(json.dumps(dict(protocol='exploratory-material-evaluator',games=rows),separators=(',',':'))+'\n')
