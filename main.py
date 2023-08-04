from flask import Flask, render_template

app = Flask(__name__)


# Criar a 1a pagina do site

# Route -> homeTeste.com/

# Função -> O que será exibido na página
@app.route("/")
def homePage():
    return render_template("home.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)


# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# Servidor heroku

