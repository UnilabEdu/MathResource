from flask import redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_user import current_user

from src.extensions import db
from src.user.models import User

admin = Admin(name="Admin Panel", template_mode="bootstrap4")


class LogOutLink(MenuLink):
    def get_url(self):
        return url_for("auth.log_out")


class AdminModelView(ModelView):

    def is_accessible(self):
        # როგორ მოხდეს მომხმარებლის ვალიდაცია
        # კონკრეტული როლით
        if current_user.is_authenticated and current_user.has_roles("Admin"):
            return True

    def inaccessible_callback(self, name, **kwargs):
        # რა მოხდეს არაავტორიზებული იუზერის შემთხვევაში
        return redirect(url_for("user.login", next=request.url))


class TeacherModelView(ModelView):

    def is_accessible(self):
        # როგორ მოხდეს მომხმარებლის ვალიდაცია
        # კონკრეტული როლით
        if current_user.is_authenticated:
            return True

    def inaccessible_callback(self, name, **kwargs):
        # რა მოხდეს არაავტორიზებული იუზერის შემთხვევაში
        return redirect(url_for("user.login", next=request.url))


admin.add_view(AdminModelView(User, db.session))
admin.add_link(LogOutLink(name="Logout"))
