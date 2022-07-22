import os
from .extensions import login_manager


class TestConfig(object):
    SECRET_KEY = "my secret key"
    basedir = os.path.abspath(os.path.dirname(__file__))
    # DB settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    login_manager.login_view = "auth.log_in"

    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Enable email authentication
    USER_ENABLE_USERNAME = True  # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    USER_ENABLE_CONFIRM_EMAIL = False

