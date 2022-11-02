from flask import Flask, render_template
import requests as req
import random

app = Flask(__name__)

raw_api = req.get("https://motivational-quote-api.herokuapp.com/quotes")
data = raw_api.json()


@app.route("/")
def index():
    integer = random.randint(0, 33)
    return render_template("index.html", id=integer)


@app.route("/quote")
def get_quote(integer):
    integer = random.randint(0, 33)
    quote_obj = data[integer]
    return render_template("quotes.html", id=quote_obj["id"], author=quote_obj["person"], quote=quote_obj["quote"])


if __name__ == "__main__":
    app.run(port=5000)