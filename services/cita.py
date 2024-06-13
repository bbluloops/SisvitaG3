from flask import Blueprint, request, jsonify
from model.cita import tbCita
from utils.db import db

Citas = Blueprint('Citas', __name__)

@Citas.route('/Citas/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@Citas.route('/Citas/v1/listar', methods=['GET'])
def getCitas():
    result = {}
    citas = tbCita.query.all()
    result["data"] = citas
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@Citas.route('/Citas/v1/insert', methods=['POST'])
def insertCitas():
    result = {}
    body = request.get_json()
    idRecomendacionApoyo = body.get('idRecomendacionApoyo')
    idEstudiante = body.get('idEstudiante')
    fechaHoraCita = body.get('fechaHoraCita')

    if not idRecomendacionApoyo or not idEstudiante or not fechaHoraCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Cita = tbCita(idRecomendacionApoyo, idEstudiante, fechaHoraCita)
    db.session.add(Cita)
    db.session.commit()
    result["data"] = Cita
    result["status_code"] = 201
    result["msg"] = "Se agregó la cita"
    return jsonify(result), 201

@Citas.route('/Citas/v1/update', methods=['POST'])
def updateCitas():
    result = {}
    body = request.get_json()
    idCita = body.get('idCita')
    idRecomendacionApoyo = body.get('idRecomendacionApoyo')
    idEstudiante = body.get('idEstudiante')
    fechaHoraCita = body.get('fechaHoraCita')

    if not idCita or not idRecomendacionApoyo or not idEstudiante or not fechaHoraCita:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    Cita = tbCita.query.get(idCita)
    if not Cita:
        result['status_code'] = 400
        result["msg"] = "La cita no existe"
        return jsonify(result), 400
    
    Cita.idRecomendacionApoyo = idRecomendacionApoyo
    Cita.idEstudiante = idEstudiante
    Cita.fechaHoraCita = fechaHoraCita
    db.session.commit()

    result["data"] = Cita
    result["status_code"] = 202
    result["msg"] = "Se modificó la cita"
    return jsonify(result), 202

@Citas.route('/Citas/v1/delete', methods=['DELETE'])
def deleteCitas():
    result = {}
    body = request.get_json()
    idCita = body.get('idCita')
    if not idCita:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    Cita = tbCita.query.get(idCita)
    if not Cita:
        result["status_code"] = 400
        result["msg"] = "La cita no existe"
        return jsonify(result), 400
    
    db.session.delete(Cita)
    db.session.commit()

    result["data"] = Cita
    result['status_code'] = 200
    result["msg"] = "Se eliminó la cita"
    return jsonify(result), 200