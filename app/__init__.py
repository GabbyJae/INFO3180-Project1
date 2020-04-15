from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kennard@localhost/project1'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://dyjqtslarhyere:b2f411993be728694c8ac4527428966ed83cb41666d790a8097a857bcf756b4d@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d4jiktmkbc6b1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config.from_object(__name__)

from app import views
