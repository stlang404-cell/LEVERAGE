"""Synthetic format-selection comparison, not calibrated LEVERAGE match strengths."""
from pathlib import Path
import random,math,json,statistics

def trial(n,fmt,seed):
    rng=random.Random(seed);latent=[2000-40*i for i in range(n)];observed=[v+rng.gauss(0,80) for v in latent];ranking=sorted(range(n),key=lambda i:(-observed[i],i));games=0;loads=[0]*n
    def game(a,b):
        nonlocal games
        games+=1;loads[a]+=1;loads[b]+=1
        u=rng.random();draw=.25
        if u<draw:return .5
        return float((u-draw)/(1-draw)<min(1,max(0,1/(1+10**((latent[b]-latent[a])/400))+.03)))
    def pair(a,b):
        score=game(a,b)+1-game(b,a)
        if score==1:
            score+=game(a,b)+1-game(b,a)
            if score==2:return a if observed[a]>=observed[b] else b
            return a if score>2 else b
        return a if score>1 else b
    if fmt=='knockout':
        alive=ranking
        while len(alive)>1:alive=[pair(alive[i],alive[-i-1]) for i in range(len(alive)//2)]
        winner=alive[0]
    elif fmt=='round_robin':
        scores=[0.0]*n
        for a in range(n):
            for b in range(a+1,n):
                value=game(a,b)+1-game(b,a);scores[a]+=value;scores[b]+=2-value
        winner=max(range(n),key=lambda i:(scores[i],observed[i],-i))
    else:
        scores=[0.0]*n;met=set()
        for _ in range(math.ceil(math.log2(n))+1):
            todo=sorted(range(n),key=lambda i:(-scores[i],-observed[i],i))
            while todo:
                a=todo.pop(0);b=next((j for j in todo if tuple(sorted((a,j))) not in met),todo[0]);todo.remove(b);met.add(tuple(sorted((a,b))))
                value=game(a,b)+1-game(b,a);scores[a]+=value;scores[b]+=2-value
        finalists=sorted(range(n),key=lambda i:(-scores[i],-observed[i],i))[:2];winner=pair(*finalists)
    return dict(selected_best=winner==0,winner_true_rank=winner+1,games=games,champion_games=loads[winner],max_games=max(loads))
if __name__=='__main__':
    summaries=[]
    for n in (4,8,16):
        for fmt in ('knockout','round_robin','swiss_final'):
            rows=[trial(n,fmt,s) for s in range(1000)];p=statistics.mean(x['selected_best'] for x in rows);z=1.96;d=1+z*z/1000;center=(p+z*z/2000)/d;half=z*math.sqrt(p*(1-p)/1000+z*z/4000000)/d
            summaries.append(dict(entrants=n,format=fmt,trials=1000,best_selected=p,binomial_wilson95=[center-half,center+half],mean_winner_true_rank=statistics.mean(x['winner_true_rank'] for x in rows),median_total_games=statistics.median(x['games'] for x in rows),median_champion_games=statistics.median(x['champion_games'] for x in rows),max_games_any_player=max(x['max_games'] for x in rows)))
    Path('research/results/r0/tournaments.json').write_text(json.dumps(dict(seed_range=[0,999],draw_probability=.25,first_seat_logistic_bonus=.03,observed_rating_noise_sd=80,paired_games=True,summary=summaries),indent=2)+'\n');print(json.dumps(summaries,indent=2)[:1500])
