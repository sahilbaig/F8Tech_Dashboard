from flask import Flask , render_template ,redirect , url_for
from F8Tech.forms import RegistrationForm , UpdateForm
from F8Tech import app ,db 
from F8Tech.models import User
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/register" ,methods=["POST", "GET"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user= User(name=form.name.data , salary = form.salary.data , location= form.location.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('update'))
    return render_template("register.html" , form = form)

@app.route("/update", methods= ["GET"])
def update():
    user= User.query.order_by(User.id.desc())
    return render_template("update_page.html" , users=user)

@app.route("/update/<int:user_id>",methods=["GET","POST"])
def update_user(user_id):
    user= User.query.get(user_id)
    form= UpdateForm()
    if form.validate_on_submit():
        user.name=form.name.data
        user.salary=form.salary.data
        user.location=form.location.data
        db.session.commit()
        return redirect(url_for('update'))
    form.name.data= user.name
    form.location.data = user.location
    form.salary.data = user.salary
    return render_template("update_user.html" , form=form)

@app.route("/date",methods=["GET","POST"])
def date():
    return render_template("date.html")