# CORPORATE LADDER — research package v0.1

## Decision

Proceed with **Leverage as a research lead**, not a production-approved competitive ruleset. Its network cuts fit the vision, but the prototype has restrictive connectivity, an anchor-abandonment asymmetry and 13 repetition draws in 48 sampled games. Relay is the fallback for further interactive testing. No candidate has demonstrated enough depth or fairness to be declared definitive. Preserve the ambition while gating the civilization behind core-game validation.

Exact playable rules: [03_FORMAL_RULESETS.md](03_FORMAL_RULESETS.md). Five candidates are independently defined there: Leverage (network collapse), Relay (deployment/jumps/delivery), Commitment (forced anchor response), Allocation (visible tactical energy) and Orbit (shared local rotation). “Original” means proposed here, not proven novel against all prior games.

## Executed evidence

240 deterministic-rule games: 48 per candidate, random/random, greedy/random and shallow-search/greedy; 8 seeds with color-swapped agents. 11 tests passed, including reachable-state invariants, targeted rule fixtures, numerical LMSR samples and transfer conservation. Leverage first/draw/second: 14/13/21, median 27.5 plies; Relay 22/2/24, median 17 plies. These pooled small samples cannot establish optimal seat advantage or depth. Complete distributions, reasons, branching, openings and agent comparisons are in [04](04_SIMULATION_RESULTS.md); raw games and hash manifest in `results/`.

External references are linked with explicit freshness limitations in 01. No live literature search, human playtest, production build, Windows installer, physical-iPhone test or population-scale benchmark was executed. Corporate/economic architecture is a concrete proposal, not implemented functionality. Eleven passing tests do not validate a full economy.

## World and finance proposal

Event-driven deterministic simulation with separate people, positions, titles, grades, organizations and ownership. Roles unlock budgets, rosters, recruitment, restructuring and governance; salary and authority require funded real positions. Start small, grow to 2k/20k only after benchmarks. Visible official matches use real local engine traces; approximate background leagues are disclosed and cannot rewrite committed outcomes.

Double-entry integer ledger, funded payroll/prizes, separate cash/wealth/claims, cash-backed dividends and explicit issuance. Optional binary LMSR markets are third-party only with pre-funded subsidy, conflict exclusion and idempotent settlement; no real-money transactions. The player can progress without betting and recover after job/wealth loss.

## First playable and remaining decisions

First build a disposable interactive board prototype, then a vertical slice containing one local AI match loop, three small companies, a real vacancy, salary/prize consequences and save/reload. Do not build the entire civilization. Resolve connectivity rules, draw behavior, deeper engine strength, novelty, human interest, deterministic market arithmetic and platform packaging before claiming a final design. [16](16_DEVELOPMENT_ROADMAP.md) gives staged gates; [17_CLAUDE_CODE_MASTER_PROMPT.md](17_CLAUDE_CODE_MASTER_PROMPT.md) is the implementation directive and explicitly preserves the unresolved research gate.

## Reproduce

From repository root with Python 3.12 (no third-party dependencies):

```sh
python -m unittest discover -s research/experiments -v
python research/experiments/arena.py --pairs 8
python research/experiments/variants.py
python research/experiments/report.py
```

The simulation overwrites `research/results/games.json`; report regenerates metrics and manifest. Wall time is machine-dependent; compare game payloads excluding `seconds`. This is disposable research code, not production implementation. Source, raw evidence, limitations and next experiments are retained together.

## Executed connectivity follow-up

A separate 96-game experiment tested strict resulting connectivity (48/48 draws) and own-piece cleanup after every action (29/48 draws). Both performed worse on sampled draw frequency and are rejected as default fixes. These variants do not modify or replace v0.1. See 04 and `results/variants.json`. More research remains necessary before a production rules freeze.

## Final R0 supersession note

This document preserves historical evidence and proposals. The current [final R0 report](../docs/LEVERAGE_R0_FINAL_RESEARCH_REPORT.md) records **RESEARCH STOP**, with exact new rules/results in research 20–21. No historical recommendation here authorizes implementation of an unapproved or rejected ruleset. Frozen rule text and old experiment sources/results remain unchanged.
