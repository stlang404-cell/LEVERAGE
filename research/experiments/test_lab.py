import unittest, math
from collections import Counter
from arena import *
class RulesTests(unittest.TestCase):
    def test_initial_and_reachable_states(self):
        for game in GAMES:
            rng=random.Random(918)
            for trial in range(8):
                s=initial(game);h=Counter({key(s):1})
                for _ in range(80):
                    invariant(s)
                    if outcome(s,game,h)[0] is not None:break
                    legal=moves(s,game)
                    self.assertEqual(len(legal),len(set(legal)))
                    for m in legal:
                        t=apply(s,m,game)
                        self.assertEqual(t,apply(s,m,game));invariant(t)
                        self.assertEqual(t.turn,-s.turn)
                        self.assertEqual(t.ply,s.ply+1)
                    s=apply(s,rng.choice(legal),game);h[key(s)]+=1
    def test_leverage_cut(self):
        b=[0]*25;b[0]=2;b[5]=1;b[1]=1;b[6]=1;b[7]=-1;b[8]=-1;b[9]=-2
        s=State(tuple(b));m=('move',6,7,0)
        self.assertIn(m,moves(s,'leverage'))
        t=apply(s,m,'leverage')
        self.assertEqual(t.board[8],-1) # still linked to opposing leader
        b[9]=0;b[24]=-2;s=State(tuple(b))
        self.assertEqual(apply(s,m,'leverage').board[8],0)
    def test_equal_power_cannot_capture(self):
        b=[0]*25;b[0]=2;b[24]=-2;b[11]=1;b[12]=-1
        self.assertNotIn(('move',11,12,0),moves(State(tuple(b)),'leverage'))
    def test_jump_and_delivery(self):
        b=[0]*25;b[12]=2;b[17]=1;b[24]=-2
        s=State(tuple(b),reserves=(0,0));m=('move',12,22,0)
        self.assertIn(m,moves(s,'relay'))
        t=apply(s,m,'relay');self.assertEqual(outcome(t,'relay',Counter({key(t):1})),(1,'delivery'))
    def test_forced_leader_and_immobility(self):
        b=[0]*25;b[0]=2;b[1]=-1;b[5]=-1;b[24]=-2;b[23]=1
        s=State(tuple(b));self.assertTrue(all(m[1]==0 for m in moves(s,'commitment')))
        # Adjacent enemies may be captured; being attacked is not chess check.
        self.assertIn(('move',0,1,0),moves(s,'commitment'))
    def test_rotation_inverse(self):
        s=initial('orbit');t=apply(s,('rotate',0,0,1),'orbit');u=apply(t,('rotate',0,0,-1),'orbit')
        self.assertEqual(s.board,u.board)
    def test_energy_and_block(self):
        s=initial('allocation')
        self.assertNotIn(('move',0,2,2),moves(s,'allocation'))
        t=apply(s,('move',0,5,1),'allocation');self.assertEqual(t.energy,(3,3))
    def test_repetition_and_limit(self):
        for game in GAMES:
            s=initial(game)
            self.assertEqual(outcome(s,game,Counter({key(s):3})),(0,'repetition'))
            self.assertEqual(outcome(replace(s,ply=100),game,Counter()),(0,'limit'))
    def test_missing_leader(self):
        b=list(initial('leverage').board);b[2]=0
        self.assertEqual(outcome(State(tuple(b)),'leverage',Counter()),(-1,'leader'))
class FinanceTests(unittest.TestCase):
    def cost(self,q,b=20):
        m=max(q);return m+b*math.log(sum(math.exp((v-m)/b) for v in q))
    def test_lmsr_bounds_and_round_trip(self):
        for q in ((0,0),(50,-10),(1000,0)):
            for amount in (1,10,100):
                nxt=(q[0]+amount,q[1]);c=self.cost(nxt)-self.cost(q)
                self.assertGreaterEqual(c,-1e-10);self.assertLessEqual(c,amount+1e-10)
                self.assertAlmostEqual(c+self.cost(q)-self.cost(nxt),0)
        self.assertAlmostEqual(self.cost((0,0)),20*math.log(2))
    def test_ledger_conservation(self):
        accounts={'household':10000,'corporation':50000,'maker':10000}
        def transfer(a,b,c):
            assert c>=0 and accounts[a]>=c
            accounts[a]-=c;accounts[b]+=c
        before=sum(accounts.values())
        transfer('corporation','household',2000);transfer('household','maker',500)
        transfer('maker','household',700)
        self.assertEqual(sum(accounts.values()),before)
        with self.assertRaises(AssertionError):transfer('household','maker',999999)
if __name__=='__main__':unittest.main(verbosity=2)
