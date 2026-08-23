# Smart Q&A Bot

A fast, fully local Q&A assistant that answers user questions grounded in a
defined knowledge base. Reference material is loaded directly into the
prompt context and an on-device LLM generates precise, grounded answers —
giving instant responses with zero API latency and zero API cost.

## Architecture

```
User Question
      |
Reference Knowledge Base (business/domain context)
      |
Prompt Assembly ("Answer using this information: <context> \n Question: <question>")
      |
Ollama LLM (llama3.2:1b)
      |
Answer (printed to console)
```

## Files

| File | Role |
|---|---|
| `faqBot.py` | Everything — input capture, context assembly, LLM call, output |

## Setup

1. Install [Ollama](https://ollama.com) and pull the model:
   ```
   ollama pull llama3.2:1b
   ```

2. Install dependencies:
   ```
   pip install ollama
   ```

3. Run it:
   ```
   python faqBot.py
   ```

4. Type a question when prompted, e.g. *"What are the Riverside store's
   hours?"* or *"Can I return a final sale item?"*

## How it works, in plain words

1. **Ask** — The script takes a question from the terminal.
2. **Ground the model** — A defined knowledge base (here, a full business
   FAQ profile for a fictional outdoor retailer, Larkspur Outfitters —
   store locations, hours, shipping, returns, membership, repairs, and
   employment info) is placed directly in the prompt alongside the
   question, so the model answers from that source rather than from
   general training knowledge.
3. **Generate** — The combined prompt is sent to `llama3.2:1b` via
   `ollama.generate()`.
4. **Answer** — The model responds instantly, fully grounded in the
   supplied knowledge base — no network round-trip, no external vector
   database dependency. Ask about store hours, return policy, membership
   perks, repair pricing, or shipping, and it answers only from the
   provided facts.

This context-grounded design is well suited to focused, fixed-size knowledge
bases where speed and zero infrastructure matter — the same grounding
principle that Semantic Search and RAG-based projects extend with retrieval
when the knowledge base grows too large to fit in a single prompt.

## Cost notes

Runs entirely locally through Ollama — **zero API cost**, no internet
connection required after the model is pulled.
