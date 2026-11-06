import unittest,random
from collections import Counter
from continuation import Config,State,CONFIGS,adj,initial,key,component,moves,transition,result,choose
class ContinuationTests(unittest.TestCase):
    def state(self,items,n=5):
        b=[0]*(n*n)
        for i,v in items.items():b[i]=v
        return State(tuple(b),reserve=(0,0))
    def test_rotation_color_symmetry(self):
        for c in CONFIGS:
            s=initial(c);size=c.size**2
            flip=lambda st:State(tuple(-v for v in st.board[::-1]),-st.turn,st.reserve[::-1],st.ply)
            self.assertEqual(s.board,flip(s).board)
            transformed={(k,size-1-i if i>=0 else -1,size-1-j) for k,i,j in moves(s,c)}
            self.assertEqual(transformed,set(moves(flip(s),c)))
    def test_push_and_anchor_component(self):
        c=Config('p',mechanic='pressure');s=self.state({0:2,11:1,12:-1,24:-2})
        m=('push',11,12);self.assertIn(m,moves(s,c))
        t=transition(s,m,c);self.assertEqual(t.board[12],1);self.assertEqual(t.board[13],0) # pushed agent collapses
        s=self.state({0:2,11:1,12:-2,17:-1,6:1}) # attacker support and defender support equal
        self.assertIn(m,moves(s,c));t=transition(s,m,c)
        self.assertEqual(t.board[13],-2);self.assertEqual(t.board[17],0)
    def test_push_blocked_edge(self):
        c=Config('p',mechanic='pressure');s=self.state({0:2,3:1,4:-1,24:-2})
        self.assertNotIn(('push',3,4),moves(s,c))
    def test_breach_not_anchor(self):
        c=Config('b',mechanic='breach');s=self.state({0:2,11:1,12:-1,24:-2})
        self.assertIn(('breach',11,12),moves(s,c));t=transition(s,('breach',11,12),c)
        self.assertEqual(t.board[11:13],(0,0))
        s=self.state({0:2,11:1,12:-2});self.assertNotIn(('breach',11,12),moves(s,c))
    def test_relay_no_enemy_jump(self):
        c=Config('r',mechanic='relay');s=self.state({0:2,11:1,12:1,24:-2})
        self.assertIn(('move',11,13),moves(s,c))
        s=self.state({0:2,11:1,12:-1,24:-2});self.assertNotIn(('move',11,13),moves(s,c))
    def test_terminal_and_repetition(self):
        for c in CONFIGS:
            s=initial(c);self.assertEqual(result(s,c,Counter({key(s):3})),(0,'repetition'))
            self.assertEqual(result(State(s.board,ply=120),c,Counter()),(0,'limit'))
            b=list(s.board);b[b.index(-2)]=0
            self.assertEqual(result(State(tuple(b)),c,Counter()),(1,'anchor'))
    def test_walks_and_material(self):
        for c in CONFIGS:
            s=initial(c);rng=random.Random(72);h=Counter({key(s):1})
            for _ in range(120):
                if result(s,c,h)[0] is not None:break
                ms=moves(s,c);self.assertEqual(len(ms),len(set(ms)))
                for m in ms:
                    t=transition(s,m,c)
                    self.assertEqual(len(t.board),c.size**2)
                    self.assertTrue(all(v in (-2,-1,0,1,2) for v in t.board))
                    self.assertTrue(all(r>=0 for r in t.reserve))
                    self.assertLessEqual(sum(v!=0 for v in t.board)+sum(t.reserve),sum(v!=0 for v in s.board)+sum(s.reserve))
                    self.assertEqual(t,transition(s,m,c))
                s=transition(s,rng.choice(ms),c);h[key(s)]+=1
    def test_search_budget_and_history(self):
        c=CONFIGS[0];s=initial(c);h=Counter({key(s):1});before=h.copy()
        m,n,d=choose(s,c,'deep',random.Random(1),h,80)
        self.assertIn(m,moves(s,c));self.assertLessEqual(n,80);self.assertGreaterEqual(d,1)
        self.assertEqual(+h,+before)
    def test_immediate_anchor_capture(self):
        c=CONFIGS[0];s=self.state({0:2,11:1,6:1,12:-2});h=Counter({key(s):1})
        m,n,d=choose(s,c,'tactical',random.Random(1),h)
        self.assertEqual(m,('move',11,12))
if __name__=='__main__':unittest.main()
