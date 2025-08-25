import streamlit as st
import requests
import pickle

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

API_KEY = 'a3ba276aadb31581cdc699fd7c0ff903'

st.title("Movie Recommendation System")

option = st.selectbox(
    'Select a movie:',movies['title'].values)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)  
    response.raise_for_status()  
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_names.append(movies.iloc[i[0]].title)

        # recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_names
    # return recommended_movie_names,recommended_movie_posters

if st.button('Recommend'):
    # recommended_movie_names,recommended_movie_posters = recommend(option)
    recommended_movie_names = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        # st.image(recommended_movie_posters[0])

    with col2:
        st.text(recommended_movie_names[1])
        # st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        # st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        # st.image(recommended_movie_posters[3])
    with col5:
        st.text( recommended_movie_names[4])
        # st.image(recommended_movie_posters[4])