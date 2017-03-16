from proySoftware import app
from flask import render_template


from controladores.perfilUsuario import *

@app.route('/')
def index():
    return render_template('_views/index.html')
