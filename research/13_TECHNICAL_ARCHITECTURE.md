# Offline architecture and platform tradeoffs

## Candidate stacks

|Stack|Strengths|Cost / limitation|
|---|---|---|
|TypeScript + Vite + React + workers + IndexedDB + Tauri|Shared browser/PWA rules and UI; small desktop shell possible|Rust/Windows packaging, WebView differences; JS determinism discipline|
|Same web app + Electron|Consistent bundled Chromium desktop|Larger memory/distribution; still needs separate phone browser validation|
|Godot + GDScript/C#|Strong 2D tooling and desktop packaging|Web export/storage/PWA integration and iOS constraints need proof; separate DOM accessibility work|
|Native Windows + separate Swift client|Best per-platform control|Two implementations and no straightforward iPhone PWA; reject at current scope|

Recommend the shared TS web core provisionally, choose Tauri versus Electron only after a Windows packaging spike. React handles screens; canvas/sprites can render board but retain an accessible DOM move grid/log. No network dependency at gameplay runtime. Development dependencies may require Internet during installation; shipped app does not.

## Boundaries

Rules package: pure serializable state/action/repetition, rule version. Engine worker: cancellable search over rules package. World worker: deterministic event queue, employees, staffing and finance. Ledger service: integer journal with invariants, atomic batches. UI sends commands and receives immutable views; it never directly edits balances or resolves matches. Markets consume committed public events, not private worker state. Asset bundles/fonts local; analytics off by default and no accounts.

World PRNG uses specified integer algorithm and independent named streams (scenario seed, domain, event id). Store seed/counters and engine versions. Board legal outcomes have no RNG; AI tie-breaking may use recorded seeds. Avoid Math.random, wall-clock ordering and unbounded recursion. Production search reproducibility uses node budgets, not elapsed time; wall-clock watchdog may return last completed iteration and logs actual action. Integer board and finance operations replay identically; specify deterministic log/exp approximation for LMSR before cross-platform financial replay.

## Saving

IndexedDB transaction stores append-only event batch plus current snapshot pointer and checksums. Two snapshot slots, generation counters, manifest, rule/schema versions; commit only after all new records are written. Startup validates latest generation and falls back to previous complete snapshot if corruption occurs. Export/import versioned save with hash, size limit and validation; hash detects corruption, not malicious editing. Migration runs on a copy and retains prior export. Replay hash compared after load. Desktop may add atomic file backup through an adapter while preserving portable browser save format.

PWA caches versioned app shell/assets through service worker; activate an update only at safe saved boundaries. Offline works after initial installation/cache population, not before first download. iPhone Home Screen installation, IndexedDB quota/eviction, background suspension and OS-version compatibility must be verified on a physical device. Request persistent storage where supported, but never promise browser storage cannot be evicted. Offer frequent user exports. Do not rely on background tabs advancing the world; process turns when foregrounded. No mandatory sync.

## Quality and performance gates

Unit tests plus independent transition oracle, invariant fuzzing, fixed-seed replay, worker cancel/restart, round-trip save, interrupted-write recovery, migration rollback, financial conservation and settlement idempotence. Integration: launch offline, play full match, advance review, receive funded salary, save, kill, reopen and reproduce balances/history. Desktop Windows clean-machine installer test; iPhone device offline/relaunch/export/import test. No platform builds were executed here. Targets and scale experiments are in 09; do not describe them as achieved benchmarks.
