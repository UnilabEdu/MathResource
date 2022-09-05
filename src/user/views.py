from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from src.user.forms import RegistrationForm, LoginForm
from src.user.models import User, BaseModel
from src.extensions import login_manager
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth',
                           __name__,
                           template_folder='templates')





@auth_blueprint.route('/registration', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    # return request.args
    # print("Before validation")
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        register = User(first_name=form.first_name.data, last_name=form.last_name.data, region=form.region.data,
                        school=form.school.data, school_class=form.school_class.data, email=form.email.data,
                        password=hashed_password)
        try:
            register.save()
        except:
            flash("user registration failed", "danger")
        else:
            flash('user registered!', "success")

        return redirect(url_for('auth.profile'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"{user.email} logged in succesfully")
                return redirect(url_for("main.main"))
            else:
                flash('login failed', 'danger')
        else:
            flash("User by that email does not exist")
    return render_template("auth.html", form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    flash("Succesfully logged out")
    return redirect(url_for('main.main'))
