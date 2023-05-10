
from flask import Blueprint, jsonify, request
from app.config import app, db
from app.models import Task

bp = Blueprint('tasks', __name__)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    new_task_data = request.json

    try:
        new_task = Task(
            title=new_task_data['title'], description=new_task_data['description'], completed=False)

        db.session.add(new_task)

        db.session.commit()

        return jsonify({'message': 'Task added successfully'}, 200)
    except:
        return jsonify({'message': 'There was an error adding the task'}, 400)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        task = Task.query.filter_by(id=task_id).first()

        task = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
        }

        return jsonify(task), 200
    except:
        return jsonify({'error': 'Task not found'}), 404


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    edit_task = request.get_json()

    for task in tasks:
        if task['id'] == task_id:
            task['id'] = edit_task

            return jsonify(edit_task), 200

    return jsonify({'error': 'Task not found'}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)

            return jsonify({'message': 'Task removed'}), 200

    return jsonify({'error': 'Task not found'}), 404
