# Final R0 quantitative appendix

**Experimentally supported:** behaviors of these agents and configurations only. **Verified:** completed records and targeted/oracle tests. No human fun/depth result or release fairness claim. Exact candidate rules are in [20_R0_FORMAL_CANDIDATES.md](20_R0_FORMAL_CANDIDATES.md).

## Main protocol

Three candidates × 32 seeds (0–31) × 7 games = **672 games**, including **288 color-swapped unequal-agent pairs** and 96 single random/random controls. Even seeds use canonical starts; odd seeds share a two-random-legal-ply opening before both paired games. All agents use public state; no random outcome rule. Greedy/tactical/deep have depth caps 1/2/4 and common hard 1,200-node turn ceiling; actual effort varies with completed depths. Iterative deepening accepts only completed roots. Cache stores legal lists, static evaluations and preferred moves, NEVER repetition-sensitive search values. Entries bounded at 4,096 per table; ordering can alter budgeted results. Deeper roots share alpha safely; correctness tested against exhaustive depth-two minimax on 24 sampled states. Alternate evaluator is untuned material/centrality, not a learned or independently rated engine.

Intervals use percentile bootstrap over 32 matched seed clusters (3,000 resamples, seed 5901); eight or four clusters for smaller diagnostics. Agent pairs and protocols sharing a seed are correlated. Degenerate intervals from all wins/draws do not imply zero true uncertainty. First-player score includes half a draw, pools deliberately different agents and starting-position modes, and is NOT optimal first-player advantage. Raw first-action/four-ply counts concern actions after the shared prefix, not distinct strategic plans.

|Candidate|N|First / draw / second|First score [95% cluster]|Length p50 / p90 / p95|Branch p50 / p90 / mean|Endings|
|---|---:|---|---|---|---|---|
|A|224|78 / 61 / 85|0.484 [0.444–0.525]|23.5 / 71 / 109|9 / 14 / 9.1|{'anchor': 163, 'repetition': 53, 'limit': 8}|
|B|224|32 / 156 / 36|0.491 [0.480–0.500]|87 / 120 / 120|8 / 13 / 8.9|{'insufficient_road_material': 12, 'immobile': 65, 'repetition': 68, 'limit': 76, 'road': 3}|
|C|224|150 / 0 / 74|0.670 [0.594–0.737]|18 / 19 / 19|4 / 7 / 4.3|{'immobile': 223, 'delivered_two': 1}|

## Skill differentiation

|Candidate|Stronger / weaker|W / D / L|Score [paired cluster 95%]|
|---|---|---|---|
|A|greedy/random|64 / 0 / 0|1.000 [1.000–1.000]|
|A|tactical/greedy|41 / 18 / 5|0.781 [0.711–0.844]|
|A|deep/tactical|21 / 42 / 1|0.656 [0.594–0.719]|
|B|greedy/random|63 / 1 / 0|0.992 [0.977–1.000]|
|B|tactical/greedy|0 / 64 / 0|0.500 [0.500–0.500]|
|B|deep/tactical|0 / 64 / 0|0.500 [0.500–0.500]|
|C|greedy/random|49 / 0 / 15|0.766 [0.656–0.859]|
|C|tactical/greedy|38 / 0 / 26|0.594 [0.531–0.672]|
|C|deep/tactical|32 / 0 / 32|0.500 [0.422–0.578]|

## Search behavior, interaction and opening counts

|Candidate|Deep completed depth counts|Move ms p50 / p95, all agents|Captures / multi-piece collapses|Distinct first / four-action prefixes|Anchor-only reached|
|---|---|---|---|---|---|
|A|{2: 8, 3: 223, 4: 1118}|1.03 / 65.07|556 / 274|15 / 109|0|
|B|{3: 221, 4: 3540}|1.86 / 88.97|599 / 241|12 / 119|0|
|C|{4: 552}|0.16 / 5.61|0 / 0|14 / 123|0|

Timing includes concurrent runs on a Linux/Python 3.12 environment with four CPU-equivalents and 32 GiB cgroup RAM limit. Main process max RSS includes retained results and interpreter, not just search heap: see per-file metadata (A 38,928 KiB; B 52,028 KiB; C 18,624 KiB in delivered run). Separate cache-on/off cold-position timing and traced-allocation experiments are in bench.json. Tracing costs are excluded from benchmark timing samples. No Windows/phone or full-world inference follows.

## Controlled board-size sweep

Same reserves (A 5, B 8 plus starting piece, C no reserves/three runners), canonical start and deep/tactical paired seeds 0–3 at each size. 5x5 uses canonical controls, not the mixed main pool. Only four paired seeds per size: descriptive, not a board-size verdict. A draws 8/8, 5/8 and 4/8 at sizes 5/6/7, so this controlled test does not support a universal larger-is-worse conclusion. C first/second seat outcomes flip with board-fill parity: 5x5 first wins 8/8, 6x6 second wins 7/8, 7x7 first wins 7/8; medians reach 19/30/43 plies. Filling all empties gives last-move parity, but earlier immobilization can change it and the 5x5 root is not solved.

|Candidate / size|N|First / draw / second|Length median|Mean branch|Deep completed depths|
|---|---|---|---|---|---|
|A/5|8|0 / 8 / 0|18.5|9.0|{2: 2, 3: 24, 4: 60}|
|A/6|8|1 / 5 / 2|44.5|9.7|{2: 3, 3: 80, 4: 159}|
|A/7|8|2 / 4 / 2|56|10.3|{2: 8, 3: 46, 4: 205}|
|B/5|8|0 / 8 / 0|120|8.0|{3: 25, 4: 455}|
|B/6|8|0 / 8 / 0|120|9.5|{3: 194, 4: 286}|
|B/7|8|0 / 8 / 0|120|14.1|{2: 13, 3: 379, 4: 88}|
|C/5|8|8 / 0 / 0|19|4.3|{4: 76}|
|C/6|8|1 / 0 / 7|30|4.5|{4: 113}|
|C/7|8|7 / 0 / 1|43|4.4|{4: 167}|

## Exploratory A ablations

All canonical deep/tactical pairs, seeds 0–7, 16 games/configuration. These controls were exploratory after main observations. Compare to the matching canonical control, not the random/greedy-enriched main total.

|Config|W / draw / second|Endings|
|---|---|---|
|A5|2 / 14 / 0|{'repetition': 13, 'anchor': 2, 'limit': 1}|
|A5_component_power|1 / 15 / 0|{'repetition': 14, 'limit': 1, 'anchor': 1}|
|A5_formation|1 / 7 / 8|{'repetition': 7, 'anchor': 9}|
|A5_reserve3|2 / 14 / 0|{'anchor': 2, 'repetition': 14}|
|A5_reserve7|0 / 11 / 5|{'repetition': 8, 'anchor': 5, 'limit': 3}|
|A5_rooted|1 / 15 / 0|{'repetition': 15, 'anchor': 1}|
|A5_target_only|1 / 15 / 0|{'repetition': 14, 'anchor': 1, 'limit': 1}|

## Compute and evaluator sensitivity

|Condition|Candidate|Strong W / D / L|Score [paired 95%]|
|---|---|---|---|
|strength6000.json|A|8 / 8 / 0|0.750 [0.625–0.875]|
|strength6000.json|C|9 / 0 / 7|0.562 [0.500–0.688]|
|profiles.json|A|8 / 8 / 0|0.750 [0.625–0.875]|
|profiles.json|B|0 / 8 / 0|0.500 [0.500–0.500]|
|profiles.json|C|7 / 0 / 9|0.438 [0.312–0.500]|

The 6,000-node agent has depth cap six; this is a disclosed larger-compute comparison, not an equal-effort depth experiment. Material evaluator comparisons use canonical even seeds 0–14 for A/C and 0–6 for B; compare to matching main subsets, not aggregate rates. Neither profile is trained/calibrated or a human skill model. Material evaluation omits the B road/C race features, so it is a feature ablation, not an independent expert engine.

## Old draw classification and exact endgames

All prior 240 baseline, 96 connectivity and 392 continuation records reproduced, excluding elapsed timing. Previous seven draw totals match exactly. Only **10 of 225** prior continuation draws reached two anchors with exhausted reserves. Pressure7 had 26 move-limit draws and 17 repetitions, but zero bare-anchor cases; therefore bare-anchor deadlock cannot explain its observed decline. Pressure6 had 17 zero-capture games versus 4 for pressure5. Old pressure7 deep agent completed depth two on 636/782 turns versus 85/552 for pressure5. Density, interaction and search coverage differ; size/reserves were confounded previously. All old limit draws had exhausted reserves. Remaining non-bare-anchor traps are NOT proved unavoidable. Raw per-game diagnostics are in prior_draw_diagnosis.json.

Exact A fresh-history anchor-only retrograde tablebases: 1,200 / 2,520 / 4,704 states on sizes 5/6/7; zero drawn states, maximum attractor layers 14/18/22. Independent coordinate-oracle Bellman verification covers all 1,200 5x5 entries. Existing repetition/remaining 120-ply clock can override fresh-history conclusions. No main A game reached the bare-anchor class: this mathematical repair is real, but does not by itself validate the full-game draw reduction.

C has a monotone bound n²−6 moves and cannot repeat; 5x5 root remains UNKNOWN after 250,000 proof-search nodes (not a draw). Reduced 3x3 root is a proved first-player win, 4x4 a proved second-player win under this reference. Their outcomes do not solve 5x5. Initially occupied home cells never become empty because of wakes; at most n−3 entry gaps remain, so two-delivery is impossible on the reduced 3/4 boards. Those small solutions are immobilization outcomes. B declares a draw when both sides lack n total potential pieces, which preempts later immobilization contests; this is an explicit adjudication choice, not a general solved endgame.

No full-board dominant opening, calibrated comeback rate, human strategic diversity, enjoyment or qualitative depth is established. Completed-depth changes and deterministic action divergence are not proof of chess-level depth.

## Weighted framework and sensitivity

Criteria weights: simplicity 12, tactics 10, position 14, skill separation 12, draw behavior 12, diversity 8, endgame quality 8, AI feasibility 8, visual readability 6, originality 5, implementation risk 5. The unknown experiential criteria sum to 51 weight. Unknown criteria range 1–5, not disguised as measured scores. Designer provisional simplicity/AI/risk: A 4/4/4, B 3/2/3, C 4/4/4; these are hypotheses. Observed-skill proxy = 1+8·max(0, deep score−0.5), capped at 5; draw proxy = 1+4·(1−draw fraction). They are declared preference transforms, not depth metrics. Proxies use the mixed main sample and should not overrule canonical evidence.

Default midpoint totals and ranges below use unknown midpoint 3 versus extremes 1/5. Draw-heavy shifts eight points from position to draws; skill-heavy shifts eight points from position to skill. Overlapping ranges and ranking changes prohibit a robust winner claim. A final human prototype decision cannot be manufactured from midpoint scores.

|Weights|A midpoint [range]|B midpoint [range]|C midpoint [range]|Midpoint lead|
|---|---|---|---|---|
|default|65.4 [45.0–85.8]|51.7 [31.3–72.1]|65.0 [44.6–85.4]|A|
|draw_heavy|66.8 [49.6–84.0]|50.5 [33.3–67.7]|68.2 [51.0–85.4]|C|
|skill_heavy|64.2 [47.0–81.4]|48.5 [31.3–65.7]|61.8 [44.6–79.0]|A|

**Decision: RESEARCH STOP for production and rules freeze.** No winner. A is the best narrowly scoped diagnostic lead because it retains identity, repairs a proved endgame defect and shows some search separation. Its default canonical deep/tactical control draws 14/16; higher-compute comparisons still draw 8/16. B/C are rejected for advancement under current evidence, not proved devoid of interesting play. The smallest next task is a proof/strong-search analysis of one archived first-repetition A canonical position, then a tightly bounded human teach-back/replay session if a defensible alternative is found. Do not expand corporate production to avoid this gate.

## Reproduce

Use `python -m research.experiments.r0.run --candidate A --seeds 32` (repeat B/C); `--sizes --seeds 4` for each candidate. Commands and diagnostics are listed in r0/README.md. Run writes only owned R0 outputs; use --output-dir for isolated reruns. Historical files remain unchanged. `report.py` regenerates this appendix plus summary/weights JSON; `audit.py` checks every recorded transition with the independent oracle, terminal results and budget ceilings.
