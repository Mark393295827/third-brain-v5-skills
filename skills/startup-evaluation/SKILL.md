---
name: startup-evaluation
description: Evaluate startup health using entrepreneurship, VC, and execution frameworks. Use when assessing a startup idea, company, pitch, due diligence target, fundraising readiness, or business model health.
version: "1.2"
updated: "2026-05-24"
assumes: "The idea or company can be assessed through stage, customer, market, product, team, traction, capital, and risk evidence."
conflicts_with: "Do not treat founder claims, TAM slides, or investor narratives as verified facts; use deep-research or verify-before-claim for evidence checks."
---

# Startup Evaluation

Evaluate the health of a startup, not just the attractiveness of its pitch.

This skill combines:

- MIT Disciplined Entrepreneurship: beachhead, customer, value, business model, validation
- Timmons model: opportunity x team x resources dynamic fit
- VC 5T model: Team, Target Market, Tech/Product, Traction, Terms
- PMF and pretotyping: behavior evidence before build effort
- Efficiency models: define the question, use MECE, test assumptions cheaply

## Usage Template

**Prompt**
```text
Use startup-evaluation on this company/idea.
Assess startup health, evidence quality, red flags, fundraising readiness, and the next cheapest validation step.
```

**Use Case**
- Founder wants a health check before building, hiring, or fundraising.
- Investor wants a due diligence memo or pass/lean-in decision.
- Team wants to identify the one constraint limiting progress.

**Expected Result**
- A structured startup health memo with scores, evidence, risks, and validation experiments.

**Output Example**
- Stage: Seed. Health score: 62/100. Verdict: promising but not Series A ready. Top constraint: weak retention evidence. Next test: 20-customer paid pilot with D30 retention threshold.

**Verification Case**
- The output separates facts, assumptions, and opinions; every score cites evidence or marks missing evidence.

**Verified Effect**
- Startup enthusiasm becomes a health dashboard, risk register, and concrete validation plan.

## Success Metrics

- Stage, startup type, and evaluation objective are explicit.
- Scores distinguish evidence-backed health from narrative confidence.
- The memo identifies top constraint, fatal risks, runway status, and next cheapest test.
- VC-scale companies are judged by power-law upside; bootstrapped companies are judged by cashflow and durability.

## When to Use

- "Evaluate this startup."
- "Is this business healthy?"
- "Should I invest / join / keep building / fundraise?"
- "Review my pitch deck or startup idea."
- "What is the next validation experiment?"

## Startup Health Model

Use this equation as the mental model:

```text
Startup Health =
  Opportunity quality
  x Team quality
  x Evidence momentum
  x Capital discipline
  x Learning velocity
  - Fatal risks
```

Do not average away a fatal flaw. A brilliant market with no reachable customer, no team fit, or six weeks of runway is unhealthy.

## Step 1: Classify the Case

Before scoring, classify:

| Field | Options |
|---|---|
| Stage | idea, pre-seed, seed, Series A, growth, mature |
| Startup type | lifestyle/SME, innovation-driven, VC-scale, hard tech, AI-native |
| Evaluation lens | founder health check, investor due diligence, fundraising readiness, pivot decision |
| Evidence state | narrative only, interviews, behavior, payment, retention, repeatable growth |

If data is missing, continue with assumptions and mark confidence low.

## Step 2: Evidence Ladder

Rank claims by evidence quality:

| Level | Evidence | Weight |
|---|---|---|
| 0 | Founder belief, TAM slide, friend feedback | very weak |
| 1 | Customer interviews about past behavior | weak |
| 2 | Landing page, waitlist, demo usage | moderate |
| 3 | Paid pilot, preorder, signed LOI, repeated use | strong |
| 4 | Retention, expansion, organic referral, healthy unit economics | very strong |

Quotes and intentions do not prove demand. Payment, repeated usage, retention, and referral are stronger.

## Step 3: Score Startup Health

Default weights. Adjust only when stage or startup type clearly requires it.

| Dimension | Weight | Healthy signal | Red flag |
|---|---:|---|---|
| Customer pain and beachhead | 15 | narrow painful use case, reachable buyer, urgent workflow | vague user, nice-to-have pain |
| Market and timing | 15 | large/growing market or focused profitable niche, clear timing window | TAM-only logic, market too early/late |
| Value proposition and 10x | 15 | 10x better, 1/10 cost, or new capability | marginal improvement |
| PMF and traction | 15 | retention, payment, pull, repeatable channel | paid growth only, high churn, weak usage |
| Business model and unit economics | 10 | LTV/CAC > 3, clear pricing, gross margin path | CAC unknown, payback too long |
| Team and governance | 15 | founder-market fit, complementary roles, written equity/decision rules | solo gaps, cofounder conflict, weak recruiting |
| Capital and runway | 10 | 12-18 month runway, milestone-based spend, financing plan | <6 month runway, unfocused burn |
| Moat and risk control | 5 | data, network, distribution, regulatory or execution moat | easily copied, platform/model dependency |

Score each dimension:

```text
0 = absent
1 = narrative only
2 = weak signal
3 = plausible but incomplete
4 = evidence-backed
5 = strong and repeatable
```

Final score:

| Score | Status | Meaning |
|---:|---|---|
| 80-100 | Healthy | Scale or fundraise if risks are bounded. |
| 65-79 | Promising | Continue, but fix the top constraint before major spend. |
| 50-64 | Fragile | Narrow scope and validate before hiring/fundraising. |
| 0-49 | Unhealthy | Pivot, pause, or redesign assumptions. |

## Step 4: VC 5T Cross-Check

For VC-backed or investor-facing evaluations, add a 5T view:

| 5T | Question |
|---|---|
| Team | Why this team? What unfair insight or execution proof exists? |
| Target Market | Can this become a power-law outcome, not just a good business? |
| Tech/Product | Is there defensibility beyond using current tools? |
| Traction | Is growth pulled by customers and retention, not only paid push? |
| Terms | Does valuation, dilution, and round structure leave room for returns? |

Use the 5T view to decide whether the company is venture-scale. A healthy bootstrapped company can still be a poor VC investment.

## Step 5: AI-Native and Hard-Tech Addendum

Use when relevant:

| Question | Why it matters |
|---|---|
| Is this Type 1, 2, or 3 AI? | Tools on existing software, replacement software, or software becoming labor have different TAM and pricing logic. |
| Does the product improve 10-40% or 10-40x? | VC outcomes need step-change value, not small convenience. |
| What remains if code or models get cheaper? | Moat must move to data, workflow, distribution, trust, regulation, or physical execution. |
| Is there product surplus? | Products built for the next model can fail before users adopt them. |
| Are hardware, supply chain, regulation, or deployment loops bottlenecks? | Hard-tech health depends on non-software execution constraints. |

## Step 6: Runway and Financing Health

Use these thresholds:

| Metric | Green | Yellow | Red |
|---|---|---|---|
| Runway | 18+ months | 6-18 months | <6 months |
| Fundraising start | before 12 months runway | 6-12 months | after crisis starts |
| LTV/CAC | 3-5+ | 1-3 | <1 or unknown at scale |
| CAC payback | <12 months | 12-18 months | >18 months |
| Burn focus | tied to next milestone | mixed | vanity hiring/spend |

Capital should buy evidence for the next milestone. Spending that does not reduce the top uncertainty is unhealthy.

## Step 7: Diagnose the Constraint

Name one primary constraint:

| Constraint | Typical fix |
|---|---|
| No painful problem | customer discovery and problem pivot |
| Wrong beachhead | segment narrower by buyer, workflow, urgency |
| Weak value proposition | quantify before/after value and 10x wedge |
| No behavior evidence | pretotype, paid pilot, concierge MVP |
| Weak retention | reduce scope, improve core workflow, delay scale |
| Team gap | recruit missing builder/seller/operator, clarify equity and decisions |
| Capital risk | cut burn, milestone fundraising, smaller experiment |
| Moat risk | build data loop, distribution edge, workflow lock-in, trust layer |

## Step 8: Output Format

Return:

```markdown
## Startup Health Memo

Stage / type / lens:
Verdict:
Health score:
Confidence:

### Evidence Ledger
Facts:
Assumptions:
Missing evidence:

### Scorecard
| Dimension | Score | Evidence | Risk |

### Top Constraint
...

### Red Flags
...

### Fundraising Readiness
...

### Next Cheapest Test
Hypothesis:
Experiment:
Metric:
Decision rule:
Cost/time:

### 30-Day Operating Focus
...
```

## Quality Gates

- [ ] Stage, type, and lens are explicit.
- [ ] Facts, assumptions, and missing evidence are separated.
- [ ] Health score uses the scorecard and does not hide fatal risks.
- [ ] VC-scale and bootstrapped-health judgments are not conflated.
- [ ] Customer pain, beachhead, PMF, unit economics, team, runway, and moat are covered.
- [ ] Top constraint is singular and actionable.
- [ ] Next cheapest test has a metric, threshold, cost/time box, and decision rule.
- [ ] Final verdict names residual uncertainty.

## Anti-Patterns

- Treating a large TAM as proof of opportunity.
- Scoring a startup from pitch quality rather than customer behavior.
- Averaging high team quality with zero demand evidence.
- Recommending fundraising before knowing the milestone capital will prove.
- Calling an AI wrapper defensible without data, distribution, workflow, or trust moat.
- Giving many generic suggestions instead of one constraint and one next test.

## Connections

- [[wiki/concepts/创业基础框架]] — Timmons opportunity x team x resources
- [[wiki/concepts/创业机会识别]] — opportunity sources, beachhead, TAM/SAM/SOM
- [[wiki/concepts/产品市场契合]] — MVP, retention, payment, referral
- [[wiki/concepts/创业融资]] — runway, LTV/CAC, fundraising stages
- [[wiki/concepts/创业团队建设]] — founder fit, complementary roles, equity rules
- [[wiki/concepts/顶级VC评估框架]] — 5T, TOPSCAN, T2D3
- [[maps/创业知识库]] — entrepreneurship system map
- [[maps/VC与一级投资知识库]] — investor evaluation map
- [[maps/效率思维与模型]] — hypothesis-driven, MECE, cheap tests
