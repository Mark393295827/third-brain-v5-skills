---
name: knowledge-ops
description: Manage a multi-layered knowledge system — ingest, organize, deduplicate, vectorize, sync, and retrieve across wiki files, vector DB, memory, and external stores. Use when the user wants to save, organize, sync, search, or scale their knowledge base.
version: "1.3"
updated: "2026-05-27"
assumes: "A wiki or knowledge base already exists and needs organization, sync, retrieval, or scale."
conflicts_with: "Do not modify immutable sources; use wiki-ingest for new source capture and wiki-lint for health reports."
---

# Knowledge Operations

Manage a multi-layered knowledge system for ingesting, organizing, syncing, vectorizing, and retrieving knowledge across multiple stores.

## Usage Template

**Prompt**
```text
Use knowledge-ops to organize this knowledge base. Deduplicate, classify, sync, and prepare semantic retrieval.
```

**Use Case**
- Scaling from a small wiki to a multi-layer knowledge system with search, memory, and vector storage.

**Expected Result**
- The agent proposes or runs organization, deduplication, vector sync, and retrieval steps.

**Output Example**
- A sync report listing indexed notes, duplicates, skipped files, merge candidates, and retrieval test queries.

**Verification Case**
- The output reports what was indexed, skipped, merged, or flagged for manual review.

**Verified Effect**
- A growing wiki becomes searchable, deduplicated, and ready for semantic retrieval.

## Success Metrics

- Report states files indexed, skipped, deduplicated, merged, or flagged for review.
- At least one retrieval test query demonstrates the organized knowledge can be found.
- No immutable source file is modified during organization.
- Duplicate sources, weak links, provenance debt, and stale metadata are separated into reviewable queues instead of silently merged or invented.
- Retrieval preserves the LLM Wiki pattern: Markdown source/concept pages are primary, vector search is optional acceleration.

## When to Use

- User wants to "save this to my knowledge base"
- Syncing knowledge across systems (wiki, memory, vector DB, git repos)
- Deduplicating or organizing existing knowledge
- User asks "what do I know about X?" (semantic search)
- User says "sync", "organize", "deduplicate", "vectorize"
- Knowledge base is growing beyond ~300 nodes and manual navigation is slowing down

---

## Knowledge Layers

Resolve wiki and system paths from `system/config.md` when available. If no config exists, default to `wiki/`, `sources/`, `maps/`, and `system/`.

### Layer 1: Active Execution Truth
- GitHub issues, PRs, Linear tasks — current operational state
- Rule: if it affects an active plan or release, put it here first

### Layer 2: Quick Access Memory
- Agent-specific memory files (e.g., `~/.claude/projects/*/memory/`)
- Markdown with frontmatter — user preferences, feedback, project context
- Automatically loaded at session start

### Layer 3: Durable Wiki
- Curated, interlinked wiki pages (concepts, entities, outputs)
- The canonical store for long-term knowledge
- Cross-referenced with `[[wikilinks]]`

### Layer 4: Vector Store (Optional RAG Support) ⭐
- **ChromaDB** (local, no API key needed) or any vector DB
- Enables **semantic search** across hundreds of nodes
- Embeddings generated locally via `sentence-transformers` (free)
- Automatic sync with wiki on every ingest

Karpathy-style rule: do not let vector search become the knowledge base. Use vectors to find pages; use Markdown to hold understanding, provenance, connections, and review queues.

---

## Vector Store Setup (Local, Free)

### Recommended Stack

| Component | Tool | Cost | Why |
|-----------|------|:----:|-----|
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) | Free | Local, 384-dim, fast |
| Vector DB | ChromaDB | Free | Local, persistent, simple API |
| Sync Trigger | Watchdog (file monitoring) | Free | Auto-index on file change |

### Quick Start

```bash
pip install chromadb sentence-transformers watchdog
```

### Sync Script Structure

```python
# sync_wiki_to_vector.py — run on ingest or periodically

from sentence_transformers import SentenceTransformer
import chromadb
import os, glob, hashlib

# Initialize
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./vector_store")
collection = client.get_or_create_collection("wiki")

def sync_wiki():
    wiki_dir = os.environ.get("WIKI_DIR", "wiki")
    files = glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True)
    for f in files:
        with open(f, "r") as fh:
            content = fh.read()
        doc_id = hashlib.sha256(f.encode()).hexdigest()[:16]
        # Check if already indexed (by hash)
        existing = collection.get(ids=[doc_id])
        if existing["ids"]:
            continue
        # Embed and store
        embedding = model.encode(content[:5000]).tolist()
        collection.add(
            documents=[content[:5000]],
            embeddings=[embedding],
            ids=[doc_id],
            metadatas=[{"path": f, "updated": os.path.getmtime(f)}]
        )

def semantic_search(query, k=5):
    q_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[q_embedding], n_results=k)
    return results
```

### Auto-Sync with Watchdog

```python
# auto_watch.py — runs in background
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WikiSyncHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            sync_wiki()  # re-index changed file

observer = Observer()
observer.schedule(WikiSyncHandler(), path="./wiki", recursive=True)
observer.start()
```

---

## Ingestion Workflow

### 1. Classify
| Type | Primary Store | Secondary |
|------|--------------|-----------|
| Business decision | Memory (project) | Wiki decision log |
| Personal preference | Memory (user) | — |
| Reference info | Memory (reference) | Wiki concept page |
| Research output | Wiki outputs/ | Memory summary |
| Session knowledge | Session-learn extraction | Wiki concepts/entities |

### 2. Deduplicate
- Search existing knowledge before creating
- Check wiki concepts, entities, and memory for duplicates
- **Vector search** across knowledge base for semantic duplicates
- Treat duplicate clippings and secondary summaries as provenance variants: link them to the canonical source unless they add unique block refs or evidence.
- Do not merge primary filings, interviews, and local synthesis reports into one source; preserve evidence hierarchy.

### 3. Store
- Write to the appropriate layer
- If wiki page created/updated → **trigger vector sync** (auto or manual)
- Update summaries and indexes
- Cross-reference with `[[wikilinks]]`

### 4. Retrieve (Semantic Search)
When user asks "what do I know about X":
1. Start with exact filename / wikilink / `rg` search over Markdown.
2. Use ChromaDB or semantic search only when lexical search misses likely concepts.
3. Return matched wiki paths + relevance scores or match reasons.
4. Load top-3 files into context (respecting token budget).
5. Prefer compiled concept/entity pages over raw source notes unless provenance is disputed.

### 5. Verify
- Confirm stored knowledge can be retrieved
- Check that links resolve correctly
- Verify vector search returns relevant results
- Confirm P0/P1 wiki health remains clean after organization: no source-ref breaks, empty pages, or newly orphaned wiki nodes

---

## Review Queues

Use explicit queues for knowledge debt:

| Debt type | Queue action |
|---|---|
| Weak concept/entity link | decide create page, redirect, relabel, or ignore as example text |
| Duplicate source | choose canonical source and keep provenance note if useful |
| Missing source hash/source_id | recover original file/URL before filling |
| Single-source claim now has more evidence | upgrade evidence level only after source refs are attached |
| Fast-changing product/finance claim | schedule primary-source or current-doc verification |
| V5 structure debt | batch by MOC priority rather than rewriting the whole vault |
| Reusable agent workflow | extract to existing skill/SOP if it has objective, constraints, failure modes, verification, and write-back |

## AutoResearch Boundary

Allow autonomous knowledge improvement loops only when:

- the metric is objective, such as broken-source-ref count, orphan count, missing frontmatter count, or retrieval hit rate
- the check is cheap and repeatable
- sources remain immutable
- every auto-fix is reviewable in git or a lint report

If the target is interpretive quality, strategy, taste, or claim confidence, use a supervised review queue instead.

---

## Quality Gates

- [ ] Knowledge classified to correct layer
- [ ] No duplicates created (searched first + vector checked)
- [ ] Vector store in sync with wiki (auto or batch)
- [ ] Index/summary updated
- [ ] Cross-references added
- [ ] Verification: knowledge is retrievable (file + vector)
- [ ] Knowledge debt queued with clear next action
- [ ] Markdown-first retrieval path tested before vector-only retrieval
