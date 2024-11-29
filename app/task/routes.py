from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import database
from app.models.user import Task
task_bp = Blueprint('task', __name__, template_folder='../templates')

@task_bp.route('/task/new_task', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        name = request.form['task_name']
        deadline = request.form['task_ddl']
        tag_color = request.form['task_color']
        details = request.form['task_details']
        task = Task(name=name, deadline=datetime.strptime(deadline, '%Y-%m-%dT%H:%M'), 
                    details=details, tag_color=tag_color)
        database.session.add(task)
        database.session.commit()
        return redirect(url_for('base.base'))
    return render_template('new_task.html')

@task_bp.route('/task/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get(id)
    if task:
        database.session.delete(task)
        database.session.commit()
    return redirect(url_for('base.base'))
