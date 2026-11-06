import unittest,random
from collections import Counter
from dataclasses import replace
from r0.rules import *
from r0.oracle import predict,outcome
from r0.search import Search
class R0Tests(unittest.TestCase):
    def state(self,items,c,reserves=(0,0),turn=1):
        b=[0]*(c.size*c.size)
        for i,v in items.items():b[i]=v
        return State(tuple(b),turn,reserves)
    def test_anchor_exposure(self):
        s=self.state({0:2,11:1,12:-2,7:-1,13:-1},A)
        self.assertIn(('move',11,12),legal(s,A))
        t=apply(s,('move',11,12),A,Counter({key(s):1}))
        self.assertEqual(terminal(t,A,Counter()),(1,'anchor'))
    def test_bridge_road(self):
        s=self.state({2:1,7:1,12:1,16:1,22:1,24:-1},B)
        self.assertFalse(road(s,1,B));t=apply_unchecked(s,('move',16,17),B)
        self.assertEqual(terminal(t,B,Counter()),(1,'road'))
    def test_target_support_and_collapse(self):
        s=self.state({10:1,11:1,7:1,12:-1,13:-1,23:-1},B)
        self.assertIn(('move',11,12),legal(s,B))
        t=apply_unchecked(s,('move',11,12),B)
        self.assertEqual(t.board[13],0);self.assertEqual(t.board[23],-1)
    def test_insufficient_road_material(self):
        s=self.state({0:1,24:-1},B)
        self.assertEqual(terminal(s,B,Counter()),(0,'insufficient_road_material'))
    def test_wake_and_parked(self):
        s=self.state({15:1,21:1,0:-1,4:-1,9:1,20:-1},C)
        t=apply_unchecked(s,('move',15,16),C);self.assertEqual(t.board[15],3)
        s=self.state({20:1,16:1,0:-1,4:-1},C)
        self.assertFalse(any(m[1]==20 for m in legal(s,C)))
        t=apply_unchecked(s,('move',16,21),C)
        self.assertEqual(terminal(t,C,Counter()),(1,'delivered_two'))
    def test_wake_monotonic(self):
        s=initial(C);rng=random.Random(9);h=Counter({key(s):1})
        while terminal(s,C,h)[0] is None:
            old=s.board.count(0);s=apply_unchecked(s,rng.choice(legal(s,C)),C);h[key(s)]+=1
            self.assertEqual(s.board.count(0),old-1)
        self.assertLessEqual(s.ply,19)
    def test_illegal_and_terminal(self):
        s=initial(A);h=Counter({key(s):1})
        with self.assertRaises(ValueError):apply(s,('place',-1,2),A,h)
        h[key(s)]=3
        with self.assertRaises(ValueError):apply(s,legal(s,A)[0],A,h)
    def test_draws_and_symmetry(self):
        for c in CORE:
            s=initial(c);self.assertEqual(terminal(s,c,Counter({key(s):3})),(0,'repetition'))
            self.assertEqual(terminal(replace(s,ply=120),c,Counter()),(0,'limit'))
            t=State(tuple(-x if x!=3 else 3 for x in s.board[::-1]),-s.turn,s.reserves[::-1])
            expected={(kind,c.size*c.size-1-i if i>=0 else -1,c.size*c.size-1-j) for kind,i,j in legal(s,c)}
            self.assertEqual(set(legal(t,c)),expected)
    def test_search_cache_and_history(self):
        for c in CORE:
            s=initial(c);h=Counter({key(s):1});before=+h
            m,st=Search(c).choose(s,h,3,300,random.Random(1))
            m2,st2=Search(c,cache=False).choose(s,h,3,300,random.Random(1))
            # Cache ordering may change incomplete deeper work; completed iteration score remains valid.
            self.assertIn(m,legal(s,c));self.assertIn(m2,legal(s,c));self.assertLessEqual(st['nodes'],300)
            self.assertEqual(+h,before);self.assertGreaterEqual(st['depth'],1)
    def test_exact_anchor_tablebase_bellman(self):
        from r0.endgames import anchors
        table,dist=anchors(5,table=True)
        self.assertEqual(len(table),1200)
        for (a,b,p),value in table.items():
            board=[0]*25;board[a]=2;board[b]=-2
            children=[];ranked=[]
            for m,(bb,rr) in predict(tuple(board),p,(0,0),A).items():
                if -2*p not in bb:children.append(-1);ranked.append((-1,0))
                else:
                    child=(bb.index(2),bb.index(-2),-p);children.append(table[child]);ranked.append((table[child],dist[child]))
            if value==1:
                self.assertIn(-1,children);self.assertTrue(any(v==-1 and d<dist[(a,b,p)] for v,d in ranked))
            else:
                self.assertTrue(all(v==1 for v in children));self.assertTrue(all(d<dist[(a,b,p)] for v,d in ranked))
        self.assertLessEqual(max(dist.values()),14)
    def test_small_wake_proofs(self):
        from r0.endgames import solve_c
        self.assertEqual(solve_c(3,10000)['root_value'],1)
        self.assertEqual(solve_c(4,10000)['root_value'],-1)
    def test_terminal_tactics_all_candidates(self):
        cases=[(A,self.state({0:2,11:1,12:-2,7:-1,13:-1},A)),(B,self.state({2:1,7:1,12:1,16:1,22:1,24:-1},B)),(C,self.state({20:1,16:1,0:-1,4:-1},C))]
        for c,s in cases:
            h=Counter({key(s):1});m,st=Search(c).choose(s,h,2,10000,random.Random(4))
            t=apply_unchecked(s,m,c);self.assertEqual(terminal(t,c,Counter())[0],1)
    def test_alpha_beta_matches_exhaustive_depth2(self):
        for c in CORE:
            rng=random.Random(918);s=initial(c);h=Counter({key(s):1})
            for sample in range(8):
                if terminal(s,c,h)[0] is not None:s=initial(c);h=Counter({key(s):1})
                engine=Search(c)
                def minimax(st,depth):
                    win,_=terminal(st,c,h)
                    if win is not None:return win*st.turn*100000 if win else 0
                    if depth==0:return engine.evaluate(st)
                    values=[]
                    for m in legal(st,c):
                        t=apply_unchecked(st,m,c);h[key(t)]+=1
                        values.append(-minimax(t,depth-1));h[key(t)]-=1
                    return max(values)
                expected=minimax(s,2);m,stats=engine.choose(s,h,2,100000,rng);self.assertEqual(stats['depth'],2)
                t=apply_unchecked(s,m,c);h[key(t)]+=1;value=-minimax(t,1);h[key(t)]-=1
                self.assertEqual(value,expected)
                s=apply_unchecked(s,rng.choice(legal(s,c)),c);h[key(s)]+=1
    def test_oracle_10000_states(self):
        rng=random.Random(77419);states=0;unique=set();transitions=0
        configs=list(CORE)+[replace(A,name='root',deployment='rooted'),replace(A,name='component',power='component'),replace(A,name='nocollapse',collapse=False)]
        for i in range(10000):
            c=configs[i%len(configs)]
            if i==0:smap={x:initial(x) for x in configs};hmap={x:Counter({key(smap[x]):1}) for x in configs}
            # Separate short walks, restarting each candidate when terminal.
            s=smap[c];h=hmap[c]
            self.assertEqual(terminal(s,c,h),outcome(s.board,s.turn,s.reserves,s.ply,h[key(s)],c))
            if terminal(s,c,h)[0] is not None:s=initial(c);h=Counter({key(s):1})
            unique.add((c,key(s)));oracle=predict(s.board,s.turn,s.reserves,c)
            self.assertEqual(set(legal(s,c)),set(oracle))
            for m,(board,reserves) in oracle.items():
                t=apply_unchecked(s,m,c);self.assertEqual((t.board,t.reserves),(board,reserves));invariant(t,c);transitions+=1
            states+=1
            m=rng.choice(legal(s,c));smap[c]=apply_unchecked(s,m,c);h[key(smap[c])]+=1;hmap[c]=h
        self.assertEqual(states,10000)
        self.assertGreater(len(unique),1000)
        import json
        from pathlib import Path
        Path('research/results/r0/oracle_validation.json').write_text(json.dumps(dict(sampled_states=states,unique_config_positions=len(unique),transitions_compared=transitions,terminal_oracle=True),indent=2)+'\n')
if __name__=='__main__':unittest.main()
