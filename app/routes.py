from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from app import db
from app.models import Rafael
# Crea un blueprint para organizar las rutas

main = Blueprint('main', __name__)


# Ruta para la página web
@main.route('/')
def home():
    flash('¿Cual es tu nombre?')
    rafael_list = Rafael.query.all()
    return render_template('index.html', rafael_list=rafael_list)

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

# API con información de la UNID
@main.route("/api/unid", methods=["GET"])
def unid():
    return jsonify({
        "name": "Universidad Interamericana para el Desarrollo",
        "acronym": "UNID",
        "city": "Acapulco City",
        "country": "Mexico"
    })


# 🟢 API para listar registros de la tabla `kevin`
@main.route("/api/rafael", methods=["GET"])
def get_rafael():
    rafael_list = Rafael.query.all()
    return jsonify([{
        "id": k.id,
        "nombre": k.nombre,
        "apellidos": k.apellidos,
        "telefono": k.telefono
    } for k in rafael_list])

# 🔵 API para agregar un nuevo registro
@main.route("/api/rafael/add", methods=["POST"])
def add_rafael():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    telefono = request.form.get('telefono')

    if not nombre or not apellidos or not telefono:
        return "Error: Todos los campos son obligatorios", 400

    new_entry = Rafael(nombre=nombre, apellidos=apellidos, telefono=telefono)
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('main.home'))


# 🔴 API para eliminar un registro
@main.route("/api/rafael/delete/<string:id>", methods=["POST"])
def delete_rafael(id):
    entry = Rafael.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        return redirect(url_for('main.home'))

    return jsonify({"error": "Usuario no encontrado"}), 404




