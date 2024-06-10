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
    OpcionesTests=tbOpcionesTest.query.all()
    result["data"]=OpcionesTests
    result["status_code"]=200
    result["msg"]="Se recupero las opciones del test sin inconvenientes"
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

    opcionesTest = tbOpcionesTest(idPreguntaTest, respuestaOpcionTest, puntajeOpcionTest)
    db.session.add(opcionesTest)
    db.session.commit()
    result["data"] = opcionesTest
    result["status_code"] = 201
    result["msg"] = "Se agrego las opciones del test"
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
    
    opcionesTest = tbOpcionesTest.query.get(idOpcionTest)
    if not opcionesTest:
        result['status_code'] = 400
        result["msg"] = "no existen opciones del test"
        return jsonify(result), 400
    
    opcionesTest.idOpcionTest = idOpcionTest
    opcionesTest.idPreguntaTest = idPreguntaTest
    opcionesTest.respuestaOpcionTest = respuestaOpcionTest
    opcionesTest.puntajeOpcionTest = puntajeOpcionTest
    db.session.commit()

    result["data"] = opcionesTest
    result["status_code"] = 202
    result["msg"] = "Se modificó las opciones del test "
    return jsonify(result), 202

@OpcionesTests.route('/OpcionesTests/v1/delete', methods=['DELETE'])
def deleteOpcionesTests():
    result={}
    body=request.get_json()
    idOpcionTest=body.get('idOpcionTest')
    if not idOpcionTest:
        result["status_code"]=400
        result["msg"]="Debe consignar un id de las opciones del test"
        return jsonify(result),400

    opcionesTest=tbOpcionesTest.query.get(idOpcionTest)
    if not opcionesTest:
        result["status_code"]=400
        result["msg"]="No existe opciones test"
        return jsonify(result),400
    
    db.session.delete(opcionesTest)
    db.session.commit()

    result["data"]=opcionesTest
    result["status_code"]=200
    result["msg"]="Se eliminó opciones test"
    return jsonify(result),200