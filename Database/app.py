from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

class MLData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(20))
	address = db.Column(db.String(50))
	action = db.Column(db.String(40))
	timestamp = db.Column(db.String(40))
	date = db.Column(db.String(40))
	day = db.Column(db.String(40))
	holiday=db.Column(db.String(40))

