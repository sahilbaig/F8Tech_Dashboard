from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField ,TextAreaField , IntegerField , DateField
from wtforms.validators import DataRequired, EqualTo ,ValidationError , Email , Length

class RegistrationForm(FlaskForm):
    name=StringField('Name' , validators=[DataRequired()])
    salary= IntegerField('Salary', validators=[DataRequired()] )
    location = StringField('Location', validators=[Length(max=6)])
    submit= SubmitField('Submit')

class UpdateForm(FlaskForm):
    name=StringField('Name' , validators=[DataRequired()])
    salary= IntegerField('Salary', validators=[DataRequired()] )
    location = StringField('Location', validators=[Length(max=6)])
    submit= SubmitField('Update')
