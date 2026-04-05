# main.py (FastAPI)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import get_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "active"}

@app.get("/quote")
def get_quote():
    # Split your string into a proper JSON object
    full = get_api()  # "Character(Anime): Quote"
    try:
        info, quote_text = full.split("): ")
        char_name, anime_name = info.split("(")
    except Exception:
        char_name, anime_name, quote_text = "---", "---", full

    return {
        "character": char_name.strip(),
        "anime": anime_name.strip(),
        "quote": quote_text.strip()
    }