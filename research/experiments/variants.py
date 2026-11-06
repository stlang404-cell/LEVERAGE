"""Isolated Leverage follow-up; never mixes altered rules into v0.1 games.json."""
import arena, json
from collections import Counter
from pathlib import Path
base_moves,base_apply=arena.moves,arena.apply

def run(variant):
    def transition(s,m,game):
        t=base_apply(s,m,game)
        if variant=='own_cleanup':
            b=list(t.board);keep=arena.connected(b,s.turn)
            for k,v in enumerate(b):
                if v*s.turn>0 and k not in keep:b[k]=0
            t=arena.replace(t,board=tuple(b))
        return t
    def legal(s,game):
        ms=base_moves(s,game)
        if variant=='strict_connected':
            ms=[m for m in ms if len(arena.connected(base_apply(s,m,game).board,s.turn))==sum(v*s.turn>0 for v in base_apply(s,m,game).board)]
        return ms
    arena.moves=legal;arena.apply=transition
    rows=[]
    for a,b in [('random','random'),('greedy','random'),('search','greedy')]:
        for seed in range(8):
            rows.extend([arena.play('leverage',a,b,seed),arena.play('leverage',b,a,seed)])
    arena.moves=base_moves;arena.apply=base_apply
    return rows
if __name__=='__main__':
    result={v:run(v) for v in ('strict_connected','own_cleanup')}
    Path('research/results/variants.json').write_text(json.dumps(result))
    for v,rows in result.items():print(v,dict(Counter(x['winner'] for x in rows)),dict(Counter(x['reason'] for x in rows)))
