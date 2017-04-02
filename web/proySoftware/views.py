#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import app
from flask import render_template

from models import *
from utils import *
from flask import request
from functools import wraps
from flask import redirect
from flask import url_for

from controladores.perfilUsuario import *
from controladores.login import *
from controladores.registro import *
from controladores.detalle import *


  
class busquedaForm(Form):
    busqueda = StringField('busqueda')
  
@app.route('/')
@app.route('/<int:page>', methods=['GET'])
def index(page=1):
    lista = Videojuego.query.paginate(page, 20, False)
    for videojuego in lista.items:
        insert_atributes(videojuego)
    formulario = busquedaForm()
    return render_template('_views/index.html', videojuegos=lista, busquedaForm=formulario)
  
  
def insert_atributes(videojuego):
    picture = get_videogame_cover(videojuego.id)
    if picture:
      videojuego.picture = picture
      
def buscarVideojuego(texto, page):
    videogame = Videojuego.query.filter(Videojuego.titulo == texto ).paginate(page, 20, False)
    if not videogame.items:
        videogame = Videojuego.query.filter(Videojuego.puntnMedia == texto).paginate(page, 20, False)
    if not videogame.items:
        videogame = Videojuego.query.filter(Videojuego.id == PlataformaVideojuego.id_videojuego and Plataforma.id == PlataformaVideojuego.id_plataforma and Plataforma.nombre == texto).paginate(page, 20, False)
    if not videogame.items:
        videogame = Videojuego.query.filter(Videojuego.id == GeneroVideojuego.id_videojuego and Genero.id == GeneroVideojuego.id_plataforma and Genero.nombre == texto).paginate(page, 20, False)
    return videogame
  
@app.route('/<int:page>', methods=['GET'])
@app.route('/<int:page>/<texto>/', methods=['GET'])
def indexBuscado(page, texto):
    lista = buscarVideojuego(texto, page)
    if lista.items:
      for videojuego in lista.items:
        insert_atributes(videojuego)
    formulario = busquedaForm()
    return render_template('_views/index.html', videojuegos=lista, busquedaForm=formulario)
      
@app.route('/', methods=['POST'])
def indexBusqueda():
    formulario = busquedaForm(request.form)
    texto = formulario.data['busqueda']
    response = make_response(redirect(url_for('indexBuscado',page=1, texto=texto)))
    return response
