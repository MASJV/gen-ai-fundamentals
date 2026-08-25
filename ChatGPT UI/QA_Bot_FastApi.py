from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# to run uvicorn chatgptdemo:app --reload

# Load .env
load_dotenv(override=True)

# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# FastAPI app
app = FastAPI(title="Simple ChatGPT API")


# Request model
class ChatRequest(BaseModel):
    message: str


# Chat API
@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "reply": answer
    }


# Serve frontend
app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)