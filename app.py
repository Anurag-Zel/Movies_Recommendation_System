import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
    
movies_details = pickle.load(open('merged_db.pkl','rb')) 
movies_details = pd.DataFrame(movies_details)


def recommend(movie) : 
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    
    for i in movies_list :
        name =  movies.iloc[i[0]].title
        genre = ", ".join(movies_details[movies_details['title'] == name]['genres'].values[0])
        director = ", ".join(movies_details[movies_details['title'] == name]['crew'].values[0])
        release_date = movies_details[movies_details['title'] == name]['release_date'].values[0]
        recommended_movies.append([name,genre,director,release_date])
    return recommended_movies    

selected_movie_name = st.selectbox(
    "Select Movie",
    movies['title'].values,
)


if st.button("Recommend"):
    names = recommend(selected_movie_name)

    st.markdown(f""" <h4>Top 5 Movie Recommendations :  </h4> """, unsafe_allow_html=True)

    names = recommend(selected_movie_name)

    cols = st.columns(2)  
    col_index = 0

    for i in names:
        movie_name = i[0]
        genre = i[1]
        director = i[2]
        release_date = i[3]

        with cols[col_index]:  
            st.markdown(f"""
            <div style='border:1px solid #ccc; padding:10px; border-radius:10px; margin-bottom:10px;'>
            <h5><span style='font-weight:bold;'>🎬 <span style='color:#FF5733;'>Movie:</span></span> <span style='color:#FF8C00;'>{movie_name}</span></h5>
            <span style='font-weight:bold;'>🎭 <span style='color:#33C3FF;'>Genre:</span></span> <span style='color:#1E90FF;'>{genre}</span><br>
            <span style='font-weight:bold;'>🎥 <span style='color:#28B463;'>Director:</span></span> <span style='color:#2ECC71;'>{director}</span><br>
            <span style='font-weight:bold;'>📅 <span style='color:#8E44AD;'>Release Date:</span></span> <span style='color:#9B59B6;'>{release_date}</span>
            </div>
            """, unsafe_allow_html=True)
        col_index = 1 - col_index    