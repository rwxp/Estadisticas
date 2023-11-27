from flask import render_template

def mostrar_landing():
    return render_template("landing.html")

def mostrar_cursos():
    return render_template("cursos.html")