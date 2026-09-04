# مسیر یادگیری — AI Workspace (عمیق، کم‌درس)

هدف نهایی: **AI Workspace شبیه Notion** + **AI Browser Agent**.  
با **۸ درس** (نه ۱۳+) به MVP می‌رسی — هر درس = چند ساعت کار عمیق، نه یک مفهوم سطحی.

## قانون طلایی

| کجا | چه کار می‌کنی |
|------|----------------|
| **Colab** | مدل، LoRA، RAG، eval، prompt |
| **همین ریپو (لوکال)** | UI، FastAPI، Playwright Browser Agent |

هر درس: **چرا (تئوری) → کد → تمرین → اتصال به محصول → journal**.

---

## نقشهٔ ۸ درس → محصول

| # | درس | خروجی محصول | زمان تقریبی |
|---|-----|-------------|-------------|
| **00** | Setup Colab | محیط آماده | ۱–۲ ساعت |
| **01** | LLM + Prompt + JSON | دکمه Rewrite/Summarize + قرارداد ویرایش بلاک | ۴–۶ ساعت |
| **02** | Dataset + LoRA | مدل با لحن/فرمت ورک‌اسپیس خودت | ۴–۶ ساعت |
| **03** | RAG | «Ask workspace» با citation | ۴–۶ ساعت |
| **04** | FastAPI | `/ai/complete`, `/ai/rag`, `/pages` | ۳–۵ ساعت |
| **05** | UI ورک‌اسپیس | صفحه، بلاک، AI panel | ۴–۶ ساعت |
| **06** | Browser Agent | URL → خلاصه → صفحه Research | ۴–۶ ساعت |
| **07** | Eval + MVP Demo | دمو یکپارچه + README | ۳–۴ ساعت |

```
صفحات/بلاک‌ها     ← 04, 05
AI روی سند        ← 01, 02
RAG               ← 03, 04
Browser Agent     ← 06
کیفیت/دمو         ← 07
```

---

## Lesson 00 — Setup ✓

- فایل: [`notebooks/00_colab_setup.ipynb`](../notebooks/00_colab_setup.ipynb)
- GPU، پکیج‌ها، Drive، tokenizer smoke test

---

## Lesson 01 — LLM، Prompt Engineering، Structured Output ← **الان**

- فایل: [`notebooks/01_llm_inference.ipynb`](../notebooks/01_llm_inference.ipynb)
- **یک درس عمیق** که قبلاً ۳ درس جدا بود (inference + prompt + JSON)

### بخش‌های درس
1. **مدل چطور کار می‌کند** — next-token prediction، autoregressive
2. **Tokenizer** — token، BPE، هزینه/latency، context window
3. **Chat template** — system/user/assistant، فرمت Qwen
4. **Generation** — temperature، top_p، max_tokens، stop
5. **Prompt engineering** — system prompt، few-shot، anti-patterns
6. **Structured output** — JSON schema، parse، retry
7. **قرارداد محصول** — `{action, block_id, content}`
8. **اندازه‌گیری** — tokens/sec، VRAM

### تمرین‌ها
- ۳ prompt برای rewrite + مقایسه
- ۱ prompt برای summarize
- ۱ prompt برای JSON معتبر (rewrite/split action)
- یادداشت در `docs/journal.md`

**بعد از Lesson 01 → Lesson 02 (LoRA).**

---

## Lesson 02 — Dataset + LoRA (ادغام دیتاست + fine-tune)

- فایل: `notebooks/02_lora_workspace.ipynb` *(بعد از اتمام 01 ساخته می‌شود)*
- instruction format (JSONL)، کیفیت > کمیت، ۵۰+ نمونه workspace
- LoRA/PEFT روی Colab، checkpoint روی Drive
- قبل/بعد روی ۱۰ سناریوی واقعی
- اتصال: مدل سفارشی در `packages/ai-core`

---

## Lesson 03 — RAG (ادغام embedding + retrieval + generate)

- فایل: `notebooks/03_rag_workspace.ipynb`
- chunking، metadata (page_id, block_id)، embedding
- retrieve → augment → generate → cite
- تمرین: «Ask workspace» با `sources: [page_id]`
- اتصال: endpoint `/ai/rag` در API

---

## Lesson 04 — FastAPI محصول

- فایل: `notebooks/04_api_product.ipynb` + [`apps/api`](../apps/api)
- قرارداد REST، in-memory → بعداً DB
- Colab یا curl → API لوکال
- wiring به `packages/ai-core`

---

## Lesson 05 — UI شبیه Notion

- مسیر: [`apps/web`](../apps/web)
- sidebar، صفحه، بلاک، انتخاب متن → AI panel
- Rewrite / Summarize / Ask workspace

---

## Lesson 06 — Browser Agent → Workspace

- فایل: `notebooks/06_browser_agent.ipynb` + [`packages/browser-agent`](../packages/browser-agent)
- mock در Colab، Playwright واقعی لوکال
- observe → think → act، tools: goto/click/extract
- نتیجه → صفحه Research جدید

---

## Lesson 07 — Eval + MVP Demo Day

- فایل: `notebooks/07_eval_mvp.ipynb`
- eval set ثابت (`data/evals/`)، hallucination RAG، token/latency
- چک‌لیست MVP:
  - [ ] ساخت/ویرایش صفحه
  - [ ] AI rewrite / summarize
  - [ ] Ask workspace با citation
  - [ ] Browser Agent → صفحه جدید
  - [ ] README دمو

---

## مدل‌های پیشنهادی (Colab T4)

| کار | مدل |
|-----|-----|
| Inference + LoRA | `Qwen/Qwen2.5-1.5B-Instruct` |
| Embedding | `sentence-transformers/all-MiniLM-L6-v2` |
| کیفیت بالاتر (اختیاری) | API مدل بزرگ کنار مدل لوکال |

---

## ریتم هر درس (۴–۶ ساعت)

1. markdown «چرا» را **بخوان** (۱۵–۳۰ دقیقه)
2. همه cellها را **اجرا** کن
3. تمرین‌ها را **تمام** کن — بدون تمرین درس تمام نیست
4. اگر گفت sync به ریپو → `packages/` یا `apps/`
5. یک پارagraph در `docs/journal.md`

---

## الان چه کار کنی؟

1. [`notebooks/01_llm_inference.ipynb`](../notebooks/01_llm_inference.ipynb) را در Colab باز کن
2. **همه بخش‌ها** را بخوان و اجرا کن (این درس طولانی‌تر است — عادی است)
3. تمرین‌ها + JSON structured output را تمام کن
4. بگو **«درس 01 تمام»**
