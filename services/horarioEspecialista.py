from flask import Blueprint, request, jsonify
from model.horarioEspecialista import tbHorarioEspecialista
from utils.db import db

HorariosEspecialistas = Blueprint('HorariosEspecialistas', __name__)

@HorariosEspecialistas.route('/HorariosEspecialistas/v1',methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@HorariosEspecialistas.route('/HorariosEspecialistas/v1/listar', methods=['GET'])
def getHorariosEspecialistas():
    result = {}
    horariosEspecialistas = tbHorarioEspecialista.query.all()
    result["data"] = horariosEspecialistas
    result["status_code"] = 200
    result["msg"] = "Se recupero los horarios de los especialistas sin inconvenientes"
    return jsonify(result), 200

@HorariosEspecialistas.route('/HorariosEspecialistas/v1/insert', methods=['POST'])
def insertHorariosEspecialistas():
    result = {}
    body = request.get_json()
    idEspecialista = body.get('idEspecialista')
    diaHorarioEspecialista = body.get('diaHorarioEspecialista')
    horaInicioHorarioEspecialista = body.get('horaInicioHorarioEspecialista')
    horaFinHorarioEspecialista = body.get('horaFinHorarioEspecialista')

    if not idEspecialista or not diaHorarioEspecialista or not horaInicioHorarioEspecialista or not horaFinHorarioEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    HorarioEspecialista = tbHorarioEspecialista(idEspecialista, diaHorarioEspecialista, horaInicioHorarioEspecialista, horaFinHorarioEspecialista)
    db.session.add(HorarioEspecialista)
    db.session.commit()
    result["data"] = HorarioEspecialista
    result["status_code"] = 201
    result["msg"] = "Se agrego un horario al especialista"
    return jsonify(result), 201

@HorariosEspecialistas.route('/HorariosEspecialistas/v1/update', methods=['POST'])
def updateHorariosEspecialistas():
    result = {}
    body = request.get_json()
    idHorarioEspecialista = body.get('idHorarioEspecialista')
    idEspecialista = body.get('idEspecialista')
    diaHorarioEspecialista = body.get('diaHorarioEspecialista')
    horaInicioHorarioEspecialista = body.get('horaInicioHorarioEspecialista')
    horaFinHorarioEspecialista = body.get('horaFinHorarioEspecialista')

    if not idHorarioEspecialista or not idEspecialista or not diaHorarioEspecialista or not horaInicioHorarioEspecialista or not horaFinHorarioEspecialista:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    HorarioEspecialista = tbHorarioEspecialista.query.get(idHorarioEspecialista)
    if not HorarioEspecialista:
        result['status_code'] = 400
        result["msg"] = "El horario no existe"
        return jsonify(result), 400
    
    HorarioEspecialista.idEspecialista = idEspecialista
    HorarioEspecialista.diaHorarioEspecialista = diaHorarioEspecialista
    HorarioEspecialista.horaInicioHorarioEspecialista = horaInicioHorarioEspecialista
    HorarioEspecialista.horaFinHorarioEspecialista = horaFinHorarioEspecialista
    db.session.commit()

    result["data"] = HorarioEspecialista
    result["status_code"] = 202
    result["msg"] = "Se modificó el horario"
    return jsonify(result), 202

@HorariosEspecialistas.route('/HorariosEspecialistas/v1/delete', methods=['DELETE'])
def deleteHorariosEspecialistas():
    result = {}
    body = request.get_json()
    idHorarioEspecialista = body.get('idHorarioEspecialista')
    if not idHorarioEspecialista:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400

    HorarioEspecialista = tbHorarioEspecialista.query.get(idHorarioEspecialista)
    if not HorarioEspecialista:
        result["status_code"] = 400
        result["msg"] = "El horario no existe"
        return jsonify(result), 400
    
    db.session.delete(HorarioEspecialista)
    db.session.commit()

    result["data"] = HorarioEspecialista
    result["status_code"] = 200
    result["msg"] = "Se eliminó el horario"
    return jsonify(result), 200