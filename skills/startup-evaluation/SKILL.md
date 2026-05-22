---
name: startup-evaluation
description: Evaluate startups using the 24-step disciplined entrepreneurship framework. Use when assessing a startup idea, conducting due diligence, or analyzing a business model.
version: "1.1"
updated: "2026-05-22"
assumes: "The idea or company can be assessed through customer, market, value, and validation assumptions."
conflicts_with: "Do not treat market assumptions as verified research; use deep-research or verify-before-claim for evidence checks."
---

# Startup Evaluation — 24-Step Framework

Evaluate startups systematically using MIT's Disciplined Entrepreneurship framework by Bill Aulet.

## Usage Template

**Prompt**
```text
Use startup-evaluation on this idea. Assess customer, market, beachhead, value proposition, business model, risks, and next validation step.
```

**Use Case**
- Evaluating a startup idea, company, or product direction before investing more time or money.

**Expected Result**
- The agent returns a structured assessment with assumptions, evidence, risks, and validation experiments.

**Output Example**
- A one-page startup memo with beachhead customer, painful use case, assumptions, risks, and cheapest test.

**Verification Case**
- The output distinguishes known facts from assumptions and names the next cheapest test.

**Verified Effect**
- Startup enthusiasm becomes an evidence map, risk register, and practical validation plan.

## Success Metrics

- Assessment distinguishes facts, assumptions, risks, and unknowns.
- Beachhead customer, painful use case, value proposition, and business model hypothesis are stated.
- Next cheapest validation test has a metric and decision rule.

## When to Use

- User wants to evaluate a startup idea
- User is conducting due diligence on a company
- User wants to analyze a business model
- User says "assess this startup" or "evaluate this business"

## The 24-Step Framework

### Phase 1: Market Identification (Steps 1-5)

| Step | Question | Key Metric |
|:----:|----------|------------|
| 1 | **Market Segmentation** — Who are the potential customers? | Customer segments identified |
| 2 | **Beachhead Market** — Which segment to start with? | Clear initial target |
| 3 | **End-User Profile** — Who exactly is the buyer? | Detailed persona |
| 4 | **TAM Calculation** — How big is the market? | Total Addressable Market |
| 5 | **Customer Acquisition** — How do they find you? | Acquisition channels |

### Phase 2: Customer Understanding (Steps 6-10)

| Step | Question | Key Metric |
|:----:|----------|------------|
| 6 | **Decision Making Unit** — Who decides to buy? | DMU mapped |
| 7 | **Acquisition Process** — What's the buying journey? | Funnel stages |
| 8 | **Customer LTV** — What's a customer worth? | Lifetime Value |
| 9 | **Competitive Landscape** — Who else serves this market? | Competitive map |
| 10 | **Product Solution** — What do you offer? | Value proposition |

### Phase 3: Product Development (Steps 11-15)

| Step | Question | Key Metric |
|:----:|----------|------------|
| 11 | **Value Proposition** — Why you? | Unique value |
| 12 | **Quantified Value** — How much better? | Metrics |
| 13 | **Pricing Strategy** — What to charge? | Price points |
| 14 | **Sales Channel** — How to deliver? | Channel strategy |
| 15 | **Marketing Strategy** — How to attract? | Marketing plan |

### Phase 4: Business Model (Steps 16-20)

| Step | Question | Key Metric |
|:----:|----------|------------|
| 16 | **Business Model** — How to make money? | Revenue model |
| 17 | **Customer CAC** — What does it cost to acquire? | Acquisition cost |
| 18 | **Sales Process** — How to close deals? | Sales funnel |
| 19 | **Market Size** — More precise estimate? | Refined TAM |
| 20 | **Financing Strategy** — How to fund? | Capital needs |

### Phase 5: Execution (Steps 21-24)

| Step | Question | Key Metric |
|:----:|----------|------------|
| 21 | **Team Design** — Who's needed? | Team gaps |
| 22 | **Board Design** — Governance structure? | Board composition |
| 23 | **Milestones** — Key checkpoints? | Milestone plan |
| 24 | **Iteration** — How to adapt? | Feedback loops |

## Quick Evaluation Checklist

For rapid assessment, focus on these critical factors:

### ✅ Market (Steps 1-5)
- [ ] Clear market segment identified
- [ ] TAM > $1B (for VC-backed) or > $100M (for bootstrapped)
- [ ] Beachhead market clearly defined
- [ ] Customer acquisition channels exist

### ✅ Product-Market Fit (Steps 6-10)
- [ ] Clear buyer persona
- [ ] LTV/CAC > 3
- [ ] Competitive advantage identified
- [ ] Value proposition is compelling

### ✅ Business Model (Steps 16-20)
- [ ] Revenue model is clear
- [ ] Unit economics work
- [ ] Capital requirements are reasonable

### ✅ Execution (Steps 21-24)
- [ ] Team has relevant experience
- [ ] Milestones are achievable
- [ ] Feedback loops exist

## Evaluation Scoring

| Score | Market | Product | Team | Verdict |
|:-----:|--------|---------|------|---------|
| **A** | Large, growing, clear entry | Strong PMF, defensible | Experienced, complementary | Strong invest |
| **B** | Good size, some competition | PMF emerging, needs iteration | Capable, some gaps | Conditional invest |
| **C** | Small or crowded | Weak PMF, undifferentiated | Inexperienced or incomplete | Pass or pivot needed |
| **D** | No clear market | No product-market fit | Wrong team | Clear pass |

## Quality Gates

- [ ] Known facts are separated from assumptions.
- [ ] Beachhead customer and painful use case are explicit.
- [ ] Market, product, business model, and execution risks are scored.
- [ ] Competitive alternatives are named.
- [ ] Next cheapest validation test is concrete and measurable.
- [ ] Final verdict includes residual uncertainty.

## Key Insights from Bill Aulet

1. **Start small, think big** — Beachhead market first, then expand
2. **Customer discovery > product development** — Talk to customers before building
3. **LTV/CAC is the key metric** — Must be > 3 for sustainable business
4. **Innovation-driven vs. small business** — Different frameworks for different types
5. **Discipline over inspiration** — Follow the process, don't rely on genius

## Connections

- [[wiki/concepts/产品市场契合]] — PMF is the core goal
- [[wiki/concepts/创新扩散]] — How new products get adopted
- [[wiki/concepts/飞轮效应]] — Business model growth logic
- [[wiki/concepts/精益思维]] — Rapid iteration methodology
- [[wiki/concepts/7种战略力量]] — Competitive advantage framework
- [[maps/VC与一级投资知识库]] — VC evaluation frameworks
