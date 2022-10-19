from flask import Flask
from flask_user import UserManager
from src.config import TestConfig
from src.extensions import db, login_manager, migrate, mail
from src.models.user import User, Roles, Contacts, About, Team, Documents
from src.models.question import UsersTasks

from src.admin import admin, UserView, RoleView, MenuLink, StaticView, UsersTasksView, ContactsView, AboutView, TeamView, DocumentsView


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
    mail.init_app(app)
    admin.add_view(UserView(User, db.session, category='User Management'))
    admin.add_view(RoleView(Roles, db.session, category='User Management'))
    admin.add_view(UsersTasksView(UsersTasks, db.session, category='User Management'))
    admin.add_view(ContactsView(Contacts, db.session, category='General Management'))
    admin.add_view(AboutView(About, db.session, category='General Management'))
    admin.add_view(TeamView(Team, db.session, category='General Management'))
    admin.add_view(DocumentsView(Documents, db.session, category='General Management'))
    admin.add_link(MenuLink(name='Dashboard', url='/'))
    admin.add_view(StaticView(TestConfig.basedir + '/static', '/static', name='Static Files'))

    @app.before_first_request
    def create_tables():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    from src.views.auth.routes import auth_blueprint
    from src.views.main.routes import main_blueprint
    from src.admin.views import admins_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admins_blueprint)


