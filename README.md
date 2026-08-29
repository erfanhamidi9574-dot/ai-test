# AI Workspace

Notion-like **AI Workspace** with an **AI Browser Agent** — built while learning applied ML engineering step by step on **Google Colab**.

## Vision (final product)

| Capability | What it means |
|---|---|
| Workspace | Pages, blocks, nested docs (Notion-like) |
| AI writing | Summarize, rewrite, continue, structured edit on page content |
| Knowledge | RAG over your pages + uploaded docs |
| Browser Agent | AI that opens pages, clicks, extracts, and reports back into the workspace |

This repo is both a **learning curriculum** and the **product codebase**. You do not skip ahead: each lesson unlocks the next piece of the product.

## How to learn (rules)

1. Open the lesson notebook in Colab (links in `docs/LEARNING_PATH.md`).
2. Read the short “Why” section, then run every cell.
3. Complete the **Exercises** before moving on.
4. Sync any reusable code back into `packages/` or `apps/` when the lesson says so.
5. Max ~20% reading / ~80% coding per session.

**Colab** = models, RAG, fine-tuning, eval.  
**Local (this repo)** = workspace UI, API, Browser Agent (Playwright needs a real browser).

## Repo map

```
ai-workspace/
├── docs/                 # Roadmap & theory notes (short)
├── notebooks/            # Colab lessons (open in Colab)
├── apps/
│   ├── web/              # Workspace UI (Notion-like)
│   └── api/              # FastAPI backend
├── packages/
│   ├── ai-core/          # prompts, RAG, model client
│   └── browser-agent/    # Playwright agent tools
├── data/                 # sample docs & eval sets
└── scripts/              # helpers (export notebooks, smoke tests)
```

## Start here

→ Open [`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md) and begin **Lesson 00**.

## Prerequisites

- Google account (Colab)
- Python basics (you have them)
- Optional local: Node 20+, Python 3.11+, Docker

## Status

Curriculum + scaffolds are in place. Product features land lesson-by-lesson.
