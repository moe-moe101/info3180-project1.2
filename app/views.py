"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import psycopg2

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.models import Profile
from app.forms import AddProfileForm

# Routes for application

@app.route('/')
def home():
    """Render Home Page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render about page"""
    return render_template('about.html')

@app.route('/profiles')
def display_profiles():
    profiles = Profile.query.all()
    return render_template('profiles.html', profiles=profiles)

@app.route('/profile/<userid>')
def display_specific_profile(userid):
    profile = Profile.query.filter_by(userid ='userid').first()
    return render_template('userprofile.html', userid=userid)

@app.route('/profile',methods=['POST','GET'])
def profile():
    profile_form = AddProfileForm()
    if request.method =='POST' and profile_form.validate_on_submit():
        profile = Profile(profile_form.firstname.data, profile_form.lastname.data, profile_form.gender.data, profile_form.email.data, profile_form.location.data, profile_form.biography.data)
        db.session.add(profile)
        db.session.commit()

        flash('Profile successfully added','success')
        return redirect (url_for('profiles'))
    #else:
        #flash_errors(profile_form)
    return render_template('profile.html')

#Additional routing applicable to all flask apps.

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404