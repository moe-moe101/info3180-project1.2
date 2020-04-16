from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.fields import SelectField

class AddProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender Type', choices=[('Female','female'),('Male','male'),('Other','other')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired('File was empty!'), FileAllowed(['jpg', 'png', 'Images only!'])])

