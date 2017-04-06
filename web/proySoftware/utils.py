#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import login_manager
import json
from flask import request

from models import *

def load_user(user_id):
        return Usuario.get(user_id)


def get_user_cookie():
    """
    Función: retorna los datos de la cookie
    """
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


def get_user_id():
    """
    Función: retorna el id del objeto usuario
    """
    n_ick = get_user_cookie()['nick']

    user = Usuario.query.filter_by(nick=n_ick).first()

    return user.id

def get_user_contrasena(n_ick):
    """
    Función: retorna la contraseña del objeto usuario
    """
    user = Usuario.query.filter_by(nick=n_ick).first()
    return user.contrasena

def get_user():
    """
    Función: retorna en objeto usuario
    """
    n_ick = get_user_cookie()['nick']

    user = Usuario.query.filter_by(nick=n_ick).first()

    return user

def get_user_name(pk):
    user = Usuario.query.filter(Usuario.id == pk).first()
    return user.nick

def get_videogame_id(titulo):
    videogame = Videojuego.query.filter(Videojuego.titulo==titulo).first()
    return videogame.id

def get_videogame_pictures(pk):
    """
    Parámetros: id de un videojuego
    Función: retorna una lista de imágenes o [] vacio
    """
    picture = Imagen.query.join(ImagenVideojuego).filter(
            ImagenVideojuego.id_videojuego == pk,
            ImagenVideojuego.id_imagen == Imagen.id
            ).all()

    if not picture:
        return []
    return picture

def get_videogame_cover(pk):
    """
    Parámetros: id de un videojuego
    Función: retorna un string perteneciente a la url de la imagen o [] vacio
    """ 
    picture = Imagen.query.filter(
            ImagenVideojuego.id_videojuego == pk,
            ImagenVideojuego.id_imagen == Imagen.id).first()
    if not picture:
        return []
    return picture.nombre

def insertar_analisis(user_id, videojuego_id, texto):
    analisis = Analisis()
    analisis.id_usuario = user_id
    analisis.id_videojuego = videojuego_id
    analisis.analisis = texto
    db.session.add(analisis)
    db.session.commit()
  
def get_analisis(videojuego_id):
    analisis = Analisis.query.filter(Analisis.id_videojuego == videojuego_id).all()
    return analisis
  
def insertar_comentario(user_id, analisis_id, texto):
    comentario = Comentario()
    comentario.id_usuario = user_id
    comentario.id_analisis = analisis_id
    comentario.comentario = texto
    db.session.add(comentario)
    db.session.commit()
    
def get_comentario(analisis_id):
    comentario = Comentario.query.filter(Comentario.id_analisis == analisis_id).all()
    return comentario  
  
