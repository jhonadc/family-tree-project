from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm
from .. import db
from ..models import Role, User


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


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
