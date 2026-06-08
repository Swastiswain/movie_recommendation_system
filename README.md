# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **NLP**, **TF-IDF**, **Cosine Similarity**, **FastAPI**, and **OMDb API**.

The system recommends movies similar to a selected movie based on textual features and displays movie details such as posters, ratings, and release years.

---

## 🚀 Live Features

✅ Movie Search

✅ Content-Based Recommendations

✅ NLP Text Processing

✅ TF-IDF Vectorization

✅ Cosine Similarity Matching

✅ OMDb API Integration

✅ FastAPI Backend

✅ Responsive Frontend (HTML, CSS, JavaScript)

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- Python 3.11
- Pandas
- NumPy
- Scikit-Learn
- HTTPX

### Machine Learning / NLP

- TF-IDF Vectorizer
- Cosine Similarity
- NLTK
- Content-Based Filtering

### Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

### External API

- OMDb API

---

## 📂 Project Structure

```text
movie_recommendation_system/
│
├── main.py
├── app.py
├── movies.py
│
├── df.pkl
├── indices.pkl
├── tfidf.pkl
├── tfidf_matrix.pkl
│
├── movies_metadata.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

### 1. Data Preprocessing

Movie metadata is cleaned and transformed.

Features used:

- Overview
- Genres
- Keywords
- Cast
- Crew

---

### 2. NLP Processing

Text preprocessing includes:

- Lowercasing
- Tokenization
- Stopword Removal
- Lemmatization

---

### 3. TF-IDF Vectorization

The textual features are converted into numerical vectors using:

```python
TfidfVectorizer()
```

---

### 4. Similarity Calculation

Movie similarity is calculated using:

```python
cosine_similarity()
```

Movies with the highest similarity scores are recommended.

---

### 5. OMDb Integration

Movie information such as:

- Poster
- IMDb Rating
- Release Year

is fetched dynamically using OMDb API.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Swastiswain/movie_recommendation_system.git

cd movie_recommendation_system
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OMDB_API_KEY=your_api_key_here
```

Get your API key from:

https://www.omdbapi.com/apikey.aspx

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📸 Sample Workflow

1. Search a movie (Example: Avatar)
2. System finds similar movies
3. Recommendations are ranked using cosine similarity
4. Posters and ratings are fetched from OMDb

---

## 🎯 Future Improvements

- Hybrid Recommendation System
- User Authentication
- Watchlist Feature
- Movie Trailers
- TMDB Integration
- Collaborative Filtering
- Deep Learning Recommendations

---

## 📈 Learning Outcomes

This project demonstrates:

- Natural Language Processing
- TF-IDF Vectorization
- Cosine Similarity
- Recommendation Systems
- FastAPI Development
- API Integration
- Frontend Development
- Model Deployment

---

## 👨‍💻 Author

### Swasti Swain

Computer Science Engineering Student

GitHub:

https://github.com/Swastiswain

---

## ⭐ If you like this project

Give the repository a star and feel free to contribute.
