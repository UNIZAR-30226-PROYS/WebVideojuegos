#!/usr/bin/env python
from proySoftware import app


from flask import request
from flask import render_template

@app.route('/perfilUsuario/', methods=['GET'])
def perfilUsuario():
    return render_template('_views/perfilUsuario.html')
