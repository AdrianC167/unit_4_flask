from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print


app = Flask(__name__)

my_todo = ["graduate", 'get into college']

@app.route("/", methods= ["GET", 'POST'])
def todo():

    conn = pymysql.connect(
        database = "achen_todos",
        user = "achen",
        password = "232126110",
        host = "10.100.33.60",
        cursorclass = pymysql.cursors.DictCursor

    )

    cursor = conn.cursor()
    cursor.execute("SELECT `description` FROM `todos`")
    results = cursor.fetchall()
    if request.method == 'POST':
        new_todo = request.form[my_todo]
        my_todo.append(new_todo)
    
    return render_template("todo.html.jinja",todos = results)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    del my_todo[todo_index]
    
    return redirect('/')