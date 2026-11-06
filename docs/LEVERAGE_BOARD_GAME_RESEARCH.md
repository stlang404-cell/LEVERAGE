# Board-game research and decision

## Reconciliation

**Verified:** original [00–16 research](../research/00_EXECUTIVE_SUMMARY.md), [17 directive](../research/17_CLAUDE_CODE_MASTER_PROMPT.md), v0.1 rules/source and raw evidence were reviewed and preserved. They are historical, not current product-title guidance. Prior evidence: 240 baseline games over five candidates and 96 connectivity follow-ups; 11 original tests. The strict-connectivity and own-cleanup fixes drew 48/48 and 29/48 respectively and were rejected as defaults. Prior pooled Wilson intervals were descriptive, not valid certification of fairness; duplicate random/random swaps were acknowledged. New protocol avoids those duplicated equal-agent games and uses paired seed clusters.

**Plausible but unverified:** network sacrifice can express LEVERAGE's strategic identity. **Speculative:** exceptional depth/originality, balance and player appeal. A release board game has not been selected. The design criteria remain simplicity, position/tactics, fairness, local-engine feasibility and readable stakes; the [historical weighted comparison](../research/06_FINAL_BOARD_GAME_RECOMMENDATION.md) is not a measured ranking.

## Frozen definitions and new hypotheses

Historical v0.1 exact rules are in [03](../research/03_FORMAL_RULESETS.md); unchanged `arena.py` and original result hashes preserve traceability. New [laboratory v0.2 rules](../research/18_CONTINUATION_FORMAL_RULES.md) and `continuation.py` deliberately isolate a free-movement scaffold. It removes the asymmetric connectivity restriction but leaves anchor abandonment possible; do not claim it solves that issue.

Three mechanically different refinements relative to free movement:

- **Breach:** equal-power agents can mutually sacrifice to cut a defended network; anchors excluded.
- **Pressure:** equal-power pieces can push an enemy, including its anchor, into an empty cell, then enemy network cleanup.
- **Relay:** jump a friendly piece to an empty cell, adding mobility without another capture or victory rule.

These are original proposals here, not cleared novelty claims. Controls: 5×5 free movement; pressure with 6×6/6 reserves, 7×7/7 reserves and a 5×5 predeployed formation. Changing size plus reserves is a bundled comparison. No extra piece types. All use anchor removal, threefold, no-pass and 120-ply limit, unlike v0.1's 100. Other victory systems are next experiments, not mixed into these results.

## New measured results

**Experimentally supported:** 392 additional games: 56 per configuration, eight seeds, random/greedy/tactical/deep agents, swapped sides for unequal agents. Hard 800-node per-turn cap, greedy depth 1, tactical 2, deep maximum 4 with fully completed iterative-deepening roots only. See [full results, bootstrap uncertainty, branching, openings and actual depths](../research/19_CONTINUATION_RESULTS.md) and [raw games](../research/results/continuation.json).

|Configuration|First / draw / second|Deep vs tactical W/D/L|Interpretation under these agents|
|---|---|---|---|
|free5|12 / 25 / 19|3 / 13 / 0|Some strength separation, many draws|
|breach5|12 / 24 / 20|4 / 11 / 1|No compelling draw cure|
|pressure5|12 / 27 / 17|1 / 15 / 0|Pressure animation potential does not imply game quality|
|relay5|11 / 29 / 16|0 / 16 / 0|Mobility alone failed to separate these agents|
|pressure6|10 / 38 / 8|0 / 16 / 0|Larger bundle worsened draws|
|pressure7|6 / 43 / 7|0 / 16 / 0|Longer play and many hard limits|
|pressure5 formation|7 / 39 / 10|0 / 16 / 0|Starting with supports did not rescue play|

Small-cluster intervals are exploratory; resampling all wins/all draws yields degenerate intervals and does NOT imply zero true uncertainty. The same evaluator across agents may produce repeated plans. Completed depth varies: relay5 deep agent reached depth 2 or 3 only; free5 reached depth 4 on 60 moves, not every move. No claim of grandmaster strength, solved fairness or qualitative strategic discovery follows. Opening counts measure action-sequence diversity only.

**Verified by rule argument:** two anchors with no agents/reserves cannot capture under any of these new rules. Equal power prevents capture, breach excludes anchors, relay has no jumper, pushes never eject. All such bounded endgames draw. Connectivity abandonment remains common in recorded states. This is a structural weakness worth addressing before broader world implementation. No forced opening win, unavoidable draw from the start or dominant opening has been proved. Test fixtures demonstrate local forced outcomes, not solved openings.

## Research decision

**Continue research.** Reject advancing any current v0.2 variant as the release game. Do not rationalize high draws as sophistication. Retain the network idea for one further focused round and old Relay as an alternative control; neither is production-approved. Next formally compare anchor vulnerability/positional siege and delivery-only victory with independent rules, held-out evaluation and human repeated sessions. Avoid adding multiple special actions merely to mask a weak endgame. Consider rejecting network capture if it cannot produce readable sustained choices.

## Population, forecast and performance evidence

**Experimentally supported, narrow scope:** [world fixture](../research/results/world_bench.json), Python 3.12/Linux, 30 ticks each at 120/2k/20k employees; stable reporting tree, salary transfers, 13 initial history records, sparse payroll. It scans all people each tick; it is a baseline, not an optimized event scheduler. Under allocation tracing and concurrent game workload, 20k fixture p95 tick ~1.01 s, peak traced allocation ~47.9 MB including JSON serialization, JSON ~7.36 MB. The 2k p95 was ~110 ms. Traced Python costs are not JS heap/RSS or a full game benchmark. Full matching, governance, migration and 50-year histories excluded. Do not claim old 500 ms target passed.

Synthetic forecasts: 5,000 generated outcomes, Brier score decreases from 0.2351 at one noisy public observation to 0.1696 at 32; improvement from 16 to 32 is only ~0.0030. Junior estimate is closer to latent probability than 32-observation estimate in 11.34% of cases. This supports the toy averaging hypothesis only; it does not demonstrate calibrated game forecasting or trading profit. See [finance research](LEVERAGE_FINANCE_AND_RESEARCH.md).

## Reproduce and audit

```sh
python -m unittest discover -s research/experiments -v
python research/experiments/continuation.py
python research/experiments/world_bench.py
python research/experiments/continuation_report.py
python research/experiments/audit_continuation.py
```

Baseline reproduction remains separately documented; do not overwrite historical evidence casually. New manifests hash new sources/results. Trace audit rechecks every action/terminal and exactly replays one deep-agent game per configuration excluding timings; it shares the rules code and is not the missing independent oracle. Human teaching, novelty review, real phone/Windows behavior, full market lifecycle and 20k full-world scaling remain unresolved.
