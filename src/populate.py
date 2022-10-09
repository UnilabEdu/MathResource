from src.user.models import User, Roles, Team
from src.questions.models import UsersTasks, Task
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
        user1 = User()
        user1.create(first_name='Name', last_name='lastname', region='tbilisi', school='43',
                     school_class='2a', email='user@user.com',
                     password=generate_password_hash('password123', method='sha256'),
                     email_confirmed_at=datetime.datetime.now())
        user2 = User()
        user2.create(first_name='Name2', last_name='lastname2', region='tbilisi2',
                     school='432', school_class='2a2', email='user2@user.com',
                     password=generate_password_hash('password123', method='sha256'),
                     email_confirmed_at=datetime.datetime.now(), role_id=2)

        role1 = Roles(name='User')
        role2 = Roles(name='Admin')
        db.session.add_all([role1, role2])
        db.session.flush()
        db.session.add_all([user1, user2])
        db.session.commit()
        task_1 = UsersTasks(user_id=user2.id,task_id='1',correct='False', used_hint='True', skipped='False')
        db.session.add(task_1)
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
