# Formal rulesets, laboratory version 0.1

These rules govern the recorded experiments. These are research candidates, not established competitive games. `experiments/arena.py` is an executable cross-check. A production engine must reject illegal actions at its public boundary; the research `apply` function assumes membership in `moves`.

## Shared definitions

All five candidates use a 5×5 square board. Coordinates (x,y) range 0–4. Cell index is 5y+x. North (+) begins at y=0; South (−) at y=4; North moves first. Orthogonal adjacency means Manhattan distance exactly one. Diagonals do not connect. Occupied cells hold one piece. Each player owns exactly one anchor (A) and regular agents (P). A and P differ only where explicitly stated. No hidden information or random match rule exists.

Initial anchors: North (2,0), South (2,4). Leverage and Relay start with no on-board agents and five agents in reserve per side. Commitment, Allocation and Orbit start with four agents on each player's home row at x=0,1,3,4, and no reserves. Captured pieces leave the game permanently. Each turn is exactly one legal action; there is no pass. Newly placed pieces act only on a later turn. All effects finish before changing the player to move.

Terminal precedence after each turn: missing North anchor → South win; missing South anchor → North win; delivery victory where specified; third occurrence of the full position → draw; 100 completed plies → draw; no legal action for the next player → draw except Commitment, where that player loses. A full position consists of every cell, side to move, remaining reserves and energy. Position history starts with the initial position counted once. Ply count is excluded from repetition. No simultaneous anchor removal is reachable under legal rules. At delivery, test only the player who just moved: delivery of the opponent by a rotation is not the mover's win. No other scoring or tie-break exists.

Out-of-board actions, acting with the opponent's pieces, placing without reserve, overwriting friendly pieces, actions not described below, and actions after termination are illegal. There is no chess check, mandatory safe anchor rule, promotion, castling or implicit action. Anchors can move into danger and be captured. Official play uses no pie rule in v0.1; a swap opening is a proposed experiment, not part of this version.

## L — Leverage: network collapse

Action: either place one reserve P on an empty cell orthogonally adjacent to any friendly on-board piece, or move one friendly piece one orthogonal step.

A move to an empty cell by P is legal only if, after the move, **every** friendly on-board piece belongs to the friendly anchor's connected component. A move to an empty cell by A has no connectivity restriction. This deliberately allows an anchor to abandon agents; abandoned agents stay on board, still support adjacency, and remain legal placement neighbors. They do not automatically disappear. Whether this exception is desirable remains an open question.

For a capture, the destination must contain an enemy. In the position BEFORE the move define power(i,owner) = 1 + number of orthogonally adjacent pieces of owner to cell i. A and P count equally. Capture is legal iff the moving piece's power is strictly greater than the target's power. Replace target with mover; vacate origin. Then simultaneously remove every remaining opposing piece outside the opposing anchor's orthogonally connected friendly component. If its anchor was captured, that component is empty. No further cascade, friendly cleanup or recalculation of capture legality occurs. Capture moves by P are exempt from the empty-cell connectivity rule. Thus isolated attacking pieces can survive; this is exact v0.1 behavior, not a hidden rule.

Victory: capture the opposing anchor, possibly through structural collapse that ultimately opens an attack. Isolation of non-anchor agents alone does not win. Draw rules are shared. Endgame: lone equal-power anchors cannot capture each other; repetition or 100 plies bounds play. This is a known weakness. Signature: concentrated support wins local fights, but bridges expose whole branches.

## R — Relay: deployment and delivery

Action: place reserve P in an empty cell of your home row, or move any friendly piece one orthogonal step onto an empty or enemy cell, or jump over exactly one orthogonally adjacent friendly piece to the cell immediately beyond it in that same direction. Landing may be empty or enemy; intervening friendly piece stays. No chain jumps. Enemy landings capture regardless of piece type. No other capture occurs. A jump cannot wrap across rows or columns.

Victory: capture the enemy anchor OR end your own turn with your anchor on the enemy home row. A delivery ends the game before the opponent can capture it. Endgame: anchors retain delivery potential without other pieces. Two victory routes may obscure defense; test separately against delivery-only. Signature: deploy launch pads, sacrifice them, or chase the runner.

## C — Commitment: forced defense

Action: move any piece one orthogonal step to an empty or enemy cell, capturing on an enemy landing. If at turn start your anchor has at least one orthogonally adjacent enemy, you MUST move your anchor; no other piece may move. Capturing the threatening enemy with the anchor is allowed. The destination need not be safe. No placement, jump or cleanup.

Victory: capture the opposing anchor or leave the opponent with no legal action. Otherwise shared draw rules. Endgame: adjacent anchors create immediate capture threats, with tempo determining the result. This is intentionally harsh commitment rather than chess check. Signature: force an anchor response to win time elsewhere. Originality is weak; retain as a control candidate rather than claim invention of forced-response games.

## A — Allocation: deterministic action budget

Each side has energy 3 initially, visible to both. Action: select a friendly piece and integer cost k in [1, own energy]; move exactly k cells orthogonally in one direction. All intervening cells must be empty. Friendly landing forbidden. Empty landing always allowed. For an enemy landing let armor = number of enemy-owned pieces orthogonally adjacent to the target in the pre-move position. Capture is permitted iff k > armor. The target itself is not armor. After the move, own energy becomes min(3, energy − k + 2); opposing energy is unchanged. There is no bank, pass or separate recharge. A one-step attack captures an unprotected anchor.

Victory: enemy anchor capture. Shared draws and immobility. Endgame: energy creates alternating bursts and recovery moves; no economic currency affects it. Signature: force the opponent to spend reach before attacking protected formations. Cost 3 versus armor 3 or 4 cannot capture, potentially creating fortresses.

## O — Orbit: shared spatial transformation

Action: choose any axis-aligned 2×2 square containing at least one of your pieces; rotate all four cells, including empty cells and enemy pieces, exactly 90° clockwise or counterclockwise. No direct piece movement, placement, capture or collapse exists. A piece at top-left rotates to top-right clockwise. You may select a square containing only the opponent's anchor plus one of your agents; ownership gives permission, not immunity to displacement.

Victory: end your turn with your own anchor on the opposing home row. Shared draws and immobility. Endgame: anchors cannot be removed. Local inverse rotations make stalling plausible; repetition prevents infinite play but does not guarantee satisfying play. Signature: use enemy pieces as shared handles to transport your anchor. This is novel relative to the supplied concepts, not a verified novelty claim against all published games.

## Scope and rule-change log

Board size fixed at 5×5 for inexpensive rejection tests; requested 6/7/8 and hex variants are compared conceptually in 02, not measured. The v0.1 baseline was not tuned after seeing outcomes. Two separately recorded follow-ups are defined in 04 and variants.py; neither replaces these rules. One capture test fixture originally had equal attacker/defender power; an additional friendly support corrected the fixture. Rules were unchanged; initial failed test is described in 05. No other variant is mixed into results.
