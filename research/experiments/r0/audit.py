"""Independent transition/terminal checks for all final R0 recorded executions."""
from pathlib import Path
from collections import Counter
import json
from .rules import *
from .oracle import predict,outcome
from .run import play,AGENTS
from .report import load

def main():
    rows=load('*.json');positions=0;replays=0;identities=set()
    for row in rows:
        c=Config(**row['config']);s=initial(c);h=Counter({key(s):1});identity=json.dumps([row['config'],row['agents'],row['seed'],row['opening'],row['profile']],sort_keys=True);identities.add(identity)
        for m in row['prefix']:
            s=apply(s,tuple(m),c,h);h[key(s)]+=1
        for index,raw in enumerate(row['trace']):
            m=tuple(raw);reference=terminal(s,c,h);independent=outcome(s.board,s.turn,s.reserves,s.ply,h[key(s)],c)
            assert reference==independent==(None,None)
            expected=predict(s.board,s.turn,s.reserves,c);assert m in expected
            t=apply(s,m,c,h);assert (t.board,t.reserves)==expected[m];invariant(t,c);positions+=1
            st=row['search'][index];agent=row['agents'][index%2]
            assert 0<=st['nodes']<=AGENTS[agent][1] and 0<=st['depth']<=AGENTS[agent][0]
            s=t;h[key(s)]+=1
        assert terminal(s,c,h)==outcome(s.board,s.turn,s.reserves,s.ply,h[key(s)],c)==(row['winner'],row['reason'])
        assert s.ply==row['plies']
        if c in CORE and row['agents']==['deep','tactical'] and row['seed']==0 and row['profile']=='structure' and row['opening']=='canonical' and c.candidate not in locals().get('done',set()):
            if 'done' not in locals():done=set()
            again=play(c,*row['agents'],row['seed'],row['opening'],row['profile'])
            for field in ('winner','reason','plies','prefix','trace','branches','search','events'):
                assert json.loads(json.dumps(again[field]))==row[field],(c.name,field)
            done.add(c.candidate);replays+=1
    result=dict(recorded_executions=len(rows),distinct_trial_identities=len(identities),independent_transitions_checked=positions,independent_terminal_checks=True,exact_representative_replays=replays,excluded_from_replay=['elapsed timing'])
    Path('research/results/r0/audit.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
