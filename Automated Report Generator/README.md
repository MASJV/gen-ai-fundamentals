# Travel Planner

A quick trip-planning assistant that takes a free-text description of your
trip — starting point, destination, dates, and budget — and returns it back
as a clean, structured JSON object, ready to be consumed by any downstream
app (a booking flow, a calendar entry, a budget tracker) instead of a wall
of prose.

## Architecture

```
User Input (free text: starting location, destination, dates, budget)
      |
Prompt Assembly ("Plan a trip based on the following details... 
                  Return only valid JSON in this exact format: {...}")
      |
Ollama LLM (llama3.2:1b)
      |
Structured JSON Output
   { "starting location": [...], "destination": [...],
     "travel dates": [...], "budget": "..." }
```

## Files

| File | Role |
|---|---|
| `travelPlanner.py` | Everything — input capture, prompt assembly with a JSON-format instruction, LLM call, output |

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
   python travelPlanner.py
   ```

4. Describe your trip when prompted, e.g. *"Flying from Mumbai to Bali,
   leaving Dec 10th and back by Dec 17th, budget around ₹80,000."*

## How it works, in plain words

1. **Ask** — The script takes one free-text description of the trip from
   the terminal — no rigid form fields, just however you'd naturally
   describe it.
2. **Constrain the output shape** — The prompt doesn't just ask the model
   to "plan a trip"; it explicitly demands the response come back as valid
   JSON in an exact, predefined schema (`starting location`, `destination`,
   `travel dates`, `budget`).
3. **Generate** — The prompt is sent to `llama3.2:1b` via
   `ollama.generate()`.
4. **Structured result** — The printed output is machine-readable JSON
   rather than freeform text, so the same trip details you typed in casual
   language come back normalized and ready to plug into another system.

## Cost notes

Runs entirely locally through Ollama — **zero API cost**, no internet
connection required after the model is pulled.