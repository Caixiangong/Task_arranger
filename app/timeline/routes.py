from flask import Blueprint, render_template, request, redirect, url_for
from app import database
from app.models.user import Task
timeline_bp = Blueprint('timeline', __name__, template_folder='../templates')

@timeline_bp.route('/timeline')
def timeline():
    tasks = Task.query.order_by(Task.deadline.asc()).all()
    return render_template('timeline.html', tasks=tasks)