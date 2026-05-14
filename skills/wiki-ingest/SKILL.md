---
name: wiki-ingest
description: Ingest sources (articles, PDFs, videos, notes) into a persistent interlinked knowledge wiki. Creates source notes, entity pages, concept pages, and updates navigation. Based on the STOW (Source → Think → Organize → Write) pattern.
version: "1.2"
updated: "2026-05-13"
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
- `sources/src-YYYYMMDD-title.md`, `wiki/concepts/concept-name.md`, `wiki/entities/entity-name.md`, and `system/log.md` update.

**Verification Case**
- New wiki pages have frontmatter, source references, at least two `[[wikilinks]]`, and timeline entries.

**Verified Effect**
- Knowledge stops being a loose summary: the source becomes traceable, linked, and reusable across future sessions.

**V5.2 Closure Add-on**
- Classify every input as `external-fact`, `human-experience`, `internal-state`, or `environment-signal`.
- For high-value ingests, decide whether to create one behavior experiment and one creativity experiment.
- Record governance risks: single-source claims, missing provenance, stale-page risk, and review queue items.

## When to Use

- User drops a file and says "ingest this"
- User shares a link/article/video/PDF to be processed
- User says "add this to the wiki" or "save this to my knowledge base"
- User mentions a source that should be captured

## Workflow

### Step 1: Capture

Create an immutable source note in `sources/`:

```markdown
---
source_id: "src-YYYYMMDD-short-slug"
title: "Original Source Title"
author: ""
url: ""
created_at: "YYYY-MM-DD"
captured_at: "YYYY-MM-DDTHH:MM:SS"
source_type: "article | book | video-transcript | paper | conversation"
trust_level: "1-unverified | 2-expert-source"
hash: "sha256-16char"
status: "raw | ingested"
---
```

**Rules:**
- Never modify source files after creation
- Extract 3-7 Key Insights with block refs (`^ki-short-name`)
- Flag single-source claims with `> [!warning] Single source`
- Assign an input class: `external-fact | human-experience | internal-state | environment-signal`

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

### Step 4: Update Navigation

1. Update the wiki overview / living synthesis
2. Update the central index
3. Update relevant MOC (map of content) pages

### Step 5: Convert to Behavior / Creativity When Warranted

After a high-value ingest, run these checks:

| Check | Create / Update |
|-------|-----------------|
| The source implies a habit, action, identity shift, pain point, or repeated decision | `08_behaviors/action-sops/` or `08_behaviors/reviews/` |
| The source suggests a product, content asset, analogy, cross-domain pattern, or minimum test | `09_creativity/experiments/` |
| The source contains single-source claims, missing provenance, or stale-page risk | `system/governance-dashboard.md` or review queue |

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

Append to `system/log.md` with:
- Source ingested
- Entity pages created/updated
- Concept pages created/updated
- Maps updated
- Behavior / creativity experiments created or explicitly skipped
- Governance risks recorded

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
