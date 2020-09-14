from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField ,TextAreaField , IntegerField , DateField
from wtforms.validators import DataRequired, EqualTo ,ValidationError , Email , Length ,NoneOf
from wtforms_validators import AlphaNumeric , Integer

class RegistrationForm(FlaskForm):
    name=StringField('Name' , validators=[DataRequired(), AlphaNumeric(message="Special characters not allowed")])
    salary= StringField('Salary', validators=[DataRequired() , Integer(message=' Should be numeric only')] )
    location = StringField('Location', validators=[Length(max=6 , message='Should not exceed 6 characters'), Integer(message='Should be numeric only')])
    dob = DateField('Date of Birth')     
    # format='%Y-%m-%d'
    submit= SubmitField('Submit')


class UpdateForm(FlaskForm):
    name=StringField('Name' , validators=[DataRequired(), AlphaNumeric(message="Special characters not allowed") ])
    # salary= IntegerField('Salary', validators=[DataRequired() ])
    salary= StringField('Salary', validators=[DataRequired() , Integer(message='Should be numeric only')] )

    location = StringField('Location', validators=[Length(max=6 , message='Should not exceed 6 characters'), Integer(message='Should be numeric only') ])
    dob = DateField('Date of Birth')
    submit= SubmitField('Update')


