import datetime

from flask import Flask, render_template_string
from flask_user import UserManager
from src.config import TestConfig
from src.extensions import db, login_manager, migrate

from src.user.models import User, Role, UserRoles, Teacher
from src.questions.models import Answer, UsersTasks

from src.admin import admin, UserView, RoleView, MenuLink, StaticView, TeacherModelView, UsersTasksView, UserRolesView


def create_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    register_extension(app)
    register_blueprints(app)
    return app


def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    usermanager = UserManager(app, db, User)
    migrate.init_app(app, db)
    admin.add_view(UserView(User, db.session, category='User Management'))
    admin.add_view(RoleView(Role, db.session, category='User Management'))
    admin.add_view(UsersTasksView(UsersTasks, db.session, category='User Management'))
    admin.add_view(UserRolesView(UserRoles, db.session, category='User Management'))
    admin.add_view(TeacherModelView(Teacher, db.session, category='User Management'))
    admin.add_link(MenuLink(name='Dashboard', url='/'))
    admin.add_view(StaticView(TestConfig.basedir + '/static', '/static', name='Static Files'))

    @app.before_first_request
    def create_tables():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_blueprints(app):
    from src.user.views import auth_blueprint
    from src.front_end.views import main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)



