#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import login_manager
import json
from flask import request

from models import *
from datetime import date

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
  
def get_user_by_name(name):
    user = Usuario.query.filter(Usuario.nick==name).first()
    
    return user

def get_user_contrasena(n_ick):
    """
    Función: retorna la contraseña del objeto usuario
    """
    user = Usuario.query.filter(Usuario.nick==n_ick).first()
    if not user:
        return ""
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

def get_videogames_user(user_id):
    #videojuegos = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == user_id)
		videojuegos = UsuarioVideojuego.query.filter(
			UsuarioVideojuego.id_usuario == user_id, Videojuego.id == UsuarioVideojuego.id_videojuego).all()		
		for ind in videojuegos:
				vid = Videojuego.query.filter(UsuarioVideojuego.id_usuario == user_id, Videojuego.id == ind.id_videojuego).first()
				if vid :
					ind.titulo = vid.titulo
		if not videojuegos:
			return []
		return videojuegos


def insertar_analisis(user_id, videojuego_id, texto):
		analisis = Analisis()
		analisis.id_usuario = user_id
		analisis.id_videojuego = videojuego_id
		analisis.analisis = texto
		db.session.add(analisis)
		db.session.commit()
		new_action("Analizado", videojuego_id)
  
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

  
def insertar_new_user_vid(user_id, videojuego_id, jugado, deseado, texto):
    userVid = UsuarioVideojuego()
    userVid.id_usuario = user_id
    userVid.id_videojuego = videojuego_id
    userVid.jugado = jugado
    userVid.deseado = deseado
    userVid.puntuacion = texto
    db.session.add(userVid)
    db.session.commit()

def insertar_user_vid_2(user_id, videojuego_id, jugado, deseado):
	userVid = UsuarioVideojuego()
	userVid.id_usuario = user_id
	userVid.id_videojuego = videojuego_id
	userVid.jugado = jugado
	userVid.deseado = deseado
	db.session.add(userVid)
	db.session.commit()


def insertar_puntuacion(user_id, videojuego_id, texto):
		userVid = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == user_id, UsuarioVideojuego.id_videojuego == videojuego_id).first()
		if not userVid:
			insertar_new_user_vid(user_id, videojuego_id, 0, 0, texto)
		else :
			db.session.delete(userVid)
			userVid.puntuacion = texto
			db.session.add(userVid)
			db.session.commit()
		actualizarPuntnm(videojuego_id)
		actuPuntMedUsuario()
		new_action("Puntuado", videojuego_id)
      
def actualizarPuntnm(videojuego_id):
		lista = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_videojuego == videojuego_id).all()
		numVid = 0
		puntnM = 0
		if lista:
			for i in lista:
				if i.puntuacion :
					numVid = numVid + 1
					puntnM = puntnM + i.puntuacion
		else :
			numVid = 1
		puntnM = puntnM / numVid
		videojuego = Videojuego.query.filter(Videojuego.id == videojuego_id).first()
		db.session.delete(videojuego)
		videojuego.puntnMedia = puntnM
		db.session.add(videojuego)
		db.session.commit()
	
def actuPuntMedUsuario():
		user_id = get_user_id()
		lista = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == user_id).all()
		user = Usuario.query.filter(Usuario.id == user_id).first()
		puntnM = 0
		numVid = 0
		if lista:
			for i in lista:
				if i.puntuacion :
					numVid = numVid + 1
					puntnM = puntnM + i.puntuacion
		else :
			numVid = 1
		puntnM = puntnM / numVid
		db.session.delete(user)
		user.puntMediaUsur = puntnM
		db.session.add(user)
		db.session.commit()
  
def jugado_deseado(user_id, videojuego_id, select):
	userVid = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == user_id, UsuarioVideojuego.id_videojuego == videojuego_id).first()
	if not userVid:
	  if select == 0:
	    insertar_user_vid_2(user_id, videojuego_id, 1, 0)
	  else:
	    insertar_user_vid_2(user_id, videojuego_id, 0, 1)
	else :
	  db.session.delete(userVid)
	  userVid.deseado = select
	  userVid.jugado = (select + 1) % 2 
	  db.session.add(userVid)
	  db.session.commit()

def new_action(texto, id_vid):
		user_id = get_user_id()
		acciones = Acciones()
		acciones.accion = texto
		acciones.fecha = date.today()
		acciones.id_usuario = user_id
		acciones.id_videojuego = id_vid
		db.session.add(acciones)
		db.session.commit()
		
def get_actions(user_id):	
		acciones = Acciones.query.order_by(Acciones.fecha.desc()).filter(
			Acciones.id_usuario == user_id, Videojuego.id == Acciones.id_videojuego).limit(20).all()
		for ind in acciones:
				vid = Videojuego.query.filter(Acciones.id_usuario == user_id, Videojuego.id == ind.id_videojuego).first()
				punt = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == user_id, UsuarioVideojuego.id_videojuego == ind.id_videojuego).first()
				if vid :
					ind.titulo = vid.titulo
					if punt :
						ind.puntuacion = punt.puntuacion
		if not acciones:
			return []
		return acciones
		
		
		