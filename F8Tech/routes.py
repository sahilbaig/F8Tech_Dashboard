from flask import Flask , render_template ,redirect , jsonify ,url_for
from F8Tech.forms import RegistrationForm , UpdateForm 
from F8Tech import app ,db 
from F8Tech.models import User , DatePart  , DatePart2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime   #this part added
from wtforms.validators import InputRequired, Email, Length, AnyOf,ValidationError


@app.route("/register" ,methods=["POST", "GET"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        todays_datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
        user= DatePart(name=form.name.data , salary = form.salary.data , location= form.location.data , dob=form.dob.data ) #here added
        db.session.add(user)
        db.session.commit()
        user1=todays_datetime-user.dob
        user.age=int((user1.days)/365)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('update'))       
    return render_template("register.html" , form = form)

@app.route("/update", methods= ["GET"])
def update():
    user= DatePart.query.order_by(DatePart.id.desc())
    return render_template("update_page.html" , users=user)

@app.route("/update/<int:user_id>",methods=["GET","POST"])
def update_user(user_id):
    user= DatePart.query.get(user_id)
    form= UpdateForm()
    if form.validate_on_submit():
        user.name=form.name.data
        user.salary=form.salary.data
        user.location=form.location.data
        user.dob=form.dob.data
        todays_datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day) #this part here       
        db.session.commit()
        user1=todays_datetime-user.dob
        user.age=int((user1.days)/365)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('update'))
    form.name.data= user.name
    form.location.data = user.location
    form.salary.data = user.salary
    form.dob.data=user.dob
    return render_template("update_user.html" , form=form)

@app.route("/",methods=["GET","POST"])
def date():
    user1=db.session.query(func.avg(DatePart.salary)).group_by(DatePart.age).order_by(DatePart.age.asc()).all()
    result_list=[]
    result_list = [row[0] for row in user1]

    user2=db.session.query(DatePart.age).group_by(DatePart.age).order_by(DatePart.age.asc()).all()
    result_list2=[]
    result_list2 = [row[0] for row in user2]

    les=len(result_list2)
    list_new=[]
    for i in range(0,les):
        list_new.append(result_list2[i])


    return render_template("date2.html",user=result_list,age=list_new)

