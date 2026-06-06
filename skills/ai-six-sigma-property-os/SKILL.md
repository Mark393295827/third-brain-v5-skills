---
name: ai-six-sigma-property-os
description: Design an AI Six Sigma Black Belt operating model for property service, maintenance dispatch, environmental testing, quote generation, CRM follow-up, and workflow quality dashboards. Use when the user needs a Property Agent OS, AI + Ontology + DMAIC management system, CTQ metrics, agent-team roles, work-order states, or MVP roadmap for operations quality.
version: "1.0"
updated: "2026-06-06"
assumes: "The business has real or planned property service workflows with customers, work orders, workers, quotes, evidence, and quality metrics."
conflicts_with: "Do not replace legal, safety, environmental compliance, payroll, tax, or customer-contract review; keep high-impact AI decisions under human confirmation."
---

# AI Six Sigma Property OS

Build a practical operating model for property service quality using:

```text
Ontology defines the business world.
Agent Team executes and audits workflows.
Six Sigma DMAIC continuously reduces errors, delay, rework, and cost.
```

This skill is for designing the management system before building software. It should produce executable operating structure: ontology, roles, CTQ metrics, work-order flow, database tables, dashboards, and MVP scope.

## Usage Template

**Prompt**
```text
Use ai-six-sigma-property-os for my Property Agent OS.
Design an AI + Ontology + DMAIC Black Belt operating model for property work orders, worker dispatch, environmental testing, quote generation, CRM follow-up, evidence upload, and quality dashboards.
```

**Use Case**
- Founder wants to turn messy property maintenance operations into a measurable AI workflow.
- Operator needs CTQ metrics, root-cause analysis, dispatch rules, quote controls, and evidence gates.
- Product team needs a first-stage MVP plan before building a full property SaaS.

**Expected Result**
- A practical operating memo with pyramid model, DMAIC loop, ontology objects, agent roles, CTQ scorecard, dashboard design, core tables, work-order states, control plan, and MVP roadmap.

**Output Example**
- MVP Stage 1: classify work orders, recommend workers, generate quote draft, require evidence upload, and track response time, completion time, rework rate, complaint rate, quote error, gross margin.

**Verification Case**
- Every module maps to at least one CTQ metric, data field, owner, human confirmation point, and control check.

**Verified Effect**
- A service workflow becomes a measurable quality flywheel instead of ad hoc manual coordination.

## Success Metrics

- Defines the business objective and first-stage operating scope.
- Produces a DMAIC workflow tied to real property operations, not generic quality jargon.
- Names ontology objects, required fields, agent roles, CTQ metrics, dashboards, and work-order states.
- Separates AI recommendations from human approval for quotes, dispatch exceptions, safety, compliance, and customer-impacting decisions.
- Includes a narrow MVP roadmap focused on work orders, workers, quotes, evidence, and quality dashboard before expanding.

## When to Use

- "Design my Property Agent OS."
- "Build an AI Six Sigma model for property maintenance."
- "Use DMAIC to improve dispatch, quote, and service quality."
- "Create CTQ metrics and dashboards for my work-order business."
- "Design agent roles for property, environmental testing, and CRM operations."

## Operating Pyramid

Use this as the top-level model:

```text
Business goals
  Reduce cost / raise speed / stabilize quality / make repeatable / support financing
      ↓
Six Sigma Black Belt layer
  DMAIC / data analysis / root cause / control plan
      ↓
Ontology semantic layer
  Customer / property / asset / work order / worker / route / quote / rule / evidence
      ↓
Agent Team execution layer
  Classify / dispatch / quote / audit / review / control
      ↓
Field operations
  Repair request / service / environmental test / payment / review
```

Core rule:

```text
Ontology clarifies.
Agents execute and audit.
DMAIC improves the system after every work order.
```

## Step 1: Define the Operating Scope

Classify the case before designing:

| Field | Options |
|---|---|
| Business type | property repair, maintenance, environmental testing, cleaning, inspection, CRM follow-up |
| Stage | idea, manual pilot, spreadsheet MVP, internal tool, SaaS product |
| First workflow | work-order classification, dispatch, quote, evidence, quality dashboard |
| Human approval level | all decisions, quote only, exceptions only, mostly automated |
| Data maturity | no data, sheets, CRM, database, integrated system |

Default MVP scope:

```text
1. work-order classification
2. worker dispatch recommendation
3. quote draft generation
4. evidence upload and audit
5. quality dashboard
```

Do not expand into a full ERP, marketplace, payroll system, or finance system before this loop works.

## Step 2: DMAIC Workflow

Map Six Sigma to the property workflow:

| DMAIC | Property OS use |
|---|---|
| Define | Define customer pain, work-order types, SLA, service standards, CTQ metrics |
| Measure | Track response time, dispatch time, completion time, quote error, rework, complaint, evidence completeness |
| Analyze | Find root causes for delay, wrong dispatch, missing evidence, wrong quote, low rating |
| Improve | Update dispatch rules, quote rules, worker matching, SOPs, customer scripts |
| Control | Use dashboards, alerts, approval gates, SOP audits, agent review, weekly Black Belt review |

Every work order should become a learning event:

```text
Work order creates data
Data reveals problems
Problems trigger root-cause analysis
Root causes improve rules
Rules train agents
Agents improve speed and quality
More volume creates better data
```

## Step 3: MECE Quality Domains

Score quality across seven non-overlapping domains:

| Domain | Controls | Core metrics |
|---|---|---|
| Customer quality | experience, response, satisfaction | first response time, satisfaction, complaint rate |
| Work-order quality | classification, dispatch, completion, acceptance | first-time fix rate, rework rate, timeout rate |
| Worker quality | skills, location, reliability, rating | on-time rate, completion rate, customer score |
| Quote quality | accuracy, margin, approval | quote error rate, gross margin, close rate |
| Process quality | end-to-end flow | cycle time, bottleneck, wait time |
| Data quality | completeness, accuracy, traceability | missing field rate, missing photo rate, missing location rate |
| Knowledge quality | SOPs, rules, lessons | SOP hit rate, rule update frequency, case review rate |

If a module has no metric, it is not ready for automation.

## Step 4: Ontology Objects

Define the business world before defining agents.

Minimum ontology:

| Object | Required fields |
|---|---|
| Customer | id, name, contact, address, priority, consent flags |
| Property | id, address, building, unit, access rules, manager |
| Asset | id, property_id, type, model, location, maintenance history |
| WorkOrder | id, customer_id, property_id, type, priority, SLA, status, description, evidence_required |
| Worker | id, skills, service area, location, availability, rating, capacity |
| Quote | id, work_order_id, labor, materials, travel, margin, approval_status |
| Evidence | id, work_order_id, photos, video, signature, location, timestamps, checklist |
| Rule | id, trigger, condition, action, owner, version |
| Review | id, work_order_id, issue, root_cause, countermeasure, owner, due_date |

Add environmental testing fields only when needed:

| Object | Fields |
|---|---|
| TestResult | work_order_id, pollutant_type, device_id, value, unit, threshold, calibration_status |
| Device | id, model, calibration_date, operator, status |

## Step 5: Agent Team Roles

Use agents as a Black Belt team, not as unbounded autonomous decision-makers.

| Agent | Responsibility | Human gate |
|---|---|---|
| Define Agent | define problem, SLA, CTQ, work-order type | new service standard |
| Measure Agent | calculate metrics and missing data | metric definition changes |
| Analyze Agent | run 5 Why, fishbone, bottleneck analysis | root-cause acceptance |
| Improve Agent | propose SOP, quote, dispatch, route improvements | policy and pricing changes |
| Control Agent | monitor dashboard, alerts, control plan | closure of exceptions |
| Dispatch Agent | recommend worker by skill, distance, availability, SLA | high-risk or low-confidence dispatch |
| Quote Agent | draft quote and margin calculation | customer-facing quote approval |
| Review Agent | detect wrong orders, missing evidence, abnormal quotes, risk | case closure and disciplinary action |

## Step 6: CTQ Metrics

Use CTQ (Critical to Quality) as the operating scoreboard:

| Goal | Metrics |
|---|---|
| Fast | first response time, dispatch time, completion time |
| Accurate | classification accuracy, dispatch accuracy, quote accuracy |
| Stable | rework rate, complaint rate, timeout rate |
| Cheap | cost per order, empty-run rate, material waste |
| Profitable | gross margin, close rate, repeat purchase |
| Controlled | evidence completeness, SOP execution rate, data completeness |

Set thresholds:

```text
Green = acceptable
Yellow = watch
Red = root-cause review required
```

## Step 7: Dashboard Design

Return four dashboards:

| Dashboard | Required widgets |
|---|---|
| Business | new orders today, completed orders today, revenue, gross margin, satisfaction, alerts |
| Process | avg response time, avg dispatch time, avg completion time, overdue orders, rework, waiting materials |
| Quality | classification accuracy, dispatch accuracy, quote error, evidence completeness, SOP hit rate, complaint rate |
| Worker | location, active orders, completed orders, on-time rate, score, empty-run rate |

Every dashboard metric must trace to a table field.

## Step 8: Root-Cause Analysis

For each red metric, use fishbone categories:

| Category | Questions |
|---|---|
| People | wrong skill, unclear customer service note, customer unavailable |
| Machine | tool missing, test device failure, no system reminder |
| Material | stockout, wrong part, unavailable consumable |
| Method | unclear SOP, bad dispatch rule, quote approval too slow |
| Environment | route too far, weather, access restriction |
| Measurement | missing start time, no acceptance standard, incomplete data |

Then run 5 Why until the countermeasure changes a rule, SOP, field, training item, or control threshold.

## Step 9: Work-Order State Flow

Use this default state machine:

```text
submitted
  -> classified
  -> data_needed
  -> dispatch_recommended
  -> quote_drafted
  -> quote_approved
  -> assigned
  -> in_progress
  -> evidence_uploaded
  -> quality_review
  -> customer_acceptance
  -> closed
```

Exception states:

```text
waiting_customer
waiting_material
worker_rejected
quote_rejected
rework_required
cancelled
escalated
```

## Step 10: Output Format

Return:

```markdown
## AI Six Sigma Property OS Memo

Business objective:
MVP scope:
Human approval boundaries:

### Pyramid Model
...

### DMAIC Workflow
| Phase | Action | Data | Owner | Gate |

### Ontology
| Object | Required fields | Why it matters |

### CTQ Scorecard
| Goal | Metric | Formula | Green | Yellow | Red |

### Agent Team
| Agent | Input | Action | Output | Human gate |

### Work-Order State Flow
...

### Core Tables
...

### Dashboards
...

### MVP Roadmap
Phase 1:
Phase 2:
Phase 3:

### Risks and Controls
...
```

## Quality Gates

- [ ] MVP is limited to work orders, workers, quotes, evidence, and quality dashboard unless the user explicitly asks to expand.
- [ ] Each CTQ metric has a formula or data source.
- [ ] Each agent has a bounded input, output, and human gate.
- [ ] Quote, dispatch exception, safety, compliance, customer privacy, and payment-impacting steps keep human approval.
- [ ] Root-cause analysis ends in a rule, SOP, field, training item, threshold, or owner; not just commentary.
- [ ] The output separates current facts from assumptions and missing data.
