"""Final R0 predeclared tournament. Run as python -m research.experiments.r0.run."""
from .rules import *
from .search import Search
from collections import Counter
from dataclasses import asdict,replace
from pathlib import Path
import json,random,time,platform,argparse,resource
AGENTS={'random':(0,0),'greedy':(1,1200),'tactical':(2,1200),'deep':(4,1200),'deep6':(6,6000)}
def play(c,a,b,seed,opening='canonical',profile='structure'):
    s=initial(c);h=Counter({key(s):1});rng=random.Random(seed);searches={p:Search(c,profile=profile) for p in (1,-1)};trace=[];stats=[];branches=[];times=[];events=Counter();prefix=[]
    if opening=='random2':
        for _ in range(2):
            m=random.Random(seed*31+s.ply).choice(legal(s,c));prefix.append(m);s=apply_unchecked(s,m,c);h[key(s)]+=1
    start=time.perf_counter()
    while True:
        win,reason=terminal(s,c,h)
        if win is not None:break
        agent=a if s.turn==1 else b;depth,budget=AGENTS[agent];ms=legal(s,c);branches.append(len(ms));t=time.perf_counter()
        if depth==0:m=rng.choice(ms);st=dict(nodes=0,depth=0,cache_hits=0,iterations=[],cache_entries=0)
        else:m,st=searches[s.turn].choose(s,h,depth,budget,rng)
        times.append(time.perf_counter()-t)
        old=sum(v not in (0,3) for v in s.board);captured=s.board[m[2]]*s.turn<0
        s=apply_unchecked(s,m,c);invariant(s,c);h[key(s)]+=1;trace.append(m);stats.append(st)
        if captured:
            events['captures']+=1
            if old-sum(v not in (0,3) for v in s.board)>1:events['multi_piece_collapses']+=1
        if c.candidate=='A' and s.board.count(2)==s.board.count(-2)==1 and sum(v!=0 for v in s.board)==2 and s.reserves==(0,0):events['anchor_only_plies']+=1
    return dict(config=asdict(c),agents=[a,b],seed=seed,opening=opening,prefix=prefix,profile=profile,winner=win,reason=reason,plies=s.ply,trace=trace,branches=branches,search=stats,move_seconds=times,seconds=time.perf_counter()-start,events=dict(events))
def write_result(data,output):
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    # These names are owned generated outputs; remove stale parts on a repeat run.
    for old in output.parent.glob(output.stem+'_part*.json'):old.unlink()
    payload=json.dumps(data,separators=(',',':'))+'\n'
    if len(payload.encode())<=1800000:output.write_text(payload);return [str(output)]
    paths=[]
    for start in range(0,len(data['games']),100):
        part=dict(data,games=data['games'][start:start+100],part=start//100+1,total_games=len(data['games']))
        path=output.with_name(output.stem+f'_part{start//100+1}.json');path.write_text(json.dumps(part,separators=(',',':'))+'\n');paths.append(str(path))
    if output.exists():output.unlink()
    return paths
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--seeds',type=int,default=32);ap.add_argument('--sizes',action='store_true');ap.add_argument('--candidate',choices=['A','B','C']);ap.add_argument('--output-dir',default='research/results/r0');args=ap.parse_args()
    configs=[c for c in CORE if not args.candidate or c.candidate==args.candidate]
    for c in configs:
        rows=[]
        if not args.sizes:
            for seed in range(args.seeds):
                opening='canonical' if seed%2==0 else 'random2'
                rows.append(play(c,'random','random',seed,opening))
                for a,b in [('greedy','random'),('tactical','greedy'),('deep','tactical')]:
                    rows.extend([play(c,a,b,seed,opening),play(c,b,a,seed,opening)])
        else:
            for n in (6,7):
                variant=replace(c,name=c.candidate+str(n),size=n)
                for seed in range(args.seeds):
                    rows.extend([play(variant,'deep','tactical',seed),play(variant,'tactical','deep',seed)])
        output=Path(args.output_dir)/f"{c.candidate}_{'sizes' if args.sizes else 'main'}.json"
        data=dict(protocol='r0-1',agents=AGENTS,seed_count=args.seeds,python=platform.python_version(),platform=platform.platform(),max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,games=rows)
        print(write_result(data,output),len(rows),'games',flush=True)
if __name__=='__main__':main()
