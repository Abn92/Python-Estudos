from flask import render_template

from main import app


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)
