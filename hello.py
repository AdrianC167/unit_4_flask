from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template("index.html.jinja")


@app.route('/ping')
def page2():
    return "pong"

@app.route("/hello/<name>")
def hello(name):
    return f'Hello {name}'
