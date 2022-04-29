from flask_user import UserMixin
from src.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    region = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    school = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    school_class = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)

    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')

    roles = db.relationship('Role', secondary='user_roles', lazy=True)

    answers = db.relationship('Answer', backref='users', lazy=True)


    def __init__(self, first_name, last_name, region, school, school_class, email, email_confirmed_at, password):
        self.email = email
        self.school_class = school_class
        self.school = school
        self.region = region
        self.last_name = last_name
        self.first_name = first_name
        self.email_confirmed_at = email_confirmed_at
        self.password = password

    def create(self):
        print(self)
        db.session.add(self)
        db.session.commit()




class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
