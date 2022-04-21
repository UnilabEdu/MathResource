from flask import Blueprint, render_template

main_blueprint = Blueprint('main',
                           __name__,
                           template_folder='templates/main')


@main_blueprint.route('/')
def main():
    return render_template("index.html")


@main_blueprint.route('/contacts')
def contacts():
    return render_template('contacts.html')


@main_blueprint.route('/about_project')
def about():
    return render_template('about.html')

@main_blueprint.route('/example_page')
def example_page():
    return render_template('example.html')

@main_blueprint.route('/not_found')
def not_found():
    return render_template('example.html')
