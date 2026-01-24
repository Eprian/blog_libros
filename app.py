from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        content=render_template("about.html")
    )

@app.route("/libros")
def libros():
    return render_template(
        "index.html",
        content=render_template("books.html")
    )

@app.route("/autores")
def autores():
    return render_template(
        "index.html",
        content="<h1>Autores</h1>"
    )

@app.route("/contacto")
def contacto():
    return render_template(
        "index.html",
        content="<h1>Contacto</h1>"
    )

if __name__ == "__main__":
    app.run(debug=True)