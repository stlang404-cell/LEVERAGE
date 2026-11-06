# Continuation experimental results

**Experimentally supported:** observed behavior under the named weak research agents, not human depth or optimal fairness. **Verified:** stated command completed and result records exist.

392 new games, seven configurations, eight independent seed clusters per configuration. Runtime 262.73 s; 3.12.14, Linux-6.18.57-x86_64-with-glibc2.41. Concurrent synthetic population work can affect elapsed times. No Windows/iPhone runtime was used.

## Protocol

Per configuration and seed 0–7: one random/random game, color-swapped greedy/random, tactical/greedy and deep/tactical pairs (7 games per seed, 56 per configuration). No duplicate random/random color swaps. Different protocols sharing a seed are clustered together in uncertainty estimates. The same seeds across configurations are matched random streams but trajectories diverge. Record all moves, not only openings. All agents use the SAME evaluator and terminal handling. Greedy depth cap 1, tactical 2, deep 4; iterative deepening commits only a fully completed root iteration. Each turn has hard 800-node cap including prior iterations; actual nodes and deepest completed iteration are retained. Uncompleted deeper searches are discarded; deeper cap is not evidence of reaching that depth. No quiescence, learned evaluation or transposition table.

Intervals: percentile bootstrap of 8 seed clusters, 5,000 resamples with seed 112. Small cluster count makes these exploratory intervals unstable. All-win/all-draw clusters yield degenerate intervals; that is not zero true uncertainty. First-player score includes 0.5 per draw and pools these protocols; it measures this experiment, not game-theoretic advantage. Agent score is measured across both colors within each seed. Seeds are not humans or an independent evaluator. Do not use these intervals to certify fairness.

|Config|First / draw / second|First score [cluster 95%]|Plies p50 / p90|Mean branch|End reasons|Distinct first / four-ply openings|
|---|---|---|---|---|---|---|
|free5|12 / 25 / 19|0.438 [0.411–0.464]|32.5 / 120|8.6|{'limit': 13, 'anchor': 31, 'repetition': 12}|6 / 25|
|breach5|12 / 24 / 20|0.429 [0.375–0.491]|33 / 120|8.5|{'anchor': 32, 'repetition': 18, 'limit': 6}|6 / 25|
|pressure5|12 / 27 / 17|0.455 [0.438–0.482]|31 / 120|8.5|{'repetition': 19, 'anchor': 29, 'limit': 8}|6 / 25|
|relay5|11 / 29 / 16|0.455 [0.402–0.509]|21 / 88|11.8|{'limit': 4, 'anchor': 27, 'repetition': 25}|6 / 24|
|pressure6|10 / 38 / 8|0.518 [0.491–0.545]|31.5 / 120|10.1|{'anchor': 18, 'limit': 12, 'repetition': 26}|6 / 25|
|pressure7|6 / 43 / 7|0.491 [0.464–0.518]|103 / 120|12.0|{'limit': 26, 'anchor': 13, 'repetition': 17}|6 / 25|
|pressure5_formation|7 / 39 / 10|0.473 [0.446–0.491]|41 / 120|8.8|{'limit': 15, 'anchor': 17, 'repetition': 24}|8 / 32|

## Strength and completed search depth

|Config|Pair|Stronger W/D/L|Stronger score [paired 95%]|
|---|---|---|---|
|free5|greedy/random|16/0/0|1.000 [1.000–1.000]|
|free5|tactical/greedy|9/7/0|0.781 [0.750–0.844]|
|free5|deep/tactical|3/13/0|0.594 [0.531–0.688]|
|breach5|greedy/random|15/1/0|0.969 [0.906–1.000]|
|breach5|tactical/greedy|9/7/0|0.781 [0.750–0.844]|
|breach5|deep/tactical|4/11/1|0.594 [0.469–0.688]|
|pressure5|greedy/random|16/0/0|1.000 [1.000–1.000]|
|pressure5|tactical/greedy|9/7/0|0.781 [0.750–0.844]|
|pressure5|deep/tactical|1/15/0|0.531 [0.500–0.594]|
|relay5|greedy/random|15/0/1|0.938 [0.812–1.000]|
|relay5|tactical/greedy|8/8/0|0.750 [0.750–0.750]|
|relay5|deep/tactical|0/16/0|0.500 [0.500–0.500]|
|pressure6|greedy/random|14/2/0|0.938 [0.875–1.000]|
|pressure6|tactical/greedy|1/15/0|0.531 [0.500–0.594]|
|pressure6|deep/tactical|0/16/0|0.500 [0.500–0.500]|
|pressure7|greedy/random|10/6/0|0.812 [0.656–0.938]|
|pressure7|tactical/greedy|3/13/0|0.594 [0.531–0.688]|
|pressure7|deep/tactical|0/16/0|0.500 [0.500–0.500]|
|pressure5_formation|greedy/random|14/2/0|0.938 [0.875–1.000]|
|pressure5_formation|tactical/greedy|0/16/0|0.500 [0.500–0.500]|
|pressure5_formation|deep/tactical|0/16/0|0.500 [0.500–0.500]|

|Config|Deep agent completed depth counts|Move time p50 / p95 ms (all agents)|Disconnected side-positions / total side-positions|
|---|---|---|---|
|free5|{2: 78, 3: 561, 4: 60}|1.41 / 35.44|2393 / 5994|
|breach5|{2: 64, 3: 328, 4: 15}|0.67 / 62.01|1896 / 5274|
|pressure5|{2: 85, 3: 456, 4: 11}|1.22 / 36.92|1959 / 5422|
|relay5|{2: 133, 3: 38}|0.10 / 42.43|1264 / 3486|
|pressure6|{2: 130, 3: 127}|0.34 / 46.58|1575 / 5886|
|pressure7|{2: 636, 3: 133, 4: 13}|1.12 / 44.93|3775 / 9318|
|pressure5_formation|{2: 62, 3: 130}|0.30 / 35.49|2451 / 6896|

## Interpretation boundaries

No opening is proven dominant. Distinct action sequences do not establish strategic variety. No comeback cohort, human readability metric, calibrated rating ladder or subjective qualitative strategy change was measured. Agent comparisons can expose horizon sensitivity but cannot show exceptional depth. Node cap and evaluator may favor one configuration. The terminal limit is 120 instead of historical 100 and all continuation variants remove v0.1 empty-move connectivity, so compare mechanics to free5 within this run. Size comparisons also alter reserves. Population benchmark and forecast experiment are in world_bench.json.

**Verified by rule argument:** with only two anchors on board and empty reserves, every variant here has no route to capture: both powers are one, breach forbids anchors, relay lacks a friendly jumping piece, pressure pushes but never ejects. Thus all such endgames draw under the bound. This is a genuine strategic limitation, not repaired by the new mechanics. Reduced opening states were not solved. Next: anchor-pressure victory or targeted anchor vulnerability must be formally compared against network identity and teaching burden.

## Reproduction

From repository root: `python research/experiments/continuation.py`, `python research/experiments/world_bench.py`, `python research/experiments/continuation_report.py`, `python -m unittest discover -s research/experiments -v`. No dependencies outside Python 3.12 standard library. Baseline sources/results are preserved unchanged. Timing varies; game traces are deterministic for these scripts and budgets.
