from flask import Flask, render_template, request


app = Flask(__name__)

my_todo = ["graduate", 'get into college']

@app.route("/", methods= ["GET", 'POST'])
def todo():
    new_todo = request.form["new_todo"]
    my_todo.append(new_todo)
    return render_template("todo.html.jinja",todos = my_todo)

