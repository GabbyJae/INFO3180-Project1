from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kennard@localhost/project1'
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://irgzkebawokoll:4fa46aa6e90ecef44c58f725181bffb7d00f69e40b930fc49578099df28c9ed7@ec2-18-215-99-63.compute-1.amazonaws.com:5432/daspicoks1kchk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config.from_object(__name__)

from app import views
