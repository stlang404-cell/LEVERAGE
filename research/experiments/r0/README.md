# Final R0 laboratory

Python 3.12, standard library only, run from repository root. **Decision: RESEARCH STOP**, no selected release game. See the [final report](../../../docs/LEVERAGE_R0_FINAL_RESEARCH_REPORT.md), [exact rules](../../20_R0_FORMAL_CANDIDATES.md) and [quantitative appendix](../../21_R0_RESULTS.md). This directory extends the existing research hierarchy; original engines/results remain unchanged.

## Executed experiment commands

```sh
python -m unittest discover -s research/experiments -v
python -m research.experiments.r0.run --candidate A --seeds 32
python -m research.experiments.r0.run --candidate B --seeds 32
python -m research.experiments.r0.run --candidate C --seeds 32
python -m research.experiments.r0.run --sizes --candidate A --seeds 4
python -m research.experiments.r0.run --sizes --candidate B --seeds 4
python -m research.experiments.r0.run --sizes --candidate C --seeds 4
python -m research.experiments.r0.ablations
python -m research.experiments.r0.profiles
python -m research.experiments.r0.size_controls
python -m research.experiments.r0.endgames
python -m research.experiments.r0.tournaments
python -m research.experiments.r0.diagnose
python -m research.experiments.r0.bench
python -m research.experiments.r0.extract_case
python -m research.experiments.r0.report
python -m research.experiments.r0.audit
python -m research.experiments.r0.manifest
python -m research.experiments.r0.check
```

The A canonical control was executed as the following Python API calls, in addition to the commands above; it is required for the ablation/size report:

```python
from pathlib import Path
from research.experiments.r0.rules import A
from research.experiments.r0.run import play, write_result
rows = []
for seed in range(8):
    rows.extend([play(A, 'deep', 'tactical', seed),
                 play(A, 'tactical', 'deep', seed)])
write_result(dict(protocol='canonical-control-for-ablations', games=rows),
             Path('research/results/r0/A_canonical_control.json'))
```

Main run writes only its owned R0 output and removes stale owned parts on repeat; use `--output-dir /tmp/r0-rerun` for an isolated run. Main B is split into three readable JSON files with at most 100 games per part. Diagnostic scripts overwrite their own R0 files; retain delivered copies or use a separate copy of the research directory before rerunning. Do not regenerate historical reports casually. Elapsed times/RSS may differ; compare actions, completed depths, nodes, outcomes and histories.

672 main games plus 248 diagnostic/control executions = 920 records, 904 distinct trial identities. Sixteen canonical controls repeat main conditions; those are not independent extra evidence. Three representative games were also exactly replayed in audit. Synthetic 9,000 tournament selections, tablebase states/proof nodes and CLI actions are NOT counted as board matches. Statistics and limitations are in 21.

## Earlier baseline reproduction

Original `arena.py --pairs 8 --output /tmp/leverage-v01-reproduced.json` reproduced all 240 baseline records. To avoid changing saved evidence, frozen arena.py, variants.py and continuation.py were copied into `/tmp/leverage-r0-baseline/research/experiments/`, with `research/results/` created there. From that temporary root, variants.py and continuation.py were run unchanged; all 96 variant and 392 continuation records matched, excluding elapsed seconds in continuation. [Reproduction record](../../results/r0/baseline_reproduction.json) preserves the exact baseline commit and counts. Old manifests still verify those original sources/results. The temporary directory is not a second project or a Git worktree.

## Code boundaries

- `rules.py`: public legality/transition boundary, fixtures' pure deterministic rules and terminal priorities.
- `oracle.py`: independent coordinate/set implementation of legal effects and terminals, no imports from the reference rules.
- `search.py`: iterative alpha-beta. Cached legality/static evaluation and preferred moves only; no score reuse that ignores repetition history. Per-table entry cap 4,096. A completed root is retained if the next iteration exhausts its budget.
- `run.py`: paired canonical/random-two-ply starts and full traces. Seed 0–31, common 1,200-node ceiling for depths 1/2/4; depth-six diagnostic uses 6,000 nodes, explicitly unequal compute.
- `endgames.py`: exact anchor-only retrograde analysis under fresh history; finite C solver with UNKNOWN on budget exhaustion.
- `tournaments.py`: synthetic logistic-strength model, assumed 25% draws, greedy Swiss and rating fallback; not calibrated to the board or identical to the proposed product scheduler.
- `audit.py`: checks every recorded action and terminal through the independent oracle; replays one canonical deep/tactical game per candidate excluding timing.
- `extract_case.py`: saves the first repeated A canonical position at ply 14, full history and remaining clock; it makes no win/draw proof claim.
- `report.py`, `manifest.py`, `check.py`: measurements, preference sensitivity, hashes and documentation/evidence checks.

Tests include 10,000 sampled reachable states (9,326 unique configuration-positions), 97,623 transition comparisons, independent terminal checks, illegal actions, immediate wins, history preservation, budget bounds, alpha-beta versus exhaustive depth-two minimax and Bellman/rank verification of all 1,200 5×5 anchor-only states. Sampling is not exhaustive full-game validation; rank verification supports finite forced endings, not general opening depth.

## Interactive human research harness

```sh
python -m research.experiments.r0.play --candidate A --ai deep
```

North is the human. `?` lists indexed legal actions, coordinates, power and capture removals; type an action number, `ai` for a laboratory autopilot turn, or `quit`. South uses the specified local agent. This is an unscored research interface: no career, markets, production assets or saving. The retained scripted smoke used `?`, `ai`, `quit`; no human participant has validated fun/readability. Research selectors A/B/C do not authorize rejected product modes.
