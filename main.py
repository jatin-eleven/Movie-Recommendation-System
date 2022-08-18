
from flask import Flask, render_template, url_for, redirect, jsonify, request
from ml import MovieRecommendation
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        title = request.form['title']
        result = MovieRecommendation(title)
        print(result)
        return render_template("index.html", result=result)

    return render_template("index.html")





if __name__ == '__main__':
  app.run(debug=True, port = 5110)