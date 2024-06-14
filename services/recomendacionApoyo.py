from flask import Blueprint, request, jsonify
from model.recomendacionApoyo import tbRecomendacionApoyoTratamiento
from utils.db import db

RecomendacionesApoyos = Blueprint('RecomendacionesApoyos', __name__)

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/listar', methods=['GET'])
def getRecomendacionesApoyos():
    result = {}
    recomendacionesApoyos = tbRecomendacionApoyoTratamiento.query.all()
    result["data"] = recomendacionesApoyos
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/insert', methods=['POST'])
def insertRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    idRespuestas = body.get('idRespuestas')
    descripcionRecomendacionApoyo = body.get('descripcionRecomendacionApoyo')
    fechaInicioRecomendacionApoyo = body.get('fechaInicioRecomendacionApoyo')
    fechaFinRecomendacionApoyo = body.get('fechaFinRecomendacionApoyo')

    if not idEspecialista or not idRespuestas or not descripcionRecomendacionApoyo or not fechaInicioRecomendacionApoyo or not fechaFinRecomendacionApoyo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendacionApoyoTratamiento(idEspecialista, idRespuestas, descripcionRecomendacionApoyo, fechaInicioRecomendacionApoyo, fechaFinRecomendacionApoyo)
    db.session.add(RecomendacionApoyo)
    db.session.commit()
    result["data"] = RecomendacionApoyo
    result["status_code"] = 201
    result["msg"] = "Se agregó la recomendación o el tratamiento"
    return jsonify(result), 201

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/update', methods=['POST'])
def updateRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idRecomendacionApoyo = body.get('idRecomendacionApoyo')
    idEspecialista = body.get('idEspecialista')
    idRespuestas = body.get('idRespuestas')
    descripcionRecomendacionApoyo = body.get('descripcionRecomendacionApoyo')
    fechaInicioRecomendacionApoyo = body.get('fechaInicioRecomendacionApoyo')
    fechaFinRecomendacionApoyo = body.get('fechaFinRecomendacionApoyo')

    if not idRecomendacionApoyo or not idEspecialista or not idRespuestas or not descripcionRecomendacionApoyo or not fechaInicioRecomendacionApoyo or not fechaFinRecomendacionApoyo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendacionApoyoTratamiento.query.get(idRecomendacionApoyo)
    if not RecomendacionApoyo:
        result['status_code'] = 400
        result["msg"] = "La recomendacion o el tratamiento no existe"
        return jsonify(result), 400
    
    RecomendacionApoyo.idEspecialista = idEspecialista
    RecomendacionApoyo.idRespuestas = idRespuestas
    RecomendacionApoyo.descripcionRecomendacionApoyo = descripcionRecomendacionApoyo
    RecomendacionApoyo.fechaInicioRecomendacionApoyo = fechaInicioRecomendacionApoyo
    RecomendacionApoyo.fechaFinRecomendacionApoyo = fechaFinRecomendacionApoyo
    db.session.commit()

    result["data"] = RecomendacionApoyo
    result["status_code"] = 202
    result["msg"] = "Se modificó la recomendacion o el tratamiento"
    return jsonify(result), 202

@RecomendacionesApoyos.route('/RecomendacionesApoyos/v1/delete', methods=['DELETE'])
def deleteRecomendacionesApoyos():
    result = {}
    body = request.get_json()
    idRecomendacionApoyo = body.get('idRecomendacionApoyo')
    if not idRecomendacionApoyo:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    RecomendacionApoyo = tbRecomendacionApoyoTratamiento.query.get(idRecomendacionApoyo)
    if not RecomendacionApoyo:
        result["status_code"] = 400
        result["msg"] = "La recomendacion o el tratamiento no existe"
        return jsonify(result), 400
    
    db.session.delete(RecomendacionApoyo)
    db.session.commit()

    result["data"] = RecomendacionApoyo
    result['status_code'] = 200
    result["msg"] = "Se eliminó la recomendacion o el tratamiento"
    return jsonify(result), 200