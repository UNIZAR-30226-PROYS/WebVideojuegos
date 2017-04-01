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

# def insert_atributes(videojuego):
 #   picture = get_product_cover(videojuego.id)
 #   if picture:
 #     videojuego.picture = picture
    
@app.route('/')
@app.route('/<int:page>', methods=['GET'])
def index(page=1):
    lista = Videojuego.query.paginate(page, 20, False)
    for videojuego in lista.items:
        insert_atributes(videojuego)

    return render_template('_views/index.html', videojuegos=lista)
def insert_atributes(videojuego):
    picture = get_videogame_cover(videojuego.id)
    if picture:
      videojuego.picture = picture
