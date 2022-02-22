from flask_user import UserMixin
from src.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')

    users = db.relationship('Answer', backref='answers')

    roles = db.relationship('Role', secondary='user_roles')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class Task(db.model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    steps = db.relationship('TaskStep', backref='task_steps')


class TaskStep(db.model):
    __tablename__ = "task_steps"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.collumn(db.Integer, db.ForeignKey(Task.id))
    answer_id = db.relationship('Answer', backref='answers')


class Answer(db.model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    task_step_id = db.Column(db.Integer, db.ForeignKey(TaskStep.id))


class UsersTasks(db.model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('tasks.id', ondelete='CASCADE'))
