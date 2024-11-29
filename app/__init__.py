from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import inspect
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timedelta
from .models.user import database
    

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SECRET_KEY'] = 'caixiangong'
    app.config['WTF_CSRF_ENABLED'] = False
    database.init_app(app)
    from .base.routes import base_bp
    from .task.routes import task_bp
    from .timeline.routes import timeline_bp
    from .chat.routes import chat_bp

    app.register_blueprint(base_bp, url_prefix='/')

    app.register_blueprint(task_bp, url_prefix='/')

    app.register_blueprint(timeline_bp, url_prefix='/')

    app.register_blueprint(chat_bp, url_prefix='/')
    with app.app_context():
        inspector = inspect(database.engine)
        tables = inspector.get_table_names()
        if len(tables) == 0:
            database.create_all()
            database.session.commit()
    return app