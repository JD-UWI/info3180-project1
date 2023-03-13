"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
import math
from app import app, db
from flask import render_template, request, redirect, url_for,flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import NewProperty
from app.models import Properties



###
# Routing for your application.
###
rootdir = os.getcwd()

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET', 'POST'])
def newproperties():
    """Render the  form to add a new property."""
    form = NewProperty()

    if request.method == "POST":
        if form.validate_on_submit():
            # Save property information to database
            title = form.title.data
            description = form.description.data
            roomnum = form.roomnum.data
            bathnum = int(math.floor(float(form.bathnum.data)))
            propertytype = form.property.data
            location = form.location.data
            price = form.price.data
            image = form.photo.data
            imgname = secure_filename(image.filename)
            image.save(os.path.join(app.config['PROPERTIES'],imgname))

            propertyinfo = Properties(title, description, roomnum, bathnum, price, propertytype, location, imgname)

            db.session.add(propertyinfo)
            db.session.commit()

            flash('Property information saved successfully')
            return redirect(url_for("properties"))

    return render_template('newProperties.html',form=form)

@app.route('/properties')
def properties():
    """Render the a list of all properties in the database."""
    properties = Properties.query.all()

    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def propertyID(propertyid):
    """Render an individual property by the specific property id."""
    property = Properties.query.get(propertyid)
    if property is None:
        flash('ID Invalid, try again')
    return render_template('property.html', property=property)


@app.route('/properties/<filename>')    
def get_image(filename):
    return send_from_directory(app.config['PROPERTIES'],filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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
