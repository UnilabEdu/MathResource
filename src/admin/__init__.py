from flask import redirect, url_for, request
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink
from flask_user import current_user
from src.models.question import UsersTasks
from markupsafe import Markup
from flask_admin.helpers import get_form_data

from src.models.user import User


class AuthMixin(ModelView):

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.has_roles('Admin')
        else:
            return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class LogOutLink(MenuLink):
    def get_url(self):
        return url_for("auth.logout")


class AdminView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            print(current_user)
            return current_user.has_roles('Admin')
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class AdminModelView(AuthMixin):
    pass


class TeacherModelView(AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_exclude_list = ['password', ]
    column_searchable_list = ['first_name', 'last_name', 'email']
    column_filters = ['last_name', 'school']
    column_editable_list = ['email', 'school']
    can_export = True


class UserView(AuthMixin):
    can_create = True
    can_delete = False
    column_list = ("first_name", "last_name", "region", "school", "school_class", "email", 'email_confirmed_at', 'Tasks')
    column_exclude_list = ['password', ]
    column_searchable_list = ['first_name', 'last_name', 'email']
    can_export = True
    # form_overrides = dict(email_confirmed_at=DateTimeField)

    def use_button(view, context, model, name):
        checkout_url = url_for('.checkout_view')

        _html = '''
                    <form action="{checkout_url}" method="POST">
                        <input id="user_id" name="user_id"  type="hidden" value="{user_id}">
                        <button type='submit'>Checkout</button>
                    </form>
                '''.format(checkout_url=checkout_url, user_id=model.id)

        return Markup(_html)

    column_formatters = {
        'Tasks': use_button
    }

    @expose('/checkout', methods=['POST'])
    def checkout_view(self):
        form = get_form_data()
        user_id = form['user_id']
        user_tasks = UsersTasks.query.filter_by(user_id=user_id).all()


        return self.render('admin/result.html', user_tasks = user_tasks)

class RoleView(AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name']
    can_export = True


class StaticView(FileAdmin):
    can_export = True


class UsersTasksView(AuthMixin):
    can_create = False
    can_delete = False
    can_edit = True
    column_searchable_list = ['user_id', 'task_id']
    column_list = ('user_id', 'task_id', 'correct', 'used_hint')
    can_export = True


class UserRolesView(AuthMixin):
    can_create = False
    can_delete = True
    can_edit = True
    column_searchable_list = ['id', 'user_id', 'role_id']
    column_list = ('id', 'user_id', 'role_id')
    column_filters = ['role_id']
    # column_editable_list = ['role_id']
    can_export = True


class ContactsView(AuthMixin):
    can_create = True
    can_delete = True
    can_edit = True
    column_list = ('contact_source', 'info')


class AboutView(AuthMixin):
    can_create = True
    can_delete = True
    can_edit = True
    column_list = ('info',)


class TeamView(AuthMixin):
    can_create = True
    can_edit = True
    column_filters = ['position']
    column_list = ('person', 'position', 'description', 'linkedin', 'github', 'dribble', 'behance')


class DocumentsView(AuthMixin):
    can_edit = True
    can_delete = True
    can_create = True
    column_list = ('doc_type', 'doc_content')
    column_filters = ['doc_type']


class TestView(BaseView):
    @expose('/')
    def test(self):
        users = User.query.all()
        return self.render('admin/test_html.html', users=users)


admin = Admin(name="Admin Panel", template_mode='bootstrap4', index_view=AdminView())

