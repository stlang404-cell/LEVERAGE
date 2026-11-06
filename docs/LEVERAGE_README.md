# LEVERAGE documentation hub

One deep board game within a persistent corporate civilization: compete for actual positions, develop rivals, lead organizations and build fictional wealth. Simple to operate; difficult to master is the goal, not a demonstrated result.

## Current decision

**Continue board-game research; do not begin full production.** The 392-game continuation tested three new mechanics plus board/formation variants. None earned advancement. All current anchor-only endgames draw, and stronger agents often repeated rather than revealing rich play. A small interactive research prototype and career slice are reasonable next steps; a premium production commitment is not.

**Verified:** 20 tests pass in the current suite; frozen v0.1 files/results retained. **Experimentally supported:** 392 new games, paired seed-cluster intervals, recorded actual depths, Python population fixtures and synthetic forecast comparisons. **Plausible but unverified:** career/tournament/finance/UI architecture. **Speculative:** exceptional strategic depth, strong release AI, player retention and full platform/scale readiness. **Rejected:** new default connectivity fixes, multiple disconnected release games, compulsory betting and full-civilization implementation now.

Official product title is LEVERAGE. Old CORPORATE LADDER headings and previous directives survive as historical research. New work follows this hub and its master prompt, not conflicting historical UX/product-name guidance.

## Read the current design

|Document|Purpose|
|---|---|
|[Vision](LEVERAGE_VISION.md)|Player fantasy, pillars and nonnegotiable requirements|
|[Board research](LEVERAGE_BOARD_GAME_RESEARCH.md)|Formal variants, measured comparisons and stop/go decision|
|[Corporate world](LEVERAGE_CORPORATE_WORLD.md)|Actual seats, apply/compete/approval/promote, authority and history|
|[Finance and research](LEVERAGE_FINANCE_AND_RESEARCH.md)|Rank/tool progression, public-data fairness, optional funded markets|
|[UI and art](LEVERAGE_UI_ART_DIRECTION.md)|Four destinations, executive header, concrete desktop/phone layouts|
|[Feature audit](LEVERAGE_FEATURE_AUDIT.md)|Keep/improve/simplify/defer/reject decisions|
|[Roadmap](LEVERAGE_IMPLEMENTATION_ROADMAP.md)|Playable stages, dependencies and measurable gates|
|[Claude master prompt](LEVERAGE_CLAUDE_MASTER_PROMPT.md)|Current implementation directive with unresolved-rule guardrails|
|[Open questions](LEVERAGE_OPEN_QUESTIONS.md)|Highest-risk uncertainties and next experiments|
|[Platform research](LEVERAGE_PLATFORM_RESEARCH.md)|Fresh Tauri/MDN source checks; actual device tests outstanding|

## Evidence and traceability

- [Historical executive summary](../research/00_EXECUTIVE_SUMMARY.md), numbered 00–17 documents and original five-game experiments are preserved.
- [Frozen v0.1 rules](../research/03_FORMAL_RULESETS.md), [original results](../research/04_SIMULATION_RESULTS.md) and [original manifest](../research/results/manifest.json).
- [New laboratory v0.2 rules](../research/18_CONTINUATION_FORMAL_RULES.md), [continuation results](../research/19_CONTINUATION_RESULTS.md), [raw games](../research/results/continuation.json), [new manifest](../research/results/continuation_manifest.json), [tests](../research/results/continuation_tests.txt), [trace audit](../research/results/continuation_audit.json), [population/forecast data](../research/results/world_bench.json).

## Recommended first playable

One real local board match, readable network previews, replay and reliable saving, plus three small six-person company teams, a funded intern seat and a real lead vacancy. Apply in one action; compete under identical rules; a posted guaranteed selection appoints its qualified winner. Loss leaves training, public play and another vacancy. Title, reporting scope, salary, research tools and office insignia change; board power does not. Betting waits for lifecycle tests.

Corporate cash, personal cash, ownership and marked wealth remain distinct; researched forecasts use public histories and uncertainty, never hidden future outcomes. Permanent history comes from committed events. Twenty thousand full employees, market solvency lifecycle, human readability, Windows installer and physical iPhone offline tests are still gates, not delivered product capabilities.

## Run the research

Python 3.12, standard library only; from repository root:

```sh
python -m unittest discover -s research/experiments -v
python research/experiments/continuation.py
python research/experiments/world_bench.py
python research/experiments/continuation_report.py
python research/experiments/audit_continuation.py
python research/experiments/check_docs.py
```

Simulation commands overwrite their own new result files; timing varies. Original v0.1 reproduction instructions remain in its summary. No production implementation, remote inference, account or runtime network service has been added.
