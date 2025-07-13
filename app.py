from flask import Flask, request, render_template, jsonify, url_for,session
from markupsafe import escape
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'


# http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    return 'No ha hecho login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Omitimos validación de usuario y password
        usuario = request.form['username']
        # agregar el usuario a la sesión
        session['username'] = usuario
        # session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route("/index")
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

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


#jinja
@app.route("/templateJinga")
def templateJinga():
    return render_template("saludo.html")

@app.route("/saludo", methods=["POST"])
def saludar():
    nombre = request.form.get("nombre")
    return render_template("saludo.html", nombre=nombre)

#json
@app.route('/api/mostrar/<nombre>', methods=['GET'])
def mostar_json(nombre):
    valores ={'nombre':nombre}
    return jsonify(valores)