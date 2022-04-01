from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def example():
    return render_template('example.html')