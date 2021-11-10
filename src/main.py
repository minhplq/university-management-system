from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_movie_db = [
    {
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again.",  # noqa: E501
        "genres": ["Action", "Adventure", "Fantasy"],
        "casts": ["Daisy Ridley", "Adam Driver"],
    }
]


class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


@app.get("/", response_model=List[Movie])
async def index():
    return fake_movie_db
