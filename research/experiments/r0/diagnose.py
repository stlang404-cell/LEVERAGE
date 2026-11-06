"""Classify recorded v0.2 draws without changing their results or frozen engine."""
from pathlib import Path
from collections import Counter,defaultdict
import json
from .. import continuation as old

def main():
    data=json.loads(Path('research/results/continuation.json').read_text());cs={x['name']:old.Config(**x) for x in data['configs']};groups=defaultdict(list);rows=[]
    for row in data['games']:
        c=cs[row['config']];s=old.initial(c);h=Counter({old.key(s):1});seen_anchor_only=False;first=None;captures=0;material=[];first_seen={old.key(s):0};repeat_gap=None
        for raw in row['trace']:
            m=tuple(raw);captures+=int(s.board[m[2]]*s.turn<0);s=old.transition(s,m,c);h[old.key(s)]+=1
            anchor_only=s.board.count(2)==s.board.count(-2)==1 and sum(v!=0 for v in s.board)==2 and s.reserve==(0,0)
            if anchor_only and first is None:first=s.ply
            seen_anchor_only|=anchor_only
            if old.key(s) in first_seen:repeat_gap=s.ply-first_seen[old.key(s)]
            else:first_seen[old.key(s)]=s.ply
            material.append(sum(v!=0 for v in s.board))
        out=dict(config=c.name,agents=row['agents'],seed=row['seed'],winner=row['winner'],reason=row['reason'],anchor_only_reached=seen_anchor_only,anchor_only_first_ply=first,captures=captures,terminal_pieces=material[-1],reserves_left=sum(s.reserve),repeat_span=repeat_gap,completed_depths=dict(Counter(row['depths'])))
        rows.append(out);groups[c.name].append(out)
    summary={name:dict(games=len(rs),draws=sum(x['winner']==0 for x in rs),anchor_only_games=sum(x['anchor_only_reached'] for x in rs),draw_reasons=dict(Counter(x['reason'] for x in rs if x['winner']==0)),draw_agents={str(pair):sum(x['winner']==0 for x in rs if tuple(x['agents'])==pair) for pair in {tuple(x['agents']) for x in rs}},zero_capture_games=sum(x['captures']==0 for x in rs),limit_with_reserves=sum(x['reason']=='limit' and x['reserves_left']>0 for x in rs)) for name,rs in groups.items()}
    Path('research/results/r0/prior_draw_diagnosis.json').write_text(json.dumps(dict(summary=summary,games=rows),separators=(',',':'),sort_keys=True)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
