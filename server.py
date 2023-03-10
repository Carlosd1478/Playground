from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/play")
def play():
    num = 3
    return render_template("index.html", color = "blue", times=num)

@app.route("/play/<int:times>")
def multiply(times):
    num = times
    return render_template("index.html", color = "blue", times=num)

@app.route("/play/<int:times>/<string:color>")
def multiply_an_colors(times,color):
    num = times
    color = color
    return render_template("index.html", color = color, times=num)


if __name__ == "__main__":
    app.run(debug = True, port=5001)