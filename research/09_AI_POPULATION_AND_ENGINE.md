# Local AI population and engine

## Persistent agents

Store stable employee IDs, procedural portrait seed, age, ambitions, loyalty, risk preference, job-location preference, liquidity preference, career history, rival links, training exposure and rating mean/uncertainty. Personality is a preference vector, not scripted certainty. Rating is measured performance, latent skill is a simulation parameter, and neither is job title. Learning follows bounded diminishing returns, aging and practice; publish career changes as events. Replacement cohorts enter through recruitment and retirements, not by silently rerolling rivals.

## Match engine

Pure deterministic rules module → legal action list → transition → result/repetition. Search runs in a worker and returns action, principal variation, depth, nodes and rule-version hash. Difficulty uses node budget and fallible evaluation, never illegal actions or hidden future knowledge. Seeded tie choices are recorded for replay. Begin with iterative deepening alpha-beta, move ordering and transposition entries that include repetition context or avoid unsound repetition reuse. Compare MCTS only if branch/search measurements justify it. The disposable Python depth-two engine is not a release engine.

Evaluation features: anchor danger, legal mobility, connected reserve deployment, bridge vulnerability, support and material. Use ablation against a fixed baseline. A suggested move explanation must cite verifiable local facts (“this capture disconnects 3 agents”), not claim a forced win without completed proof search. Mistake labels require a stable deeper reference, confidence threshold and displayed horizon. No grandmaster or superhuman promise.

## Simulation levels and consistency

Active player-visible and official wagerable matches use full engine traces at fixed node budgets. Background unwatched leagues may use a calibrated probabilistic outcome model P(A wins)=1/(1+10^((rB−rA)/400)), plus separately calibrated draw probability; that formula alone is not calibrated for this game. These are explicitly “simulated league results,” not invented move replays. Use keyed PRNG streams by event/entity ID so viewport changes never change outcomes. A match becomes detail-locked before opening a market; it cannot switch result generators because the player watches it. Private analysis never feeds public odds.

Store events and snapshots, aggregate inactive departments weekly, detail-update people on scheduled events. Level changes cannot overwrite committed results, financial settlement or career history. Players can inspect how a result was generated. Consistency of visible outcome commitments is required; exact equivalence of all detail levels is not claimed.

## Budgets to measure, not achieved claims

Desktop worker target ≤100 ms p95 ordinary simulation tick at 2,000 staff; 20,000 staff target ≤500 ms p95 batched daily tick; phone main-thread interactions target ≤50 ms. Engine worker cancellable within 100 ms after an interaction, hard deadline with last completed iteration. Record device, CPU, browser, seed, heap, GC and save sizes. A packed 256-byte employee row would consume ~5.1 MB at 20,000 before histories/indexes/JS overhead; it is arithmetic, not measured memory. History growth needs annual compaction and exportable full audit archives. Population scale remains unverified.
