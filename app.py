from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import sparql_request


@app.route('/', methods=["POST", "GET"])
def main_page():  # put application's code here
    if request.method == "POST":
        data = request.form.get('input_movie')
        return(sparql_request.results_dict)
        return render_template("index.html", data=data)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
