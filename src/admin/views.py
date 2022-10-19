from flask import Blueprint, render_template, request
from src.models.user import User

admins_blueprint = Blueprint('admins',
                             __name__,
                             template_folder='templates/admin')


@admins_blueprint.route('/')
def admin():
    return render_template("admin/index.html")


@admins_blueprint.route('/task_progress')
def task_progress():
    return render_template("admin/task_progress.html")


@admins_blueprint.route('/user_stats', methods=['POST', 'GET'])
def user_stats():
    user_id = request.form['get_id']
    user = User.query.get(user_id)
    return render_template('admin/task_progress.html', user=user)
