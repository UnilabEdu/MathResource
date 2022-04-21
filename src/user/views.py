from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from src.user.forms import RegistrationForm, LoginForm
from src.user.models import User

user_blueprint = Blueprint('users',
                           __name__,
                           template_folder='templates/users')


@user_blueprint.route('/registration', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data
        region = form.region.data
        school = form.school.data
        school_class = form.school_class.data
        email = form.email.data
        password = form.password.data

        user = User(first_name, last_name, region,school ,school_class , email, password)

        try:
            user.create()
        except:
            flash("user registration failed", "danger")
        else:
            flash('user registered!', "success")

        form.first_name.data = ''
        form.last_name.data = ''
        form.school.data = ''
        form.school_class.data = ''
        form.email.data = ''
        form.password.data = ''

        return redirect(url_for('users.register_user'))

    return render_template('auth.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    print(form.validate_on_submit())

    if form.validate_on_submit():

        email = form.email.data

        user_by_email = User.get_by_email(email)

        if user_by_email and user_by_email.check_password(form.password.data):

            try:
                login_user(user_by_email)
            except:
                flash('login failed', 'danger')
                return render_template("login.html", form=form)
            else:
                flash('login successful', "success")
            next = request.args.get("next")

            if next is None:
                next = url_for('user.profile')

            return redirect(url_for("user.profile"))

        else:
            flash("such email doesn't exists", 'danger')

    return render_template("login.html", form=form)