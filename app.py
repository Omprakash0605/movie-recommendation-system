
import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #10121b;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #aaa;
    font-size: 17px;
    margin-bottom: 30px;
}

.movie-card {
    background: #1e2030;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #34364a;
    text-align: center;
    min-height: 110px;
}

.movie-number {
    color: #a78bfa;
    font-size: 14px;
}

.movie-name {
    color: white;
    font-size: 17px;
    font-weight: bold;
    margin-top: 12px;
}

.stButton button {
    background-color: #7c3aed;
    color: white;
    border-radius: 8px;
    border: none;
    height: 45px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #6d28d9;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# LOAD MODEL FILES
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

@st.cache_resource
def load_data():

    with open(MODEL_DIR / "movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open(MODEL_DIR / "similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return movies, similarity


try:
    movies, similarity = load_data()

except FileNotFoundError:
    st.error("Model files not found. Check your models folder.")
    st.stop()

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()


# -------------------------------
# RECOMMENDATION FUNCTION
# -------------------------------

def recommend(movie):

    movie_index = np.flatnonzero(
        movies["title"].to_numpy() == movie
    )[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in movie_list:

        if i[0] == movie_index:
            continue

        recommendations.append(
            movies.iloc[i[0]]["title"]
        )

        if len(recommendations) == 5:
            break

    return recommendations


# -------------------------------
# HEADER
# -------------------------------

st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to your favourites!'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# -------------------------------
# MOVIE SELECTION
# -------------------------------

st.subheader("🍿 Select Your Favourite Movie")

movie_list = movies["title"].dropna().tolist()

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list,
    index=None,
    placeholder="Search for a movie..."
)

# -------------------------------
# RECOMMEND BUTTON
# -------------------------------

if st.button("✨ Recommend Movies", use_container_width=True):

    if selected_movie is None:

        st.warning("Please select a movie first.")

    else:

        recommended_movies = recommend(selected_movie)

        st.divider()

        st.subheader(f"Movies similar to {selected_movie}")

        if recommended_movies:

            cols = st.columns(5)

            for i, movie in enumerate(recommended_movies):

                with cols[i]:

                    st.markdown(
                        f"""
                        <div class="movie-card">
                            <div class="movie-number">
                                RECOMMENDATION {i+1}
                            </div>
                            <div class="movie-name">
                                🎥 {movie}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:
            st.warning("No recommendations found.")

# -------------------------------
# FOOTER
# -------------------------------

st.divider()

st.markdown(
    "<p style='text-align:center;color:#888;'>"
    "Built using Python | Bag of Words | Cosine Similarity | Streamlit"
    "</p>",
    unsafe_allow_html=True
)
