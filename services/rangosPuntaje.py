from flask import Blueprint, request, jsonify
from model.rangosPuntaje import tbRangosPuntaje
from utils.db import db

# Definición de blueprint
RangosPuntajes = Blueprint('RangosPuntajes', __name__)

@RangosPuntajes.route('/RangosPuntajes/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@RangosPuntajes.route('/RangosPuntajes/v1/listar', methods=['GET'])
def getRangosPuntaje():
    result = {}
    ranPuntaje = tbRangosPuntaje.query.all()
    result["data"] = ranPuntaje
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los rangos de puntaje sin inconvenientes"
    return jsonify(result), 200

@RangosPuntajes.route('/RangosPuntajes/v1/insert', methods=['POST'])
def insertRangosPuntaje():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    minimoPuntaje = body.get('minimoPuntaje')
    maximoPuntaje = body.get('maximoPuntaje')
    interpretacionPuntaje = body.get('interpretacionPuntaje')

    if not idTest or not minimoPuntaje or not maximoPuntaje or not interpretacionPuntaje:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    rangoPuntaje = tbRangosPuntaje(idTest, minimoPuntaje, maximoPuntaje, interpretacionPuntaje)
    db.session.add(rangoPuntaje)
    db.session.commit()
    result["data"] = rangoPuntaje
    result["status_code"] = 201
    result["msg"] = "Se agregó el rango de puntaje"
    return jsonify(result), 201

@RangosPuntajes.route('/RangosPuntajes/v1/update', methods=['POST'])
def updateRangosPuntajes():
    result = {}
    body = request.get_json()
    idRangoTest = body.get('idRangoTest')
    idTest = body.get('idTest')
    minimoPuntaje = body.get('minimoPuntaje')
    maximoPuntaje = body.get('maximoPuntaje')
    interpretacionPuntaje = body.get('interpretacionPuntaje')

    if not idRangoTest or not idTest or not minimoPuntaje or not maximoPuntaje or not interpretacionPuntaje:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    rangosPuntajes = tbRangosPuntaje.query.get(idRangoTest)
    if not rangosPuntajes:
        result['status_code'] = 400
        result["msg"] = "El rango de puntaje no existe"
        return jsonify(result), 400

    rangosPuntajes.idTest = idTest
    rangosPuntajes.minimoPuntaje = minimoPuntaje
    rangosPuntajes.maximoPuntaje = maximoPuntaje
    rangosPuntajes.interpretacionPuntaje = interpretacionPuntaje
    db.session.commit()

    result["data"] = rangosPuntajes
    result["status_code"] = 202
    result["msg"] = "Se modificó el rango de puntaje"
    return jsonify(result), 202

@RangosPuntajes.route('/RangosPuntajes/v1/delete', methods=['DELETE'])
def deleteRangosPuntajes():
    result = {}
    body = request.get_json()
    idRangoTest = body.get('idRangoTest')
    if not idRangoTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400

    rangosPuntajes = tbRangosPuntaje.query.get(idRangoTest)
    if not rangosPuntajes:
        result["status_code"] = 400
        result["msg"] = "El rango no existe"
        return jsonify(result), 400

    db.session.delete(rangosPuntajes)
    db.session.commit()

    result["data"] = rangosPuntajes
    result["status_code"] = 200
    result["msg"] = "Se eliminó el rango"
    return jsonify(result), 200
