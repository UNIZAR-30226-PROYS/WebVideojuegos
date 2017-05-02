#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from proySoftware import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import flash
from flask import session
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import *

from ..models import *
from ..views import *
from ..utils import *
from registro import RegistroForm

#formulario para login
class LoginForm(Form):
    nick = StringField('nick', [validators.Length(min=1, max=20)])
    password = PasswordField('password', [validators.Length(min=1, max=25)])
#login get
@app.route('/login/', methods=['GET'])
def regLog():
    '''
    Router: solo accesible mediante el método GET de HTTP/HTTPS.
    Función: envia a la ruta de registro_login.html
    '''
    formulario = LoginForm()
    regform = RegistroForm()
    data = get_user_cookie()
    return render_template("_views/registro_login.html", saves=data, loginForm = formulario, registroForm =regform)
#login post
@app.route('/login/', methods=['POST'])
def login():
    '''
    Router: solo accesible mediante el método POST de HTTP/HTTPS.
    Función: recupera el formulario de login y procede a la validación de sus datos.
    '''
    formulario = LoginForm(request.form)
    n_ick = formulario.data['nick']
    clave = get_user_contrasena(n_ick)
    data = get_user_cookie()
    if formulario.validate() and clave == formulario.data['password']:
        session['nick'] = n_ick
        session['username'] = formulario.data['nick']
        data.update(formulario.data)
        response = make_response(redirect(url_for('index')))
        response.set_cookie('character', json.dumps(data))
        flash('Login Completado', 'success')
    else :
        flash('Datos Incorrectos', 'danger')
        response = make_response(redirect(url_for('login')))
    return response
#logout del usuario
@app.route('/logout/', methods=['GET'])
def loggout():
    '''
    Router: solo accesible mediante el método GET de HTTP/HTTPS.
    Función: elimina los cookies y la session de usario, para completar
    el proceso de logout.
    '''
    response = make_response(redirect(url_for('index')))
    data = {}
    if 'nick' in session:
        session.pop('nick')
    response.set_cookie('character', json.dumps(data))
    flash('Logout Completado', 'success')
    return response