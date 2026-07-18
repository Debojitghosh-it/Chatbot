import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai

# -----------------------
# Load Environment
# -----------------------

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------
# FastAPI
# -----------------------

app = FastAPI(title="Ultra Mind AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Request Model
# -----------------------


class ChatRequest(BaseModel):
    message: str


import re


def clean_response(text: str) -> str:
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)

    # Remove inline code
    text = re.sub(r"`([^`]*)`", r"\1", text)

    # Remove bold/italic
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)

    # Remove headings
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)

    # Remove blockquotes
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)

    # Remove unordered list markers
    text = re.sub(r"^[\-\*\+]\s*", "", text, flags=re.MULTILINE)

    # Remove numbered list markers
    text = re.sub(r"^\d+\.\s*", "", text, flags=re.MULTILINE)

    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# -----------------------
# Routes
# -----------------------


@app.get("/")
def home():
    return {"status": "Running", "model": "gemini-3.5-flash"}


@app.post("/chat")
def chat(data: ChatRequest):

    prompt = f"""
Answer the following question in plain text only.

Do NOT use:
- Markdown
- Bold
- Italics
- Bullet points
- Numbered lists
- Emojis
- Headings
- Tables

Use simple paragraphs.

Question:
{data.message}
"""

    if not prompt:
        return {"response": "Please enter a message."}

    if prompt.lower() == "exit":
        return {"response": "Bye! Have a great day 👋"}

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash", contents=prompt
        )

        answer = clean_response(response.text)

        return {"response": answer}

    except Exception as e:

        return {"response": str(e)}
