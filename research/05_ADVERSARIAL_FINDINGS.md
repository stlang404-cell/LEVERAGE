# Adversarial investigation and unresolved defects

## Verified constructive cases

- Leverage rejects equal-power captures (fixture). Its capture cleanup removes disconnected opposing agents while retaining connected ones (fixture). A lone anchor versus lone anchor has no strict-power capture: no forced victory is promised, and a hard draw bounds it.
- Leverage anchor movement can strand its own agents; only empty-cell P movement checks full friendly connectivity. This asymmetry is explicitly specified but likely undesirable. It allows disconnected support islands and can severely restrict ordinary movement. Research v0.2 should compare (a) connectivity required for every move, (b) own disconnected cleanup, (c) no connectivity movement constraint. Do not silently implement any variant as v0.1.
- Orbit clockwise followed by inverse rotation restores the board (fixture); with suitable opponent participation it supports two-turn cycles. Side-to-move repetition catches cycles. Board restoration alone is not a proof of unavoidable draw.
- Relay anchor can jump over a friendly agent onto the enemy row and immediately win (fixture). Players must see delivery threats, not just captures.
- Allocation's intervening occupied cells block long moves (fixture). Armor ≥3 is immune to all legal attacks under the maximum energy 3, while that local configuration survives. Whether a fortress is sustainable against rearrangement is unknown.
- Commitment threat forces anchor movement, but permits a threatened destination. Calling this “check” would misteach the rules.

## Observations

Leverage has 13 repetition draws in 48 sampled games; Orbit 10 repetition and 8 limit draws. See 04 for every candidate's endings. Draw prevention by limit is not a strategic cure. No forced opening win or proof of fairness was discovered; exhaustive opening searches were NOT run. Comeback and dominant-opening rates are unknown.

## Test incident and scope

The first network-cut fixture failed because attack and defense each had one supporting neighbor, making the proposed capture illegal. Adding a second attacker support fixed the test fixture; no rules were relaxed. The corrected 11-test suite passed. Tests include deterministic random walks, not exhaustive state-space validation. Search and transitions share code, so correlated engine bugs remain possible; build an independent reference implementation before official competition.

## Follow-up experiment plan (two variants now executed below)

1. Compare the three Leverage connectivity variants above at equal node budgets with 200 independent paired seeds. Reject variants with >15% nonterminal draws under stronger agents, or with repeatable opening traps that survive defense search. This 15% is a design gate, not a law of good games.
2. Compare capture threshold > versus ≥ with anti-trade constraints only if needed. Equal-power captures could destroy the support-network identity; measure tactical horizon, not just draw reduction.
3. Evaluate Relay delivery-only against dual victory. Collect teach-back errors and opening rush rates.
4. Penalizing repetition in evaluation is allowed as an agent change, but must not conceal a rules-level forced draw. Preserve old baseline agents.
5. Run tactical proof searches and reduced-board tablebases. Known forced sequences currently mean only the local terminal fixtures, never solved opening lines.

## Executed connectivity follow-up

A separate 96-game experiment tested strict resulting connectivity (48/48 draws) and own-piece cleanup after every action (29/48 draws). Both performed worse on sampled draw frequency and are rejected as default fixes. These variants do not modify or replace v0.1. See 04 and `results/variants.json`. More research remains necessary before a production rules freeze.
