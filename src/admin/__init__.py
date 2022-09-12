from flask import redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink
from flask_user import current_user

from src.extensions import db
from src.user.models import User


class AuthMixin(object):

    def is_accessible(self):
        return current_user.has_roles('Admin')

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))


class LogOutLink(MenuLink):
    def get_url(self):
        return url_for("auth.logout")


class AdminModelView(ModelView):
    pass


class TeacherModelView(ModelView, AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_exclude_list = ['password', ]
    column_searchable_list = ['first_name', 'last_name', 'email']
    column_filters = ['last_name', 'school']
    column_editable_list = ['email', 'school']
    can_export = True


class UserView(ModelView, AuthMixin):
    can_create = True
    can_delete = False
    can_edit = True
    column_exclude_list = ['password', ]
    column_searchable_list = ['first_name', 'last_name', 'email']
    column_filters = ['roles']
    column_editable_list = ['roles']
    can_export = True


class RoleView(ModelView, AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name']
    can_export = True


class StaticView(FileAdmin, AuthMixin):
    can_export = True


class UsersTasksView(ModelView, AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_searchable_list = ['user_id', 'task_id']
    column_list = ('user_id', 'task_id', 'correct', 'used_hint')
    can_export = True


class UserRolesView(ModelView, AuthMixin):
    can_create = False
    can_delete = True
    can_edit = True
    column_searchable_list = ['id', 'user_id', 'role_id']
    column_list = ('id', 'user_id', 'role_id')
    column_filters = ['role_id']
    # column_editable_list = ['role_id']
    can_export = True


class ContactsView(ModelView, AuthMixin):
    can_create = True
    can_delete = True
    can_edit = True
    column_list = ('contact_source', 'info')


class AboutView(ModelView, AuthMixin):
    can_create = True
    can_delete = True
    can_edit = True
    column_list = ('info',)


class TeamView(ModelView, AuthMixin):
    can_create = True
    can_edit = True
    column_filters = ['position']
    column_list = ('person', 'position', 'description', 'linkedin', 'github', 'dribble', 'behance')


class DocumentsView(ModelView, AuthMixin):
    can_edit = True
    can_delete = True
    can_create = True
    column_list = ('doc_type', 'doc_content')
    column_filters = ['doc_type']


admin = Admin(name="Admin Panel", template_mode="bootstrap4")
