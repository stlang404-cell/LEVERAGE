"""Local interactive research board, not a production game. No dependencies/network."""
from .rules import *
from .search import Search
from .run import AGENTS
from collections import Counter
import argparse,random

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',choices=['A','B','C'],default='A');ap.add_argument('--ai',choices=AGENTS,default='deep');ap.add_argument('--seed',type=int,default=7);args=ap.parse_args()
    c=next(c for c in CORE if c.candidate==args.candidate);s=initial(c);h=Counter({key(s):1});rng=random.Random(args.seed);engine=Search(c)
    print(f'LEVERAGE final R0 lab {c.name}; YOU = North, AI = South. A=anchor, o=agent, x=enemy agent, Z=enemy anchor, #=wake. Human enjoyment/readability untested.')
    print('Enter move number, ? for annotated actions, ai to play your turn, or quit. No saving or corporate systems in this research harness.')
    while True:
        print('   '+' '.join(str(x) for x in range(c.size)))
        for y in range(c.size):print(str(y)+'  '+' '.join({0:'.',1:'o',-1:'x',2:'A',-2:'Z',3:'#'}[v] for v in s.board[y*c.size:(y+1)*c.size]))
        print('Reserves',s.reserves)
        win,reason=terminal(s,c,h)
        if win is not None:print('FINAL',win,reason);return
        ms=legal(s,c)
        if s.turn==1:
            try:text=input('North move (?/ai/quit):').strip()
            except EOFError:return
            if text=='quit':print();return
            if text=='?':
                for i,m in enumerate(ms):
                    kind,origin,dest=m;details=''
                    if origin>=0 and c.candidate=='A':details=f' power {support(s.board,origin,s.turn,c)}'
                    if s.board[dest]*s.turn<0:
                        after=apply_unchecked(s,m,c);details+=f' removes {sum(v not in (0,3) for v in s.board)-sum(v not in (0,3) for v in after.board)} enemy pieces'
                    print(' '.join(map(str,(i,kind,('reserve' if origin<0 else (origin%c.size,origin//c.size)),'→',(dest%c.size,dest//c.size),details))).rstrip())
                continue
            if text!='ai':
                try:m=ms[int(text)];assert int(text)>=0
                except (ValueError,IndexError,AssertionError):print('Choose a listed nonnegative action number.');continue
            else:m,_=engine.choose(s,h,4,1200,rng)
        else:
            depth,budget=AGENTS[args.ai]
            m=rng.choice(ms) if depth==0 else engine.choose(s,h,depth,budget,rng)[0]
            print('South:',m)
        s=apply(s,m,c,h);h[key(s)]+=1
if __name__=='__main__':main()
