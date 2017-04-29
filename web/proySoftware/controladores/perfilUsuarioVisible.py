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
from perfilUsuario import *

@app.route('/perfil/<name>', methods=['GET'])
def perfilUsuarioVisible(name):
#perfil get, devuelve la informacion del perfil
    usuario = get_user_by_name(name)
    print name
    #action=get_action_list()
    #favorites=get_favorite_list()
    #form = UpdateList()
    imgForm = ImgPerfilForm()
    #return render_template("_views/perfilUsuarioVisible.html", user=usuario, logueado=data)
    return render_template("_views/perfilUsuarioVisible.html", user=usuario)
  
  
  
  