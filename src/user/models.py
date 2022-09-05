from flask_user import UserMixin
from src.extensions import db


class BaseModel(db.Model):
    """
    this class describes sqlalchemy db model  with basic crud functions
    attribs :
        - id : Primary Key

    methods :
        - Create
        - Read
        - Update
        - Delete
        - Save
        - Read_all
    """

    __abstract__ = True

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    @classmethod
    def read_all(cls):
        return cls.query.all()

    @classmethod
    def read(cls, name):
        return cls.query.filter_by(name=name).first()  # could use .all()#

        # cls.query.filter(cls.age >= 2)

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    region = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    school = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    school_class = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)

    email_confirmed_at = db.Column(db.DateTime(), nullable=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

    roles = db.relationship('Role', secondary='user_roles', lazy=True)

    answers = db.relationship('Answer', backref='users', lazy=True)

    def __init__(self, first_name, last_name, region, school, school_class, email, email_confirmed_at, password):
        self.email = email
        self.school_class = school_class
        self.school = school
        self.region = region
        self.last_name = last_name
        self.first_name = first_name
        self.email_confirmed_at = email_confirmed_at
        self.password = password

    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})


class Role(BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.name


class UserRoles(BaseModel):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class Teacher(BaseModel, UserMixin):
    __tablename__ = 'Teachers'

    id = db.Column(db.Integer(), primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    region = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    school = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)

    email_confirmed_at = db.Column(db.DateTime(), nullable=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

    # roles = db.relationship('Role', lazy=True)

    def __init__(self, first_name, last_name, region, school, email, email_confirmed_at, password):
        self.email = email
        self.school = school
        self.region = region
        self.last_name = last_name
        self.first_name = first_name
        self.email_confirmed_at = email_confirmed_at
        self.password = password

    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})


class Contacts(BaseModel):
    __tablename__ = 'Contacts'

    id = db.Column(db.Integer(), primary_key=True)
    contact_source = db.Column(db.Text(96), unique=True)
    info = db.Column(db.Text(192), unique=True)

    def __init__(self, contact_source, info):
        self.contact_source = contact_source
        self.info = info


class About(BaseModel):
    __tablename__ = 'About'

    id = db.Column(db.Integer(), primary_key=True)
    info = db.Column(db.Text(), unique=True)

    def __init__(self, info):
        self.info = info


class Team(BaseModel):
    __tablename__ = 'Team'

    id = db.Column(db.Integer(), primary_key=True)
    person = db.Column(db.Text(), nullable=True)
    position = db.Column(db.Text(), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    linkedin = db.Column(db.Text(), nullable=True)
    github = db.Column(db.Text(), nullable=True)
    dribble = db.Column(db.Text(), nullable=True)
    behance = db.Column(db.Text(), nullable=True)

    def __init__(self, person, position, **kwargs):
        self.person = person
        self.position = position
        # self.description = []
        # self.linkedin = []
        # self.github = []
        # self.dribble = []
        # self.behance = []

    def __repr__(self):
        f'Info: {self.person} {self.position} {self.description} Contacts: {self.linkedin} {self.github} {self.dribble} {self.behance}'


class Documents(BaseModel):
    __tablename__ = 'Documents'

    id = db.Column(db.Integer(), primary_key=True)
    doc_type = db.Column(db.String(), unique=True)
    doc_content = db.Column(db.Text())
