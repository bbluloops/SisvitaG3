from flask import Blueprint, request, jsonify
from model.ubigeo import tbUbigeo
from utils.db import db

Ubigeos = Blueprint('Ubigeos', __name__)

@Ubigeos.route('/Ubigeos/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@Ubigeos.route('/Ubigeos/v1/listar', methods=['GET'])
def getUbigeos():
    result = {}
    ubigeos = tbUbigeo.query.all()
    result["data"] = ubigeos
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los datos sin inconvenientes"
    return jsonify(result), 200

@Ubigeos.route('/Ubigeos/v1/insert', methods=['POST'])
def insertUbigeos():
    result = {}
    body = request.get_json()
    idUbigeo = body.get('idUbigeo')
    Distrito = body.get('Distrito')
    Provincia = body.get('Provincia')
    Departamento = body.get('Departamento')
    Poblacion = body.get('Poblacion')
    Superficie = body.get('Superficie')
    X = body.get('X')
    Y = body.get('Y')

    if not idUbigeo or not Distrito or not Provincia or not Departamento or not Poblacion or not Superficie or not X or not Y:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    ubigeo = tbUbigeo(idUbigeo, Distrito, Provincia, Departamento, Poblacion, Superficie, X, Y)
    db.session.add(ubigeo)
    db.session.commit()
    result["data"] = ubigeo
    result["status_code"] = 201
    result["msg"] = "Se agregó el ubigeo"
    return jsonify(result), 201

@Ubigeos.route('/Ubigeos/v1/update', methods=['POST'])
def updateUbigeos():
    result = {}
    body = request.get_json()
    idUbigeo = body.get('idUbigeo')
    Distrito = body.get('Distrito')
    Provincia = body.get('Provincia')
    Departamento = body.get('Departamento')
    Poblacion = body.get('Poblacion')
    Superficie = body.get('Superficie')
    X = body.get('X')
    Y = body.get('Y')

    if not idUbigeo or not Distrito or not Provincia or not Departamento or not Poblacion or not Superficie or not X or not Y:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    ubigeo = tbUbigeo.query.get(idUbigeo)
    if not ubigeo:
        result['status_code'] = 400
        result["msg"] = "El ubigeo no existe"
        return jsonify(result), 400
    
    ubigeo.Distrito = Distrito
    ubigeo.Provincia = Provincia
    ubigeo.Departamento = Departamento
    ubigeo.Poblacion = Poblacion
    ubigeo.Superficie = Superficie
    ubigeo.X = X
    ubigeo.Y = Y
    db.session.commit()

    result["data"] = ubigeo
    result["status_code"] = 202
    result["msg"] = "Se modificó el ubigeo"
    return jsonify(result), 202

@Ubigeos.route('/Ubigeos/v1/delete', methods=['DELETE'])
def deleteUbigeos():
    result = {}
    body = request.get_json()
    idUbigeo = body.get('idUbigeo')
    if not idUbigeo:
        result['status_code'] = 400
        result["msg"] = "Debe consignar un ubigeo valido"
        return jsonify(result), 400
    
    ubigeo = tbUbigeo.query.get(idUbigeo)
    if not ubigeo:
        result["status_code"] = 400
        result["msg"] = "El ubigeo no existe"
        return jsonify(result), 400
    
    db.session.delete(ubigeo)
    db.session.commit()

    result["data"] = ubigeo
    result['status_code'] = 200
    result["msg"] = "Se eliminó el ubigeo"
    return jsonify(result), 200