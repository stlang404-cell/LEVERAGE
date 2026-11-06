"""Disposable CORPORATE LADDER rules laboratory. Python 3.12; standard library only."""
from dataclasses import dataclass, replace
from collections import Counter
import random, math, json, argparse, time
N=5
GAMES=('leverage','relay','commitment','allocation','orbit')
@dataclass(frozen=True)
class State:
    board: tuple
    turn: int=1
    reserves: tuple=(5,5)
    energy: tuple=(3,3)
    ply: int=0

def adjacent(i):
    x,y=i%N,i//N
    return tuple(j for j in (i-1,i+1,i-N,i+N) if 0<=j<N*N and abs(j%N-x)+abs(j//N-y)==1)
def initial(game):
    b=[0]*25;b[2]=2;b[22]=-2
    if game in ('commitment','allocation','orbit'):
        for i in (0,1,3,4): b[i]=1;b[24-i]=-1
    return State(tuple(b),reserves=(5,5) if game in ('leverage','relay') else (0,0))
def key(s): return (s.board,s.turn,s.reserves,s.energy)
def connected(b,p):
    roots=[i for i,v in enumerate(b) if v==2*p]
    seen=set(roots);todo=list(roots)
    while todo:
        for j in adjacent(todo.pop()):
            if b[j]*p>0 and j not in seen: seen.add(j);todo.append(j)
    return seen

def power(b,i,p): return 1+sum(b[j]*p>0 for j in adjacent(i))
def moves(s,game):
    b,p=s.board,s.turn;idx=0 if p==1 else 1;out=[]
    if 2 not in b or -2 not in b:return []
    if game in ('leverage','relay') and s.reserves[idx]:
        for j,v in enumerate(b):
            if v==0 and (any(b[k]*p>0 for k in adjacent(j)) if game=='leverage' else j//5==(0 if p==1 else 4)):
                out.append(('place',-1,j,0))
    if game=='orbit':
        for y in range(4):
            for x in range(4):
                q=(y*5+x,y*5+x+1,(y+1)*5+x+1,(y+1)*5+x)
                if any(b[i]*p>0 for i in q):
                    out.extend(('rotate',q[0],0,d) for d in (-1,1))
        return out
    for i,v in enumerate(b):
        if v*p<=0:continue
        if game=='allocation':
            for cost in range(1,s.energy[idx]+1):
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    x,y=i%5+dx*cost,i//5+dy*cost
                    if not (0<=x<5 and 0<=y<5):continue
                    j=y*5+x
                    path=[(i//5+dy*k)*5+i%5+dx*k for k in range(1,cost)]
                    if any(b[k] for k in path) or b[j]*p>0:continue
                    if b[j]*p<0 and cost<=sum(b[k]*(-p)>0 for k in adjacent(j)):continue
                    out.append(('move',i,j,cost))
            continue
        for j in adjacent(i):
            if b[j]*p>0:
                if game=='relay':
                    k=2*j-i
                    if 0<=k<25 and abs(k%5-i%5)+abs(k//5-i//5)==2 and b[k]*p<=0:
                        out.append(('move',i,k,0))
                continue
            if b[j]*p<0 and game=='leverage' and power(b,i,p)<=power(b,j,-p):continue
            if game=='leverage' and not b[j] and abs(v)==1:
                temp=list(b);temp[j]=temp[i];temp[i]=0
                if len(connected(temp,p))!=sum(v*p>0 for v in temp):continue
            out.append(('move',i,j,0))
    if game=='commitment':
        leader=b.index(2*p)
        if any(b[j]*p<0 for j in adjacent(leader)):
            out=[m for m in out if m[1]==leader]
    return sorted(set(out))
def apply(s,m,game):
    b=list(s.board);kind,i,j,c=m;p=s.turn;idx=0 if p==1 else 1
    reserves=list(s.reserves);energy=list(s.energy)
    if kind=='place':b[j]=p;reserves[idx]-=1
    elif kind=='rotate':
        q=(i,i+1,i+6,i+5)
        vals=[b[k] for k in q]
        for z,k in enumerate(q):b[k]=vals[(z-c)%4]
    else:
        capture=b[j]*p<0
        b[j]=b[i];b[i]=0
        if game=='leverage' and capture:
            keep=connected(b,-p)
            for k,v in enumerate(b):
                if v*p<0 and k not in keep:b[k]=0
        if game=='allocation':energy[idx]=min(3,energy[idx]-c+2)
    return State(tuple(b),-p,tuple(reserves),tuple(energy),s.ply+1)
def outcome(s,game,history):
    if 2 not in s.board:return -1,'leader'
    if -2 not in s.board:return 1,'leader'
    if game in ('relay','orbit'):
        # Only the mover's delivery wins, including a rotation of both anchors.
        p=-s.turn
        if s.board.index(2*p)//5==(4 if p==1 else 0):return p,'delivery'
    if history[key(s)]>=3:return 0,'repetition'
    if s.ply>=100:return 0,'limit'
    if not moves(s,game):return (-s.turn if game=='commitment' else 0),'immobile'
    return None,None

def evaluate(s,p,game):
    if 2*p not in s.board:return -10000
    if -2*p not in s.board:return 10000
    val=15*sum((1 if v*p>0 else -1) for v in s.board if v)
    for i,v in enumerate(s.board):
        if not v:continue
        sign=1 if v*p>0 else -1
        val+=sign*(4-abs(i%5-2)-abs(i//5-2))
        if abs(v)==2 and game in ('relay','orbit'):
            owner=1 if v>0 else -1
            progress=i//5 if owner==1 else 4-i//5
            val+=sign*progress*12
    return val

def choose(s,game,agent,rng,history,budget=400):
    legal=moves(s,game)
    if agent=='random':return rng.choice(legal),0
    nodes=0
    def negamax(st,depth,alpha,beta,h):
        nonlocal nodes
        nodes+=1
        result,_=outcome(st,game,h)
        if result is not None:return result*st.turn*10000 if result else 0
        if depth==0 or nodes>=budget:return evaluate(st,st.turn,game)
        best=-math.inf
        for m in moves(st,game):
            child=apply(st,m,game);h[key(child)]+=1
            score=-negamax(child,depth-1,-beta,-alpha,h);h[key(child)]-=1
            best=max(best,score);alpha=max(alpha,score)
            if alpha>=beta:break
        return best
    ordered=list(legal);rng.shuffle(ordered);scores=[]
    depth=1 if agent=='greedy' else 2
    # Equal per-root quotas avoid starving later moves. Report actual nodes.
    root_budget=max(1,budget//len(legal))
    for m in ordered:
        child=apply(s,m,game);h=history.copy();h[key(child)]+=1
        before=nodes
        old_budget=budget;budget=nodes+root_budget
        score=-negamax(child,depth-1,-math.inf,math.inf,h)
        budget=old_budget;scores.append((score,m))
    return max(scores,key=lambda x:x[0])[1],nodes

def invariant(s):
    assert len(s.board)==25 and all(v in (-2,-1,0,1,2) for v in s.board)
    assert s.board.count(2)<=1 and s.board.count(-2)<=1
    assert s.turn in (-1,1) and all(0<=r<=5 for r in s.reserves)
    assert all(0<=e<=3 for e in s.energy)
def play(game,a,b,seed):
    s=initial(game);h=Counter({key(s):1});rng=random.Random(seed)
    branches=[];opening=[];nodes=0
    while True:
        result,reason=outcome(s,game,h)
        if result is not None:break
        legal=moves(s,game);branches.append(len(legal))
        m,n=choose(s,game,a if s.turn==1 else b,rng,h);nodes+=n
        if s.ply<4:opening.append(m)
        s=apply(s,m,game);invariant(s);h[key(s)]+=1
    return dict(game=game,agents=[a,b],seed=seed,winner=result,reason=reason,plies=s.ply,branches=branches,opening=opening,nodes=nodes)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',type=int,default=12);ap.add_argument('--output',default='research/results/games.json');args=ap.parse_args()
    rows=[];start=time.time()
    for game in GAMES:
        for a,b in [('random','random'),('greedy','random'),('search','greedy')]:
            for seed in range(args.pairs):
                rows.append(play(game,a,b,seed));rows.append(play(game,b,a,seed))
        print(game,'complete',flush=True)
    with open(args.output,'w') as f:json.dump({'schema':1,'pairs':args.pairs,'seconds':time.time()-start,'games':rows},f)
if __name__=='__main__':main()
