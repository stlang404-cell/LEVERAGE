# Simulation results

Executed 240 games; 8 seeds per pairing, each with swapped agents. Python 3.12 standard library. Runtime 4.45 seconds. See raw games.json, tests.txt and manifest.json. No human playtesting.

## Aggregate observations

First-player Wilson intervals describe outright wins only, not expected score. Samples pool different agents and paired outcomes are dependent; intervals are descriptive and are NOT a fairness inference.

|Candidate|Games|First wins / draws / second wins|First-win 95% Wilson|Plies p50 / p90 / p95|Mean legal moves|End reasons|Distinct first actions|
|---|---:|---|---|---|---:|---|---:|
|allocation|48|23 / 0 / 25|0.34–0.62|12 / 31 / 48|17.0|{'leader': 48}|10|
|commitment|48|16 / 2 / 30|0.22–0.47|24.5 / 82 / 100|8.9|{'leader': 46, 'limit': 2}|5|
|leverage|48|14 / 13 / 21|0.18–0.43|27.5 / 51 / 52|5.2|{'repetition': 13, 'leader': 35}|6|
|orbit|48|20 / 18 / 10|0.29–0.56|9 / 100 / 100|16.7|{'delivery': 30, 'limit': 8, 'repetition': 10}|7|
|relay|48|22 / 2 / 24|0.33–0.60|17 / 53 / 78|11.1|{'leader': 30, 'delivery': 16, 'limit': 2}|5|

## Agent comparisons

W/D/L below is from the first named agent’s perspective, across both colors. Every pair uses seeds 0–7. Random/random duplicates under color swap are identical trajectories and must not be counted as independent samples. All agents use full legal rules and history; randomness selects moves or tie order, never match outcomes.

|Candidate|Pairing|W / D / L|
|---|---|---|
|allocation|greedy vs random|15 / 0 / 1|
|allocation|search vs greedy|16 / 0 / 0|
|commitment|greedy vs random|14 / 0 / 2|
|commitment|search vs greedy|16 / 0 / 0|
|leverage|greedy vs random|11 / 4 / 1|
|leverage|search vs greedy|12 / 3 / 1|
|orbit|greedy vs random|16 / 0 / 0|
|orbit|search vs greedy|6 / 10 / 0|
|relay|greedy vs random|16 / 0 / 0|
|relay|search vs greedy|16 / 0 / 0|

## Protocol and limits

Seeds 0–7; 100-ply hard draw; threefold repetition uses board, turn, reserves and energy, excluding ply. Greedy examines one ply; search examines up to two with alpha-beta and a target 400-node budget divided per root. Root evaluations are always performed, so 400 is a soft cap, not an equal wall-clock budget. Nodes and branching at each turn are retained. No learned evaluator, transposition table, quiescence, iterative deepening or MCTS. Sorted actions plus seeded tie permutation make runs reproducible on this Python implementation.

Opening diversity counts different first actions, not strategically distinct plans; four-ply sequences are retained. Comeback probability, optimal first-player advantage, forced opening wins, rating calibration, human interest, strategic depth and true dominant openings remain UNKNOWN. Depth-two superiority, where present, establishes only separation of these agents. Rule changes require complete reruns.

## Next experiments

Run 200 independent seeds per paired comparison; report cluster-bootstrap intervals over seed pairs for first-player score and agent strength. Extend to depths 2/4/6 at fixed measured node budgets and tuned evaluation. Sweep Leverage over 6×6/7×7 and reserve counts only after formalizing those variants. Enumerate reduced-board endgames and perform proof-number search on tactical failures. Define a comeback cohort by a preregistered independent evaluation gap; avoid selecting only eventual winners. Recruit at least 12 human testers for teach-back, strategic diversity and repeated-session interest.

## Connectivity follow-up: separate rules variants

Executed 96 additional games (48 per variant), same seeds/agents/budgets. strict_connected rejects ANY action whose resulting own pieces are not all in the own anchor component. own_cleanup keeps the v0.1 generator but removes all disconnected OWN pieces after every action, in addition to the original enemy capture cleanup. These are distinct research rules, not v0.1 changes. Both use the base terminal rules.

|Variant|First / draw / second|Ending reasons|
|---|---|---|
|strict_connected|0 / 48 / 0|{'repetition': 40, 'immobile': 6, 'limit': 2}|
|own_cleanup|10 / 29 / 9|{'repetition': 23, 'immobile': 4, 'leader': 19, 'limit': 2}|

Strict connectivity drew all 48 sampled games; own cleanup drew 29/48. Reject BOTH as default fixes on this evidence. Neither warrants replacing v0.1. The no-connectivity-constraint variant and deeper opponents remain next experiments. These samples do not prove forced draws.
