from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin


db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()
migrate = Migrate()

