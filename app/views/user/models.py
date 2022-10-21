from app.extensions import db, ma
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.now)


class UserSchema(ma.SQLAlchemyAutoSchema):  # User serializer
    class Meta:
        model = User
