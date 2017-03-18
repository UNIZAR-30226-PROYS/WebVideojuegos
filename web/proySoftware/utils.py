#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import login_manager
import json
from flask import request

from models import *

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
