from flask import Blueprint, jsonify, render_template

# Crea un blueprint para organizar las rutas
main = Blueprint('main', __name__)

# Ruta para la página web
@main.route('/')
def home():
    return render_template('index.html')

# Ruta para la API     
@main.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to my API!"})
 
@main.route("/api/unid", methods= ['GET'])
def unid():
    return jsonify(
    {
        "name": "Universidad Interamericana Pars El Desarrollo",
        "acronym": "UNID",
        "city": "Acapulco",
        "country": "México",
        "message": "Hola, bienvenido a mi API",
    }
    )