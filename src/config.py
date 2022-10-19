import os
from .extensions import login_manager


class TestConfig(object):
    SECRET_KEY = "my secret key"
    basedir = os.path.abspath(os.path.dirname(__file__))
    # DB settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    login_manager.login_view = "login"

    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Enable email authentication
    USER_ENABLE_USERNAME = True  # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    USER_ENABLE_CONFIRM_EMAIL = False

    # ReCaptcha Settings
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    RECAPTCHA_PUBLIC_KEY = '6Lco4wsiAAAAAFI7WNBQ4730aj50b70ZwpThCVms'
    RECAPTCHA_PRIVATE_KEY = '6Lco4wsiAAAAAC1q79bhCBXqeVoGUJ21Uuh8ngqJ'

    # Flask_Mail Settings
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '63230bc4e9e304'
    MAIL_PASSWORD = 'ccd0d346245a48'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    SECURITY_PASSWORD_SALT = 'my_precious_two'

class Constants(object):
    TEMPLATE_FOLDER = '../../templates'