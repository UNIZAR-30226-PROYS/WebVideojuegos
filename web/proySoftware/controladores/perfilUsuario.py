#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proySoftware import app


from flask import request
from flask import render_template

from flask import flash

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import *

from ..models import *
from ..views import *
from ..utils import *
from registro import *
#formulario para modificar imagen de perfil
class ImgPerfilForm(Form):
    imagen = StringField('imagen')

@app.route('/perfilUsuario/', methods=['GET'])
def perfilUsuario():
#perfil get, devuelve la informacion del perfil
    '''
    Router: solo accesible mediante el método GET de HTTP/HTTPS.
    Descripción: perfil devuelve una template de perfilUsuario.html. Pasa los datos
    del usuario obtenidos mediante get_user y el formulario para cambiar la imagen,
    de perfil.
    '''
    data = get_user_cookie()
    name = get_user_cookie()['nick']
    usuario = get_user_by_name(name) 
    #action=get_action_list()
    #favorites=get_favorite_list()
    #form = UpdateList()
    imgForm = ImgPerfilForm()
    return render_template("_views/perfilUsuario.html", user=usuario, logueado=data, imgForm=imgForm)
  
#modificar la imagen de perfil del usuario mediante url
@app.route('/mod_img/', methods=['POST'])
def mod_img():
    '''
    Router: solo accesible mediante el método POST de HTTP/HTTPS.
    Descripción: mod_img devuelve una llamada a perfil para que actualice la template con los
    los cambios de información referentes a la nueva imagen de perfil.
    Función: recupera la información del formulario de cambio de imagen de perfil y actualiza
    la inforamción de la base de datos.
    '''
    formulario = ImgPerfilForm(request.form)
    name = get_user_cookie()['nick']
    usuario = get_user_by_name(name) 
    db.session.delete(usuario)
    if formulario.data['imagen'] != '':
      usuario.avatar = formulario.data['imagen']
    else:
      usuario.avatar = '/static/img/avatar.jpg'
    db.session.add(usuario)
    db.session.commit()
    flash('Imagen de perfil cambiada', 'success')
    return perfilUsuario()

#modificar datos de usuario [get, post]
#permite modificar los datos almacenados referentes al usuario
@app.route('/mod_datos/', methods=['GET', 'POST'])
def mod_datos():
    '''
    Router: accesible mediante los métodos GET y POST de HTTP/HTTPS.
    Descripción: para el GET devuelve la template del modificar.html con un formulario para
    modificar los datos de usuario, para el POST recupera la información del formulario y
    la inserta en la base de datos luego redirecciona a perfilUsuario .
    Función: se encarga de la modificación de los datos del usuario
    '''
    if request.method == 'GET' :
      formulario = RegistroForm()
      name = get_user_cookie()['nick']
      usuario = get_user_by_name(name) 
      data = get_user_cookie()
      return render_template("_modules/modificar.html", saves=data, user=usuario, registroForm = formulario)
    else :
      formulario = RegistroForm(request.form)
      data = get_user_cookie()
      data.update(formulario.data)
      usuario = get_user()
      db.session.delete(usuario)
      usuario.genero = data.get('sexo', ' ')
      usuario.nombre = data.get('nombre', ' ')
      usuario.descripcion = data.get('descripcion', ' ')
      db.session.add(usuario)
      db.session.commit()
      imgForm = ImgPerfilForm()
      #form = UpdateList()
      flash('Datos Modificados Satisfactoriamente', 'success')
      return render_template("_views/perfilUsuario.html", user=usuario, logueado=data, imgForm=imgForm)
  
  
#elimina la cuenta del usuario actual
@app.route('/deletUser/', methods=['GET'])
def deletUser():
    '''
    Router: accesible mediante el método GET de HTTP/HTTPS.
    Descripción: deletUser redirecciona al router de index.
    Función: Elimina todos los datos almacenados en la base de datos referentes
    al usario y hace logout.
    '''
    response = make_response(redirect(url_for('index')))
    data = get_user_cookie()
    usuario = get_user()
    analist = Analisis.query.filter(Analisis.id_usuario == usuario.id).all()
    comlist = Comentario.query.filter(Comentario.id_usuario == usuario.id).all()
    if comlist:
      for jt in comlist:
          db.session.delete(jt)
          db.session.commit()
    if analist:
      for it in analist:
          db.session.delete(it)
          db.session.commit()
    userVidList = UsuarioVideojuego.query.filter(UsuarioVideojuego.id_usuario == usuario.id).all()        
    if userVidList:
      for userVid in userVidList:
          db.session.delete(userVid)
          db.session.commit()
    db.session.delete(usuario)
    db.session.commit()
    data = {}
    if 'nick' in session:
        session.pop('nick')
    response.set_cookie('character', json.dumps(data))
    return response


  
  
  
  