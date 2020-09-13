from flask import Flask , render_template ,redirect , jsonify ,url_for
from F8Tech.forms import RegistrationForm , UpdateForm , DateForm
from F8Tech import app ,db 
from F8Tech.models import User , DatePart 
from flask_sqlalchemy import SQLAlchemy

@app.route("/date" ,methods=["POST", "GET"])
def index():
    form= DateForm()
    if form.validate_on_submit():
        user= DatePart(name=form.name.data , salary = form.salary.data , location= form.location.data , dob=form.dob.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('check'))
    return render_template("home.html" , form =form)

@app.route("/register" ,methods=["POST", "GET"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('update'))
        user= User(name=form.name.data , salary = form.salary.data , location= form.location.data)
        db.session.add(user)
        db.session.commit()
        
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

@app.route("/",methods=["GET","POST"])
def date():
    user= db.session.query(User.salary).all()
    return render_template("date2.html",user=user)

@app.route("/check",methods=["Get"])
def check():
    user=DatePart.query.get(1)
    return render_template("check.html" , user=user)