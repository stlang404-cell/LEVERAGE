# Existing games: source map and design arguments

Evidence labels: **D** = documented in named rules/reference; **T** = reasoning from those rules; **H** = untested transfer hypothesis. Links below are reference destinations, not claims of live retrieval. No browsing/search connector was available; these sources were not freshly fetched or exhaustively reviewed in this task. Publication dates and quotations are deliberately omitted where not checked. Before public release verify every rules comparison against the linked primary source, and perform a broader novelty search.

|Game / reference|Documented rule or structure (D)|Design argument (T) and project hypothesis (H)|
|---|---|---|
|[Chess, FIDE Laws](https://handbook.fide.com/chapter/E012023)|Different movement roles, king safety, repetition/draw rules|T: forcing threats constrain branching. H: a single anchor can explain stakes without six types|
|[Go, AGA rules](https://www.usgo.org/content.aspx?page_id=22&club_id=454497&module_id=524979)|Connected groups, liberties and ko|T: local capture can affect distant groups. H: explicit bridge-cut previews can make network tactics readable|
|[Shogi, Japan Shogi Association](https://www.shogi.or.jp/)|Captured pieces can reenter through drops|T: material need not only decrease. H: fixed reserves offer deployment timing with less recycling complexity|
|[Hive, publisher](https://www.gen42.com/games/hive)|Hex connectivity, surrounding a queen, no fixed board|T: movement legality can carry positional tension. H: all-friendly-connected constraints may be too restrictive|
|[Tak, rules](https://ustak.org/play-beautiful-game-tak/)|Placement, stacks and road victory|T: layered tactical and spatial goals need few roles. H: delivery plus capture may be less coherent than one spatial goal|
|[Hex, mathematical overview](https://www.maths.ed.ac.uk/~csangwin/hex/)|Connection on a rhombus of hexagons; standard Hex has no draws|T: topology shapes objectives. Strategy stealing establishes existence for a first-player win under standard assumptions, not a constructive solution. H: swap openings deserve testing|
|[Onitama, publisher](https://www.arcanewonders.com/product/onitama/)|Public movement cards circulate; capture master or reach temple|T: public changing constraints create timing. H: distinct public resource cycles can replace chance|
|[Santorini, publisher](https://roxley.com/products/santorini)|Move and build; height matters; optional powers change play|T: actions alter future action space. H: fixed symmetric rules simplify engine and tournament trust|
|[Arimaa, official](https://arimaa.com/arimaa/)|Multiple steps per turn, freezing, trap squares, goal|T: simple local primitives can make move combinations costly to search. H: avoid multi-step turns until affordable search is demonstrated|

These references motivate mechanics; they do not establish that Leverage is original, balanced or commercially viable. Originality here means independently proposed combinations. A patent/legal clearance or exhaustive ludographic survey was not performed.

## What creates depth, and what does not

T: Tactical forcing sequences reward calculation; positional tradeoffs reward plans whose benefits persist beyond a shallow horizon. Sacrifices matter when material and initiative are not equivalent. Reversibility creates maneuver but can also create perpetual defense. More cells, legal actions or game states alone prove none of these qualities. Finite deterministic games can have theoretical solutions too expensive to compute; lack of a known solution is not evidence of depth.

T: Square orthogonal geometry emphasizes bottlenecks and corners; hex geometry raises local degree. First-move initiative can survive perfectly symmetric starting material. Color-swapped agents help separate agent strength from seat advantage, but low-skill agents do not estimate optimal play.

H: Style should emerge from choices between reserve tempo, compact support and risky bridges. A style slider must not invent rules or secretly improve information. Spectators need visible imminent threats, move explanation and replay controls; a score bar alone cannot explain a collapse.

## Engine and economy references

[Knuth and Moore, An Analysis of Alpha-Beta Pruning, Artificial Intelligence 6 (1975), DOI 10.1016/0004-3702(75)90019-3](https://doi.org/10.1016/0004-3702(75)90019-3) supports alpha-beta as a standard search technique, not this evaluator's strength. [Browne et al., A Survey of Monte Carlo Tree Search Methods, IEEE TCIAIG (2012), DOI 10.1109/TCIAIG.2012.2186810](https://doi.org/10.1109/TCIAIG.2012.2186810) is a research follow-up for high branching. [Hanson, Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation, Journal of Prediction Markets (2007)](https://mason.gmu.edu/~rhanson/mktscore.pdf) motivates LMSR. [Glickman's rating research](https://www.glicko.net/research.html) motivates explicit uncertainty. These methods require project-specific calibration; no external benchmark is attributed to this project.
