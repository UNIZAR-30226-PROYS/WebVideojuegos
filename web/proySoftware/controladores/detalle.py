#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
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


def puntnMedia(pk):
    """
    Parámetros: id de un videojuego
    Descripción: Recupera la puntuacion media
    Función: retorna un entero de la puntuación
    """
    vid = Videojuego.query.filter_by(id=pk).first()
    return vid.puntnMedia