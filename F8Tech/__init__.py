from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__) 
app.config['SECRET_KEY']='meowmeow'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)

from F8Tech import routes