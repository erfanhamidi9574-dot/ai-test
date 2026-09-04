# Product Vision — AI Workspace

## One-liner
A **Notion-like workspace** where AI edits your pages, answers from your knowledge, and can **browse the web** as an agent that writes results back into the workspace.

## MVP (end of 8 deep lessons, ~3–4 weeks)

Must demo:

1. **Pages + blocks** — create a page, edit paragraph blocks  
2. **AI on selection** — rewrite / summarize a block  
3. **Ask workspace** — RAG over pages with source citations  
4. **Browser Agent (narrow)** — given a URL, extract main text → create a Research page  

## Explicit non-goals (month 1)

- Training a foundation model from scratch  
- Full Notion parity (databases, permissions, realtime collab)  
- Production multi-tenant SaaS hardening  

## Architecture (target)

```
apps/web  ──►  apps/api  ──►  packages/ai-core (LLM + RAG)
                    │
                    └──►  packages/browser-agent (Playwright tools)
```

- **Colab**: train/experiment (LoRA, RAG prototypes, eval)  
- **Local**: UI + API + real browser agent  

## Success metric for learning

You can explain and change every layer you ship — not only call an API.
