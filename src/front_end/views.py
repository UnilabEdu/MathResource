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
    # should be replaced with data from database
    team_info = [
        {
            "person":"სანდრო ასათიანი",
            "position":"ოუნერი",
        },        {
            "person":"თემო ჩიჩუა",
            "position":"ოუნერი Back-End დეველოპერი",
        },        {
            "person":"ანანო ასპანიძე",
            "position":"პროექტის მენეჯერი (ჰედი)",
        },        {
            "person":"ნენე არაბული",
            "position":"დიზაინი (ჰედი)",
        },        {
            "person":"მარიშა არაბული",
            "position":"დიზაინი (ჰედი)",
        },        {
            "person":"ეკატერინა ხარბედია",
            "position":"დიზაინი (ჰედი)",
        },        {
            "person":"ნოკა ყიფიანი",
            "position":"Front-End დეველოპერი",
        },        {
            "person":"დავით ცალანი",
            "position":"Front-End დეველოპერი",
        },        {
            "person":"დავით ჭინჭარაშვილი",
            "position":"Back-End დეველოპერი",
        },        {
            "person":"გიორგი მხეიძე",
            "position":"პროექტის მენეჯერი",
        },        {
            "person":"ოთო ბენიაიძე",
            "position":"დიზაინი",
        },        {
            "person":"ლუკა ბლიაძე",
            "position":"Front-End დეველოპერი",
        },       {
            "person":"მერი გოგიჩაშვილი",
            "position":"Front-End დეველოპერი",
        },       {
            "person":"გიორგი ბიწაძე",
            "position":"Front-End დეველოპერი",
        },      {
            "person":"ნიკა ქვრივიშვილი",
            "position":"Back-End დეველოპერი",
        },
    ]
    return render_template('about.html', team=team_info)

@main_blueprint.route('/example_page')
def example_page():
    return render_template('example.html')

@main_blueprint.route('/not_found')
def not_found():
    return render_template('example.html')
