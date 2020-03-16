from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kennard@localhost/project1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config.from_object(__name__)
from app import views