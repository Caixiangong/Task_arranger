from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app import database
from app.models.user import Task
base_bp = Blueprint('base', __name__, template_folder='../templates')
from flask_sqlalchemy import SQLAlchemy
@base_bp.route('/')
def base():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)