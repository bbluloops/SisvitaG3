from flask import Blueprint, request, jsonify
from model.Test import tbTest
from utils.db import db
#DEFINIR RUTAS
Tests = Blueprint('Tests',__name__)

@Tests.route('/Tests/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='sisvitag3'
    return jsonify(result)

@Tests.route('/Tests/v1/listar',methods=['GET'])
def getTests():
    result={}
    test=tbTest.query.all()
    result["data"]=test
    result["status_code"]=200
    result["msg"]="Se recupero los tests sin inconvenientes"
    return jsonify(result),200

@Tests.route('/Tests/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    autorTest = body.get('autorTest')
    descripcionTest = body.get('descripcionTest')
    nombreTest = body.get('nombreTest')

    if not autorTest or not descripcionTest or not nombreTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    Test = tbTest(autorTest, descripcionTest, nombreTest)
    db.session.add(Test)
    db.session.commit()
    result["data"] = Test
    result["status_code"] = 201
    result["msg"] = "Se agrego el test"
    return jsonify(result), 201


@Tests.route('/Tests/v1/update', methods=['POST'])  
def update():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    autorTest = body.get('autorTest')
    descripcionTest = body.get('descripcionTest')
    nombreTest = body.get('nombreTest')

    if not idTest or not autorTest or not descripcionTest or not nombreTest:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400  

    Test = tbTest.query.get(idTest)
    if not Test:
        result["status_code"] = 400
        result["msg"] = "test no existe"
        return jsonify(result), 400

    Test.autorTest = autorTest
    Test.descripcionTest = descripcionTest
    Test.nombreTest = nombreTest
    db.session.commit()

    result["data"] = Test
    result["status_code"] = 202
    result["msg"] = "Se modificó el test"
    return jsonify(result), 202

@Tests.route('/Tests/v1/delete', methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    idTest=body.get('idTest')
    if not idTest:
        result["status_code"]=400
        result["msg"]="Debe consignar un id de test"
        return jsonify(result),400

    Test=tbTest.query.get(idTest)
    if not Test:
        result["status_code"]=400
        result["msg"]="El test no existe"
        return jsonify(result),400
    
    db.session.delete(Test)
    db.session.commit()

    result["data"]=Test
    result["status_code"]=200
    result["msg"]="Se eliminó el test"
    return jsonify(result),200