
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewProperty(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    roomnum = StringField('No. of Rooms', validators=[InputRequired()])
    bathnum = StringField('No. of Bathrooms', validators=[InputRequired()])
    property = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])