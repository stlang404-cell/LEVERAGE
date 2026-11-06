# Board-game research — final R0

**Decision: RESEARCH STOP.** No selected ruleset for production or freeze. Read the [final report](LEVERAGE_R0_FINAL_RESEARCH_REPORT.md) for the decision and [quantitative appendix](../research/21_R0_RESULTS.md) for reproducible comparisons.

## What changed in the evidence

All 728 earlier recorded games reproduced. The old draw counts were correct, but only 10 of 225 v0.2 draws reached the bare-anchor trap. Most larger-board draws require other explanations; they are not proved unavoidable. Current R0 retains history and clock effects instead of declaring every repetition a structural defect.

Three independently specified games were implemented and compared: [EA-0.3.0, BW-0.3.0 and WR-0.3.0 formal rules](../research/20_R0_FORMAL_CANDIDATES.md). In 672 main games (224 each), draws were 61, 156 and 0. The 248 other executions test size, deployment, power, collapse, reserves, formation, evaluator and larger compute; 16 repeat main identities as controls. Full trial IDs and paired uncertainty are retained.

A repairs unconditional anchor-capture deadlocks and shows some depth separation, but canonical deep/tactical controls draw 14/16. B's road objective rarely decides results and both stronger main pairings draw every game. C is finite and decisive, but 223/224 games end in immobilization, with no deep-over-tactical advantage and an observed first-seat score of 0.670. None earns advancement simply by outperforming random agents or eliminating draws.

**Verified in scope:** 10,000 sampled states, 9,326 unique configuration-positions and 97,623 independent transition comparisons, plus independent terminal checks and tactical tests. A exact anchor-only tablebases are decisive under fresh history on 5/6/7 boards. Human interest and readability remain unknown. No opening solution for a full-size candidate was established.

## Current research lead, not winner

A (Exposed Anchor EA-0.3.0) is the smallest diagnostic lead, not a production selection. Analyze one archived first-repetition position with full history before building more systems. A predeployed formation is only an exploratory lead; it is not silently adopted. Weighted rankings reverse under reasonable preferences and leave 51% weight unknown.

## Traceability and running

- [Frozen v0.1 rules](../research/03_FORMAL_RULESETS.md), [original results](../research/04_SIMULATION_RESULTS.md), [v0.2 rules](../research/18_CONTINUATION_FORMAL_RULES.md), [v0.2 results](../research/19_CONTINUATION_RESULTS.md).
- [New rules](../research/20_R0_FORMAL_CANDIDATES.md), [new results](../research/21_R0_RESULTS.md), [R0 guide](../research/experiments/r0/README.md), [raw summary](../research/results/r0/summary.json), [audit](../research/results/r0/audit.json), [manifest](../research/results/r0/manifest.json).

Local human research harness: `python -m research.experiments.r0.play --candidate A`. This is a research inspection tool with selectable candidates, not authorization to implement rejected games as release modes. Original historical sources and raw evidence remain unchanged.
