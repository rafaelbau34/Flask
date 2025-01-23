from flask import Flask, Blueprint, jsonify, render_template, flash, request

# Crea un blueprint para organizar las rutas

main = Blueprint('main', __name__)


# Ruta para la página web
@main.route('/')
def home():
    flash('¿Cual es tu nombre?')
    return render_template('index.html')

@main.route('/greet', methods=['POST', 'GET'])
def greet():
   
    flash('Hola ' + str(request.form['name_input']) + ', nos da gusto verte!')
    return render_template('index.html')
 
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