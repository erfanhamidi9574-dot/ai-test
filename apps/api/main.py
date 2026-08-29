"""AI Workspace API — scaffold. Grows with lessons 07+."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Workspace API", version="0.1.0")


class Health(BaseModel):
    status: str = "ok"
    product: str = "ai-workspace"


class Block(BaseModel):
    id: str
    type: str = "paragraph"
    content: str = ""


class Page(BaseModel):
    id: str
    title: str
    blocks: list[Block] = Field(default_factory=list)


# In-memory store for early lessons (replaced by DB later)
PAGES: dict[str, Page] = {
    "welcome": Page(
        id="welcome",
        title="Welcome",
        blocks=[
            Block(id="b1", content="This is your Notion-like AI Workspace scaffold."),
            Block(id="b2", content="AI rewrite, RAG, and Browser Agent land lesson-by-lesson."),
        ],
    )
}


@app.get("/health", response_model=Health)
def health() -> Health:
    return Health()


@app.get("/pages/{page_id}", response_model=Page)
def get_page(page_id: str) -> Page:
    if page_id not in PAGES:
        return Page(id=page_id, title="Untitled", blocks=[])
    return PAGES[page_id]


@app.get("/pages", response_model=list[Page])
def list_pages() -> list[Page]:
    return list(PAGES.values())


# /ai/* endpoints arrive in Lesson 07
