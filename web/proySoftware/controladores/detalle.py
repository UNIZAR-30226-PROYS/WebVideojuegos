#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from flask import request
from flask import redirect
from flask import url_for
from flask import make_response
from flask import flash
from flask import session
from wtforms.validators import *

from ..models import *
from ..utils import *

#formulario para analisis
class AnalisisForm(Form):
    analisis = StringField('analisis')

@app.route('/<name>/<int:pk>/', methods=['GET'])
def details(name, pk):
		'''
		Router: solo accesible mediante el método GET de HTTP/HTTPS.
		Descripción: details hace una petición get de Videojuego que satisfaga
		id = pk recuperada de la url
		'''
		videojuego = Videojuego.query.get(pk)
		cover = get_videogame_cover(pk)
		score = puntnMedia(pk)
		analisForm = AnalisisForm()
		return render_template('_views/detalles.html',
            videojuego=videojuego,
            cover=cover,
            score=score,
						analisForm=analisForm)

@app.route('/<name>/<int:pk>/', methods=['POST'])
def detalles(name, pk):
		#cargar info de los formularios
		formulario = AnalisisForm(request.form)
		if 'nick' in session:
			flash('Enviado', 'success')
			response = make_response(redirect(url_for('details', name=name, pk=pk)))
		else :
			flash('Login requerido', 'danger')
			response = make_response(redirect(url_for('details', name=name, pk=pk)))
		return response
	
def puntnMedia(pk):
    '''
    Parámetros: id de un videojuego
    Descripción: Recupera la puntuacion media
    Función: retorna un entero de la puntuación
    '''
    vid = Videojuego.query.filter_by(id=pk).first()
    return vid.puntnMedia