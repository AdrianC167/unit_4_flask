from flask import Flask, render_template, request, redirect


app = Flask(__name__)

my_todo = ["graduate", 'get into college']

@app.route("/", methods= ["GET", 'POST'])
def todo():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        my_todo.append(new_todo)
    
    return render_template("todo.html.jinja",todos = my_todo)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    del my_todo[todo_index]
    
    return redirect('/')