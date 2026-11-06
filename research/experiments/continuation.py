"""LEVERAGE laboratory v0.2. Independent sized rules; never edits arena v0.1."""
from dataclasses import dataclass,replace,asdict
from collections import Counter
import random,json,time,platform,hashlib,math,statistics
from pathlib import Path
@dataclass(frozen=True)
class Config:
    name:str; size:int=5; reserves:int=5; mechanic:str='free'; formation:bool=False
@dataclass(frozen=True)
class State:
    board:tuple; turn:int=1; reserve:tuple=(5,5); ply:int=0
CONFIGS=[Config('free5'),Config('breach5',mechanic='breach'),Config('pressure5',mechanic='pressure'),Config('relay5',mechanic='relay'),Config('pressure6',6,6,'pressure'),Config('pressure7',7,7,'pressure'),Config('pressure5_formation',mechanic='pressure',formation=True)]
def adj(i,n):
    return tuple(j for j in (i-1,i+1,i-n,i+n) if 0<=j<n*n and abs(i%n-j%n)+abs(i//n-j//n)==1)
def initial(c):
    n=c.size;b=[0]*(n*n);x=(n-1)//2;b[x]=2;b[n*n-1-x]=-2;r=c.reserves
    if c.formation:
        for j in (x-1,x+1):b[j]=1;b[n*n-1-j]=-1
        r-=2
    return State(tuple(b),reserve=(r,r))
def key(s):return s.board,s.turn,s.reserve
def component(b,p,n):
    seen={i for i,v in enumerate(b) if v==2*p};todo=list(seen)
    while todo:
        for j in adj(todo.pop(),n):
            if b[j]*p>0 and j not in seen:seen.add(j);todo.append(j)
    return seen
def power(b,i,p,n):return 1+sum(b[j]*p>0 for j in adj(i,n))
def moves(s,c):
    b,p,n=s.board,s.turn,c.size;out=[]
    if 2 not in b or -2 not in b:return out
    if s.reserve[0 if p==1 else 1]:
        for i,v in enumerate(b):
            if v==0 and any(b[j]*p>0 for j in adj(i,n)):out.append(('place',-1,i))
    for i,v in enumerate(b):
        if v*p<=0:continue
        for j in adj(i,n):
            if not b[j]:out.append(('move',i,j))
            elif b[j]*p<0:
                a,d=power(b,i,p,n),power(b,j,-p,n)
                if a>d:out.append(('move',i,j))
                elif a==d:
                    if c.mechanic=='breach' and abs(v)==abs(b[j])==1:out.append(('breach',i,j))
                    if c.mechanic=='pressure':
                        k=2*j-i
                        if 0<=k<n*n and abs(k%n-j%n)+abs(k//n-j//n)==1 and not b[k]:out.append(('push',i,j))
            elif c.mechanic=='relay':
                k=2*j-i
                if 0<=k<n*n and abs(k%n-i%n)+abs(k//n-i//n)==2 and not b[k]:out.append(('move',i,k))
    return sorted(out)
def transition(s,m,c):
    kind,i,j=m;b=list(s.board);p=s.turn;r=list(s.reserve)
    disrupted=b[j]*p<0
    if kind=='place':b[j]=p;r[0 if p==1 else 1]-=1
    elif kind=='breach':b[i]=b[j]=0
    elif kind=='push':b[2*j-i]=b[j];b[j]=b[i];b[i]=0
    else:b[j]=b[i];b[i]=0
    if disrupted:
        keep=component(b,-p,c.size)
        for k,v in enumerate(b):
            if v*p<0 and k not in keep:b[k]=0
    return State(tuple(b),-p,tuple(r),s.ply+1)
def result(s,c,h):
    if 2 not in s.board:return -1,'anchor'
    if -2 not in s.board:return 1,'anchor'
    if h[key(s)]>=3:return 0,'repetition'
    if s.ply>=120:return 0,'limit'
    if not moves(s,c):return 0,'immobile'
    return None,None
def evaluate(s,c):
    p=s.turn;n=c.size
    return sum((1 if v*p>0 else -1)*(20+2*sum(s.board[j]*v>0 for j in adj(i,n))+min(i%n,n-1-i%n,i//n,n-1-i//n)) for i,v in enumerate(s.board) if v)
class Exhausted(Exception):pass
def choose(s,c,agent,rng,h,budget=800):
    ms=moves(s,c)
    if agent=='random':return rng.choice(ms),0,0
    # Terminal-aware shallow ordering is shared, not extra hidden search.
    ordered=list(ms);rng.shuffle(ordered);nodes=0;done=0;best=ordered[0]
    def neg(st,d,alpha,beta):
        nonlocal nodes
        if nodes>=budget:raise Exhausted
        nodes+=1
        win,_=result(st,c,h)
        if win is not None:return win*st.turn*100000 if win else 0
        if not d:return evaluate(st,c)
        val=-float('inf')
        for m in moves(st,c):
            t=transition(st,m,c);h[key(t)]+=1
            try:v=-neg(t,d-1,-beta,-alpha)
            finally:h[key(t)]-=1
            val=max(val,v);alpha=max(alpha,v)
            if alpha>=beta:break
        return val
    maxdepth={'greedy':1,'tactical':2,'deep':4}[agent]
    for depth in range(1,maxdepth+1):
        scores=[]
        try:
            for m in ordered:
                t=transition(s,m,c);h[key(t)]+=1
                try:v=-neg(t,depth-1,-float('inf'),float('inf'))
                finally:h[key(t)]-=1
                scores.append((v,m))
        except Exhausted:break
        scores.sort(key=lambda x:x[0],reverse=True);best=scores[0][1];ordered=[m for _,m in scores];done=depth
    return best,nodes,done

def play(c,a,b,seed,budget=800):
    s=initial(c);h=Counter({key(s):1});rng=random.Random(seed);br=[];depths=[];nodes=0;trace=[];elapsed=[];stranded=0
    while True:
        win,reason=result(s,c,h)
        if win is not None:break
        br.append(len(moves(s,c)));start=time.perf_counter()
        m,ns,d=choose(s,c,a if s.turn==1 else b,rng,h,budget);elapsed.append(time.perf_counter()-start);nodes+=ns;depths.append(d)
        trace.append(m);s=transition(s,m,c);h[key(s)]+=1
        stranded+=sum(len(component(s.board,p,c.size))<sum(v*p>0 for v in s.board) for p in (1,-1))
    return dict(config=c.name,agents=[a,b],seed=seed,budget=budget,winner=win,reason=reason,plies=s.ply,branches=br,depths=depths,nodes=nodes,seconds=elapsed,trace=trace,stranded_side_positions=stranded)
def main():
    rows=[];start=time.time()
    for c in CONFIGS:
        for seed in range(8):
            rows.append(play(c,'random','random',seed))
            for a,b in [('greedy','random'),('tactical','greedy'),('deep','tactical')]:
                rows.extend([play(c,a,b,seed),play(c,b,a,seed)])
        print(c.name,'complete',flush=True)
    Path('research/results/continuation.json').write_text(json.dumps(dict(configs=[asdict(c) for c in CONFIGS],games=rows,seconds=time.time()-start,python=platform.python_version(),machine=platform.machine(),platform=platform.platform())))
if __name__=='__main__':main()
