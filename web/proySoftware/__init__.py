from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://proySoftware:software@localhost/software"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bbdd = SQLAlchemy(app)

#@app.route('/')
#def index():
#    return 'Hola'
import proySoftware.views
