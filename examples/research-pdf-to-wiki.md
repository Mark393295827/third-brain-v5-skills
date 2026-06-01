# Workflow: Research PDF to Wiki Brief

## Before

A PDF contains useful ideas, but the knowledge is trapped in one long file. The user wants reusable concepts, not a one-time summary.

## Input

```text
Source: a PDF, report, paper, book chapter, or long-form article.
Goal: convert the document into source notes, concept pages, and one reusable brief.
```

## Prompt

```text
Use wiki-ingest and cognitive-compile on this PDF.

First ingest the PDF into my wiki with source notes, concept pages, entity pages, and navigation updates.
Then run a cognitive compile on the strongest concept from the PDF.

Final output:
1. created/updated file list
2. 5 key insights with citations
3. one reusable brief in `OUTPUTS_DIR` (default: `wiki/outputs/`)
4. verification evidence that links and frontmatter are present
5. single-source claims and unresolved evidence gaps
```

## After

The PDF becomes:

- one durable source note
- several concept/entity notes
- one output brief
- a list of open questions for follow-up research

For unanswered external questions, run `deep-research` after ingest and ask for a source ledger, claim ledger, activity trace, and STOW handoff packet before adding new claims to the wiki.

## Output Example

```text
SOURCES_DIR/src-20260512-ai-safety-report.md
CONCEPTS_DIR/agent-evaluation.md
ENTITIES_DIR/anthropic.md
OUTPUTS_DIR/ai-safety-brief.md
LOG_FILE
```

## Verification

The workflow is complete only after the agent resolves paths from `system/config.md`, checks the new files exist, satisfies the `wiki-ingest` and `cognitive-compile` success metrics, and reports which claims are single-source.
