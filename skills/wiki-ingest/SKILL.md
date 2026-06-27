---
name: wiki-ingest
description: Ingest articles, PDFs, videos, transcripts, and notes into a persistent interlinked knowledge wiki and V6 knowledge operating system. Use when the user wants source notes, entity pages, concept pages, navigation updates, STOW processing, Obsidian provenance, clipping lifecycle handling, or supervised promotion of source-derived insights into skills, SOPs, schemas, daily loops, or governance queues.
version: "6.0"
updated: "2026-06-27"
assumes: "Vault paths are resolved from system/config.md when present; otherwise default STOW paths are used."
conflicts_with: "Do not run bulk deduplication or vector sync here; use knowledge-ops after source capture."
---

# Wiki Ingest

Ingest a source document into the knowledge wiki — creating structured, interlinked pages that compound over time.

## Usage Template

**Prompt**
```text
Use wiki-ingest on this source. Create source notes, concept pages, entity pages, navigation updates, and a verification summary.
```

**Use Case**
- Turning an article, PDF, transcript, or rough note into durable linked knowledge.

**Expected Result**
- The agent creates an immutable source note, 3-7 key insights, linked wiki pages, and a log entry.

**Output Example**
- `SOURCES_DIR/src-YYYYMMDD-title.md`, `CONCEPTS_DIR/concept-name.md`, `ENTITIES_DIR/entity-name.md`, and `LOG_FILE` update.

**Verification Case**
- New wiki pages have frontmatter, source references, at least two `[[wikilinks]]`, and timeline entries.

**Verified Effect**
- Knowledge stops being a loose summary: the source becomes traceable, linked, and reusable across future sessions.

## Success Metrics

- Creates one immutable source note, 3-7 key insights with block refs, and at least one linked wiki page.
- Each new wiki page has frontmatter, source references, at least two wikilinks, and a timeline entry.
- Final report lists created/updated files and flags single-source claims.
- Targeted post-ingest lint confirms no missing frontmatter, broken source refs, zero-inlink pages, or pages with fewer than two outbound wikilinks.
- Clippings are archived after successful ingest and the clipping queue is updated when applicable.
- Each concept page passes the Karpathy understanding gate: one-line thesis, source boundary, mechanism, connections, and what remains uncertain.
- V6 receipt states Trigger, Context, Steering/verification, State/write-back, and whether any rule was queued rather than promoted.

**V5.2 Closure Add-on**
- Classify every input as `external-fact`, `human-experience`, `internal-state`, or `environment-signal`.
- For high-value ingests, decide whether to create one behavior experiment and one creativity experiment.
- Record governance risks: single-source claims, missing provenance, stale-page risk, and review queue items.

**V6 Knowledge OS Add-on**
- Treat `input-skills-obsidian` as the fast front door and this skill as the durable compiler.
- Use Trigger -> Context -> Steering -> State before writing:
  - Trigger: user request, clipping queue, file drop, scheduled daily note, or research handoff.
  - Context: source boundary, existing wiki pages, relevant maps, and only the rules needed now.
  - Steering: source-risk label, human review boundary, independent verification, and stop condition.
  - State: source note, wiki pages, maps, log, dashboard queue, or skill/SOP promotion candidate.
- Promote an insight into a skill, SOP, schema rule, or automation only after repeated support or local verification, bounded macro-action shape, no provenance relaxation, and a cheap check.
- Prefer zero-overhead context: do not preload broad maps, whole reports, or historical summaries unless the current ingest needs them.

## When to Use

- User drops a file and says "ingest this"
- User shares a link/article/video/PDF to be processed
- User says "add this to the wiki" or "save this to my knowledge base"
- User mentions a source that should be captured

## Workflow

### Step 0: Resolve Paths

Before writing, read `system/config.md` when available and resolve `SOURCES_DIR`, `CONCEPTS_DIR`, `ENTITIES_DIR`, `MAPS_DIR`, `LOG_FILE`, `BEHAVIORS_DIR`, and `CREATIVITY_DIR`. If no config exists, use the default STOW layout.

### Step 0A: Define the Ingest Macro Action

Treat each ingest as an agentic macro action:

```text
Objective:
Trigger:
Source boundary:
Owned vault paths:
Expected source note:
Expected wiki updates:
Verification evidence:
State / write-back:
Non-goals:
Stop condition:
```

Do not start a broad autonomous expansion unless the source has objective metrics and cheap verification. Otherwise ingest once, record uncertainty, and queue follow-up research.

### Step 1: Capture

Create an immutable source note in `SOURCES_DIR`:

```markdown
---
source_id: "src-YYYYMMDD-short-slug"
source_date: "YYYY-MM-DD"
source_title: "Original Source Title"
source_author: ""
source_type: "article | book | video-transcript | pdf | epub | notebooklm-mediated | local-synthesis | primary-filing | company-interview"
source_url: ""
input_class: "external-fact | human-experience | internal-state | environment-signal"
created: "YYYY-MM-DD"
knowledge_stage: captured
evidence_level: "single-source | multi-source | curated-map"
trust_level: "1-unverified | 2-expert-source | 3-primary-source"
hash: "sha256-16char"
status: "raw | ingested"
---
```

**Rules:**
- Never modify source files after creation
- Extract 3-7 Key Insights with block refs (`^ki-short-name`)
- Flag single-source claims with `> [!warning] Single source`
- Assign an input class: `external-fact | human-experience | internal-state | environment-signal`

### Step 1A: Classify Source Risk

Use a source-risk label before writing claims:

| Source type | Default evidence | Required caution |
|---|---|---|
| primary filing / official docs | high | still check date, draft/final status, and missing fields |
| article / book / transcript | medium | mark author perspective and single-source claims |
| founder / company / investor interview | medium-low | treat metrics, adoption, roadmap, and performance as self-reported |
| NotebookLM-mediated source | low | state that the original transcript/source is not fully archived |
| local synthesis / PDF stack | low | treat as secondary-source synthesis; do not promote numbers without primary refs |
| fast-changing financial/product claim | low | add review queue item for current docs or filings |

If a clipping duplicates an existing source, create or update provenance only when it adds useful block refs; otherwise link to the canonical source and log the duplicate.

### Step 2: Auto-create Entity Pages

For every person, company, product, or project mentioned in the source:

```markdown
---
tags:
  - domain/strategy
  - type/entity
type: entity
status: seed
created: "YYYY-MM-DD"
knowledge_stage: single-source
evidence_level: single-source
---

# Entity Name
```

- Check if entity page already exists → update if needed
- Use consistent naming (English for global entities, Chinese for local)

### Step 3: Create/Update Concept Pages

For every key concept, framework, or methodology:

- Check if concept page already exists
- If exists: add new source reference, flag contradictions
- If new: create with `status: seed`, ≥2 `[[wikilinks]]`, `knowledge_stage: single-source`

**Standardized page structure** (all concept pages should follow this pattern):

```markdown
# Title

> Core thesis in one line — what is the single most important thing to know?
> (Source: [[source]])

---

## Core Mechanism

ASCII diagram showing causal relationships.

## Classifications / Comparisons

Tables comparing with related frameworks.

## Key Data (if applicable)

Bulleted list of critical numbers.

## Implications / Applications

What this means for decision-making.

## Connections

- Related concepts with brief explanation of relationship
- Source references

---

## Evolution Timeline

- **YYYY-MM-DD**：Created.
```

**Rules:**
- Start every page with a **quote block** that captures the core thesis
- Use **ASCII diagrams** for mechanisms (causal chains)
- Use **tables** for comparisons (frameworks, classifications, data)
- End with **connections** (grouped wikilinks) + **evolution timeline** (separated by `---`)

**Karpathy understanding gate:**

Before writing a concept page, answer:

```text
Core thesis: What changed in my understanding?
Mechanism: What causes what?
Boundary: What is this source allowed to prove?
Counterpoint: What could make this wrong?
Reusable bit: Is this a concept, SOP, skill, decision rule, or review item?
```

The page should compile understanding for humans and agents. Do not store a long summary that future agents must re-understand from scratch.

### Step 4: Update Navigation

1. Update the wiki overview / living synthesis
2. Update the central index
3. Update relevant MOC (map of content) pages
4. Update source batch index when the source starts or extends a topic batch
5. For Web Clipper inputs, move the processed clipping to `Clippings/archive/` and update `Clippings/README.md` if that queue exists
6. If ingest came from the daily knowledge loop, update only the supervised KR evidence section or log entry; do not rewrite the automated snapshot block.

### Step 5: Convert to Behavior / Creativity When Warranted

After a high-value ingest, run these checks:

| Check | Create / Update |
|-------|-----------------|
| The source implies a habit, action, identity shift, pain point, or repeated decision | `BEHAVIORS_DIR/action-sops/` or `BEHAVIORS_DIR/reviews/` |
| The source suggests a product, content asset, analogy, cross-domain pattern, or minimum test | `CREATIVITY_DIR/experiments/` |
| The source contains single-source claims, missing provenance, or stale-page risk | `SYSTEM_DIR/governance-dashboard.md` or review queue |

Behavior experiment minimum fields:
- source concept
- behavior hypothesis
- trigger
- 15-minute action
- success metric
- review date

Creativity experiment minimum fields:
- source ingredients
- combination formula
- target user
- hypothesis
- minimum test
- success signal
- next output

Skill / SOP conversion check:
- If the source teaches a repeatable agent workflow, mark it as a candidate for `skills/`, `commands/`, or `wiki/sops/`.
- Extract only the few "human bits" that matter: objective, constraints, failure modes, verification, and write-back target.
- Do not create a new skill when an existing skill can absorb the rule.
- V6 promotion requires evidence support plus objective check; otherwise write the candidate to governance/review queue instead of changing a skill.

### Step 6: Append Timeline

After updating or creating any wiki page, append a timeline entry at the bottom (below a `---` separator):

```markdown
---

## 演化时间线

- **YYYY-MM-DD**：创建初始版本。
- **YYYY-MM-DD**：更新了关于 X 的理解（来源：[[source]]）。旧观点 Y，新证据表明 Z。
```

**Rules:**
- Content above `---` is **compiled truth** — current best understanding, rewritable
- Content below `---` is the **timeline** — append-only, never edited or deleted
- Add an entry on creation, and every time a core claim changes

### Step 7: Log

Append to `LOG_FILE` with:
- Source ingested
- Entity pages created/updated
- Concept pages created/updated
- Maps updated
- Behavior / creativity experiments created or explicitly skipped
- Governance risks recorded

### Step 8: Targeted Post-Ingest Lint

Before final reporting, run a targeted health check over the files touched:

- source file exists and block refs resolve
- every new/updated wiki page has V6-compatible frontmatter
- every new/updated wiki page has V6-compatible provenance fields when the local schema requires them
- every new/updated wiki page has at least two outbound wikilinks
- every source reference points to an existing source
- every new concept/entity is linked from at least one relevant MOC or page
- no empty files were created
- concept pages pass the understanding gate rather than being raw summaries
- weak links are reported, not auto-created, unless the source clearly defines the concept/entity

For large batches, write or update `system/lint-report.md` with P0/P1 results and queue P2/P3 debt instead of trying to fix all historical structure issues.

## Quality Gates

- [ ] Source note created with frontmatter
- [ ] ≥2 entity pages created or updated
- [ ] ≥1 concept page created or updated
- [ ] Every wiki page has ≥2 `[[wikilinks]]`
- [ ] Navigation (overview + index + maps) updated
- [ ] Behavior conversion assessed
- [ ] Creativity conversion assessed
- [ ] Governance risks recorded
- [ ] Log appended
- [ ] Targeted post-ingest lint completed
- [ ] Clipping archived or left in queue with reason
- [ ] Understanding gate passed for new/updated concepts
- [ ] V6 receipt includes Trigger, Context, Steering/verification, State/write-back, and rule-promotion decision

## Page Format

Every wiki page uses this frontmatter:

```yaml
---
tags: [domain/xxx, type/concept|entity|sop]
type: concept | entity | sop
status: seed | growing | evergreen | stale
created: YYYY-MM-DD
knowledge_stage: captured | stored | cross-checked | applied
evidence_level: single-source | multi-source | curated-map
---
```

## Key Principles

- **Immutable sources**: raw/inbox files are never modified after ingest
- **Compound**: every new source makes the wiki richer
- **Linked**: every page ≥2 outbound `[[wikilinks]]`
- **Sourced**: every claim cites `(Source: [[source-file#^ref]])`
- **Contradictions flagged**: `> [!warning] Contradiction` when sources disagree
- **No fake provenance**: do not invent hashes, source IDs, or primary-source confidence for old or mediated materials
- **Debt is explicit**: weak links, stale metadata, duplicate sources, and fast-changing claims go to lint report or governance queue
- **Markdown first**: durable Markdown pages are the knowledge product; vector search is optional retrieval support, not a substitute for understanding
