"""Serial cold-search benchmarks, separate timing from traced allocation measurement."""
from pathlib import Path
from collections import Counter
import json,random,time,tracemalloc,platform,statistics
from .rules import *
from .search import Search

def main():
    out=[]
    for c in CORE:
        s=initial(c);h=Counter({key(s):1});rng=random.Random(801);positions=[]
        for step in range(40):
            if terminal(s,c,h)[0] is not None:break
            if step%3==0:positions.append((s,h.copy()))
            s=apply_unchecked(s,rng.choice(legal(s,c)),c);h[key(s)]+=1
        positions=positions[:8];rows=[]
        for cache in (False,True):
            times=[];nodes=[];depths=[];hits=[]
            for s,h in positions:
                engine=Search(c,cache=cache);start=time.perf_counter();m,st=engine.choose(s,h,4,1200,random.Random(1));times.append(time.perf_counter()-start);nodes.append(st['nodes']);depths.append(st['depth']);hits.append(st['cache_hits'])
            s,h=positions[0];tracemalloc.start();Search(c,cache=cache).choose(s,h,4,1200,random.Random(1));_,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
            rows.append(dict(cache=cache,positions=len(positions),seconds=times,nodes=nodes,depths=depths,cache_hits=hits,peak_traced_bytes_initial_search=peak))
        out.append(dict(candidate=c.candidate,measurements=rows))
    Path('research/results/r0/bench.json').write_text(json.dumps(dict(python=platform.python_version(),platform=platform.platform(),note='Serial within this process; other experiments may share CPU. Traced memory excludes interpreter and input state.',data=out),indent=2)+'\n')
    print('Search benchmarks saved')
if __name__=='__main__':main()
