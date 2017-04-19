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
    usuario = get_user()
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

  
  
  
  
  
  
  
  
  
  