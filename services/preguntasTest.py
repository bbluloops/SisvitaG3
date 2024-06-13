from flask import Blueprint, request, jsonify
from model.preguntasTest import tbPreguntasTest
from utils.db import db

# Definición del blueprint
PreguntasTests = Blueprint('PreguntasTests', __name__)

@PreguntasTests.route('/PreguntasTests/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@PreguntasTests.route('/PreguntasTests/v1/listar', methods=['GET'])
def getPreguntasTest():
    result = {}
    preguntaTest = tbPreguntasTest.query.all()
    result["data"] = preguntaTest
    result["status_code"] = 200
    result["msg"] = "Se recuperaron las preguntas del test sin inconvenientes"
    return jsonify(result), 200

@PreguntasTests.route('/PreguntasTests/v1/insert', methods=['POST'])
def insertPreguntasTest():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    enunciadoPreguntaTest = body.get('enunciadoPreguntaTest')

    if not idTest or not enunciadoPreguntaTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    preguntTest = tbPreguntasTest(idTest=idTest, enunciadoPreguntaTest=enunciadoPreguntaTest)
    db.session.add(preguntTest)
    db.session.commit()
    result["data"] = preguntTest
    result["status_code"] = 201
    result["msg"] = "Se agregó la pregunta del test"
    return jsonify(result), 201

@PreguntasTests.route('/PreguntasTests/v1/update', methods=['POST'])
def updatePreguntasTest():
    result = {}
    body = request.get_json()
    idPreguntaTest = body.get('idPreguntaTest')
    idTest = body.get('idTest')
    enunciadoPreguntaTest = body.get('enunciadoPreguntaTest')

    if not idPreguntaTest or not idTest or not enunciadoPreguntaTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    preguntaTest = tbPreguntasTest.query.get(idPreguntaTest)
    if not preguntaTest:
        result["status_code"] = 400
        result["msg"] = "No existe la pregunta del test"
        return jsonify(result), 400
    
    preguntaTest.idTest = idTest
    preguntaTest.enunciadoPreguntaTest = enunciadoPreguntaTest
    db.session.commit()

    result["data"] = preguntaTest
    result["status_code"] = 202
    result["msg"] = "Se modificó la pregunta del test"
    return jsonify(result), 202

@PreguntasTests.route('/PreguntasTests/v1/delete', methods=['DELETE'])
def deletePreguntasTest():
    result = {}
    body = request.get_json()
    idPreguntaTest = body.get('idPreguntaTest')
    if not idPreguntaTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id de la pregunta del test"
        return jsonify(result), 400

    preguntaTest = tbPreguntasTest.query.get(idPreguntaTest)
    if not preguntaTest:
        result["status_code"] = 400
        result["msg"] = "No existe la pregunta del test"
        return jsonify(result), 400
    
    db.session.delete(preguntaTest)
    db.session.commit()

    result["data"] = preguntaTest
    result["status_code"] = 200
    result["msg"] = "Se eliminó la pregunta del test"
    return jsonify(result), 200
