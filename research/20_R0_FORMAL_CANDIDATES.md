# Final R0 formal candidates

**Verified in stated scope:** deterministic reference engine, independent coordinate/set transition oracle and targeted terminal tests. No novelty clearance or human enjoyment result is claimed. Frozen v0.1 and v0.2 remain unchanged. These are three separate research games, not simultaneous release modes.

## Version authority and shared conventions

A = **Exposed Anchor, EA-0.3.0**. B = **Bridgework, BW-0.3.0**. C = **Wake Race, WR-0.3.0**. Raw `config.candidate` identifies A/B/C; `config.name` identifies parameter variants. Reference: `experiments/r0/rules.py`; independent oracle: `experiments/r0/oracle.py`. Protocol `r0-1` is an experiment protocol, not a rules version.

Board is n×n, default n=5. Cell (x,y) has index ny+x, 0≤x,y<n. Orthogonal neighbors have Manhattan distance one; no diagonal connection or row wrap. North (+1) begins at top y=0 and moves first; South (−1) begins at bottom y=n−1. One action per turn, no passes. Change turn after all effects. Pieces share public information. No match randomness, clock-pressure victory, hidden state or title-dependent rules.

A full position = board, side to move and both reserve counts. Start history with the initial position counted once. Three occurrences draw. At 120 completed plies draw. Victory conditions below precede these draws; no-legal-action handling follows them. Generated actions assume caller checks terminal status; public `apply` rejects illegal or post-terminal actions. No unlisted action is legal, including overwriting your own piece, using an exhausted reserve, moving outside board or passing. Captured agents never return to reserve. Search tie-breaking randomness is seeded and recorded, not a board rule.

## Candidate A — Exposed Anchor EA-0.3.0

### Initial state and actions

One anchor A per player, at (floor((n−1)/2),0) for North and its 180° rotated cell for South. Empty board elsewhere, five reserve agents P each, on every tested board size. A/P move identically except the anchor's loss ends the game.

Choose one:

1. Place one reserve P in an empty cell orthogonally adjacent to ANY friendly piece.
2. Move any own on-board piece one orthogonal step into an empty cell.
3. Capture an orthogonally adjacent enemy: an enemy anchor can ALWAYS be captured, regardless of support. An enemy agent can be captured only if mover power > target power, measured BEFORE moving. Power(i,owner)=1+number of orthogonally adjacent friendly pieces. A and P each supply one support.

Capture replaces the target with the mover and empties origin. After capture, simultaneously remove every remaining opposing piece outside its anchor's friendly orthogonally connected component. If anchor is missing, its component is empty. No own cleanup, chain recalculation or cleanup after empty moves/placements. Disconnected own agents remain, support adjacent pieces and allow reserve placement. No requirement that moves preserve connectivity. Thus abandonment remains possible; this candidate repairs anchor capture, not every network asymmetry.

### Terminal and endgame

Missing North anchor → South wins; missing South anchor → North wins. Then repetition, 120-ply draw, then no legal action → draw. No safe-anchor/check restriction: moving adjacent to an enemy can lose next turn. Only one anchor can disappear in a legal capture.

Minimal repair is relative to the prior v0.2 **free** scaffold. It does not retroactively amend v0.1. Two anchors can now capture, and exact fresh-history anchor-only tablebases have no drawn positions on tested 5/6/7 sizes. This does not prove full-game decisiveness or immunity to an already accumulated repetition history/nearby move limit.

### Tactical fixture

On 5×5, North anchor 0, North P 11, South anchor 12, South P at 7 and 13, no reserves, North turn. `move 11→12` is legal and wins despite the enemy anchor's greater support. Another fixture: North anchor 0, P at 1/5/6, South P at 7/8, South anchor 24. P6→7 is strict-power capture and removes unsupported P8. Such local combinations are examples, not proof of opening depth.

### Exact exploratory parameter variants

`A5_rooted`: placement neighbor must belong to own anchor component; movement unchanged. `A5_target_only`: disable all component cleanup, remove only captured target. `A5_component_power`: power is size of mover/target's full friendly connected component rather than adjacency; anchor exposure still applies. `A5_formation`: two agents start on cells immediately left/right of North anchor and rotated cells for South, subtracted from reserve, so 3 reserves remain. `A5_reserve3` and `A5_reserve7`: total reserves 3 or 7, otherwise default. All retain EA-0.3.0 explicit parameter tags; none is the default rules recommendation. Larger `A6/A7` retain five reserves to isolate geometry from reserve quantity.

## Candidate B — Bridgework BW-0.3.0

### Initial state and actions

No anchors or piece types. Start one agent per side at the same home-center cells as A, PLUS eight reserve agents each (nine total potential agents). Default 5×5; 6/7 tests retain this quantity.

Choose one: place a reserve agent into any empty OWN home-row cell; move an agent one orthogonal step into an empty cell; or move onto an adjacent enemy if attack > defense. Attack = count of YOUR pieces orthogonally adjacent to the TARGET cell (including the mover). Defense = count of ENEMY pieces orthogonally adjacent to the target, excluding the target itself. Both measured pre-move. A lone attacker therefore captures an unsupported target.

After capture, remove all remaining opposing components that do not touch the opponent's own home row. Friendly cleanup never occurs. Empty moves do not cause cleanup. This allows deliberate bridge cutting and strategic abandonment without a king-like piece.

### Terminal and endgame

A player wins by forming an orthogonal friendly path from any own home-row cell to the opposing home row. Test North road then South road (simultaneous newly created roads are unreachable under legal play). If neither road exists and BOTH players' on-board pieces plus reserves are fewer than n, declare a material draw: neither can ever build a road. This is an explicit early-adjudication choice; it also stops any later immobilization contest and is not a theorem that every other possible win condition is impossible. Then repetition, 120-ply draw, then no legal action → the side unable to act loses.

### Tactical fixture

North agents 2/7/12/16/22, South 24, no reserves, North turn: 16→17 closes the vertical road and wins. Capture fixture: North 7/10/11, South 12/13/23, North turn; 11→12 has two attackers versus one defender; capture removes South 13 while South 23 remains rooted on its home row. Exact helpers and fixtures are in the tests. The resemblance to connection games is acknowledged; this is a proposed hybrid, not established novelty.

## Candidate C — Wake Race WR-0.3.0

### Initial state and actions

Three identical runners each, at North home x=0, floor(n/2), n−1 and their 180° rotations for South. No reserves, anchors, captures, influence or cleanup.

Move one OWN runner one orthogonal step into an empty cell. The vacated cell becomes a permanent neutral blocked wake. Wakes block everyone; no jumping/removal. A runner reaching the opposing home row parks permanently and cannot move, including sideways. One cannot move a parked runner, through a wake, onto an occupied cell or off-board.

### Terminal and endgame

Deliver two of your three runners to the opposite home row to win. Then shared repetition/120-ply checks; if the next player has no legal move, that player loses. With reachable states, every move reduces empty cells by exactly one; from the normal start there are n²−6 empty cells, hence the game MUST terminate in at most n²−6 plies and cannot repeat or reach 120 on tested sizes. On 5×5 this bound is 19, on 6×6 30, on 7×7 43. Zero draws are structural, not evidence of depth or fairness.

### Structural entry limit

Every initially occupied enemy home-row cell remains occupied or becomes a wake, so it can NEVER become an empty landing. At most n−3 home-row gaps can receive arrivals. Thus the two-delivery condition is unreachable on the reduced 3×3/4×4 starting boards; their exact solutions concern immobilization. On 5×5 there are exactly two such gaps. This explains a structural obstacle to the advertised race without proving the full-size root solved.

### Tactical fixture

North runners at 20 and 16, South at 0/4, no wakes, North turn: 16→21 delivers the second runner and wins. North 20 is already parked and cannot move. Fewer than six total pieces in this fixture is permitted for local testing; normal games never remove runners. Blocking routes by leaving wake cells is the independent tactical mechanism. This resembles the broader blocking/racing family; novelty remains unverified and it is not chess with renamed pieces.

## Repetition, examples and human boundary

The precise public actions, terminal priorities and parameter tags above are implementable without guessing. Tests include illegal actions, endgame fixtures, symmetry, monotone wakes, an independent oracle and alpha-beta/exhaustive-depth comparisons. The CLI prints board coordinates, legal actions, support and capture consequences; it is a research interface, not evidence that pixel-art or human comprehension has passed. No human participant tested these rules in this task.
