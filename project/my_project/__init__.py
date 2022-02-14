from flask import Flask
from my_project.extensions import db, login_manager
from my_project.config import TestConfig


def create_app():
    app = Flask(__name__)

    app.config.from_object(TestConfig)

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from my_project.user.views import user_blueprint
    from my_project.front_end.view import main_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)

    login_manager.login_view = 'login'

    return app


