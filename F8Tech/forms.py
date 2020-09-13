from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField ,TextAreaField , IntegerField , DateField
from wtforms.validators import DataRequired, EqualTo ,ValidationError , Email , Length ,NoneOf

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

class DateForm(FlaskForm):
    name=StringField('Name' , validators=[DataRequired() , NoneOf(['!','@','#','$','%','^','&','*','(',')','-'])])
    salary= IntegerField('Salary', validators=[DataRequired()] )
    location = StringField('Location', validators=[Length(max=6)])
    dob = DateField('Date' , format='%Y-%m-%d')
    submit= SubmitField('Submit')


