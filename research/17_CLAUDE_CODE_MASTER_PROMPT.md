# Claude Code implementation directive

You are implementing CORPORATE LADDER from this research package. Read 00–16 in numeric order, especially the evidence boundaries in 04–06 and 15. Do not infer that a final competitive game was validated. Remain offline-first, local single-player, fictional currency only, without accounts, remote inference, paid APIs or mandatory internet. Development package downloads are separate from runtime. Protect existing work; use the existing isolated checkout and do not create a worktree unless asked.

## Rule authority and research gate

The research lead is Leverage v0.1, exactly specified in `03_FORMAL_RULESETS.md`, section L plus shared definitions; executable reference `experiments/arena.py`. Its 5×5 board, two anchors, five-agent reserves, orthogonal adjacency, pre-move strict power comparison, post-capture enemy-component cleanup, asymmetric empty-move connectivity restriction, threefold position identity and 100-ply draw are mandatory for reproducing v0.1. Read that full definition before coding; do not rename a revised game v0.1. No implied chess check or title-based advantage. The source has known undesirable anchor-abandonment behavior. Do not “fix” it silently. Implement the three explicit connectivity variants in 05 behind research-only selectors, run comparisons and ask for a rules decision only once concrete evidence is available. Relay is fallback, not an interchangeable Leverage rule.

Do not begin the entire civilization. First independently reproduce terminal and move fixtures, deterministic transitions and paired research results at the state/action level. Add illegal-action rejection at the application boundary. Keep an independent reference oracle. A research stop is acceptable if no game passes; marketing claims of depth/fairness require evidence beyond random play.

## First playable deliverable

Use TS/Vite with a responsive accessible UI and worker search provisionally; verify dependencies before selecting exact versions. Provide one full match against local AI, tutorial for power/support/cuts, legal-action preview, collapse confirmation, move history, deterministic replay and practice undo. Seeded AI tie-breaking is permitted and recorded; match rules never roll dice. Provide a small three-company world containing one real six-person team each, stable people/position IDs, an intern player, actual leader vacancy, funded weekly payroll/prize budget and review/application. A win changes rating/review/prize evidence; it does not automatically grant a CEO seat. A loss preserves practice and recovery choices. Save/load must preserve board, history, employees, balances and event versions. Betting can wait for stage 3; do not pad the slice with fake exchange panels.

## Acceptance evidence for stage 1

- Run documented clean install/build/test commands with lockfile; report actual results.
- Differential legal-action/transition tests against Python reference on at least 10,000 reachable states per frozen ruleset; targeted leader, cut, connectivity, repetition, draw-limit and illegal-action tests. Record seeds and state hashes. These are targets for future work, not checks already executed.
- Play a complete human-vs-AI game; restart from midgame save; verify exact replay and final result. Board remains usable without network. Demonstrate real input, not a screenshot/PID alone.
- Worker returns legal moves, respects cancellation and reports nodes/depth. Benchmark at fixed node budgets; higher difficulty must show measured paired strength gains before strength labels are promoted.
- One salary and prize cycle, one eligible application/appointment, one failed application and recovery path. Unique job incumbency, no negative cash and transfer conservation checked.
- Interrupted-save test recovers previous complete generation; export/import preserves canonical state hash. No secrets or runtime network calls required.
- Keyboard and touch completion, color-independent pieces, readable phone board, reduced-motion behavior. Art can be bounded interim assets but must be labelled interim.

## Later-stage architecture and requirements

Follow roadmap 16. Pure rules, engine worker, world worker, append-only events and integer ledger are separate boundaries. Key deterministic PRNG by domain/entity/event; never use viewport visibility to change a committed outcome. Detailed official matches and approximate league results are explicitly distinguished. Store real career histories, vacancies and reporting DAG; grade/title/person/position are separate. Promotions require vacancy/funding/evidence, demotions require warning/review, CEOs follow governance. Authority checks are serverless domain checks, not merely hidden buttons.

Markets follow 10: binary long-only initial scope, funded LMSR subsidy, deterministic numeric costs, bounded exposure, fees, lock before resolution, idempotent settlement and auditable void/refund. No self/controlled-outcome official betting, no private analysis while market is open; sandbox funds isolated. Track cash, claims, shares and marked wealth separately; wages/dividends/prizes have source accounts, no unlimited buyback/dividend exploit. Full financial lifecycle tests precede enabling markets.

Use the bounded pixel-art plan in 12 and measure readability. UI must expose the massive world by search, summaries and delegation rather than show thousands of seats simultaneously. Measure population CPU/heap/save growth with realistic histories before increasing scale. No claim of 20k performance from a small fixture.

Compare Tauri/Electron with an actual Windows build spike. Shipped desktop must launch without developer tooling. PWA must cache all required local assets after first install, handle iPhone suspension, use IndexedDB and export recovery; test on a real iPhone. Do not claim that browser storage is permanent or that localhost tests prove platform readiness.

## Delivery discipline

At each milestone give exact commands/results, rule/schema/build versions, playable artifact, remaining defects and a statement of what is provisional. Preserve deterministic replay corpora and migration backups. Do not call placeholders complete, fabricate benchmarks or replace failed meaningful checks with trivial ones. Keep core play enjoyable with zero bets and after dismissal/financial loss. Defer expansion whenever the current stage fails its quality gate.
