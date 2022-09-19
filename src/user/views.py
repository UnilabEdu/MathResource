import datetime
import uuid
import os
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from flask_mail import Message
from flask_user import current_user
from src.user.forms import RegistrationForm, LoginForm, ForgotForm, UpdatePass
from src.user.models import User, BaseModel
from src.extensions import login_manager, mail
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from src.config import TestConfig
from itsdangerous import URLSafeSerializer
from src.mail_funcs.funcs import send_mail, generate_confirmation_token, confirm_token


auth_blueprint = Blueprint('auth',
                           __name__,
                           template_folder='templates')

ts = URLSafeSerializer(TestConfig.SECRET_KEY)


@auth_blueprint.route('/registration', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        print('validated')
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        register = User()

        register.create(first_name=form.first_name.data, last_name=form.last_name.data, region=form.region.data,
                        school=form.school.data, school_class=form.school_class.data, email=form.email.data,
                        password=hashed_password)
        register.save()

        token = generate_confirmation_token(form.email.data)
        confirm_url = url_for('auth.confirm', token=token, _external=True)
        html = render_template('verify.html', confirm_url=confirm_url)

        send_mail(form.email.data, html)

        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/confirm/<token>')
def confirm(token):
    try:
        email = confirm_token(token)
    except :
        flash('The Confirmation link is Invalid')

    user = User.query.filter_by(email=email).first()
    if user:
        print(user.email_confirmed_at)
        user.update(email_confirmed_at=datetime.datetime.now())
        user.save()

    return redirect(url_for('auth.login')), flash('საღოლ')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.email_confirmed_at:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"{user.email} logged in successfully")
                return redirect(url_for("main.main"))
            else:
                flash('login failed', 'danger')
        else:
            return redirect(url_for('auth.login_error'))
    return render_template("auth.html", form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    flash("Successfully logged out")
    return redirect(url_for('main.main'))

@auth_blueprint.route('/password_reset', methods=['GET', 'POST'])
def reset():
    form = ForgotForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            token = generate_confirmation_token(form.email.data)
            confirm_url = url_for('auth.reset_verified', token=token, _external=True)
            html = render_template('password_reset_link.html', confirm_url=confirm_url)

            send_mail(user.email, html)

        return redirect(url_for('auth.login'))
    return render_template('forgot.html', form=form)


@auth_blueprint.route('/password_reset_verified/<token>', methods=['GET', 'POST'])
def reset_verified(token):
    form = UpdatePass()
    email = confirm_token(token)
    user = User.query.filter_by(email=email).first()
    if not user:
        print('no user found')
        return redirect(url_for('auth.login'))

    password = request.form.get('password')

    if password:

        user.password = None
        hashed_password = generate_password_hash(password, method='sha256')
        user.update(password=hashed_password)
        user.save()
        return redirect(url_for('auth.login'))

    return render_template('password_reset.html', form=form)


@auth_blueprint.route('/login_error', methods=['GET', 'POST'])
def login_error():
    return render_template('login_error.html')


