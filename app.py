from flask import Flask, render_template

app = Flask(__name__)
content = ""  # Define la variable content a nivel global
def inicio():
    return render_template(
        "index.html",
        content=render_template("about.html")
    )

@app.route("/libros")
def libros():
    return render_template(
        "index.html",
        content="<h1>Libros</h1>"
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

@app.route("/<page_name>")
def dynamic_page(page_name):
    # Intenta renderizar la página solicitada
    try:
        return render_template("index.html", content=f"<h1>{page_name}</h1><p>Contenido de la página...</p>")
    except Exception as e:
        return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)