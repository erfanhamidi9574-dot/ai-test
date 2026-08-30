# مسیر یادگیری — AI Workspace (گام‌به‌گام با Colab)

هدف نهایی: یک **AI Workspace شبیه Notion** + **AI Browser Agent**.  
با یک ماه وقت، به نسخهٔ MVP قابل‌دمو می‌رسی؛ عمق پژوهشی را عمداً کنار می‌گذاریم.

## قانون طلایی

| کجا | چه کار می‌کنی |
|------|----------------|
| **Colab** | inference، LoRA، RAG، eval، prompt |
| **همین ریپو (لوکال)** | UI ورک‌اسپیس، FastAPI، Playwright Browser Agent |

هر درس: **چرا → کد → تمرین → اتصال به محصول**.

---

## نقشهٔ محصول → درس‌ها

```
صفحات و بلاک‌ها          ← Lesson 08+ (apps/web)
AI روی سند               ← Lesson 02–04
RAG روی دانش ورک‌اسپیس   ← Lesson 05–06
مدل سفارشی دامنه         ← Lesson 03–04
API محصول                ← Lesson 07
Browser Agent            ← Lesson 09–10
ارزیابی و سرو            ← Lesson 06, 11
MVP یکپارچه              ← Lesson 12
```

---

## فاز ۰ — آماده‌سازی (روز ۱)

### Lesson 00 — محیط Colab و ریپو
- فایل: [`notebooks/00_colab_setup.ipynb`](../notebooks/00_colab_setup.ipynb)
- یاد می‌گیری: GPU در Colab، کلون ریپو، نصب پکیج، ذخیره روی Drive
- خروجی: یک cell که `torch.cuda.is_available()` را چاپ می‌کند

**Lesson 00 تمام ✓ — برو Lesson 01.**

---

## فاز ۱ — مغز AI (هفته ۱) — فقط Colab

### Lesson 01 — اولین تماس با LLM ← **الان اینجا**
- فایل: [`notebooks/01_llm_inference.ipynb`](../notebooks/01_llm_inference.ipynb)
- مفاهیم: tokenizer، chat template، temperature، max_tokens، system prompt
- تمرین: ۳ prompt برای «بازنویسی بلاک Notion» بنویس و مقایسه کن
- اتصال محصول: هستهٔ `packages/ai-core` بعداً همین الگو را دارد

### Lesson 02 — Structured output برای Workspace
- فایل: `notebooks/02_structured_output.ipynb`
- مفاهیم: JSON schema، tool/function calling سبک، ویرایش بلاک به‌صورت `{action, block_id, content}`
- تمرین: مدل را وادار کن خروجی فقط JSON معتبر بدهد
- اتصال محصول: دستورات AI روی صفحه (rewrite / summarize / split)

### Lesson 03 — دیتاست دامنهٔ Workspace
- فایل: `notebooks/03_dataset_for_workspace.ipynb`
- مفاهیم: instruction tuning format، کیفیت داده > کمیت
- تمرین: ۵۰ نمونه JSONL برای کارهای ورک‌اسپیس (خلاصه، عنوان، تبدیل bullet، استخراج action item)
- داده نمونه: `data/samples/`

### Lesson 04 — LoRA fine-tune روی Colab
- فایل: `notebooks/04_lora_finetune.ipynb`
- مفاهیم: LoRA/PEFT، overfitting، checkpoint، مقایسه قبل/بعد
- تمرین: مدل کوچک (مثلاً Qwen2.5-1.5B یا معادل) را LoRA کن و ۱۰ سؤال را ارزیابی کن
- اتصال محصول: مدل سفارشی برای لحن/فرمت ورک‌اسپیس خودت

---

## فاز ۲ — دانش ورک‌اسپیس (هفته ۲) — Colab + شروع API

### Lesson 05 — Embeddings و Chunking
- فایل: `notebooks/05_embeddings_chunking.ipynb`
- مفاهیم: chunk size، overlap، metadata (page_id, block_id)
- تمرین: چند صفحهٔ نمونه را chunk کن و retrieval دستی بساز

### Lesson 06 — RAG برای Notion-like pages
- فایل: `notebooks/06_rag_workspace.ipynb`
- مفاهیم: retrieve → augment prompt → generate → cite
- تمرین: سؤال بپرس؛ جواب باید `sources: [page_id]` برگرداند
- اتصال محصول: «Ask workspace»

### Lesson 07 — FastAPI به‌عنوان مغز محصول
- فایل: `notebooks/07_api_contract.ipynb` + کد در `apps/api`
- مفاهیم: قرارداد API (`/ai/complete`, `/ai/rag`, `/pages`)
- تمرین: لوکال API را بالا بیاور و از Colab یا curl صدا بزن
- **از اینجا بخشی از کار لوکال است**

---

## فاز ۳ — محصول Workspace (هفته ۳) — لوکال سنگین‌تر

### Lesson 08 — UI شبیه Notion (حداقلی)
- مسیر: `apps/web`
- مفاهیم: صفحه، بلاک متن، sidebar، AI side panel
- تمرین: یک صفحه بساز، انتخاب متن → «Rewrite with AI»

### Lesson 09 — Browser Agent — مبانی
- فایل: `notebooks/09_browser_agent_basics.ipynb` + `packages/browser-agent`
- مفاهیم: ابزارها (goto, click, type, extract)، حلقهٔ observe→think→act
- **توجه:** اجرای واقعی Browser Agent روی ماشین لوکال با Playwright است؛ Colab فقط طراحی agent loop و mock را تمرین می‌کند

### Lesson 10 — Browser Agent → Workspace
- مسیر: `packages/browser-agent` + API
- مفاهیم: نتیجهٔ مرورگر را به‌صورت صفحه/بلاک جدید در ورک‌اسپیس ذخیره کن
- تمرین: «این URL را بخوان و خلاصه را در صفحه Research بگذار»

---

## فاز ۴ — یکپارچه‌سازی و صنعتی‌سازی (هفته ۴)

### Lesson 11 — Eval، هزینه، latency
- فایل: `notebooks/11_eval_and_cost.ipynb`
- مفاهیم: eval set ثابت، hallucination روی RAG، اندازه‌گیری token/latency
- تمرین: harness برای ۱۰ سناریوی ورک‌اسپیس

### Lesson 12 — MVP Demo Day
- چک‌لیست:
  - [ ] ساخت/ویرایش صفحه
  - [ ] AI rewrite / summarize روی بلاک
  - [ ] Ask workspace با citation
  - [ ] یک جریان Browser Agent → صفحه جدید
  - [ ] README دمو + اسکرین‌شات/ویدیو کوتاه

---

## مدل‌های پیشنهادی روی Colab (رایگان/T4)

برای شروع سبک بمان:

| کار | پیشنهاد |
|-----|---------|
| Inference آموزشی | `Qwen/Qwen2.5-1.5B-Instruct` |
| LoRA | همان ۱.۵B یا ۳B اگر GPU آمد |
| Embedding | `sentence-transformers/all-MiniLM-L6-v2` |
| بعداً کیفیت بالاتر | API مدل بزرگ (اختیاری) کنار مدل لوکال |

---

## ریتم پیشنهادی روزانه (۲–۴ ساعت)

1. درس روز را در Colab باز کن  
2. همه cellها را اجرا کن  
3. تمرین‌ها را تمام کن  
4. اگر درس گفت: کد را به `packages/` یا `apps/` منتقل کن  
5. یک خط در `docs/journal.md` بنویس: امروز چه شکست/یادگرفتی

---

## الان چه کار کنی؟

1. [`notebooks/01_llm_inference.ipynb`](../notebooks/01_llm_inference.ipynb) را در Colab باز کن  
2. همه cellها را اجرا کن + تمرین ۳ prompt  
3. بعد از اتمام بگو **«درس 01 تمام»**

رد کردن درس‌ها = سوراخ در محصول نهایی.
