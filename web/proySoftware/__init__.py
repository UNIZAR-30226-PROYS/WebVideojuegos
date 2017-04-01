from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os



app = Flask(__name__)
app.secret_key = 'some_secret'
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://software:software@localhost/proySoftware"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#@app.route('/')
#def index():
#    return 'Hola'
import proySoftware.views
