# gen-ai-fundamentals

Core Gen AI concepts implemented as standalone projects: retrieval-augmented
generation, semantic search, structured-output generation, and a
from-scratch conversational interface. Each project folder is self-contained
with its own README covering architecture, setup, and how it works.

## Projects

| # | Project |
|---|---|
| 01 | [Smart Q&A Bot](./Smart%20Q%26A%20Bot) |
| 02 | [Automated Report Generator with Structured Output](./Automated%20Report%20Generator) |
| 03 | [Semantic Search over a Custom Dataset](./Semantic%20Search%20Over%20Dataset) |
| 04 | [PDF Q&A System using RAG Pipeline](./PDF%20Q%26A%20Rag%20System) |
| 05 | [ChatGPT-like Chat UI from Scratch](./ChatGPT%20UI) |

## Tech stack

| Category | Tools |
|---|---|
| Language | Python |
| LLM providers | OpenAI API (`gpt-4o-mini`), Ollama (`llama3`, `llama3.2:1b`, `nomic-embed-text`) |
| Backend / interface | FastAPI, uvicorn, pydantic, python-dotenv, vanilla HTML/CSS/JS |
| Retrieval / embeddings | ChromaDB, sentence-transformers (`BAAI/bge-small-en-v1.5`), scikit-learn, PyMuPDF (`fitz`) |
| Data | pandas, numpy |

## License

MIT — see [LICENSE](./LICENSE).