"""Synthetic population and public-information forecast experiments, NOT a game simulation."""
import random,time,tracemalloc,json,platform,statistics,math,hashlib
from pathlib import Path

def population(n):
    tracemalloc.start();start=time.perf_counter()
    # Each manager leads up to seven reports; IDs form an acyclic tree.
    people=[dict(id=i,position=i,manager=(i-1)//7 if i else None,rating=1000+i%1000,cash=10000,salary=100+i%50,function=('finance','operations','research')[i%3],history=[('joined',0)]+[('match',j,i%3-1) for j in range(12)]) for i in range(n)]
    setup=time.perf_counter()-start;treasury=n*100000;total=treasury+sum(p['cash'] for p in people);times=[]
    for tick in range(1,31):
        t=time.perf_counter()
        for p in people:
            if (p['id']+tick)%7==0:
                amount=p['salary'];treasury-=amount;p['cash']+=amount;p['history'].append(('pay',tick,amount))
        times.append(time.perf_counter()-t)
    assert total==treasury+sum(p['cash'] for p in people)
    payload=json.dumps(dict(people=people,treasury=treasury),separators=(',',':')).encode()
    current,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    return dict(employees=n,ticks=30,setup_seconds=setup,tick_p50=statistics.median(times),tick_p95=sorted(times)[28],peak_traced_bytes=peak,json_bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest())
def forecasts():
    rng=random.Random(20261106);rows=[];wins={k:0 for k in (1,4,8,16,32)};loss={k:0 for k in wins};n=5000
    for _ in range(n):
        gap=rng.gauss(0,300);truth=1/(1+10**(-gap/400));outcome=int(rng.random()<truth);noise=[rng.gauss(0,300) for _ in range(32)];pred={}
        for k in wins:
            estimate=gap+sum(noise[:k])/k;pred[k]=1/(1+10**(-estimate/400));loss[k]+=(pred[k]-outcome)**2
        for k in wins:wins[k]+=abs(pred[1]-truth)<abs(pred[k]-truth)
        rows.append((truth,outcome,pred))
    for k in wins:
        bins=[]
        for j in range(10):
            group=[(pred[k],y) for _,y,pred in rows if min(9,int(pred[k]*10))==j]
            if group:bins.append(dict(bin=j,n=len(group),forecast=statistics.mean(p for p,y in group),observed=statistics.mean(y for p,y in group)))
        yield dict(samples=k,cost_units=k,brier=loss[k]/n,junior_closer_to_latent_probability=wins[k]/n,bins=bins)
if __name__=='__main__':
    out=dict(platform=platform.platform(),python=platform.python_version(),cpu=platform.processor(),population=[population(n) for n in (120,2000,20000)],forecast=list(forecasts()),seed=20261106)
    Path('research/results/world_bench.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2)[:2600])
