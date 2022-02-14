from my_project import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from my_project.extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.email

    @classmethod
    def get_by_id(cls, _id):
        user_by_id = User.query.get(_id)
        return user_by_id

    @classmethod
    def get_by_email(cls, email):
        user_by_email = User.query.filter_by(email=email).first()
        return user_by_email

    def create(self):
        db.session.add(self)
        db.session.commit()
