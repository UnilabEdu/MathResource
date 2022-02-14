from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from src.user.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name: ', [DataRequired()])
    last_name = StringField('Last Name: ', [DataRequired()])
    region = SelectField(u'Programming Language', choices=[('region', 'region')])
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])

    rules = BooleanField(' ვეთანხმები კონფიდენციალუროპის პოლიტიკის და გამოყენების პირობებებს', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')


class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    login = SubmitField('Login')
