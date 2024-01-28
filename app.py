import asyncio
from flask import Flask, render_template, request, redirect
from nlp_search_titles import Searcher

app = Flask(__name__)

import sparql_request
import nlp_search_movies

given_film = ""
found_movies = []
matches = []

async def async_search_movie(film):
    return await nlp_search_movies.search_movie(film, sparql_request.movies)

@app.route('/', methods=["POST", "GET"])
def main_page():
    global matches
    global given_film
    global found_movies

    if request.method == "POST":
        given_film = request.form.get('input_movie')
        if given_film:
            matches = Searcher().search_words(given_film, list(sparql_request.movies.keys()), max_operations=5)
            return redirect('/')
    else:
        return render_template("index.html", given_film=given_film, movies=matches, found_movies=found_movies)

@app.route('/search/<film>', methods=["POST", "GET"])
async def film_select(film):
    global matches
    global given_film
    global found_movies

    if request.method == "POST":
        print(film)
        found_movies = await async_search_movie(film)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
