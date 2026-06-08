import os
import pickle
from typing import Optional, List

import pandas as pd
import numpy as np
import httpx

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from dotenv import load_dotenv



# =========================
# ENV
# =========================

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

if not OMDB_API_KEY:
    raise RuntimeError(
        "OMDB_API_KEY missing. Put it in .env as OMDB_API_KEY=xxxx"
    )

OMDB_BASE = "https://www.omdbapi.com/"


# =========================
# FASTAPI
# =========================

app = FastAPI(
    title="Movie Recommendation API",
    version="1.0"
)

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# PICKLE FILES
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DF_PATH = os.path.join(BASE_DIR, "df.pkl")
INDICES_PATH = os.path.join(BASE_DIR, "indices.pkl")
TFIDF_MATRIX_PATH = os.path.join(BASE_DIR, "tfidf_matrix.pkl")

df = None
indices = None
tfidf_matrix = None


# =========================
# MODELS
# =========================

class MovieCard(BaseModel):
    title: str
    year: Optional[str] = None
    rating: Optional[str] = None
    poster: Optional[str] = None


class RecommendationItem(BaseModel):
    title: str
    score: float
    movie: Optional[MovieCard] = None


# =========================
# LOAD FILES
# =========================

@app.on_event("startup")
def startup():

    global df
    global indices
    global tfidf_matrix

    with open(DF_PATH, "rb") as f:
        df = pickle.load(f)

    with open(INDICES_PATH, "rb") as f:
        indices = pickle.load(f)

    with open(TFIDF_MATRIX_PATH, "rb") as f:
        tfidf_matrix = pickle.load(f)

    print(indices.head(20))

# =========================
# OMDB
# =========================

async def omdb_movie(title: str):

    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            OMDB_BASE,
            params=params
        )

    data = response.json()

    if data.get("Response") == "False":
        return None

    return MovieCard(
        title=data.get("Title"),
        year=data.get("Year"),
        rating=data.get("imdbRating"),
        poster=data.get("Poster")
    )


# =========================
# TFIDF
# =========================

def recommend_movies(title, top_n=10):

    matched_titles = [
        t for t in indices.index
        if str(t).lower() == title.lower()
    ]

    if not matched_titles:
        raise Exception(
            f"Movie '{title}' not found"
        )

    idx = indices[matched_titles[0]]

    scores = (
        tfidf_matrix @ tfidf_matrix[idx].T
    ).toarray().flatten()

    movie_indices = np.argsort(scores)[::-1]

    recommendations = []

    for i in movie_indices:

        if i == idx:
            continue

        recommendations.append(
            (
                df.iloc[i]["title"],
                float(scores[i])
            )
        )

        if len(recommendations) >= top_n:
            break

    return recommendations


# =========================
# ROUTES
# =========================

@app.get(
    "/",
    response_class=HTMLResponse
)
async def homepage(
    request: Request
):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/recommend")
async def recommend(
    title: str = Query(...)
):

    try:

        recs = recommend_movies(title)

        result = []

        for movie_title, score in recs:

            movie = await omdb_movie(movie_title)

            result.append(
                RecommendationItem(
                    title=movie_title,
                    score=score,
                    movie=movie
                )
            )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )