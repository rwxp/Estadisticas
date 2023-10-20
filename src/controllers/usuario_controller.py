# Se debe definir las funciones crear usuario y mostrar usuario aca
from sqlalchemy import func
from src.models.usuario_model import Usuario
from flask import render_template 

def cantidad_usuarios():
    count = Usuario.query.all()
    return str(len(count))

def mostrar_layout():
    return render_template("user-info.html", cantidad_total=cantidad_usuarios())
