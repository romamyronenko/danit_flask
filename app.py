from flask import Flask, request, render_template, redirect, url_for

import models
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/todolists", methods=["GET", "POST"])
def todolists():
    if request.method == "POST":
        name = request.form['name']
        todolist = models.ToDoList(name=name)
        db.session.add(todolist)
        db.session.commit()
        return redirect(url_for('todolists'))

    todolists = models.ToDoList.query.all()
    return render_template('todolists.html', todolists=todolists)


@app.route("/todolists/<int:list_id>/tasks", methods=["GET", "POST"])
def tasks(list_id):
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        list_id = request.form['todo_list_id']
        todolist = models.Task(name=name, description=description, todo_list_id=list_id)
        db.session.add(todolist)
        db.session.commit()
        return redirect(url_for(f'tasks', list_id=list_id))

    tasks = models.Task.query.where(models.Task.todo_list_id == list_id).all()
    return render_template('tasks.html', list_id=list_id, tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
