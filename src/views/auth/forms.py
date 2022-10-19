from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, BooleanField, validators
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms import ValidationError
from src.models.user import User


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
                                        ('XII', 'XII'), ])
    email = EmailField('Email', validators=[DataRequired(), Length(max=60), validators.Email()])

    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=64),
                                         EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField(label="Confirm Password",
                                 validators=[EqualTo("password", message="passwords don't match")],
                                 render_kw={"placeholder": "Confirm Password"})

    rules = BooleanField(' ვეთანხმები კონფიდენციალურობის პოლიტიკას და გამოყენების პირობებებს',
                         validators=[DataRequired()])

    recaptcha = RecaptchaField()

    submit = SubmitField('რეგისტრაცია')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')


class LoginForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    region = StringField()
    school = StringField()
    school_class = StringField()
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    pass_confirm = StringField()
    rules = StringField()
    login = SubmitField('Login')
    submit = SubmitField('შესვლა')


class ForgotForm(FlaskForm):
    email = EmailField('Email', [DataRequired()])
    submit = SubmitField()


class UpdatePass(FlaskForm):
    password = PasswordField('Password', [DataRequired(), Length(min=8, max=64)], render_kw={"placeholder": "პაროლი"})
    pass_confirm = PasswordField(label="Confirm Password",
                                 validators=[EqualTo("password", message="passwords don't match")],
                                 render_kw={"placeholder": "გაიმეორე პაროლი"})
    submit = SubmitField()


class UpdateProfile(FlaskForm):
    first_name = StringField('First Name: ', [DataRequired()])
    last_name = StringField('Last Name: ', [DataRequired()])
    region = SelectField(u'region', [DataRequired()],
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
                                  ], )
    school = StringField('School: ', [DataRequired()])
    school_class = SelectField(u'school_class', [DataRequired()],
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
                                        ('XII', 'XII'), ])
    email = EmailField('Email', validators=[DataRequired(), Length(max=60), validators.Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=64),
                                                     EqualTo('pass_confirm', message='Passwords Must Match!')],
                             render_kw={"placeholder": "Password"})
    pass_confirm = PasswordField(label="Confirm Password",
                                 validators=[DataRequired(), EqualTo("password", message="passwords don't match")],
                                 render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField('პროფილის განახლება')
