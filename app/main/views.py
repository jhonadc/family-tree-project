from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/learn.html')
def learn():
    return render_template('learn.html')


@main.route('/discover.html')
def discover():
    return render_template('discover.html')


@main.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')


@main.route('/albuns.html')
def albuns():
    return render_template('albuns.html')
