# ChatGPT-like Chat UI from Scratch

A ChatGPT-styled chat interface built with plain HTML/CSS/JS on the
frontend and a FastAPI backend on the server — no chat-UI framework or
library, every bubble, input state, and fetch call is hand-built.

## Architecture

```
Browser (index.html — vanilla HTML/CSS/JS chat UI)
      |
User types message -> POST /chat  { "message": "..." }
      |
FastAPI Backend (QA_Bot_FastApi.py)
      |
OpenAI gpt-4o-mini (chat.completions)
      |
JSON Response  { "reply": "..." }
      |
Rendered as a chat bubble in the browser
```

## Files

| File | Role |
|---|---|
| `QA_Bot_FastApi.py` | FastAPI backend — `/chat` endpoint, OpenAI call, serves the frontend as static files |
| `index.html` | Full chat UI — header, scrolling message list, input bar, send button, all styled and scripted inline (no external CSS/JS files) |
| `.env.example` | Sample env file — copy to `.env` and add your real `OPENAI_API_KEY` |

## Setup

1. Install dependencies:
   ```
   pip install fastapi uvicorn openai python-dotenv
   ```

2. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-xxxx
   ```

3. The backend serves the frontend straight from a `static/` folder next to
   it — the repo already ships `index.html` there, so no manual setup is
   needed:
   ```
   static/
   └── index.html
   QA_Bot_FastApi.py
   .env
   ```

4. Run the server:
   ```
   uvicorn QA_Bot_FastApi:app --reload
   ```

5. Open `http://127.0.0.1:8000` in your browser and start chatting.

## How it works, in plain words

1. **UI, from scratch** — `index.html` renders a dark, ChatGPT-styled
   layout: a header, a scrolling message area, and an input bar. User and
   bot messages get their own bubble styles, and pressing Enter sends the
   message just like clicking Send.
2. **Send** — On send, the user's message is immediately shown in the chat
   (optimistic UI), a "Thinking..." placeholder bubble appears for the bot,
   and the input is disabled until a reply comes back.
3. **Talk to the backend** — The frontend calls `POST /chat` with the
   message as JSON — no page reload, just a `fetch()` call.
4. **Generate a reply** — FastAPI receives the request, sends it to
   `gpt-4o-mini` with a simple "helpful AI assistant" system prompt, and
   returns the reply as JSON.
5. **Render the reply** — The "Thinking..." placeholder bubble is swapped
   for the model's actual answer, the input re-enables, and the chat
   auto-scrolls to the bottom.
6. **One server, two jobs** — The same FastAPI app both serves the `/chat`
   API and hosts the static frontend (`StaticFiles(directory="static")`),
   so there's nothing else to deploy separately.

## Cost notes

The OpenAI model call is the only API usage cost. The frontend itself has no API cost; deployment/hosting cost depends on where the FastAPI application is hosted.