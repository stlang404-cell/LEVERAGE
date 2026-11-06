"""Exact A anchor-only retrograde tablebases and bounded C finite-game proof search."""
from collections import deque,defaultdict,Counter
from pathlib import Path
from dataclasses import replace
import json,time
from .rules import *

def anchors(n,table=False):
    states=[(a,b,p) for a in range(n*n) for b in range(n*n) if a!=b for p in (1,-1)];outcomes={};remaining={};parents=defaultdict(list);distance={};q=deque()
    for st in states:
        a,b,p=st;origin=a if p==1 else b;target=b if p==1 else a
        if target in adj(origin,n):outcomes[st]=1;distance[st]=1;q.append(st)
        children=[]
        for dest in adj(origin,n):
            if dest!=target:children.append((dest,b,-p) if p==1 else (a,dest,-p))
        remaining[st]=len(children)
        for child in children:parents[child].append(st)
    while q:
        child=q.popleft()
        for parent in parents[child]:
            if parent in outcomes:continue
            if outcomes[child]==-1:outcomes[parent]=1;distance[parent]=distance[child]+1;q.append(parent)
            else:
                remaining[parent]-=1
                if remaining[parent]==0:
                    outcomes[parent]=-1;distance[parent]=distance[child]+1;q.append(parent)
    if table:return outcomes,distance
    return dict(size=n,states=len(states),win=sum(v==1 for v in outcomes.values()),loss=sum(v==-1 for v in outcomes.values()),draw=len(states)-len(outcomes),max_attractor_layers=max(distance.values()),fresh_history=True)
def solve_c(n,budget):
    c=replace(C,name='C'+str(n),size=n);cache={};nodes=0;start=time.perf_counter()
    def solve(s):
        nonlocal nodes
        k=key(s)
        if k in cache:return cache[k]
        if nodes>=budget:return None
        nodes+=1
        win,_=terminal(s,c,{})
        if win is not None:v=win*s.turn;cache[k]=v;return v
        unknown=False
        for m in legal(s,c):
            v=solve(apply_unchecked(s,m,c))
            if v==-1:cache[k]=1;return 1
            if v is None:unknown=True
        if unknown:return None
        cache[k]=-1;return -1
    root=initial(c);value=solve(root)
    return dict(size=n,budget=budget,nodes=nodes,proven_states=len(cache),root_value=value,seconds=time.perf_counter()-start,semantics='value from first side; null = UNKNOWN, not draw')
if __name__=='__main__':
    out=dict(A=[anchors(n) for n in (5,6,7)],C=[solve_c(n,250000) for n in (3,4,5)])
    Path('research/results/r0/endgames.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
