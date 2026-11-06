# Highest-impact open questions

**Current decision: RESEARCH STOP.** These questions are ordered by development risk. The smallest next task is one full-history A5 repetition diagnosis, not another broad production pass. See [final report](LEVERAGE_R0_FINAL_RESEARCH_REPORT.md).

|Question / finding|Next experiment and decision rule|
|---|---|
|Can the network game sustain repeated play?|Independent reference/oracle now exists; 672 main new games still fail key gates. Diagnose first repetition, then real human sessions only if justified|
|Can anchor-only/endgame deadlocks be fixed elegantly?|EA-0.3.0 repairs fresh anchor-only endgames exactly, but default canonical strong play still draws 14/16. Explain material-rich repetition without conflating it with that solved subcase|
|Does preserving connectivity help?|Old strict/cleanup variants drew 48/48 and 29/48; do not reintroduce them without a distinct hypothesis|
|Do v0.2 mechanics help?|Old counts reproduced. Bare anchors account for only 10/225 draws; contact, evaluator and horizon effects remain distinct|
|Does larger board help?|Fixed-reserve 5/6/7 sweep now exists, four paired seeds/size; too small for a general geometry verdict|
|Is any opening forced?|A anchor-only 5/6/7 solved under fresh history; C 3/4 openings solved but 5 remains UNKNOWN at 250k proof nodes. No full-size opening dominance claim|
|Are styles/deeper plans real?|Held-out evaluators, principal-variation review, feature ablations and human plan descriptions; branching is not the metric|
|What selection formats feel fair and short?|9,000 synthetic trials expose game-load costs; real LEVERAGE calibration and human scheduling remain unverified|
|Do promotions change useful agency?|Observe P1 lead appointment and delegated roster choice, then loss/recovery; cut chores if administration dominates|
|Can research aid judgments without guaranteed returns?|Out-of-time engine datasets, calibrate/shrink public-data forecasts, costs and after-fee net returns; synthetic averaging is not validation|
|Can all money/claims reconcile?|P3 lifecycle adversarial test suite and long-run ledger/cap-table property tests before enabling markets|
|How much population is useful?|Measure event relevance to player before expanding from 120 to 2k/20k; benchmark actual world, not sparse payroll alone|
|Will permanent history bloat saves?|10/50 simulated-year histories, compact summaries with retained provenance/export; measure write latency and recovery|
|Can iPhone saves survive practical usage?|Physical-device installed PWA tests for suspension, quota exhaustion, export/import, offline first update and recovery|
|Which Windows shell?|Tauri versus Electron real clean-machine build/install/offline/memory comparison; document WebView provisioning|
|Is originality defensible?|Fresh broader abstract-game/prior-art review; existing sources are not exhaustive novelty clearance|

**Rejected:** turning unknowns into product claims to unblock production. **Plausible but unverified:** a small research slice is useful now; full production remains gated.
