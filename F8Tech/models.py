from F8Tech import db

class User(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String , nullable=False)
    salary= db.Column(db.Integer , nullable= False)
    location= db.Column(db.Integer , nullable= False)
    dob= db.Column(db.DateTime , nullable=False)

class DatePart(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String , nullable=False)
    salary= db.Column(db.Integer , nullable= False)
    location= db.Column(db.String , nullable= False)
    dob= db.Column(db.DateTime , nullable=False)
    age=db.Column(db.Integer , nullable=True)


class DatePart2(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String , nullable=False)
    salary= db.Column(db.Integer , nullable= False)
    location= db.Column(db.Integer , nullable= False)
    dob= db.Column(db.DateTime , nullable=False)
    

class DateAge(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    age=db.Column(db.Integer ,nullable=True)