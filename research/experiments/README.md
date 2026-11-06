# Disposable research harness

Python 3.12; standard library only. From repository root:

    python -m unittest discover -s research/experiments -v
    python research/experiments/arena.py --pairs 8
    python research/experiments/report.py
    python research/experiments/variants.py

`arena.py` implements five rulesets and seeded random/greedy/shallow-search agents. `apply` assumes a validated action. `test_lab.py` exercises 11 tests. `report.py` generates the baseline report and manifest. `variants.py` wraps the Leverage generator/transition for separately recorded follow-ups. Never run wrappers concurrently in one Python process: they temporarily replace module functions.

Raw games retain outcome, reason, first four actions, per-turn branching, nodes and seed. Baseline outputs are overwritten on rerun. Variant outputs are separate. Fixed board geometry means editing N alone is not a supported size variant. Commands require no packages, accounts or secrets. See 04 for independence and search-budget limitations.

## LEVERAGE continuation

The frozen sources above remain unchanged. New v0.2 `continuation.py` rules are in research/18, full results in research/19. Run continuation.py, world_bench.py, continuation_report.py, audit_continuation.py and check_docs.py from repository root. The current discovered suite includes the original 11 tests plus 9 continuation tests (20 total). The current design hub is docs/LEVERAGE_README.md.
