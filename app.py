from flask import Flask, render_template, request, redirect, url_for
from nlp_search_titles import Searcher

app = Flask(__name__)

import sparql_request
import nlp_search_movies


@app.route('/', methods=["POST", "GET"])
def main_page():  # put application's code here
    if request.method == "POST":
        data = request.form.get('input_movie')
        if data:
            matches = Searcher().search_words(data, list(sparql_request.movies.keys()), max_operations=5)
            return render_template("index.html", data=data, movies=matches)
        else:
            return render_template("index.html", data=data)

    return render_template("index.html")


@app.route('/search/<film>', methods=["POST"])
def film_select(film):
    if request.method == "POST":
        print(film)
        nlp_search_movies.search_movie(film, sparql_request.movies)
        return ""


if __name__ == '__main__':
    app.run(debug=True)
