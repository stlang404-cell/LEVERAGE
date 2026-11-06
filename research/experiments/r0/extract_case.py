"""Freeze the first repeated A5 canonical seed-0 deep/tactical position, with history."""
from pathlib import Path
from collections import Counter
import json,hashlib
from .rules import *

def main():
    source=Path('research/results/r0/A_main.json');rows=json.loads(source.read_text())['games'];row=next(r for r in rows if r['agents']==['deep','tactical'] and r['seed']==0 and r['opening']=='canonical');c=Config(**row['config']);s=initial(c);h=Counter({key(s):1});prefix=[]
    for raw in row['prefix']+row['trace']:
        m=tuple(raw);s=apply(s,m,c,h);h[key(s)]+=1;prefix.append(m)
        if h[key(s)]==2:break
    assert h[key(s)]==2 and terminal(s,c,h)[0] is None
    case=dict(rule_version='EA-0.3.0',config=row['config'],source_file=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source_agents=row['agents'],seed=0,board=s.board,turn=s.turn,reserves=s.reserves,ply=s.ply,remaining_plies=120-s.ply,trace_prefix=prefix,legal_actions=legal(s,c),history=[dict(board=k[0],turn=k[1],reserves=k[2],count=count) for k,count in sorted(h.items()) if count>0],status='First repetition (count 2), not yet a terminal draw. No winning/drawing conclusion from this extraction.')
    Path('research/results/r0/repetition_case.json').write_text(json.dumps(case,separators=(',',':'))+'\n');print('Preserved first repeated position at ply',s.ply,'with',len(case['history']),'history entries')
if __name__=='__main__':main()
