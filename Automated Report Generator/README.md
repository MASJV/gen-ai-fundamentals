# Automated Report Generator

Generates a full travel itinerary — day-wise plan, places to visit, local
food recommendations, and travel tips — from just a destination, trip
length, and budget.

## Architecture

```
User Input (destination, number of days, budget)
      |
Prompt Assembly ("Create a N-day travel itinerary for X...
                  Include: day-wise plan, places to visit,
                  local food recommendations, travel tips")
      |
Ollama LLM (llama3.2:1b) via chat()
      |
Free-form Text Itinerary
```

## Files

| File | Role |
|---|---|
| `travelPlanner.py` | Everything — input capture, prompt assembly, LLM call, output |

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

4. Enter a destination, number of days, and budget when prompted, e.g.
   *destination: "Goa", days: "4", budget: "₹25,000"*.

## How it works, in plain words

1. **Ask** — Three separate prompts collect the destination, trip length,
   and budget as plain strings — no validation or type conversion on any
   of them.
2. **Assemble the prompt** — The three inputs are dropped into a single
   instruction that explicitly asks for four sections: a day-wise plan,
   places to visit, local food recommendations, and travel tips.
3. **Generate** — The prompt is sent to `llama3.2:1b` via `ollama.chat()`
   as a single user message.
4. **Output** — The model's free-form text reply is printed as-is. Unlike
   a structured-output setup, there's no fixed schema or JSON parsing —
   the itinerary's structure (day breakdown, sections) comes entirely from
   how the model follows the prompt's instructions, not from code.

## Cost notes

Runs entirely locally through Ollama — **zero API cost**, no internet
connection required after the model is pulled.