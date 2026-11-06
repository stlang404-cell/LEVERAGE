# LEVERAGE final R0 research report

## 1. Executive recommendation

**RESEARCH STOP.** No candidate is selected for production or rules freeze. This is a stop on expansion, not a proof that the network idea cannot work. Do not ask Claude to build the corporate civilization around a rejected or unapproved board game. The revised master prompt is ready for a tightly scoped diagnostic task only.

## 2. Baseline and version preservation

Baseline commit: `ac7c71964f7331f1fc56282320891497385ce6c0`, branch `research/leverage-design-refinement`. Working tree was clean. All **240 v0.1**, **96 connectivity-variant**, and **392 v0.2** game records reproduced exactly, excluding elapsed times. Original rules, sources and raw results are retained; historical reports remain traceable. The old seven draw totals are verified: 25, 24, 27, 29, 38, 43 and 39 out of 56 each.

## 3. Exact new candidates and comparison

[Formal rules](../research/20_R0_FORMAL_CANDIDATES.md) specify every action, initial position, cleanup and terminal priority. None is a release recommendation.

|Candidate / exact version|New mechanism|Disposition|
|---|---|---|
|A — Exposed Anchor **EA-0.3.0**|Prior free-movement network plus unconditional adjacent capture of enemy anchors; strict support captures against agents|Best diagnostic lead; not approved. Repairs a proved endgame defect but canonical strong-agent repetition remains severe|
|B — Bridgework **BW-0.3.0**|Home-row supply, target-cell support capture, rooted network collapse, road victory|Reject advancement. Objective rarely decides games; stronger-agent pairings all drew in main test|
|C — Wake Race **WR-0.3.0**|Three runners leave permanent blockers; deliver two or immobilize opponent|Reject advancement. Decisive finite games, but almost all outcomes are traps rather than the intended race, and depth advantage is unreliable|

Independent means different from the network game, not proved historically novel. B resembles connection-game families; C resembles blocking/racing families. No exhaustive prior-art or human study was conducted.

## 4. New experimental evidence

**672 main games**: three candidates × 32 seeds × seven games. These contain **288 swapped-color unequal-agent pairs**, plus 96 random/random games. Canonical and shared two-ply randomized starting positions are separated in raw data. Additional size, ablation, compute, evaluator and canonical-control runs bring the total to **920 recorded executions / 904 distinct config-agent-seed-opening-profile trial identities**; 16 controls repeat main conditions. These are not 904 statistically independent observations. Separately, 9,000 synthetic tournament-selection trials are not board-game matches.

|Candidate|First wins / draws / second wins|Draw rate|Median / p90 plies|Deep vs tactical W/D/L|
|---|---|---:|---|---|
|A|78 / 61 / 85|27.2%|23.5 / 71|21 / 42 / 1|
|B|32 / 156 / 36|69.6%|87 / 120|0 / 64 / 0|
|C|150 / 0 / 74|0%|18 / 19|32 / 0 / 32|

[Quantitative appendix](../research/21_R0_RESULTS.md) includes paired cluster intervals, seat estimates, branch distributions, interactions, completed depths, opening counts, memory/runtime and every controlled comparison. First-player expected-score estimates in this agent mix: A 0.484 [0.444–0.525], B 0.491 [0.480–0.500], C 0.670 [0.594–0.737]. They are not game-theoretic fairness estimates. C's observed initiative warning must not be hidden by its zero draw rate.

## 5. Draw and deadlock diagnosis

**Verified:** only **10 of 225** old v0.2 draws reached the proven anchor-only deadlock. Most retained other material. Pressure7 had zero anchor-only cases, 26 move-limit draws and 17 repetitions. Therefore anchor deadlock was a real defect but not the main empirical explanation. Old pressure7 deep search completed depth two on 636/782 turns, versus 85/552 on pressure5; size, reserves, contact density and search coverage were confounded. This round keeps reserve quantities fixed across 5/6/7 sweeps: A drew 8/8, 5/8 and 4/8 respectively. The tiny four-pair samples do not support a universal larger-is-worse verdict or a larger-board recommendation.

**Verified in exact analysis:** A's fresh-history anchor-only tablebases have 1,200/2,520/4,704 positions on 5/6/7 boards, all decisive, with attractor bounds 14/18/22 plies. Independent Bellman checks cover all 1,200 5×5 entries. This does not override preexisting repetition counts or a nearly exhausted move limit. No main A game reached that class, so it cannot explain every full-game improvement.

A still drew **14/16** default canonical deep/tactical controls. The predeployed formation drew 7/16 in a small exploratory comparison—an interesting next hypothesis, not a rule-freeze result. Root-only deployment, component-size power and capture-without-collapse each drew 15/16; changing reserves did not establish a robust fix. No arbitrary material score was used to make A look decisive.

## 6. AI differentiation and compute limits

Greedy/tactical/deep use depth caps 1/2/4, a common 1,200-node ceiling, iterative deepening and history-safe move/static caches. A deep expected score versus tactical is 0.656 [0.594–0.719]. Most deep A and B turns completed depth four, improving on prior search coverage. C completed depth four on all its deep-agent moves but scored only 0.5 against tactical. A larger 6,000-node/depth-six agent scored 8 wins/8 draws against the 1,200-node agent; C scored 9 wins/7 losses. These are eight-pair diagnostics with unequal disclosed compute, not strong-engine certification.

Untuned material evaluation also leaves B drawing; A shows some deeper-search benefit under it. The material control omits B road/C race features and is not an independent expert engine. Evaluation quality remains a confound. Search was checked against exhaustive depth-two minimax on 24 sampled positions. No grandmaster, chess-level depth or human-like understanding claim is supported.

## 7. Exploits and unresolved weaknesses

No full-size forced opening or dominant strategy has been proved. A can leave disconnected support islands and repeat with material; the winning alternative may exceed search horizon or may not exist. B's road condition decided only three main games; its insufficient-road-material rule explicitly adjudicates some draws before possible future immobilization. C's monotone empty-cell count bounds 5×5 games by 19 plies; 223/224 ended by immobilization. The small size sweep favors the first seat 8/8 on 5×5, second 7/8 on 6×6 and first 7/8 on 7×7, consistent with last-move parity when the board fills; early immobilization can alter that. Its 5×5 opening remains UNKNOWN after 250,000 proof nodes. Reduced 3×3 is a proved first-player win and 4×4 a proved second-player win; neither solves 5×5. Initially occupied home-row cells never become empty because of wakes, leaving at most n−3 entry gaps: the two-delivery goal is impossible on those reduced boards and has exactly two available entry cells on 5×5. Their small solved outcomes concern immobilization. Agent action diversity is not established strategic diversity.

Weighted criteria and three sensitivity settings are in the appendix. Unknown human/strategic dimensions hold 51% of total weight. Default midpoint scores barely favor A; draw-heavy weights favor C. Ranges overlap widely. No numerical ranking earns a winner or defeats the stop gate.

## 8. Human playability

A playable local [CLI research interface](../research/experiments/r0/play.py) supports human-vs-AI, legal-action inspection, support and capture consequences. Its scripted smoke transcript is retained. **No human participant playtested it.** Enjoyment, teachability, visual clarity and long-term mastery remain unverified. The CLI is not a pixel-art product, usability study or Windows/iPhone validation.

## 9. Corporate competition refinements

Keep **apply → compete → approval → promote**. Use two finalists for routine lead vacancies, reusable qualification circuits for larger roles, and rare governance-backed CEO finals. Automatic applications reuse published evidence; they never create fake vacancies or grind XP. Spectator/background skips process committed outcomes; personal mandatory matches require play or explicit withdrawal/forfeit. AI teammates may represent teams but cannot impersonate a human's individual rating.

The synthetic format experiment exposes cost: at eight entrants, paired round robin had a median 56 total games / 14 champion games; knockout 18 / 8, Swiss-plus-final 34 / 10 under its assumptions. It is not calibrated to LEVERAGE. Formats, tie policy and appointment contract are posted before entry, and high draw rates block freezing official competition. Rank unlocks public-data research tools and budget scope, never stronger board pieces or privileged open-market engine information.

## 10. What is ready for Claude

The [master prompt](LEVERAGE_CLAUDE_MASTER_PROMPT.md) is ready to reproduce evidence and diagnose one archived canonical A repetition. Pure rules, independent oracle, tested fixtures, budgeted search, exact endgame code, CLI and corporate/UI/finance constraints provide a concrete research base. The intended product remains a corporate civilization with meaningful positions, persistent history, ownership and optional fictional-money markets.

## 11. What remains provisional

Rules choice, human interest, true seat advantage, competitive ratings/AI calibration, comeback dynamics, broad novelty, official tournament tie resolution, full market lifecycle and full-world/platform performance. Historical accounting and synthetic population/forecast tests remain limited; no production economy, 20k-person world, Windows installer or iPhone PWA is delivered.

## 12. Smallest next task and implementation gate

Take the first repeated position from **A5 canonical, seed 0, deep/tactical**, use the [frozen nonterminal case](../research/results/r0/repetition_case.json) with its full history and run an independent bounded win/proof investigation at a larger documented budget. Distinguish a forced draw from a horizon/evaluation failure; UNKNOWN must remain unknown. Demonstrate a defensible alternative line before adding new mechanics. If useful, run a bounded teach-back/replay trial with human participants; do not simulate enjoyment using bots.

Only reopen the prototype/rules decision when canonical strong-agent behavior and human repeated play justify it. The prior <15% nonterminal-draw target is provisional, but was not met and is not silently relaxed. If the focused task fails, retire this network capture formulation or commission a new core-game invention rather than expand production.

## 13. Reproducible evidence and claim audit

**Verified:** baseline reproductions; 34 passing tests; 10,000 sampled state/oracle comparisons (9,326 unique), 97,623 compared transitions; independent checks of all 42,765 recorded moves and terminal results; three exact representative replays; exact reduced analyses; documentation checks. **Experimentally supported:** observed match/compute/format results. **Plausible but unverified:** career, economy and minimal UI designs. **Speculative:** fun, exceptional depth and release scale. **Rejected:** advancing any current candidate or claiming a definitive winner.

Commands, raw files, audit results and hash manifests are linked from the [hub](LEVERAGE_README.md) and [R0 harness guide](../research/experiments/r0/README.md). Historical sources/results are preserved and Git history is extended with a new commit, never rewritten.
