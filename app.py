from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    app.logger.debug('mensaje a nivel debug')
    app.logger.info('mensaje a nivel info')
    app.logger.warning('mensje a nivel warn')
    app.logger.error('mensaje a nivel error')
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/saludoPost', methods=['POST'])
def postHello():
    # nombre = request.form.get('nombre')  # si viene de un formulario HTML
    nombre = request.json.get('nombre')  # si viene como JSON
    return f"<h1>Hola, {nombre}!</h1>"

#jinja
@app.route("/templateJinga")
def templateJinga():
    return render_template("saludo.html")

@app.route("/saludo", methods=["POST"])
def saludar():
    nombre = request.form.get("nombre")
    return render_template("saludo.html", nombre=nombre)