
from flask import Blueprint, jsonify, request
from app.config import app, db
from app.models import Task
from app.schemas import TaskSchema

bp = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    return jsonify(tasks_schema.dump(tasks)), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    new_task_data = request.json

    errors = task_schema.validate(new_task_data)

    if (errors):
        return jsonify(errors), 400

    try:
        new_task = Task(
            title=new_task_data['title'],
            description=new_task_data['description'],
            completed=False
        )

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

    errors = task_schema.validate(edit_task)

    if (errors):
        return jsonify(errors), 400

    task = Task.query.get(task_id)

    if task:
        task.title = edit_task.get('title', None)
        task.description = edit_task.get('description', None)
        task.completed = edit_task.get('completed', False)

        db.session.commit()

        return jsonify({'success': 'The task has been changed successfully'}), 200

    return jsonify({'error': 'Task not found'}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):

    task = Task.query.get(task_id)

    if (task):
        db.session.delete(task)

        db.session.commit()
        return jsonify({'success': 'Task has been removed successfully'}), 200

    return jsonify({'error': 'Task not found'}), 404
