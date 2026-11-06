"""Recheck recorded traces and replay seven representative deep-agent games."""
from pathlib import Path
from collections import Counter
import json
from continuation import Config,initial,key,moves,transition,result,play
r=json.loads(Path('research/results/continuation.json').read_text());configs={x['name']:Config(**x) for x in r['configs']};plies=0;replayed=0
for row in r['games']:
 c=configs[row['config']];s=initial(c);h=Counter({key(s):1})
 for raw in row['trace']:
  m=tuple(raw);assert result(s,c,h)[0] is None;assert m in moves(s,c)
  s=transition(s,m,c);h[key(s)]+=1;plies+=1
 assert result(s,c,h)==(row['winner'],row['reason'])
 assert s.ply==row['plies'] and row['nodes']<=row['budget']*s.ply
 if row['agents']==['deep','tactical'] and row['seed']==0:
  again=play(c,*row['agents'],row['seed'],row['budget'])
  for field in ('winner','reason','plies','branches','depths','nodes','trace','stranded_side_positions'):
   assert json.loads(json.dumps(again[field]))==row[field],(c.name,field)
  replayed+=1
out=dict(games_audited=len(r['games']),legal_transitions_audited=plies,representative_games_exactly_replayed=replayed,comparison_excludes='elapsed times',independent_rules_oracle=False)
Path('research/results/continuation_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
