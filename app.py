from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacto")
def contact():
    return render_template("contact.html")

@app.route("/acerca_de")
def about():
    return render_template("about.html")

@app.route("/<page_name>")
def dynamic_page(page_name):
    # Intenta renderizar la página solicitada
    try:
        return render_template(f"{page_name}.html", content='')
    except Exception as e:
        return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)