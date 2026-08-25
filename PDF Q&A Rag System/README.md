# PDF Q&A System using RAG Pipeline

A document Q&A system that answers questions grounded strictly in an 
uploaded PDF's content, running the full local Retrieval-Augmented
Generation pattern end-to-end: extract → chunk → embed → store in a vector
DB → retrieve the closest match → check it's actually relevant → generate a
grounded answer.

## Architecture

```
PDF File (sample.pdf)
   |
Text Extraction (PyMuPDF / fitz)
   |
Chunking (split on paragraph breaks)
   |
Embedding (Ollama: nomic-embed-text) -> ChromaDB (local vector store)
   |
User Question
   |
Question Embedding -> Similarity Search (top-1 match)
   |
Relevance Check (keyword overlap between question and retrieved chunk)
   |
   ┌───────────────┴───────────────┐
   |                                |
No overlap                    Overlap found
   |                                |
"Answer not found in document"   Ollama LLM (llama3) -> Grounded Answer
```

## Files

| File | Role |
|---|---|
| `rag3.py` | Everything — PDF extraction, chunking, embedding, vector storage, retrieval, relevance gate, and answer generation |
| `sample.pdf` | The source document to query — must sit alongside the script |

## Setup

1. Install [Ollama](https://ollama.com) and pull both models used:
   ```
   ollama pull nomic-embed-text
   ollama pull llama3
   ```

2. Install dependencies:
   ```
   pip install pymupdf chromadb ollama
   ```

3. Place a PDF named `sample.pdf` in the same folder as the script (or edit
   the filename in the script to point at your own file).

4. Run it:
   ```
   python rag3.py
   ```

5. Enter a question about the PDF when prompted.

## How it works, in plain words

1. **Extract** — The PDF's text is pulled out page by page with PyMuPDF.
2. **Chunk** — The text is split into paragraph-sized pieces so retrieval
   can point at a specific, relevant slice instead of the whole document.
3. **Embed & store** — Each chunk is turned into a vector using Ollama's
   `nomic-embed-text` model and saved into a local ChromaDB collection,
   configured for cosine-similarity search.
4. **Retrieve** — The question is embedded the same way, and ChromaDB
   returns the single most similar chunk.
5. **Check relevance before generating** — Before calling the LLM at all,
   the script checks whether any meaningful word from the question actually
   appears in the retrieved chunk. If nothing overlaps, it short-circuits
   straight to *"Answer not found in document"* — avoiding a wasted
   generation call on an irrelevant match.
6. **Generate** — Only when the relevance check passes is the chunk handed
   to `llama3` with an instruction to answer strictly from that context.

## Cost notes

Runs entirely locally through Ollama and a local ChromaDB instance —
**zero API cost**, no internet connection required after the models are
pulled.