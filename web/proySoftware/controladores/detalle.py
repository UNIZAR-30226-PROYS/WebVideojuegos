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
		comentario = StringField('comentario')

#class ComentarioForm(Form):
#		comentario = StringField('comentario')


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
		#comentForm = ComentarioForm()
		listAnalis = get_analisis(pk)
		if listAnalis:
			for analisis in listAnalis:
					id_user = analisis.id_usuario
					user_nick = get_user_name(id_user)
					analisis.user = user_nick
					listcoment = get_comentario(analisis.id)
					analisis.coments = listcoment
		return render_template('_views/detalles.html',
            videojuego=videojuego,
            cover=cover,
            score=score,
						analisForm=analisForm, listAnalis=listAnalis)



def comentar(name, pk):
		#cargar info de los formularios
		#formulario = ComentarioForm(request.form)
		formulario = AnalisisForm(request.form)
		if 'nick' in session:
			#obtener datos
			id = get_user_id()
			texto = formulario.data['comentario']
			#crear nuevo analisis en bd
			insertar_comentario(id, pk, texto)
			flash('Enviado', 'success')
			response = make_response(redirect(url_for('details', name=name, pk=get_videogame_id(name))))
		else :
			flash('Login requerido', 'danger')
			response = make_response(redirect(url_for('details', name=name, pk=pk)))
		return response

@app.route('/<name>/<int:pk>/', methods=['POST'])
def detalles(name, pk):
		#cargar info de los formularios
		formulario = AnalisisForm(request.form)
		if 'nick' in session:
			#obtener datos
			id = get_user_id()
			texto = formulario.data['analisis']
			if texto == '':
				response = comentar(name, pk)
			else :
				#crear nuevo analisis en bd
				insertar_analisis(id, pk, texto)
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
	
