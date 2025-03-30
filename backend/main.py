from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Poll(BaseModel):
    option1: str
    option2: str
    image1: str | None = None
    image2: str | None = None

def parse_trends():
    trends = [
        "Дюна 2 vs Оппенгеймер",
        "Человек-бензопила vs Атака титанов",
        "Burger King vs McDonald's"
    ]
    comparisons = []
    for trend in trends:
        match = re.search(r"(.+)\s(vs|или)\s(.+)", trend)
        if match:
            comparisons.append((match.group(1), match.group(3)))
    return comparisons

def get_poster(query: str):
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key=ВАШ_TMDB_API_KEY"
    response = requests.get(url).json()
    if response["results"]:
        return f"https://image.tmdb.org/t/p/w500{response['results'][0]['poster_path']}"
    return None

@app.get("/api/polls")
async def get_polls():
    comparisons = parse_trends()
    polls = []
    for option1, option2 in comparisons[:3]:
        polls.append(Poll(
            option1=option1,
            option2=option2,
            image1=get_poster(option1),
            image2=get_poster(option2),
        ))
    return polls
