from flask import Blueprint, request, jsonify
from model.registroSesiones import tbRegistroSesionesHistorial
from utils.db import db

RegistrosSesiones = Blueprint('RegistrosSesiones', __name__)

@RegistrosSesiones.route('/RegistrosSesiones/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@RegistrosSesiones.route('/RegistrosSesiones/v1/listar', methods=['GET'])
def getRegistrosSesiones():
    result = {}
    registrosSesiones = tbRegistroSesionesHistorial.query.all()
    result["data"] = registrosSesiones
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@RegistrosSesiones.route('/RegistrosSesiones/v1/insert', methods=['POST'])
def insertRegistrosSesiones():
    result = {}
    body = request.get_json()
    idEstudiante = body.get('idEstudiante')

    if not idEstudiante:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RegistroSesion = tbRegistroSesionesHistorial(idEstudiante)
    db.session.add(RegistroSesion)
    db.session.commit()
    result["data"] = RegistroSesion
    result["status_code"] = 201
    result["msg"] = "Se agregó el registro"
    return jsonify(result), 201

@RegistrosSesiones.route('/RegistrosSesiones/v1/update', methods=['POST'])
def updateRegistrosSesiones():
    result = {}
    body = request.get_json()
    idRegistroSesiones = body.get('idRegistroSesiones')
    idEstudiante = body.get('idEstudiante')

    if not idRegistroSesiones or not idEstudiante:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RegistroSesion = tbRegistroSesionesHistorial.query.get(idRegistroSesiones)
    if not RegistroSesion:
        result['status_code'] = 400
        result["msg"] = "El registro no existe"
        return jsonify(result), 400
    
    RegistroSesion.idEstudiante = idEstudiante
    db.session.commit()

    result["data"] = RegistroSesion
    result["status_code"] = 202
    result["msg"] = "Se modificó el registro"
    return jsonify(result), 202

@RegistrosSesiones.route('/RegistrosSesiones/v1/delete', methods=['DELETE'])
def deleteRegistrosSesiones():
    result = {}
    body = request.get_json()
    idRegistroSesiones = body.get('idRegistroSesiones')
    if not idRegistroSesiones:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    RegistroSesion = tbRegistroSesionesHistorial.query.get(idRegistroSesiones)
    if not RegistroSesion:
        result["status_code"] = 400
        result["msg"] = "El registro no existe"
        return jsonify(result), 400
    
    db.session.delete(RegistroSesion)
    db.session.commit()

    result["data"] = RegistroSesion
    result['status_code'] = 200
    result["msg"] = "Se eliminó el registro"
    return jsonify(result), 200