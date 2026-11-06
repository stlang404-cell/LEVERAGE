# LEVERAGE documentation hub

One original strategy game inside a living corporate civilization: actual jobs, competitive careers, rivalries, research, ownership and fictional wealth. Simple to operate and difficult to master remains the aim—not a proven capability.

## Final R0 decision: RESEARCH STOP

**No winning ruleset; no production implementation or rules freeze.** Three new candidates completed 672 main games plus 248 diagnostic/control executions. The minimal repair has real mathematical/search improvements but severe canonical repetition; the road redesign mostly draws; the decisive race challenger lacks reliable deeper-search separation. [Read the final report](LEVERAGE_R0_FINAL_RESEARCH_REPORT.md).

**Verified:** 728 prior game records reproduced, independent rule/terminal checks, exact reduced endgames and tests. **Experimentally supported:** new match, compute and synthetic tournament results. **Plausible but unverified:** corporate/finance/UI plans. **Speculative:** fun, exceptional depth, release AI, scale and platform readiness. **Rejected:** advancing a candidate merely to finish research.

## Current design

|Document|Purpose|
|---|---|
|[Final R0 report](LEVERAGE_R0_FINAL_RESEARCH_REPORT.md)|Decision, evidence, limitations and smallest next task|
|[Vision](LEVERAGE_VISION.md)|Preserved corporate fantasy and nonnegotiable contracts|
|[Board research](LEVERAGE_BOARD_GAME_RESEARCH.md)|Exact candidates, diagnostics and traceability|
|[Corporate world](LEVERAGE_CORPORATE_WORLD.md)|Actual positions, applications, tournaments, approvals and recovery|
|[Finance/research](LEVERAGE_FINANCE_AND_RESEARCH.md)|Public-data tools, optional funded markets and accounting|
|[UI/art](LEVERAGE_UI_ART_DIRECTION.md)|Four destinations, executive header and compact pixel-art layouts|
|[Feature audit](LEVERAGE_FEATURE_AUDIT.md)|Keep, simplify, defer and reject decisions|
|[Roadmap](LEVERAGE_IMPLEMENTATION_ROADMAP.md)|Stop gate before a small real career slice|
|[Claude prompt](LEVERAGE_CLAUDE_MASTER_PROMPT.md)|Ready for bounded diagnostic research; not production|
|[Open questions](LEVERAGE_OPEN_QUESTIONS.md)|Experiments that could change the stop decision|
|[Platform research](LEVERAGE_PLATFORM_RESEARCH.md)|Source-backed constraints; device tests still outstanding|

## Evidence and reproducibility

[Historical 00–17 package](../research/00_EXECUTIVE_SUMMARY.md), [v0.1 rules](../research/03_FORMAL_RULESETS.md), [original results](../research/04_SIMULATION_RESULTS.md), [v0.2 rules](../research/18_CONTINUATION_FORMAL_RULES.md) and [v0.2 results](../research/19_CONTINUATION_RESULTS.md) remain preserved. Official product name is LEVERAGE; historical CORPORATE LADDER headings retain archival context.

New: [R0 formal rules](../research/20_R0_FORMAL_CANDIDATES.md), [full measurements/weights](../research/21_R0_RESULTS.md), [summary](../research/results/r0/summary.json), [independent audit](../research/results/r0/audit.json), [tests](../research/results/r0/tests.txt), [hash manifest](../research/results/r0/manifest.json), [harness/commands](../research/experiments/r0/README.md).

```sh
python -m unittest discover -s research/experiments -v
python -m research.experiments.r0.play --candidate A
python -m research.experiments.r0.check
```

The playable CLI is a research tool; no human playtest, premium art, production economy, Windows installer or physical-iPhone validation is claimed. Keep the full product ambition, but do not use corporate complexity to hide an unresolved core game.
