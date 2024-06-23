from flask import Blueprint, request, jsonify
from model.estudiante import tbEstudiante
from utils.db import db

estudiantes = Blueprint('estudiantes', __name__)

@estudiantes.route('/Estudiantes/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@estudiantes.route('/Estudiantes/v1/listar', methods=['GET'])
def getEstudiantes():
    result = {}
    Estudiantes = tbEstudiante.query.all()
    result["data"] = Estudiantes
    result["status_code"] = 200
    result["msg"] = "Se recupero los datos sin incovenientes"
    return jsonify(result), 200

@estudiantes.route('/Estudiantes/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    nombreEstudiante = body.get('nombreEstudiante')
    apellidoEstudiante = body.get('apellidoEstudiante')
    correoEstudiante = body.get('correoEstudiante')
    contraseñaEstudiante = body.get('contraseñaEstudiante')
    idUbigeo = body.get('idUbigeo')

    if not nombreEstudiante or not apellidoEstudiante or not correoEstudiante or not contraseñaEstudiante or not idUbigeo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Estudiante = tbEstudiante(nombreEstudiante, apellidoEstudiante, correoEstudiante, contraseñaEstudiante, idUbigeo)
    db.session.add(Estudiante)
    db.session.commit()
    result["data"] = Estudiante
    result["status_code"] = 201
    result["msg"] = "Se agrego el estudiante"
    return jsonify(result), 201

@estudiantes.route('/Estudiantes/v1/update', methods=['POST'])  
def update():
    result = {}
    body = request.get_json()
    idEstudiante = body.get('idEstudiante')
    nombreEstudiante = body.get('nombreEstudiante')
    apellidoEstudiante = body.get('apellidoEstudiante')
    correoEstudiante = body.get('correoEstudiante')
    contraseñaEstudiante = body.get('contraseñaEstudiante')
    idUbigeo = body.get('idUbigeo')

    if not idEstudiante or not nombreEstudiante or not apellidoEstudiante or not correoEstudiante or not contraseñaEstudiante or not idUbigeo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400  

    Estudiante = tbEstudiante.query.get(idEstudiante)
    if not Estudiante:
        result["status_code"] = 400
        result["msg"] = "Contacto no existe"
        return jsonify(result), 400

    Estudiante.nombreEstudiante = nombreEstudiante
    Estudiante.apellidoEstudiante = apellidoEstudiante
    Estudiante.correoEstudiante = correoEstudiante
    Estudiante.contraseñaEstudiante = contraseñaEstudiante
    Estudiante.idUbigeo = idUbigeo
    db.session.commit()

    result["data"] = Estudiante
    result["status_code"] = 202
    result["msg"] = "Se modificó el contacto"
    return jsonify(result), 202

@estudiantes.route('/Estudiantes/v1/delete', methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    idEstudiante=body.get('idEstudiante')
    if not idEstudiante:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    Estudiante=tbEstudiante.query.get(idEstudiante)
    if not Estudiante:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(Estudiante)
    db.session.commit()

    result["data"]=Estudiante
    result["status_code"]=200
    result["msg"]="Se eliminó el contacto"
    return jsonify(result),200

@estudiantes.route('/Estudiantes/v1/login', methods=['POST'])
def login():
    result={}
    body = request.get_json()
    correoEstudiante = body.get('correoEstudiante')
    contraseñaEstudiante = body.get('contraseñaEstudiante')

    if not correoEstudiante or not contraseñaEstudiante:
        result["success"] = False
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Estudiante = tbEstudiante.query.filter_by(correoEstudiante=correoEstudiante).first()

    if Estudiante and Estudiante.contraseñaEstudiante == contraseñaEstudiante:
        result["data"] = Estudiante
        result["success"] = True
        result["msg"] = "Inicio de sesión exitoso"
        return jsonify(result),200
    
    result["success"]=False
    result["msg"]="Correo o contraseña incorrectos"
    return jsonify(result),401
