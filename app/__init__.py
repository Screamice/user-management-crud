from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import DB_URI

APP = Flask(__name__)
APP.secret_key = "1234567890"

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

PG_DB = SQLAlchemy(APP)