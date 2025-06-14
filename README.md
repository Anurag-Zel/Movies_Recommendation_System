# 🎬 Movie Recommender System

This is a **Machine Learning-based Movie Recommender System** built using Python and Streamlit. The application provides personalized movie suggestions based on a selected title, showing genre, director, and release date. The project is deployed and accessible at:

🔗 **Live Demo:** https://movies-recommendation-system-darkzel.streamlit.app/
🔗 **Movies Dataset:** https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
---

## 📌 Overview

This Movie Recommender System is built using **Natural Language Processing (NLP)** techniques to capture the "vibe" or essence of a movie and recommend similar ones. At its core, it uses the **Bag of Words** model to convert metadata like genres, tags, cast, and crew into numerical vectors that represent each movie.

These vectors are then compared using **cosine similarity** to determine how similar two movies are. The more aligned their content and context (vibe), the higher their similarity score.

When a user selects a movie, the system:

1. Extracts its feature vector using the Bag of Words approach.
2. Computes cosine similarity between this movie and all others in the dataset.
3. Sorts and selects the top 5 most similar movies.
4. Displays each recommendation along with:
   - 🎬 **Movie Name**
   - 🎭 **Genre**
   - 🎥 **Director**
   - 📅 **Release Date**

The UI is rendered using **Streamlit**, styled with HTML + CSS, and arranged in a neat **2x3 grid layout** for a visually appealing experience.

This project is ideal for anyone looking to understand how simple NLP models like Bag of Words can be applied to build intuitive content-based recommendation engines.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **Scikit-learn** (for cosine similarity)
- **Pickle** (for model/data serialization)

---

### 🚀 How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
