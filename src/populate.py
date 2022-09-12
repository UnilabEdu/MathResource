from src.user.models import User, Role, UserRoles, Teacher, Team
from src.extensions import db
from werkzeug.security import generate_password_hash
from src import create_app
import datetime

application = create_app()
application.app_context().push()


db.drop_all()
db.create_all()


def my_function():
    with application.app_context():
        user1 = User(first_name='Name', last_name='lastname', region='tbilisi', email_confirmed_at=None, school='43',
                     school_class='2a', email='user@user.com',
                     password=generate_password_hash('password123', method='sha256'), )
        user2 = User(first_name='Name2', last_name='lastname2', region='tbilisi2', email_confirmed_at=None,
                     school='432', school_class='2a2', email='user2@user.com',
                     password=generate_password_hash('password123', method='sha256'), )
        teacher1 = Teacher(first_name='Teacher', last_name='Teacher', region='tbilisi', email_confirmed_at=None,
                           school='55',
                           email='user@user.com',
                           password=generate_password_hash('password123', method='sha256'), )
        role1 = Role(name='User')
        role2 = Role(name='Admin')
        db.session.add_all([role1, role2])
        db.session.flush()
        db.session.add_all([user1, user2])
        db.session.commit()
        db.session.add(teacher1)
        user_role1 = UserRoles(user_id=user1.id, role_id=role1.id)
        user_role2 = UserRoles(user_id=user2.id, role_id=role2.id)
        db.session.add_all([user_role1, user_role2])
        db.session.commit()


my_function()

team_info = [
        {
            "person": "სანდრო ასათიანი",
            "position": "ოუნერი",
        }, {
            "person": "თემო ჩიჩუა",
            "position": "ოუნერი Back-End დეველოპერი",
        }, {
            "person": "ანანო ასპანიძე",
            "position": "პროექტის მენეჯერი (ჰედი)",
        }, {
            "person": "ნენე არაბული",
            "position": "დიზაინი (ჰედი)",
        }, {
            "person": "მარიშა არაბული",
            "position": "დიზაინი (ჰედი)",
        }, {
            "person": "ეკატერინა ხარბედია",
            "position": "დიზაინი (ჰედი)",
        }, {
            "person": "ნოკა ყიფიანი",
            "position": "Front-End დეველოპერი",
        }, {
            "person": "დავით ცალანი",
            "position": "Front-End დეველოპერი",
        }, {
            "person": "დავით ჭინჭარაშვილი",
            "position": "Back-End დეველოპერი",
        }, {
            "person": "გიორგი მხეიძე",
            "position": "პროექტის მენეჯერი",
        }, {
            "person": "ოთო ბენიაიძე",
            "position": "დიზაინი",
        }, {
            "person": "ლუკა ბლიაძე",
            "position": "Front-End დეველოპერი",
        }, {
            "person": "მერი გოგიჩაშვილი",
            "position": "Front-End დეველოპერი",
        }, {
            "person": "გიორგი ბიწაძე",
            "position": "Front-End დეველოპერი",
        }, {
            "person": "ნიკა ქვრივიშვილი",
            "position": "Back-End დეველოპერი",
        },
    ]


def populate_team():
    for el in team_info:
        team_member = Team(**el)
        team_member.create(commit=True)
    return


populate_team()
