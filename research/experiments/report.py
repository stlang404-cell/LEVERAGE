import json, math, statistics, hashlib, pathlib
from collections import Counter
r=json.loads(pathlib.Path('research/results/games.json').read_text());rows=r['games']
def quant(xs,p):return sorted(xs)[math.ceil(len(xs)*p)-1]
def wilson(w,n):
 z=1.96;d=1+z*z/n;c=(w/n+z*z/(2*n))/d;h=z*math.sqrt(w/n*(1-w/n)/n+z*z/(4*n*n))/d
 return f'{c-h:.2f}–{c+h:.2f}'
s=['# Simulation results','',f"Executed {len(rows)} games; {r['pairs']} seeds per pairing, each with swapped agents. Python 3.12 standard library. Runtime {r['seconds']:.2f} seconds. See raw games.json, tests.txt and manifest.json. No human playtesting.",'','## Aggregate observations','','First-player Wilson intervals describe outright wins only, not expected score. Samples pool different agents and paired outcomes are dependent; intervals are descriptive and are NOT a fairness inference.','', '|Candidate|Games|First wins / draws / second wins|First-win 95% Wilson|Plies p50 / p90 / p95|Mean legal moves|End reasons|Distinct first actions|','|---|---:|---|---|---|---:|---|---:|']
for game in sorted(set(x['game'] for x in rows)):
 a=[x for x in rows if x['game']==game];c=Counter(x['winner'] for x in a);lens=[x['plies'] for x in a];br=[b for x in a for b in x['branches']]
 s.append(f"|{game}|{len(a)}|{c[1]} / {c[0]} / {c[-1]}|{wilson(c[1],len(a))}|{statistics.median(lens):g} / {quant(lens,.9)} / {quant(lens,.95)}|{statistics.mean(br):.1f}|{dict(Counter(x['reason'] for x in a))}|{len(set(tuple(x['opening'][0]) for x in a))}|")
s+=['','## Agent comparisons','','W/D/L below is from the first named agent’s perspective, across both colors. Every pair uses seeds 0–7. Random/random duplicates under color swap are identical trajectories and must not be counted as independent samples. All agents use full legal rules and history; randomness selects moves or tie order, never match outcomes.','','|Candidate|Pairing|W / D / L|','|---|---|---|']
for game in sorted(set(x['game'] for x in rows)):
 for strong,weak in [('greedy','random'),('search','greedy')]:
  a=[x for x in rows if x['game']==game and set(x['agents'])=={strong,weak}];c=Counter(x['winner']*(1 if x['agents'][0]==strong else -1) for x in a)
  s.append(f'|{game}|{strong} vs {weak}|{c[1]} / {c[0]} / {c[-1]}|')
s+=['','## Protocol and limits','', 'Seeds 0–7; 100-ply hard draw; threefold repetition uses board, turn, reserves and energy, excluding ply. Greedy examines one ply; search examines up to two with alpha-beta and a target 400-node budget divided per root. Root evaluations are always performed, so 400 is a soft cap, not an equal wall-clock budget. Nodes and branching at each turn are retained. No learned evaluator, transposition table, quiescence, iterative deepening or MCTS. Sorted actions plus seeded tie permutation make runs reproducible on this Python implementation.', '', 'Opening diversity counts different first actions, not strategically distinct plans; four-ply sequences are retained. Comeback probability, optimal first-player advantage, forced opening wins, rating calibration, human interest, strategic depth and true dominant openings remain UNKNOWN. Depth-two superiority, where present, establishes only separation of these agents. Rule changes require complete reruns.', '', '## Next experiments','', 'Run 200 independent seeds per paired comparison; report cluster-bootstrap intervals over seed pairs for first-player score and agent strength. Extend to depths 2/4/6 at fixed measured node budgets and tuned evaluation. Sweep Leverage over 6×6/7×7 and reserve counts only after formalizing those variants. Enumerate reduced-board endgames and perform proof-number search on tactical failures. Define a comeback cohort by a preregistered independent evaluation gap; avoid selecting only eventual winners. Recruit at least 12 human testers for teach-back, strategic diversity and repeated-session interest.']
vpath=pathlib.Path('research/results/variants.json')
if vpath.exists():
 variants=json.loads(vpath.read_text())
 s+=['', '## Connectivity follow-up: separate rules variants', '', 'Executed 96 additional games (48 per variant), same seeds/agents/budgets. strict_connected rejects ANY action whose resulting own pieces are not all in the own anchor component. own_cleanup keeps the v0.1 generator but removes all disconnected OWN pieces after every action, in addition to the original enemy capture cleanup. These are distinct research rules, not v0.1 changes. Both use the base terminal rules.', '', '|Variant|First / draw / second|Ending reasons|', '|---|---|---|']
 for v,a in variants.items():
  c=Counter(x['winner'] for x in a)
  s.append(f"|{v}|{c[1]} / {c[0]} / {c[-1]}|{dict(Counter(x['reason'] for x in a))}|")
 s+=['', 'Strict connectivity drew all 48 sampled games; own cleanup drew 29/48. Reject BOTH as default fixes on this evidence. Neither warrants replacing v0.1. The no-connectivity-constraint variant and deeper opponents remain next experiments. These samples do not prove forced draws.']
pathlib.Path('research/04_SIMULATION_RESULTS.md').write_text('\n'.join(s)+'\n')
files=['research/experiments/arena.py','research/experiments/test_lab.py','research/results/games.json','research/experiments/variants.py','research/results/variants.json']
pathlib.Path('research/results/manifest.json').write_text(json.dumps({'command':'python research/experiments/arena.py --pairs 8','python':'3.12.14','seed_range':[0,7],'files_sha256':{p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() for p in files}},indent=2)+'\n')
print('\n'.join(s[:16]))
