from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import pandas as pd
import MySQLdb
import pandas.io.sql as psql
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

#check if database exists
#generate databaseq
class MLData(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(20))
	address = db.Column(db.String(50))
	action = db.Column(db.String(40))
	timestamp = db.Column(db.String(40))
	date = db.Column(db.String(40))
	day = db.Column(db.String(40))
	holiday=db.Column(db.String(40))



def addData(user,address,action,timestamp,date,day,holiday):
	entry = MLData(user=user,address=address,action=action,timestamp=timestamp,date=date,day=day,holiday=holiday)
	db.session.add(entry)
	db.session.commit()	

addData("Setev","1011 home","turn on light","10:34:35","10-24-30","Monday","0")





# setup the database connection.  There's no need to setup cursors with pandas psql.
datab=MySQLdb.connect(host=HOST, user=USER, passwd=PW, datab=db)

# create the query
query = "select * from TABLENAME"

# execute the query and assign it to a pandas dataframe
df = psql.read_sql(query, con=datab)
# close the database connection
datab.close()



#make function to accept data from ML code and add to DB

#take all the data from DB and turn it into panda shit.

#get in contact with Derrick about scripts.