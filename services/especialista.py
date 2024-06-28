from flask import Blueprint, request, jsonify
from model.especialista import tbEspecialistas
from utils.db import db

especialistas = Blueprint('especialistas', __name__)

@especialistas.route('/Especialistas/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@especialistas.route('/Especialistas/v1/listar', methods=['GET'])
def getEspecialistas():
    result = {}
    Especialistas = tbEspecialistas.query.all()
    result["data"] = Especialistas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@especialistas.route('/Especialistas/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    nombreEspecialista = body.get('nombreEspecialista')
    apellidoEspecialista = body.get('apellidoEspecialista')
    correoEspecialista = body.get('correoEspecialista')
    contraseñaEspecialista = body.get('contraseñaEspecialista')

    if not nombreEspecialista or not apellidoEspecialista or not correoEspecialista or not contraseñaEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Especialista = tbEspecialistas(nombreEspecialista, apellidoEspecialista, correoEspecialista, contraseñaEspecialista)
    db.session.add(Especialista)
    db.session.commit()
    result["data"] = Especialista
    result["status_code"] = 201
    result["msg"] = "Se agregó al especialista"
    return jsonify(result), 201

@especialistas.route('/Especialistas/v1/update', methods=['POST'])
def update():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    nombreEspecialista = body.get('nombreEspecialista')
    apellidoEspecialista = body.get('apellidoEspecialista')
    correoEspecialista = body.get('correoEspecialista')
    contraseñaEspecialista = body.get('contraseñaEspecialista')

    if not idEspecialista or not nombreEspecialista or not apellidoEspecialista or not correoEspecialista or not contraseñaEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Especialista = tbEspecialistas.query.get(idEspecialista)
    if not Especialista:
        result['status_code'] = 400
        result["msg"] = "El especialista no existe"
        return jsonify(result), 400
    
    Especialista.nombreEspecialista = nombreEspecialista
    Especialista.apellidoEspecialista = apellidoEspecialista
    Especialista.correoEspecialista = correoEspecialista
    Especialista.contraseñaEspecialista = contraseñaEspecialista
    db.session.commit()

    result["data"] = Especialista
    result["status_code"] = 202
    result["msg"] = "Se modificó al especialista"
    return jsonify(result), 202

@especialistas.route('/Especialistas/v1/delete', methods=['DELETE'])
def delete():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    if not idEspecialista:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    Especialista = tbEspecialistas.query.get(idEspecialista)
    if not Especialista:
        result["status_code"] = 400
        result["msg"] = "El especialista no existe"
        return jsonify(result), 400
    
    db.session.delete(Especialista)
    db.session.commit()

    result["data"] = Especialista
    result['status_code'] = 200
    result["msg"] = "Se eliminó al especialista"
    return jsonify(result), 200

@especialistas.route('/Especialistas/v1/login', methods=['POST'])
def login():
    result={}
    body = request.get_json()
    correoEspecialista = body.get('correoEspecialista')
    contraseñaEspecialista = body.get('contraseñaEspecialista')

    if not correoEspecialista or not contraseñaEspecialista:
        result["success"] = False
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Especialista = tbEspecialistas.query.filter_by(correoEspecialista=correoEspecialista).first()

    if Especialista and Especialista.contraseñaEspecialista == contraseñaEspecialista:
        result["data"] = Especialista
        result["success"] = True
        result["msg"] = "Inicio de sesión exitoso"
        return jsonify(result),200
    
    result["success"]=False
    result["msg"]="Correo o contraseña incorrectos"
    return jsonify(result),401