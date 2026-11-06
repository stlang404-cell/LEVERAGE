"""Budgeted iterative alpha-beta; history-safe transposition ordering and static caches."""
from collections import Counter
from dataclasses import replace
import random,heapq
from .rules import legal,apply_unchecked,terminal,key,adj,rooted
class Exhausted(Exception):pass
class Search:
    def __init__(self,c,cache=True,profile='structure'):
        self.c=c;self.cache=cache;self.profile=profile;self.actions={};self.values={};self.ordering={};self.hits=0
    def moves(self,s):
        k=key(s)
        if self.cache and k in self.actions:self.hits+=1;return self.actions[k]
        ms=legal(s,self.c)
        if self.cache:
            if len(self.actions)>=4096:self.actions.clear()
            self.actions[k]=ms
        return ms
    def evaluate(self,s):
        k=key(s)
        if self.cache and k in self.values:self.hits+=1;return self.values[k]
        n=self.c.size;b=s.board
        def score(p):
            owned=[i for i,v in enumerate(b) if v!=3 and v*p>0]
            if self.profile=='material':return 20*len(owned)+8*s.reserves[0 if p==1 else 1]+sum(min(i%n,n-1-i%n,i//n,n-1-i//n) for i in owned)
            if self.c.candidate=='A':
                if 2*p not in b or -2*p not in b:return 0
                anchor=b.index(2*p);enemy=b.index(-2*p)
                return 20*len(owned)+8*s.reserves[0 if p==1 else 1]-100*sum(b[j]*p<0 for j in adj(anchor,n))-sum(abs(i%n-enemy%n)+abs(i//n-enemy//n) for i in owned)+2*len(rooted(b,p,self.c))
            if self.c.candidate=='B':
                dist={i:(0 if b[i]==p else 1 if not b[i] else 4) for i in range(n*n) if i//n==(0 if p==1 else n-1)};heap=[(v,i) for i,v in dist.items()];heapq.heapify(heap)
                while heap:
                    d,i=heapq.heappop(heap)
                    if d!=dist[i]:continue
                    if i//n==(n-1 if p==1 else 0):return 15*len(owned)-25*d+3*len(rooted(b,p,self.c))
                    for j in adj(i,n):
                        nd=d+(0 if b[j]==p else 1 if not b[j] else 4)
                        if nd<dist.get(j,999):dist[j]=nd;heapq.heappush(heap,(nd,j))
                return -999
            delivered=sum(i//n==(n-1 if p==1 else 0) for i in owned)
            progress=sum(i//n if p==1 else n-1-i//n for i in owned)
            mobility=sum(b[j]==0 for i in owned if i//n!=(n-1 if p==1 else 0) for j in adj(i,n))
            return 100*delivered+8*progress+3*mobility
        v=score(s.turn)-score(-s.turn)
        if self.cache:
            if len(self.values)>=4096:self.values.clear()
            self.values[k]=v
        return v
    def choose(self,s,history,depth,budget,rng):
        ms=list(self.moves(s));rng.shuffle(ms);nodes=0;done=0;best=ms[0];start_hits=self.hits;iterations=[]
        def neg(st,d,alpha,beta):
            nonlocal nodes
            if nodes>=budget:raise Exhausted
            nodes+=1
            win,_=terminal(st,self.c,history)
            if win is not None:return win*st.turn*100000 if win else 0
            if d==0:return self.evaluate(st)
            acts=list(self.moves(st));preferred=self.ordering.get(key(st))
            if preferred in acts:acts.remove(preferred);acts.insert(0,preferred)
            value=-10**9;selected=acts[0]
            for m in acts:
                child=apply_unchecked(st,m,self.c);history[key(child)]+=1
                try:v=-neg(child,d-1,-beta,-alpha)
                finally:history[key(child)]-=1
                if v>value:value=v;selected=m
                alpha=max(alpha,v)
                if alpha>=beta:break
            # This table is move ordering ONLY: never reuse a score ignoring repetition/ply.
            if self.cache:
                if len(self.ordering)>=4096:self.ordering.clear()
                self.ordering[key(st)]=selected
            return value
        for level in range(1,depth+1):
            scored=[];alpha=-10**9
            try:
                for m in ms:
                    child=apply_unchecked(s,m,self.c);history[key(child)]+=1
                    try:v=-neg(child,level-1,-10**9,-alpha)
                    finally:history[key(child)]-=1
                    scored.append((v,m));alpha=max(alpha,v)
            except Exhausted:break
            scored.sort(key=lambda x:x[0],reverse=True);best=scored[0][1];ms=[m for _,m in scored];done=level;iterations.append((level,best,scored[0][0]))
        return best,dict(nodes=nodes,depth=done,cache_hits=self.hits-start_hits,iterations=iterations,cache_entries=len(self.actions)+len(self.values)+len(self.ordering))
