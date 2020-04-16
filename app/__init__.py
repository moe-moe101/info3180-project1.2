from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wh@tw!llw3do20d@y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mamos2009@localhost/mamos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

from app import views, models
