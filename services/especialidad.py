from flask import Blueprint, request, jsonify
from model.especialidad import tbEspecialidad
from utils.db import db

Especialidades = Blueprint('Especialidades', __name__)

@Especialidades.route('/Especialidades/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@Especialidades.route('/Especialidades/v1/listar', methods=['GET'])
def getEspecialidades():
    result = {}
    especialidades = tbEspecialidad.query.all()
    result["data"] = especialidades
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@Especialidades.route('/Especialidades/v1/insert', methods=['POST'])
def insertEspecialidades():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    nombreEspecialidad = body.get('nombreEspecialidad')

    if not idEspecialista or not nombreEspecialidad:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Especialidad = tbEspecialidad(idEspecialista, nombreEspecialidad)
    db.session.add(Especialidad)
    db.session.commit()
    result["data"] = Especialidad
    result["status_code"] = 201
    result["msg"] = "Se agregó la especialidad"
    return jsonify(result), 201

@Especialidades.route('/Especialidades/v1/update', methods=['POST'])
def updateEspecialidades():
    result = {}
    body = request.get_json()
    idEspecialidad = body.get('idEspecialidad')
    idEspecialista = body.get('idEspecialista')
    nombreEspecialidad = body.get('nombreEspecialidad')

    if not idEspecialidad or not idEspecialista or not nombreEspecialidad:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Especialidad = tbEspecialidad.query.get(idEspecialidad)
    if not Especialidad:
        result['status_code'] = 400
        result["msg"] = "La especialidad no existe"
        return jsonify(result), 400
    
    Especialidad.idEspecialista = idEspecialista
    Especialidad.nombreEspecialidad = nombreEspecialidad
    db.session.commit()

    result["data"] = Especialidad
    result["status_code"] = 202
    result["msg"] = "Se modificó la especialidad"
    return jsonify(result), 202

@Especialidades.route('/Especialidades/v1/delete', methods=['DELETE'])
def deleteEspecialidades():
    result = {}
    body = request.get_json()
    idEspecialidad = body.get('idEspecialidad')
    if not idEspecialidad:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    Especialidad = tbEspecialidad.query.get(idEspecialidad)
    if not Especialidad:
        result["status_code"] = 400
        result["msg"] = "La especialidad no existe"
        return jsonify(result), 400
    
    db.session.delete(Especialidad)
    db.session.commit()

    result["data"] = Especialidad
    result['status_code'] = 200
    result["msg"] = "Se eliminó la especialidad"
    return jsonify(result), 200