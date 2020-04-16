from . import db
#CREATE EXTENSION pg-images

from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment

Base = declarative_base()

class Profile(db.Model):
    __tablename__ = 'user_profiles'

    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String (80))
    gender = db.Column(db.String(20))
    email = db.Column(db.String(120), unique = True)
    location = db.Column(db.String(120))
    biography = db.Column(db.String(350))
    photo = image_attachment('UserPicture')
    created_on = db.Column(db.DATE)

    

    def __init__(self,firstname, lastname, gender, email, location, biography,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo =photo

    def __repr__(self):
        return '<Profile %r %r>' %self.firstname %self.lastname

class UserPicture(Base, Image):
   # """User picture model."""

    user_id = Column(Integer, ForeignKey('profile.id'), primary_key=True)
    user = relationship('User')
    __tablename__ = 'user_picture'

        