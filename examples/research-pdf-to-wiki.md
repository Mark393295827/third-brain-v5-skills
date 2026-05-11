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
3. one reusable brief in wiki/outputs/
4. verification evidence that links and frontmatter are present
```

## After

The PDF becomes:

- one durable source note
- several concept/entity notes
- one output brief
- a list of open questions for follow-up research

## Output Example

```text
sources/src-20260512-ai-safety-report.md
wiki/concepts/agent-evaluation.md
wiki/entities/anthropic.md
wiki/outputs/ai-safety-brief.md
system/log.md
```

## Verification

The workflow is complete only after the agent checks the new files exist and reports which claims are single-source.
