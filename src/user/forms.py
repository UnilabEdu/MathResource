from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from src.user.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name: ', [DataRequired()])
    last_name = StringField('Last Name: ', [DataRequired()])
    region = SelectField(u'region',
                         choices=[('shida-kartli', 'შიდა-ქართლი'),
                                  ('kvemo-kartli', 'ქვემო-ქართლი'),
                                  ('samtskhe-javakheti', 'სამცხე-ჯავახეთი'),
                                  ('mtskheta-mtianeti', 'მცხეთა-მთიანეთი'),
                                  ('kakheti', 'კახეთი'),
                                  ('imereti', 'იმერეთი'),
                                  ('adjara', 'აჭარა'),
                                  ('samegrelo', 'სამეგრელო'),
                                  ('guria', 'გურია'),
                                  ('racha-lechkhumi', 'რაჭა-ლეჩხუმი'),
                                  ('svaneti', 'სვანეთი'),
                                  ('aphkhazeti', 'აფხაზეთი')
                                  ])
    school = StringField('School: ', [DataRequired()])
    school_class = SelectField(u'school_class',
                         choices=[('I', 'I'),
                                  ('II', 'II'),
                                  ('III', 'III'),
                                  ('IV', 'IV'),
                                  ('V', 'V'),
                                  ('VI', 'VI'),
                                  ('VII', 'VII'),
                                  ('VIII', 'VIII'),
                                  ('IX', 'IX'),
                                  ('X', 'X'),
                                  ('XI', 'XI'),
                                  ('XII', 'XII'),])
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField(label="Confirm Password",
                                    validators=[EqualTo("password", message="passwords don't match")],
                                    render_kw={"placeholder": "Confirm Password"})

    rules = BooleanField(' ვეთანხმები კონფიდენციალურობის პოლიტიკას და გამოყენების პირობებებს', validators=[DataRequired()])

    submit = SubmitField('რეგისტრაცია')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')


class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    login = SubmitField('Login')
