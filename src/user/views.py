from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from src.user.forms import RegistrationForm, LoginForm
from src.user.models import User
from src.extensions import login_manager, BaseModel
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth',
                           __name__,
                           template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
        # # print("after validate")
        # first_name = form.first_name.data
        # last_name = form.last_name.data
        # region = form.region.data
        # school = form.school.data
        # school_class = form.school_class.data
        # email = form.email.data
        # password = form.password.data
        #
        # user = User(
        #     first_name,
        #     last_name,
        #     region,
        #     school,
        #     school_class,
        #     email,
        #     func.now(),
        #     password
        # )

        # print(user)

        try:
            register.save()
        except:
            flash("user registration failed", "danger")
        else:
            flash('user registered!', "success")

        # form.first_name.data = ''
        # form.last_name.data = ''
        # form.school.data = ''
        # form.school_class.data = ''
        # form.email.data = ''
        # form.password.data = ''

        return redirect(url_for('auth.profile'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # email = form.email.data
        #
        # user_by_email = User.get_by_email(email)
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"{user.username} logged in succesfully")
                return redirect(url_for("auth.profile"))
            else:
                flash('login failed', 'danger')
        else:
            flash("User by that email does not exist")

        # if user_by_email and user_by_email.check_password(form.password.data):
        #
        #     try:
        #         login_user(user_by_email)
        #     except:
        #         flash('login failed', 'danger')
        #         return render_template("login.html", form=form)
        #     else:
        #         flash('login successful', "success")
        #     next = request.args.get("next")
        #
        #     if next is None:
        #         next = url_for('user.profile')
        #
        #     return redirect(url_for("user.profile"))
        #
        # else:
        #     flash("such email doesn't exists", 'danger')

    return render_template("auth.html", form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    flash("Succesfully logged out")
    return redirect(url_for('main.index'))
