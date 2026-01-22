from flask import Flask, render_template

app = Flask(__name__)
content = ""  # Define la variable content a nivel global
@app.route("/")
def index():
    print(f"Contenido: {content}")  # Agrega esta línea
    return render_template("index.html", content='')# Contenido inicial

@app.route("/")
def contact():
    return render_template("contact.html", content="<h1>Contacto</h1><p>Aquí puedes contactarnos...</p>")

@app.route("/")
def about():
    return render_template("about.html", content="<h1>Acerca de</h1><p>Información sobre el blog...</p>")

@app.route("/<page_name>")
def dynamic_page(page_name):
    # Intenta renderizar la página solicitada
    try:
        return render_template("index.html", content=f"<h1>{page_name}</h1><p>Contenido de la página...</p>")
    except Exception as e:
        return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)