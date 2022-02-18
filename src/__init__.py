import datetime

from flask import Flask, render_template_string
from flask_user import login_required, roles_required, UserManager

from src.extensions import db
from src.config import TestConfig
from src.user.models import User, Role
from src.admin import admin


def create_app():
    app = Flask(__name__)

    app.config.from_object(TestConfig)

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
        # Create 'member@example.com' user with no roles
        if not User.query.filter(User.username == 'member').first():
            user = User(
                username='member',
                email_confirmed_at=datetime.datetime.utcnow(),
                password=user_manager.hash_password('Password1'),
            )
            db.session.add(user)
            db.session.commit()

        # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
        if not User.query.filter(User.username == 'admin').first():
            user = User(
                username='admin',
                email_confirmed_at=datetime.datetime.utcnow(),
                password=user_manager.hash_password('Password1'),
            )
            user.roles.append(Role(name='Admin'))
            user.roles.append(Role(name='Agent'))
            db.session.add(user)
            db.session.commit()

    from src.user.views import user_blueprint
    from src.front_end.view import main_blueprint

    # app.register_blueprint(user_blueprint, url_prefix='/user')
    # app.register_blueprint(main_blueprint)

    # Setup Flask-User
    user_manager = UserManager(app, db, User)
    # Setup Flask Admin
    admin.init_app(app)
    return app
