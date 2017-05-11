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


from ..models import *
from ..views import *
from ..utils import *

class CambioForm(Form):
	oldPassword = PasswordField('oldpassword', [validators.Length(min=8, max=25)])
	newPassword = PasswordField('newpassword', [validators.Length(min=8, max=25)])
	repeatPassword = PasswordField('repeatpassword', [validators.Length(min=8, max=25)])
	
@app.route('/changePassword/', methods=['GET'])
def cambiarpassw():
		'''
		Router: solo accesible mediante el método GET de HTTP/HTTPS
		Descripcion: cambiopassw() envia a password.html
		Funcion: devuelve render_template("_modules/password.html")
		'''
		formulario = CambioForm()
		data = get_user_cookie()
		return render_template("_modules/pass.html", saves=data, cambioForm = formulario)
	
@app.route('/changePassword/', methods=['POST'])
def cambiopassw():
		'''
		Router: solo accesible mediante el método POST de HTTP/HTTPS
		Descripcion: Si todo es correcto,la antigua contrasena sustituye a la nueva contrasena en la base de datos
		Funcion: Cambia la contrasena del usuario
		'''
		formulario = CambioForm(request.form)
		usuario = get_user()
		if formulario.validate() and formulario.data['newPassword'] == formulario.data['repeatPassword'] :
			if formulario.data['oldPassword'] == usuario.contrasena:
				flash('Cambio de password exitoso', 'success')
				db.session.delete(usuario)
				usuario.contrasena = formulario.data['newPassword']
				db.session.add(usuario)
				db.session.commit()
				return make_response(redirect(url_for('perfilUsuario')))
			else :
				flash('Contrasena incorrecta', 'danger')
				return make_response(redirect(url_for('cambiopassw')))
		else :
			flash('Las contrasenas no coinciden o son demasiado cortas', 'danger')
			return make_response(redirect(url_for('cambiopassw')))