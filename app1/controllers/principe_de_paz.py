from flask import Flask, render_template
from app1 import app


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('Noticias.html')

@app.route('/institucion')
def institucion():
    return render_template('Institucion.html')

@app.route('/register')
def register():
    return render_template("admin_register.html")

@app.route('/clubes')
def alumno():
    return render_template('Clubes.html')

