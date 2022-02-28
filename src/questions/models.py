from src.extensions import db


class Task(db.model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    steps = db.relationship('TaskStep', backref='tasks', lazy=True)


class TaskStep(db.model):
    __tablename__ = "task_steps"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.collumn(db.Integer, db.ForeignKey(Task.id))
    answers = db.relationship('Answer', backref='task_steps', lazy=True)


class Answer(db.model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    task_step_id = db.Column(db.Integer, db.ForeignKey('task_steps.id'))


class UsersTasks(db.model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    task_id = db.Column(db.Integer(), db.ForeignKey('tasks.id', ondelete='CASCADE'))
