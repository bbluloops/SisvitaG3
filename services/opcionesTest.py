from flask import Blueprint, request, jsonify
from model.opcionesTest import tbOpcionesTest
from utils.db import db

#definicion de blueprint
OpcionesTests = Blueprint('OpcionesTests', __name__)

@OpcionesTests.route('/OpcionesTests/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='sisvitag3'
    return jsonify(result)

@OpcionesTests.route('/OpcionesTests/v1/listar', methods=['GET'])
def getOpcionesTest():
    result={}
    OpcionTests=tbOpcionesTest.query.all()
    result["data"]=OpcionTests
    result["status_code"]=200
    result["msg"]="Se recupero las opciones de los test sin inconvenientes"
    return jsonify(result),200

@OpcionesTests.route('/OpcionesTests/v1/insert', methods=['POST'])
def insertOpcionesTest():
    result = {}
    body = request.get_json()
    idPreguntaTest = body.get('idPreguntaTest')
    respuestaOpcionTest = body.get('respuestaOpcionTest')
    puntajeOpcionTest = body.get('puntajeOpcionTest')

    if not idPreguntaTest or not respuestaOpcionTest or not puntajeOpcionTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    opcionTest = tbOpcionesTest(idPreguntaTest, respuestaOpcionTest, puntajeOpcionTest)
    db.session.add(opcionTest)
    db.session.commit()
    result["data"] = opcionTest
    result["status_code"] = 201
    result["msg"] = "Se agrego la opción del test"
    return jsonify(result), 201

@OpcionesTests.route('/OpcionesTests/v1/update', methods=['POST'])
def updateOpcionesTests():
    result = {}
    body = request.get_json()
    idOpcionTest = body.get('idOpcionTest')
    idPreguntaTest = body.get('idPreguntaTest')
    respuestaOpcionTest = body.get('respuestaOpcionTest')
    puntajeOpcionTest = body.get('puntajeOpcionTest')

    if not idOpcionTest or not idPreguntaTest or not respuestaOpcionTest or not puntajeOpcionTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    opcionesTestss = tbOpcionesTest.query.get(idOpcionTest)
    if not opcionesTestss:
        result['status_code'] = 400
        result["msg"] = "La opción del test no existe"
        return jsonify(result), 400
    
   # opcionesTestss.idOpcionTest = idOpcionTest
    opcionesTestss.idPreguntaTest = idPreguntaTest
    opcionesTestss.respuestaOpcionTest = respuestaOpcionTest
    opcionesTestss.puntajeOpcionTest = puntajeOpcionTest
    db.session.commit()

    result["data"] = opcionesTestss
    result["status_code"] = 202
    result["msg"] = "Se modificó la opción del test "
    return jsonify(result), 202

@OpcionesTests.route('/OpcionesTests/v1/delete', methods=['DELETE'])
def deleteOpcionesTests():
    result={}
    body=request.get_json()
    idOpcionTest=body.get('idOpcionTest')
    if not idOpcionTest:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400

    opcionTestss=tbOpcionesTest.query.get(idOpcionTest)
    if not opcionTestss:
        result["status_code"]=400
        result["msg"]="La opción no existe"
        return jsonify(result),400
    
    db.session.delete(opcionTestss)
    db.session.commit()

    result["data"]=opcionTestss
    result["status_code"]=200
    result["msg"]="Se eliminó la opción"
    return jsonify(result),200