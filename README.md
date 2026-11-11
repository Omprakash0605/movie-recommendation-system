# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Machine Learning, and Streamlit**. It recommends the top 5 movies based on the similarity of movie descriptions, genres, keywords, cast, and crew.

## 🚀 Features

- Search and select a movie from the available movie list.
- Get the top 5 similar movie recommendations.
- Content-based filtering using the Bag of Words technique.
- Cosine Similarity to calculate movie similarity.
- Interactive web interface built with Streamlit.

## 🛠️ Tech Stack

- **Python** – Core programming language.
- **Pandas & NumPy** – Data processing.
- **Scikit-learn** – CountVectorizer and Cosine Similarity.
- **Streamlit** – Frontend web application.
- **Jupyter Notebook** – Model development and experimentation.

## 🧠 How It Works

1. Collect movie information such as overview, genres, keywords, cast, and crew.
2. Combine these features into a single `tags` column.
3. Convert text into numerical vectors using Bag of Words (CountVectorizer).
4. Calculate similarity between movies using Cosine Similarity.
5. Recommend the top 5 most similar movies based on the selected movie.

## 📂 Project Structure

```text
movie-recommendation/
│
├── dataset/
│   └── movies.csv
│
├── notebooks/
│   └── movie_recommendation.ipynb
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommendation-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`