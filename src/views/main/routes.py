from flask import Blueprint, render_template
from src.models.user import Contacts, About, Team, Documents
from flask_login import login_required
from src.config import Constants

main_blueprint = Blueprint('main',
                           __name__,
                           template_folder=Constants.TEMPLATE_FOLDER)


@main_blueprint.route('/')
def main():
    return render_template("main/index.html")


@main_blueprint.route('/contacts')
def contacts():
    contact_info = Contacts.read_all()
    return render_template('main/contacts.html', contact_info=contact_info)


@main_blueprint.route('/about_project')
def about():
    about_info = About.read_all()
    team_info = Team.read_all()
    return render_template('main/about.html', about=about_info, team=team_info)


@main_blueprint.route('/terms_and_conditions')
def terms_and_conditions():
    documents = Documents.read_all()
    return render_template('main/terms_and_conditions.html', documents=documents)


@main_blueprint.route('/example_page')
def example_page():
    return render_template('main/example.html')


@main_blueprint.route('/not_found')
def not_found():
    return render_template('main/example.html')


@main_blueprint.route('/intern_page')
@login_required
def intern_page():
    return render_template('main/internpage.html')


@main_blueprint.route('/statistics')
def statistics_page():
    return render_template('main/mathProblems.html')



