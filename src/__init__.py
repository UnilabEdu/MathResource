import datetime

from flask import Flask, render_template_string

from src.config import TestConfig
from src.extensions import db, login_manager

from src.user.models import User, Role
from src.questions.models import Answer

from src.admin import admin


def create_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    register_extension(app)
    register_blueprints(app)
    # Setup Flask Admin
    admin.init_app(app)
    return app

def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()


def register_blueprints(app):
    from src.user.views import auth_blueprint
    from src.front_end.views import main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

