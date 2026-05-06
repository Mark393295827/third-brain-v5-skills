---
name: knowledge-ops
description: Manage a multi-layered knowledge system — ingest, organize, deduplicate, vectorize, sync, and retrieve across wiki files, vector DB, memory, and external stores. Use when the user wants to save, organize, sync, search, or scale their knowledge base.
---

# Knowledge Operations

Manage a multi-layered knowledge system for ingesting, organizing, syncing, vectorizing, and retrieving knowledge across multiple stores.

## When to Use

- User wants to "save this to my knowledge base"
- Syncing knowledge across systems (wiki, memory, vector DB, git repos)
- Deduplicating or organizing existing knowledge
- User asks "what do I know about X?" (semantic search)
- User says "sync", "organize", "deduplicate", "vectorize"
- Knowledge base is growing beyond ~300 nodes and manual navigation is slowing down

---

## Knowledge Layers

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

### Layer 4: Vector Store (RAG) ⭐
- **ChromaDB** (local, no API key needed) or any vector DB
- Enables **semantic search** across hundreds of nodes
- Embeddings generated locally via `sentence-transformers` (free)
- Automatic sync with wiki on every ingest

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
    files = glob.glob("wiki/**/*.md", recursive=True)
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

### 3. Store
- Write to the appropriate layer
- If wiki page created/updated → **trigger vector sync** (auto or manual)
- Update summaries and indexes
- Cross-reference with `[[wikilinks]]`

### 4. Retrieve (Semantic Search)
When user asks "what do I know about X":
1. Encode query with `sentence-transformers`
2. Search ChromaDB for top-5 matches
3. Return matched wiki paths + relevance scores
4. Load top-3 files into context (respecting token budget)

### 5. Verify
- Confirm stored knowledge can be retrieved
- Check that links resolve correctly
- Verify vector search returns relevant results

---

## Quality Gates

- [ ] Knowledge classified to correct layer
- [ ] No duplicates created (searched first + vector checked)
- [ ] Vector store in sync with wiki (auto or batch)
- [ ] Index/summary updated
- [ ] Cross-references added
- [ ] Verification: knowledge is retrievable (file + vector)
