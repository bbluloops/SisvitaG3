from flask import Blueprint, request, jsonify
from model.respuestasTest import tbRespuestasTest
from utils.db import db

# Definición de blueprint
RespuestasTests = Blueprint('RespuestasTests', __name__)

@RespuestasTests.route('/RespuestasTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@RespuestasTests.route('/RespuestasTests/v1/listar', methods=['GET'])
def getRespuestasTest():
    result = {}
    respuestasTest = tbRespuestasTest.query.all()
    result["data"] = respuestasTest
    result["status_code"] = 200
    result["msg"] = "Se recuperaron las respuestas de los test sin inconvenientes"
    return jsonify(result), 200

@RespuestasTests.route('/RespuestasTests/v1/insert', methods=['POST'])
def insertRespuestasTest():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    idResultadoTest = body.get('idResultadoTest')
    respuestas = body.get('respuestas')
    valorRespuesta = body.get('valorRespuesta')

    if not idTest or not idResultadoTest or not respuestas or not valorRespuesta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    respuestaTest = tbRespuestasTest(idTest, idResultadoTest, respuestas, valorRespuesta)
    db.session.add(respuestaTest)
    db.session.commit()
    result["data"] = respuestaTest
    result["status_code"] = 201
    result["msg"] = "Se agregó la respuesta del test"
    return jsonify(result), 201

@RespuestasTests.route('/RespuestasTests/v1/update', methods=['POST'])
def updateRespuestasTests():
    result = {}
    body = request.get_json()
    idRespuestas = body.get('idRespuestas')
    idTest = body.get('idTest')
    idResultadoTest = body.get('idResultadoTest')
    respuestas = body.get('respuestas')
    valorRespuesta = body.get('valorRespuesta')

    if not idRespuestas or not idTest or not idResultadoTest or not respuestas or not valorRespuesta:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    respuestasTests = tbRespuestasTest.query.get(idRespuestas)
    if not respuestasTests:
        result['status_code'] = 400
        result["msg"] = "La respuesta del test no existe"
        return jsonify(result), 400

    respuestasTests.idTest = idTest
    respuestasTests.idResultadoTest = idResultadoTest
    respuestasTests.respuestas = respuestas
    respuestasTests.valorRespuesta = valorRespuesta
    db.session.commit()

    result["data"] = respuestasTests
    result["status_code"] = 202
    result["msg"] = "Se modificó la respuesta del test"
    return jsonify(result), 202

@RespuestasTests.route('/RespuestasTests/v1/obtener-por-resultado' , methods=['POST'])
def obtener_por_resultado():
    result = {}
    body = request.get_json()
    idResultado = body.get('idResultado')
    if not idResultado:
        return jsonify("Se debe consignar un id valido"),400
    RespuestasTests= tbRespuestasTest.query.where(tbRespuestasTest.idResultadoTest==idResultado).all()
    result = RespuestasTests
    return result

@RespuestasTests.route('/RespuestasTests/v1/delete', methods=['DELETE'])
def deleteRespuestasTests():
    result = {}
    body = request.get_json()
    idRespuestas = body.get('idRespuestas')
    if not idRespuestas:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400

    respuestasTests = tbRespuestasTest.query.get(idRespuestas)
    if not respuestasTests:
        result["status_code"] = 400
        result["msg"] = "La respuesta no existe"
        return jsonify(result), 400

    db.session.delete(respuestasTests)
    db.session.commit()

    result["data"] = respuestasTests
    result["status_code"] = 200
    result["msg"] = "Se eliminó la respuesta"
    return jsonify(result), 200
