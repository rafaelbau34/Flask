from flask import Blueprint, render_template, flash, request

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
 
@main.route('/contacto')
def contacto():
    return render_template('contacto.html')

@main.route('/about')
def about():
    return render_template('about.html')


