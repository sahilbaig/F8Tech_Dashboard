from F8Tech import db

class User(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String , nullable=False)
    salary= db.Column(db.Integer , nullable= False)
    location= db.Column(db.String , nullable= False)
    