# LEVERAGE continuation rules — laboratory v0.2

**Verified:** these exact definitions are implemented by `experiments/continuation.py`; fixtures and sampled legal walks exercise them. Competitive quality is unverified. This document does not amend v0.1 or its recorded results.

## Common scaffold, intentionally different from v0.1

Square n×n board, indices ny+x, orthogonal adjacency without wrapping. One anchor A and r reserve agents P per player. North anchor at (floor((n−1)/2),0); South anchor at its 180° rotated cell. North moves first. Other cells empty unless formation flag: place two own agents at x=anchorX−1 and anchorX+1 on North home row, rotate for South, subtract two from each reserve. Fixed quantities; no replenishment.

Each turn choose ONE action: deploy a reserve P to an empty cell orthogonally adjacent to any own piece; move any own piece one orthogonal step onto an empty cell; or capture an adjacent enemy if mover power strictly exceeds target power. Power BEFORE the move = 1 + orthogonally adjacent friendly pieces, A/P counted equally. Capturing replaces target with mover and vacates origin. There is NO own connectivity restriction on movement or deployment. Own disconnected agents remain, still support power and deployment. This is `free`, the control scaffold, not a correction to v0.1.

After ANY action targeting an occupied enemy cell (capture, breach or push), remove all opposing pieces outside their anchor's friendly connected component in a single simultaneous cleanup. If opposing anchor is absent, remove all opposing pieces. No own cleanup and no repeated cascades. No cleanup after an empty move or deployment.

Win only by removing the opposing anchor. Terminal precedence: missing North anchor → South wins; missing South anchor → North wins; third occurrence of full position → draw; 120 plies → draw; no legal actions → draw. Full position includes board, side to move and both reserves, excluding ply. Count initial position once. No pass, check, safe-anchor requirement, score, delivery or randomness. Actions outside these rules and actions after termination are illegal; harness transition assumes caller validation. Separate terminal detection must precede move requests.

## Three mechanical refinements, each relative to free scaffold

**Breach:** if adjacent opposing agents have EQUAL pre-move power, your agent may remove itself and the target as its entire action. Anchors can neither initiate nor be targets of breach. Then opposing cleanup as above. This tests whether intentional material sacrifice opens fortified networks without introducing a resource meter.

**Pressure:** if mover and adjacent target have EQUAL pre-move power, mover may push the enemy one further cell along the same vector if that cell is inside the board and empty. Mover enters target's former cell; origin vacated; target, including an anchor, survives at pushed cell. Then opposing cleanup. Pushing an anchor can disconnect its own supporting agents. Strict-power capture remains available. No chain pushes, no edge ejection, no push at unequal power. A and P both push and are pushed.

**Relay:** an own piece may instead jump over exactly one adjacent friendly piece in a straight orthogonal line onto the empty cell immediately beyond. No wrapping, chained jumps or capture on landing. This is a mobility refinement, not the old Relay candidate's delivery victory system.

## Preregistered comparison configurations

`free5`: n=5,r=5, no extra mechanic. `breach5`, `pressure5`, `relay5`: n=5,r=5 with named mechanic. `pressure6`: n=6,r=6. `pressure7`: n=7,r=7. `pressure5_formation`: n=5,r=5 with two predeployed agents per side and three remaining reserves.

No design is changed after its games start. All use the same evaluator and search protocol to expose differences, but that evaluator may favor some rules. Board-size variants also change reserve count, so those comparisons are bundles, not causal board-size estimates. v0.1 had a 100-ply limit; these have 120. Cross-version win/draw rates cannot be attributed to a single change. Anchor-abandonment remains possible in the free scaffold and is measured as disconnected side-positions; no claim that these refinements fix it.
