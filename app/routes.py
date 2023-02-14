from datetime import datetime
from flask import render_template, request, jsonify, Blueprint, abort
from app import db
from app.models import Mascota, Propietario

main_routes = Blueprint('main', __name__)
api_routes = Blueprint('api', __name__)


@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/mascotas', methods=['GET'])
def listar_mascotas():
    orden = request.args.get('orden', 'fecha_nacimiento')
    mascotas = Mascota.query.order_by(orden).all()
    return render_template('mascotas.html', mascotas=mascotas)

@main_routes.route('/propietarios/<int:id>/mascotas', methods=['GET'])
def listar_mascotas_propietario(id):
    propietario = Propietario.query.get_or_404(id)
    return render_template('propietario_mascotas.html', propietario=propietario)

@main_routes.route('/mascotas/<int:id>', methods=['GET'])
def mostrar_mascota(id):
    mascota = Mascota.query.get_or_404(id)
    return render_template('mascota.html', mascota=mascota)

@main_routes.route('/mascotas/<int:id>/editar', methods=['GET', 'POST'])
def editar_mascota(id):
    mascota = Mascota.query.get_or_404(id)

    if request.method == 'POST':
        mascota.nombre = request.form['nombre']
        mascota.fecha_nacimiento = datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d')
        mascota.raza = request.form['raza']
        db.session.commit()
        return jsonify({'success': True})

    return render_template('mascota_editar.html', mascota=mascota)


# Rutas para la API
@api_routes.route('/mascotas', methods=['GET'])
def listar_mascotas_api():
    orden = request.args.get('orden', 'fecha_nacimiento')
    mascotas = Mascota.query.order_by(orden).all()
    return jsonify([mascota.to_dict() for mascota in mascotas])

@api_routes.route('/mascotas', methods=['POST'])
def crear_mascota_api():
    data = request.get_json()

    if not all(key in data for key in ('nombre', 'fecha_nacimiento', 'raza', 'propietario_id')):
        abort(400, 'Faltan campos obligatorios')

    mascota = Mascota(
        nombre=data['nombre'],
        fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d'),
        raza=data['raza'],
        propietario_id=data['propietario_id']
    )

    db.session.add(mascota)
    db.session.commit()

    return jsonify(mascota.to_dict())

@api_routes.route('/mascotas/<int:id>', methods=['GET'])
def mostrar_mascota_api(id):
    mascota = Mascota.query.get_or_404(id)
    return jsonify(mascota.to_dict())
@api_routes.route('/mascotas/<int:id>', methods=['PUT'])
def actualizar_mascota_api(id):
    mascota = Mascota.query.get_or_404(id)
    data = request.get_json()

    if not all(key in data for key in ('nombre', 'fecha_nacimiento', 'raza', 'propietario_id')):
        abort(400, 'Faltan campos requeridos en la solicitud')

    mascota.nombre = data['nombre']
    mascota.fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date()
    mascota.raza = data['raza']
    mascota.propietario_id = data['propietario_id']

    db.session.commit()

    return jsonify(mascota.to_dict())