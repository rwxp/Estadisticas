# Se debe definir las funciones crear usuario y mostrar usuario aca
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from src.models.usuario_model import Usuario, db
from flask import render_template

# db = SQLAlchemy()


def mostrar_userinfo():
    cant_usuarios = str(len(Usuario.query.all()))
    sedes = db.session.query(Usuario.city, func.count(
        Usuario.id)).group_by(Usuario.city).all()
    cant_sedes = len(sedes)
    print("La cantidad de sedes es:", sedes[2][1])
    return render_template("user-info.html", total_usuarios=cant_usuarios, total_sedes=cant_sedes)


def mostrar_layout():
    return render_template("layout.html")


def mostrar_masinfo():
    return render_template("more-info.html")
