# Se debe definir las funciones crear usuario y mostrar usuario aca
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from src.models.usuario_model import Usuario, db
from flask import render_template

# db = SQLAlchemy()


def mostrar_userinfo():
    return render_template("courses.html")


def mostrar_landing():
    return render_template("landing.html")


def mostrar_masinfo():
    return render_template("more-info.html")
