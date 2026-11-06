# Implementation roadmap and gates

**Plausible but unverified:** proposed gates, not completed product tests. **Rejected:** full civilization production now. A constrained research/playability prototype may proceed.

## R0 — earn a board game

Preserve v0.1 and v0.2 laboratory identities. Build independent rules oracle; compare anchor-vulnerability/endgame fixes to network identity and readable teaching. Run at least 200 independent paired seeds with tuned and held-out evaluators, completed-depth/node accounting, tactical regression corpus and reduced-state exploit search. Invite 12 human testers for repeated sessions and teach-back. Target <15% nonterminal draws under multiple competent agents is a provisional design gate, not a theorem or substitute for interesting play. Stop if no candidate merits repeated play; do not fill the corporation with a weak game.

## P1 — genuine playable board plus small career

One board rules selector frozen for this slice, local worker AI, legal and collapse previews, complete replay/practice review. Three corporations, each one real six-person team; player starts in a funded intern seat. One real lead vacancy supports apply → paired contest → published automatic approval → appointment. Salary, funded prize, authority count and office/header change persist. Include failed application, lost contest and a recovery opportunity. Existing staff/positions do not magically multiply when player wins. No Exchange trading yet; hide disabled product panels rather than imply they work.

Acceptance: independent oracle agrees over ≥10,000 reachable states; targeted terminal/repetition/collapse tests; one fully played match and appointment; no title advantage; AI budget/cancel metrics; ledger conservation and unique incumbency; export/import; crash during save recovers previous complete generation. One no-betting loss-to-recovery session. Report commands and artifacts. UI four destinations only as they become meaningful, not four empty shells. This is an achievable prototype goal, not production release authorization.

## P2 — 120-person living competitive world

Real reporting/authority DAG, vacancy contracts, Swiss/round-robin/knockout scheduler, warnings/demotion, transfers, CEO process, persistent rival/history indices. Cases: guaranteed winner appointed, nominee vote fails for published reason, withdrawal/bye/appeal, vacancy bankrupt, AI-only succession while player uninvolved. Deterministic event ordering and replay equivalent through saves. Do not use the old review-weight formula to override a guaranteed competition. Recruitment remains cheap for routine jobs.

## P3 — research and financial laboratory

Public-data forecast datasets and rolling calibration; assistants and scenario tooling, measured marginal benefit/cost. Binary funded LMSR, integer cash ledger, deterministic cost function, fees/collateral/conflicts. Gate before enabling trade: buy/sell bounds, negative holding rejection, maker worst-case solvency, aggregate liability, duplicate settle, void/refund including fees, save/replay midtrade, authority-change conflicts, no personal/sandbox crossover. No lifecycle readiness is established by the historical two numerical tests.

## P4 — ownership and corporate finance

Equity issuance/dilution, funded dividends, valuation sensitivity, boards, founding and bankruptcy. Control changes ownership votes, never personal access to corporate cash. Test dividend cutoff/price adjustment, self-dealing, consolidated holdings, acquisition asset conservation and recovery without bets. Expand market categories only after causal influence rules and resolution predicates are testable.

## P5 — device, scale and art release gates

Measured fixtures at 120/2k/20k with realistic histories and full selected workloads, tracing and nontracing runs. Current Python population microbenchmark is not this gate; 20k p95 ~1s under tracing/concurrent load exceeds old 500 ms aspiration. Target ordinary foreground UI tasks <50 ms; world/engine off main thread, cancellation acknowledgement <100 ms. Record CPU/browser/device, p50/p95, heap/save growth, trace overhead and battery/foreground behavior. Raise targets only through an explicit product decision, not by relabeling results.

Windows: actual Windows CI build, clean VM installer without Node/Rust on player machine, offline launch with local WebView runtime path tested. Select Tauri/Electron after measured spike. iPhone: first HTTPS install, service-worker asset cache, airplane-mode launch/play/save/reload, force-close, export/import and quota failure handling on physical supported devices. Never equate desktop localhost with iPhone support. Art/accessibility/readability tests and long-campaign migration/crash soak are release gates. [Platform research](LEVERAGE_PLATFORM_RESEARCH.md) records freshly retrieved documentation and remaining tests.

Dependencies: rules before rating/forecast calibration; committed events before history/settlement; ledger before markets/equity; ownership before conflict closure; save schemas before large campaigns. Deliver build/rule/schema versions, actual checks, known defects and playable evidence at every gate. No dates promised without a staffed project plan.
