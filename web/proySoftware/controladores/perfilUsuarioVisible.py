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

@app.route('/perfilUsuarioVisible/', methods=['GET'])
def perfilUsuarioVisible():
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
    return render_template("_views/perfilUsuarioVisible.html", user=usuario, logueado=data, imgForm=imgForm)
  
  
  
  