from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "seam": generate_password_hash("hello"),
    "adrian": generate_password_hash("friedchickenx2")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

my_todo = ["graduate", 'get into college']
conn = pymysql.connect(
        database = "achen_todos",
        user = "achen",
        password = "232126110",
        host = "10.100.33.60",
        cursorclass = pymysql.cursors.DictCursor
 )


@app.route("/", methods= ["GET", 'POST'])
@auth.login_required
def todo():
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")
    results = cursor.fetchall()
    cursor.close()

    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos`(`description`) VALUES('{new_todo}')")         
        cursor.close()
        conn.commit()
    
    return render_template("todo.html.jinja",todos = results)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index} ")
    cursor.close()
    conn.commit()
    return redirect('/')

@app.route('/complete_todo/<int:todo_index>', methods = ['POST'])
def todo_complete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index} ")
    cursor.close()
    conn.commit()
    return redirect('/')