import datetime

from flask import Flask, render_template_string

from src.config import TestConfig
from src.extensions import db

from src.user.models import User, Role
from src.questions.models import Answer

from src.admin import admin


def create_app():
    app = Flask(__name__)

    app.config.from_object(TestConfig)

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()


    from src.user.views import user_blueprint
    from src.front_end.views import main_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(main_blueprint)

    # Setup Flask Admin
    admin.init_app(app)

    return app
