"""Final R0 candidate reference rules. Never imports or modifies prior engines."""
from dataclasses import dataclass
from collections import deque
@dataclass(frozen=True)
class Config:
    name:str
    candidate:str
    size:int=5
    reserve:int=5
    deployment:str='any'
    collapse:bool=True
    formation:bool=False
    power:str='adjacent'
@dataclass(frozen=True)
class State:
    board:tuple
    turn:int=1
    reserves:tuple=(5,5)
    ply:int=0
A=Config('A5','A')
B=Config('B5','B',reserve=8)
C=Config('C5','C',reserve=0)
CORE=(A,B,C)
def adj(i,n):
    x,y=i%n,i//n
    return tuple(j for j in (i-1,i+1,i-n,i+n) if 0<=j<n*n and abs(j%n-x)+abs(j//n-y)==1)
def initial(c):
    n=c.size;b=[0]*(n*n);x=(n-1)//2;r=c.reserve
    if c.candidate=='A':
        b[x]=2;b[n*n-1-x]=-2
        if c.formation:
            for j in (x-1,x+1):b[j]=1;b[n*n-1-j]=-1
            r-=2
    elif c.candidate=='B':
        b[x]=1;b[n*n-1-x]=-1
    else:
        for j in (0,n//2,n-1):b[j]=1;b[n*n-1-j]=-1
    return State(tuple(b),reserves=(r,r))
def key(s):return s.board,s.turn,s.reserves
def component(b,seeds,p,n):
    seen=set(seeds);todo=list(seen)
    while todo:
        for j in adj(todo.pop(),n):
            if b[j]*p>0 and b[j]!=3 and j not in seen:seen.add(j);todo.append(j)
    return seen
def rooted(b,p,c):
    if c.candidate=='A':seeds=[i for i,v in enumerate(b) if v==2*p]
    else:seeds=[i for i,v in enumerate(b) if v==p and i//c.size==(0 if p==1 else c.size-1)]
    return component(b,seeds,p,c.size)
def support(b,i,p,c):
    if c.power=='component':return len(component(b,[i],p,c.size))
    return 1+sum(b[j]*p>0 and b[j]!=3 for j in adj(i,c.size))
def legal(s,c):
    b,p,n=s.board,s.turn,c.size;out=[];idx=0 if p==1 else 1
    roots=rooted(b,p,c) if c.candidate!='C' else set()
    if s.reserves[idx] and c.candidate!='C':
        for j,v in enumerate(b):
            ok=(j//n==(0 if p==1 else n-1)) if c.candidate=='B' else any(b[k]*p>0 and (c.deployment!='rooted' or k in roots) for k in adj(j,n))
            if not v and ok:out.append(('place',-1,j))
    for i,v in enumerate(b):
        if v==3 or v*p<=0:continue
        if c.candidate=='C' and i//n==(n-1 if p==1 else 0):continue
        for j in adj(i,n):
            if b[j]==0:out.append(('move',i,j))
            elif b[j]!=3 and b[j]*p<0 and c.candidate!='C':
                if c.candidate=='A':ok=abs(b[j])==2 or support(b,i,p,c)>support(b,j,-p,c)
                else:ok=sum(b[k]==p for k in adj(j,n))>sum(b[k]==-p for k in adj(j,n))
                if ok:out.append(('move',i,j))
    return tuple(sorted(out))
def apply_unchecked(s,m,c):
    kind,i,j=m;b=list(s.board);p=s.turn;idx=0 if p==1 else 1;r=list(s.reserves);captured=b[j]*p<0
    if kind=='place':b[j]=p;r[idx]-=1
    else:b[j]=b[i];b[i]=3 if c.candidate=='C' else 0
    if captured and c.collapse:
        keep=rooted(b,-p,c)
        for k,v in enumerate(b):
            if v!=3 and v*p<0 and k not in keep:b[k]=0
    return State(tuple(b),-p,tuple(r),s.ply+1)
def road(s,p,c):
    return any(i//c.size==(c.size-1 if p==1 else 0) for i in rooted(s.board,p,c))
def terminal(s,c,history):
    b=s.board
    if c.candidate=='A':
        if 2 not in b:return -1,'anchor'
        if -2 not in b:return 1,'anchor'
    elif c.candidate=='B':
        if road(s,1,c):return 1,'road'
        if road(s,-1,c):return -1,'road'
        if all(sum(v==p for v in b)+s.reserves[0 if p==1 else 1]<c.size for p in (1,-1)):return 0,'insufficient_road_material'
    else:
        for p in (1,-1):
            if sum(v==p and i//c.size==(c.size-1 if p==1 else 0) for i,v in enumerate(b))>=2:return p,'delivered_two'
    if history.get(key(s),0)>=3:return 0,'repetition'
    if s.ply>=120:return 0,'limit'
    if not legal(s,c):return (-s.turn,'immobile') if c.candidate in ('B','C') else (0,'immobile')
    return None,None
def apply(s,m,c,history):
    if terminal(s,c,history)[0] is not None or m not in legal(s,c):raise ValueError('illegal or terminal action')
    return apply_unchecked(s,m,c)
def invariant(s,c):
    assert len(s.board)==c.size*c.size and s.turn in (-1,1)
    assert all(x in ((-1,0,1,3) if c.candidate=='C' else (-2,-1,0,1,2)) for x in s.board)
    assert all(x>=0 for x in s.reserves)
    if c.candidate=='A':assert s.board.count(2)<=1 and s.board.count(-2)<=1
