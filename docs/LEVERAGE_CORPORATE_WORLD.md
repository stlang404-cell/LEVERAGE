# Corporate world, tournaments and authority

**Plausible but unverified:** proposed gameplay specification; population fixture costs are measured separately in [evidence](LEVERAGE_BOARD_GAME_RESEARCH.md). History and governance are not yet a production simulation.

## Actual seats, actual authority

Preserve the entity model in [historical world design](../research/07_CORPORATE_WORLD_DESIGN.md): Person ≠ Position ≠ Title ≠ Grade ≠ Rating ≠ Ownership ≠ NetWorth. A position has stable ID, compensation envelope, function, organization, reporting parent, eligibility and occupant or vacancy. A company contains divisions, departments, offices and teams, not thousands of rank labels. Staffing capacity produces services under finite customer demand. One primary position per employee; acyclic reporting; one occupant per seat. Ownership controls governance votes, not a magical personal treasury withdrawal.

Events govern recruiting, offers, resignations, transfers, dismissal, retirement, restructuring and succession. AI people use the same vacancy/selection processes while the player is absent. Rating/uncertainty, ambition, risk preference, research skill, financial resources, rival links and employment events persist. No rerolled rival identities. For ordinary daily events, schedule only due entities; unwatched background league outcomes may be explicitly approximate, never retroactively converted to fake full-match replays. Official market matches lock full-engine resolution before listing.

## Vacancy contract: apply → compete → approval → promote

A published vacancy freezes seat ID, salary funding, qualification predicate, format, seeding method, rules version, schedule, tie-break ladder, appointment type and fallback. Apply is one button; confirmation needed only if schedule conflicts. Relevant achievements/history attach automatically. Qualification: required training certification, at least one completed review cycle, role-specific operational qualification, no active serious-budget sanction. Publish exact requirements; show one attainable next action per failed requirement. Rating bands seed matches, not unlimited title inflation.

For the first lead vacancy, tournament entry needs training and review completion; no minimum rating blocks an ambitious junior. Entries freeze before seeding. Subsequent qualifications assess scope experience, not raw cash or corporate favoritism. Thresholds are initial design values, subject to playtesting.

|Tier|Candidate count / format|Role of result|
|---|---|---|
|Department/team lead|2–4, paired-color round robin|Guaranteed appointment if prepublished legal eligibility still holds|
|Management trial|4–8, 3-round Swiss plus top-two paired final|Guaranteed funded seat or explicitly named nomination, never ambiguous|
|Director|8–16, 4-round Swiss then paired top-four bracket|Earn nomination; published operating qualification and approval checks|
|Executive circuit|16+, qualifier to 8-person round robin across scheduled days|Rank shortlist for board approval with disclosed criteria|
|Board championship|4–8 qualified nominees, paired matches|Elective board nomination; shareholder vote remains distinct|
|CEO succession|Board-qualified shortlist 2–4, paired round robin|Competitive winner preferred under charter; vote/constraints disclosed before entry|
|Control competition|Only charter-authorized, pre-funded share prize|Transfers specified shares; never invents control rights or confiscates existing ownership|

Knockout is legible and quick but one upset dominates; paired-color matches mitigate seat imbalance, not skill variance. Round robin compares all contenders but costs m(m−1) games when each pair plays both colors. Swiss reduces games but opponent strength and pairing affect results; never compare raw score across different fields. Hybrid adds excitement after broader qualification. These are design arguments, not measured promotion-fairness results. Huge brackets are not required for every vacancy.

Seeding: published rating order with stable employee-ID tie-break; balanced top/bottom bracket, recorded pairings, no repeat Swiss opponent unless unavoidable. Swiss bye assigned lowest-score player without prior bye, one point and no rating change; withdrawn participants receive no future byes. Games score 1/0.5/0; paired match total determines winner. Tie-breaks: head-to-head if all tied have met equally, then opponents' score excluding bye, then two additional color-swapped games; if still tied, use the posted prior-review operational score then seeded public lot. The final lot is a corporate selection rule, never a random board outcome; display it explicitly. Do not use sudden-death first-player advantage before fairness is known.

Withdrawal before start reseeds once; after start completed results stand and remaining games are administrative forfeits (no rating updates). Recorded engine/rules defect pauses affected round and recomputes only annulled games from saved pre-round state; funded prizes remain escrowed. Appeals within one simulated day check eligibility, logs or rules faults, not dislike of a loss. Daily scheduling respects one live player match at a time; waiting periods are Advance actions, not real-time gates. Offer nearest appropriate vacancy instead of forcing the player to play dozens of background fixtures.

## Approval is a contract

State machine: posted → applicationsClosed → qualified → competing → resultFinal → approvalPending → offered → accepted → occupied. Atomic acceptance checks funding and unique incumbency. Guaranteed appointments require no discretionary rejection. A nominated winner sees remaining constraints before applying: e.g. shareholder vote or conflict-of-interest clearance. Votes record members, public evaluation criteria, conflicts and reasons; private personality preferences cannot overturn a guaranteed appointment. If a charter appointment fails, winner retains published prize and nomination prestige and sees the next vacancy. Vacancies lost to bankruptcy void selection and refund costs under published rules.

## Authority and rewards

Employee: compete/apply/invest. Lead: roster and training. Manager: funded hiring and team budgets. Director: department restructuring and research scenarios. VP: division allocation and portfolio analytics. CEO: company strategy/capital proposal. Chair: board process. Owner: ownership voting. Research capabilities are described in [finance](LEVERAGE_FINANCE_AND_RESEARCH.md). Promotion changes scope, salary, office art, insignia and eligible contests; it never changes board pieces. Delegate routine work with caps and exception alerts.

Demotion: published objectives, warning, one recovery review, then lawful seat change; two failed reviews is proposed default. Dismissal preserves history, rating and vested property. Practice and public sponsor-funded competitions remain available. Rival firms recruit available staff. No debt or demotion blocks board access.

## Permanent history

Every former CEO, championship, bankruptcy, promotion, dynasty and comeback derives from a committed event with entity IDs, tick, predecessor and source result. Index notable events and annual summaries; archive detail without deleting award provenance. “Legendary comeback” requires a declared predicate (dismissed, later appointed above prior grade after at least one real contest), not random flavor. Store rating as-of the event, not today's rating. History is permanent within campaign retention/export limits; full audit archives must remain exportable before compaction.
