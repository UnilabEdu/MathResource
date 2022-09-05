from flask import Blueprint, render_template
from src.user.models import Contacts, About, Team, Documents

main_blueprint = Blueprint('main',
                           __name__,
                           template_folder='templates/main')


@main_blueprint.route('/')
def main():
    return render_template("index.html")


@main_blueprint.route('/contacts')
def contacts():
    contact_info = Contacts.read_all()
    return render_template('contacts.html', contact_info=contact_info)


@main_blueprint.route('/about_project')
def about():
    about_info = About.read_all()
    team_info = Team.read_all()
    return render_template('about.html', about=about_info, team=team_info)


@main_blueprint.route('/terms_and_conditions')
def terms_and_conditions():
    documents = Documents.read_all()
    return render_template('terms_and_conditions.html', documents=documents)


@main_blueprint.route('/example_page')
def example_page():
    return render_template('example.html')


@main_blueprint.route('/not_found')
def not_found():
    return render_template('example.html')
