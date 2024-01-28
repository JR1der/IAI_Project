import time

from flask import Flask, render_template, request, redirect, url_for
from nlp_search_titles import Searcher

app = Flask(__name__)

import sparql_request
import nlp_search_movies

given_film = ""
found_movies = []
matches = []


@app.route('/', methods=["POST", "GET"])
def main_page():  # put application's code here
    global matches
    global given_film
    global found_movies

    if request.method == "POST":
        given_film = request.form.get('input_movie')
        if given_film:
            matches = Searcher().search_words(given_film, list(sparql_request.movies.keys()), max_operations=5)
            return redirect('/')
        else:
            return redirect('/')
    else:
        print(found_movies)
        return render_template("index.html", given_film=given_film, movies=matches, found_movies=found_movies)


@app.route('/search/<film>', methods=["POST", "GET"])
def film_select(film):
    global matches
    global given_film
    global found_movies

    if request.method == "POST":
        print(film)
        found_movies = nlp_search_movies.search_movie(film, sparql_request.movies)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
