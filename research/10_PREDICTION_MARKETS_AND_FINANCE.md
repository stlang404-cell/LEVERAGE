# Fictional-money markets, finance and audit

No deposits, cash-out, purchasable currency, paid wagering or real-money links. All contracts and holdings are local save data. Betting is optional; salaries, sponsor stipends, tournament prizes and dividends supply non-betting progression. Losses may delay ownership without blocking core play. “Billionaire” is an eventual nominal campaign goal, not a balance promise.

## LMSR proposal and mathematical facts

For n mutually exclusive exhaustive outcomes with quantities q_i and liquidity b>0:

C(q)=b log Σ_i exp(q_i/b), p_i=exp(q_i/b)/Σ_j exp(q_j/b).

A trade Δ costs C(q+Δ)−C(q); stable implementation subtracts max(q_i/b) before exponentiation. Outcome i pays 1 per winning share; losing shares pay 0. Symmetric zero initialization has maximum theoretical maker loss b log n for the standard fully collateralized LMSR market. This bounds a SINGLE market under these assumptions, not economy-wide losses. Maker cash is funded before listing. Ten thousand b=20 binary markets require up to about 138,630 currency units of aggregate subsidy if each realizes its bound; do not assume b=20 is free.

Lab tests verify numerical trade bounds and fee-free round trips on selected examples, not all accounting, multi-outcome implementation or exploit safety. Production uses integer microcurrency ledger, fixed deterministic numeric algorithms, rounding toward conservative collateral, and reconciles residuals to a declared rounding account. Floating math in this research is not a production cash ledger.

Initial restrictions: long-only positions, no leverage, no shorting, no credit; buy with cash, sell at most held shares. Proposed fee 1% of positive gross trade consideration, paid to maker treasury, disclosed before confirmation. Max player exposure: min(10% liquid wealth, 20% market subsidy budget); minimum ticket waived for low wealth. Caps require playtesting. A simpler pari-mutuel pool has bounded payout but uncertain odds; fixed-odds books need a separate liability cap. Defer multi-outcome and linked derivatives until binary settlement is reliable.

## Official eligibility and information policy

Official markets concern third-party full-engine matches with publicly available ratings/results only. Disallow participation by player, reports under player authority, corporate entities controlled by player, portfolio companies over a disclosed control threshold, or subjects whose outcome the player can affect. Compute causal authority closure before listing; if authority changes, freeze trading, refund all participants by preannounced void rules, retain audit. Exclude executive dismissals, promotions, earnings and acquisitions from first official markets: player governance and private information make fairness difficult. Own-match sandbox markets use a separate nontransferable sandbox balance with no career, prestige or wealth effect.

Analysis of a wagerable match is locked before market open through settlement. Participants cannot use private engine analysis, alter lineups or inspect concealed world forecasts. Public model and event commitments are fixed before bets. A local user can inspect files or edit a save; tamper-proof offline wagering is impossible. The goal is coherent in-game rules, not adversarial security against the device owner. Save scumming is a preference/accessibility policy, not a reason to add accounts.

## Settlement and ledger

Contract states: drafted → funded → open → locked → resolved → settled; void is a separate audited terminal route. Fixed event ID, resolution predicate, cutoff tick and rule/engine versions at listing. Close before match computation and before new private information. Idempotent settlement key prevents duplicate payout. Reserve maker subsidy plus player deposits; settle winners, fees and released reserves atomically. Forbid negative available balances. Cancellation refunds net deposits and fees, never treats both possible outcomes as winning. Retained event explains each balance change.

Every transfer has event ID, debit account, credit account, integer amount, tick and reason. Cash conservation: total cash changes only through explicit scenario issuance/burn accounts. Securities are claims, not cash. Net worth = cash + marked holdings − liabilities; unrealized gains are not spendable cash. LMSR probability improvement and equity price appreciation can increase marked wealth without increasing total cash; this is not an infinite-money cash source.

## Corporate finance

Customer-sector treasury pays revenue for services under finite demand; wages/bonuses are corporation-to-employee transfers; prizes come from pre-funded sponsors. Initial endowments have scenario ledger entries. Equity grants transfer treasury shares or dilute existing owners through approved issuance. Shares sum to issued shares; corporate self-holdings excluded from outstanding vote/dividend denominator. Salaries and bonuses cannot exceed authorized funded obligations. Dividends distribute available corporate cash pro rata, never marked valuation gains. Board approval needed for issuance, buybacks and control sales; ex-dividend valuation prevents free dividend harvesting. New shares receive dividend rights only under recorded cutoff policy.

Public equity prices use a published deterministic valuation proposal based on discounted expected cash flow plus bounded modeled order pressure. Do NOT claim this is a real efficient market; model and calibrate it separately. Private valuations are illiquid estimates with an explicit haircut. Acquisitions transfer ownership, debt and cash under a transaction, with no duplicated assets. Holdings are capped and controlling ownership graph acyclic initially. Bankruptcy wipes out residual equity after claims; recovery stipends come from the explicit sponsor account. Anti-exploit tests must cover duplicate settlement, round-trip fees, dividend cutoff, self-dealing, share dilution, negative balances, buyback/issuance cycles and save replay.
