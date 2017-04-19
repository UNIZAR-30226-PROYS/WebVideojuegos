#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from proySoftware import app
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import make_response
from flask import flash

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import *

from datetime import date

from ..models import *
from ..views import *
from ..utils import *
#formulario de registro
class RegistroForm(Form):
	nick = StringField('nick', [validators.Length(min=4, max=20)])
	password = PasswordField('password', [validators.Length(min=8, max=25)])
	sexo = StringField('sexo', [validators.Length(min=0, max=1)])
	nombre = StringField('nombre', [validators.Length(min=0, max=140)])
	descripcion = StringField('descripcion', [validators.Length(min=0, max=500)])

#inserta un nuevo usario a la base de Datos
#requiere un parametro cookie('character')
def insert_usuario(data):
	'''
    Función: inserta un nuevo usuario a la base de datos.
  '''
	usuario = Usuario()
	usuario.nick = data.get('nick', ' ')
	usuario.contrasena = data.get('password', ' ')
	usuario.genero = data.get('sexo', ' ')
	usuario.fechaRegistro = date.today()
	usuario.avatar = '/static/img/avatar.jpg'
	db.session.add(usuario)
	db.session.commit()

#registro post, obtiene datos de registro
@app.route('/registro', methods=['POST'])
def registro():
	'''
    Router: solo accesible mediante el método POST de HTTP/HTTPS.
    Función: recupera el formulario de registro, pasa los datos a insert_usuario
	,y crea una cookie y una session para el usuario.
    '''
	formulario = RegistroForm(request.form)
	nombre = get_user_by_name(formulario.data['nick'])
	if formulario.validate() and not nombre :
		response = make_response( redirect(url_for('perfilUsuario')))
		data = get_user_cookie()
		data.update(formulario.data)
		session['nick'] = formulario.data['nick']
		session['username'] = formulario.data['nick']
		insert_usuario(data)
		response.set_cookie('character', json.dumps(data))
		flash('Registro Completado', 'success')
	else:
		response = make_response( redirect(url_for('login')))
		flash('Datos Incorrectos o usuario ya existe', 'danger')
	return response







