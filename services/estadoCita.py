from flask import Blueprint, request, jsonify
from model.estadoCita import tbEstadoCita
from utils.db import db

EstadosCita = Blueprint('EstadosCita', __name__)

@EstadosCita.route('/EstadosCita/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@EstadosCita.route('/EstadosCita/v1/listar', methods=['GET'])
def getEstadosCita():
    result = {}
    estadosCita = tbEstadoCita.query.all()
    result["data"] = estadosCita
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@EstadosCita.route('/EstadosCita/v1/insert', methods=['POST'])
def insertEstadosCita():
    result = {}
    body = request.get_json()
    idCita = body.get('idCita')
    estadoCita = body.get('estadoCita')

    if not idCita or not estadoCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    EstadoCita = tbEstadoCita(idCita, estadoCita)
    db.session.add(EstadoCita)
    db.session.commit()
    result["data"] = EstadoCita
    result["status_code"] = 201
    result["msg"] = "Se agregó el estado de cita"
    return jsonify(result), 201

@EstadosCita.route('/EstadosCita/v1/update', methods=['POST'])
def updateEstadosCita():
    result = {}
    body = request.get_json()
    idEstadoCita = body.get('idEstadoCita')
    idCita = body.get('idCita')
    estadoCita = body.get('estadoCita')

    if not idEstadoCita or not idCita or not estadoCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    EstadoCita = tbEstadoCita.query.get(idEstadoCita)
    if not EstadoCita:
        result['status_code'] = 400
        result["msg"] = "El estado de cita no existe"
        return jsonify(result), 400
    
    EstadoCita.idCita = idCita
    EstadoCita.estadoCita = estadoCita
    db.session.commit()

    result["data"] = EstadoCita
    result["status_code"] = 202
    result["msg"] = "Se modificó el estado de cita"
    return jsonify(result), 202

@EstadosCita.route('/EstadosCita/v1/delete', methods=['DELETE'])
def deleteEstadosCita():
    result = {}
    body = request.get_json()
    idEstadoCita = body.get('idEstadoCita')
    if not idEstadoCita:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    EstadoCita = tbEstadoCita.query.get(idEstadoCita)
    if not EstadoCita:
        result["status_code"] = 400
        result["msg"] = "El estado de cita no existe"
        return jsonify(result), 400
    
    db.session.delete(EstadoCita)
    db.session.commit()

    result["data"] = EstadoCita
    result['status_code'] = 200
    result["msg"] = "Se eliminó el estado de cita"
    return jsonify(result), 200