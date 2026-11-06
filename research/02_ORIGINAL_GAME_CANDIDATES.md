# Candidate inventory and design-space comparison

Exact playable definitions are in 03. All five were implemented and simulated; none has established originality or human depth. Five systems share geometry to reduce confounds, not because 5×5 is presumed optimal.

|Candidate|Required exploration|Likely patterns|Likely exploit|Learning / engine / readability hypothesis|
|---|---|---|---|---|
|Leverage|Influence networks and structural collapse|Bridge cuts, support triangles, anchor abandonment|Equal-power deadlocks; abandoned agents|Moderate; cheap flood fills; preview removed components|
|Relay|Placement and movement hybrid|Launch pads, delivery races, sacrificial blockers|Early delivery rush; dual-win oversight|Low; larger deployment branching; show landing trails|
|Commitment|Forced positional commitments|Anchor harassment, tempo diversion|Forced-anchor shuttling; first contact wins|Low; simplest engine; mark compulsory anchor|
|Allocation|Tactical resource allocation|Burst/recharge, protected formations|Armor fortresses, one-step recharge too efficient|Moderate; resource state increases transpositions; show cost explicitly|
|Orbit|Mechanism outside original proposal|Shared handles, anchor transport, counter-rotation|Undo loops and accidental opponent delivery|Moderate; reversible search is hard; animate four cells simultaneously|

## Board and army alternatives

|Choice|Tradeoff / next test|
|---|---|
|6×6|36 cells, no single center; try 6 reserves, but opening symmetry and connectivity need new fixtures|
|7×7|49 cells with one center; more maneuver space, longer approach; candidate after v0.1 network fixes|
|8×8|64 cells; readable desktop, dense phone; greater raw space does not prove depth|
|Hex radius 2|19 cells, six neighbors, no square corners; power and bridge distributions change, so retune thresholds|
|Hex radius 3|37 cells; phone cell size versus tactical routes must be playtested|
|Three types|Anchor, agent, specialist; specialist must solve an observed issue, not add jargon|
|Four / five types|More recognition and evaluator burden; reject for first research slice unless ablation shows gain|
|One / two types|This lab uses two. Anchor provides readable stakes; identical agent roles expose geometry clearly|
|Placement-only|Easy legal actions but accumulation can lock board; useful Go/Hex comparison|
|Movement-only|Bounded material and early tactics; Commitment and Allocation controls|
|Hybrid|Reserves provide recovery but create opening branching; Leverage and Relay|
|Symmetric fixed start|Comparable competition and easier paired evaluation; default|
|Asymmetric / drafted start|Adds fairness burden and matchup learning; defer|
|Fixed army / reserve|Fixed army is simpler; reserve creates positional timing. No replenishing reserves in v0.1|

## Victory comparison

Sovereignty/delivery gives a visible objective, but can produce racing rather than engagement (Relay/Orbit). Encirclement makes geometry decisive but needs explicit mobility definitions and can punish beginners invisibly. Collapse makes a small tactical cut dramatic but local power can freeze equal formations. Anchor capture is easiest to read and drives this lab's Leverage. A proposed alternative is two-turn occupation of a central office; it risks arbitrary countdown defense and was not implemented. Multiple victory routes are justified only if players reliably explain threats in teach-back tests; Relay's two routes remain an experiment. No currency, job grade or rating alters board victory.
