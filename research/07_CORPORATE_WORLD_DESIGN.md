# Corporate civilization: positions with functions

Design proposal, not implemented or scale-tested. Start with 3 corporations, 120 employees total, then grow only after measured scheduler and save tests. A 20,000-person population is a target, not a verified capability.

## Entity boundaries

Employee(id, identity, ageTicks, rating, skills, preferences, careerEvents) is a person. Position(id, organizationId, reportsToPositionId, grade, titleId, function, budgetEnvelope, eligibility, incumbentId?) is a job seat. Grade defines compensation band and authority ceiling. Title is display vocabulary. A manager may occupy one of 400 separate manager positions sharing one title. Vacancy is a position state, not a fake employee.

Organization(id, parentOrgId?, corporationId, type, region, charter, positions) represents subsidiary, division, department, office or team. Corporation(id, legalEntityId, treasuryAccount, shareRegister, boardId, charter) can own subsidiary shares. Holding ownership is separate from managerial reporting. Board seats are positions with appointment and voting rules. Cap tables can form ownership cycles unless explicitly prevented: prohibit cycles in controlling corporate ownership for the first release.

Every team produces a visible service output from staffing, assigned training, budget and match performance. Do not create seats solely to increase a count. Example: a six-person analytics team delivers forecasts, schedules training and supplies a tournament roster; its leader allocates 100 weekly budget units among recruitment/training/reserves. Output supplies contracted fictional customer demand. No staff means reduced capacity, not deletion of its history.

## Time and operations

One Advance action processes a day; matches do not consume real-world waiting. Weekly tournaments and payroll, monthly reviews and board meetings. Events ordered by (tick, phase, stable entity id, sequence). Phases: settle completed matches, settle eligible contracts, cash obligations, operations, staffing, governance, publish public feed. A contested event never changes after a market settles.

Vacancy → posted → ranked applications → offer → accepted/declined → assignment. One incumbent per position, one primary job per employee. Transfers require release or notice; resignation frees seat and retains person/holdings. Layoffs remove funded seats through an authorized reorganization and severance ledger entries. Retirement vacates a seat and triggers succession candidates. Recruitment uses preference utility, not guaranteed loyalty to the player.

Founding requires capital, charter and at least one funded revenue-producing team. Acquisition transfers shares only after consent/vote and treasury authorization; it does not overwrite employee careers. Bankruptcy: freeze new discretionary commitments, pay claims in disclosed priority, restructure or liquidate; employees become applicants. Shareholders lose residual value. No automatic personal loss beyond invested capital unless explicit debt was accepted.

## Invariants and acceptance gates

Acyclic reporting, supervisor authority over descendants only, valid organization membership, unique incumbency, no employee in two primary jobs, legal cap table totals, approved budget before payroll promises. Require property-based random staffing sequences and save/load replay equivalence before scaling. Default 120/2,000/20,000 employee benchmark scenarios must publish memory, save size and tick p95 on named devices; no benchmark was run here.
