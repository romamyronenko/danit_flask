from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    tasks = db.relationship('Task', backref='todo_list', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))

    todo_list_id = db.Column(db.Integer, db.ForeignKey('to_do_list.id'), nullable=False)
