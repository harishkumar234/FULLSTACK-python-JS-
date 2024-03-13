from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS # cross orgin request (sends request to backen with diffrent URLs )


app = Flask(__name__) # starting flask 
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"  #storing local database in our computer
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db =  SQLAlchemy(app) # creating database instance for the app where we can create edit read deleete  entities



