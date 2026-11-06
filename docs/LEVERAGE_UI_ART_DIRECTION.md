# Minimal interface and pixel-art specification

**Plausible but unverified:** layout/art specification. No production art or device usability validation is claimed. This four-destination design supersedes the preserved five-destination proposal in historical 12.

## Persistent identity header

Fields: **TITLE | EMPLOYEES OVERSEEN | POWER | RATING | NET WORTH**. Title displays position title, not rating tier. Employees counts distinct occupied reporting descendants, excluding vacancies and double-counted shared projects. Power is an authority-scope label (Team / Department / Division / Company / Board), not an invented combat statistic. Rating includes uncertainty on inspection. Net worth is marked wealth with locked cash/illiquidity in the detail overlay. Ownership is a badge separate from authority.

At ≥1024 CSS px: header 64 px high, 24 px emblem, five aligned fields, 16 px gutters, title min 180 px, wealth right aligned. At 320–430 px: header 88 px in two rows; top title/emblem (remaining width), rating 80 px; second row equal three columns for Oversees / Power / Net worth with 12 px labels and 16 px values. Never squeeze five unreadable items into one row. Tap opens a single identity overlay with complete numeric values and explicit authority. An icon-only compactness mode must retain accessible field names. At 200% text zoom allow header to grow/scroll; it must not clip the board.

## Four destinations

|Destination|Default surface|Contextual overlays, not new primary screens|
|---|---|---|
|Arena|Board, opponent, next tournament match, Play/Review|Tutorial, replay, legal/collapse explanation, spectator forecast|
|Exchange|Portfolio and a short eligible-market list|Trade confirmation, uncertainty/calibration, cash ledger|
|Career|Current position and one recommended vacancy|Apply/qualification, bracket, approval reasons, personal history|
|Empire|Team/company at current authority scope|Delegated budget, org drill-down, governance, research priorities|

People search and history live in contextual overlays in Career/Empire. Settings/save/export in header menu. No mandatory HR form, separate betting screen per match or wall of dashboards. First-time Arena needs at most three short prompts: choose, preview, confirm; full written rules remain optional.

## Desktop layout, 1280×800 reference

64 px header + 48 px destination bar; 16 px outer margins. Arena grid: flexible left 200 px rival/next-match panel, central 560 px board column, right 280 px inspector; remaining width as gutters. Five cells fit a 500 px board with 100 px cells, leaving move controls below. Inspector defaults to selected-piece power/components or last-move consequence; charts appear only when asked. Minimum viewport below 1024 collapses sidebars into drawers rather than shrinking pieces indefinitely.

## iPhone layout, 390×844 reference

Respect top/bottom safe-area insets. Header 88 px, compact match line 48 px, board width min(viewport−24 px, 480 px): 366 px at 390 width, 73.2 px cells for 5×5. A 7×7 research board would give ~52 px cells; 8×8 at 320 width would fall below 44 px and requires zoom/alternate move selection. Below board: latest-move line 40 px and primary action row 48 px. Four bottom destinations each at least 64×48 px. Remaining content scrolls; history and finances open a bottom sheet with explicit close, not a second navigation tree. These arithmetic fits exclude keyboard/large text; require real device tests.

## Spectating and finance

Use the same board. Player names/ratings at top and bottom, probability bar labelled forecast source/version and uncertainty (not engine win certainty). Compact position chip shows shares/cash-at-risk only if eligible; excluded players see a clear reason. Tap chip opens market sheet over the same arena. Public statistical research tabs fit the inspector/sheet. Private move analysis is locked while official contract is open; after settlement replace trade affordance with review. No countdown flashing, guaranteed-return colors or odds covering legal moves.

## Art, motion and accessibility

Bounded first kit: one 16×16 office tile set, two board material variants, distinct 24×24 agent and 32×32 anchor silhouettes, three company emblems, twelve 48×48 portrait bases with declared accessory variants, eight authority insignia and three trophy shapes. Offices evolve by a few authored layers at authority milestones, not one room per grade. Midnight-indigo architecture, ivory board, copper authority, teal operational cues; highlight selection by outline plus symbol, capture by distinct pattern. Nearest-neighbor sprite scaling; text uses readable scalable font, not tiny mandatory pixel type.

120–250 ms move animation target, collapse ordered with a before/after preview, reduced-motion instant transition. Tab/arrow grid, Enter select, Escape cancel, screen-reader coordinates and live move log. Pointer/touch equivalent, no hover-only content, ≥44 CSS px action targets; verify text/background contrast with measured color pairs before freezing palette. Labels/glyphs carry every color-coded state. Every high-impact financial/governance action previews cost and consequence; board confirmations configurable, no animation backlog. Measure first-match completion, mis-taps, preview comprehension and mandatory-reading time with 12 testers.

## Final R0 research interface boundary

The shipped research artifact is a terminal board inspector/human-vs-AI harness, not this pixel-art UI. It lists coordinates, legal moves, adjacency power and removal counts; its scripted smoke test is not human readability validation. **Unverified:** human teach-back, touch clarity, artwork and enjoyment. All four destinations and the executive header above remain the future product design; no new research screen is added to the product navigation. With no approved board, do not draw a polished UI around a rejected candidate to imply readiness.
