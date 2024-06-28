from flask import Blueprint, request, jsonify
from model.Test import tbTest
from model.preguntasTest import tbPreguntasTest
from model.opcionesTest import tbOpcionesTest
from model.respuestasTest import tbRespuestasTest
from model.resultadoTest import tbResultadoTest
from model.rangosPuntaje import tbRangosPuntaje
from model.registroSesiones import tbRegistroSesionesHistorial
from utils.db import db
from datetime import date
from sqlalchemy import and_
# DEFINIR RUTAS
Tests = Blueprint('Tests', __name__)

@Tests.route('/Tests/v1',methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'sisvitag3'
    return jsonify(result)

@Tests.route('/Tests/v1/listar', methods=['GET'])
def getTests():
    result = {}
    test = tbTest.query.all()
    result["data"] = test
    result["status_code"] = 200
    result["msg"] = "Se recupero los tests sin inconvenientes"
    return jsonify(result), 200

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
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    if not idTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id de test"
        return jsonify(result), 400

    Test=tbTest.query.get(idTest)
    if not Test:
        result["status_code"] = 400
        result["msg"] = "El test no existe"
        return jsonify(result), 400
    
    db.session.delete(Test)
    db.session.commit()

    result["data"] = Test
    result["status_code"] = 200
    result["msg"] = "Se eliminó el test"
    return jsonify(result), 200

@Tests.route('/Tests/v1/preguntas', methods=['POST'])
def preguntas():
    result = {}
    body = request.get_json()
    idTest = body.get('idTest')
    if not idTest:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id de test"
        return jsonify(result), 400
    OpcionesPregunta = tbOpcionesTest.query.join(
        tbPreguntasTest).where(tbPreguntasTest.idTest == idTest).all()
    print(OpcionesPregunta)
    if not OpcionesPregunta:
        result["status_code"] = 400
        result["msg"] = "La pregunta no existe"
        return jsonify(result), 400
    for opcion in OpcionesPregunta:
        PreguntaTest = tbPreguntasTest.query.where(
            opcion.idPreguntaTest == tbPreguntasTest.idPreguntaTest)
        pregunta = PreguntaTest[0].enunciadoPreguntaTest
        opcionParcial = {
            "respuestaOpcionTest": opcion.respuestaOpcionTest,
            "puntajeOpcionTest": opcion.puntajeOpcionTest
        }
        if pregunta not in result.keys():
            result[pregunta] = [opcionParcial]
        else:
            result[pregunta].append(opcionParcial)
    return jsonify(result), 200

@Tests.route('/Tests/v1/respuesta', methods=['POST'])
def respuesta():
    result = {}
    body = request.get_json()
    respuestas = body.get('respuestas')
    idTest = body.get('idTest')
    TbRegistroSesionesHistorial = tbRegistroSesionesHistorial.query.all()[-1]
    idRegistroSesiones = TbRegistroSesionesHistorial.idRegistroSesiones
    puntajeResultadoTest = 0
    infoResultado = "Prueba"
    fechaResultadoTest = date.today()
    revisadoResultadoTest = False
    tbResultadoPlantilla = tbResultadoTest(idRegistroSesiones=idRegistroSesiones, puntajeResultadoTest=puntajeResultadoTest,
                                           infoResultado=infoResultado, fechaResultadoTest=fechaResultadoTest, revisadoResultadoTest=revisadoResultadoTest)
    db.session.add(tbResultadoPlantilla)
    db.session.commit()
    idTbResultado = tbResultadoTest.query.all()[-1].idResultadoTest
    tbResultadoModificar = tbResultadoTest.query.get(idTbResultado)
    if not tbResultadoModificar:
        result["status_code"] = 400
        result["msg"] = "No se pudo crear el resultado"
        return jsonify(result), 400
    puntajeTotal = 0
    for pregunta in respuestas.keys():
        puntajeTotal += float(respuestas[pregunta]["puntajeOpcionTest"])
        RespuestaTest = tbRespuestasTest(idTest=idTest, idResultadoTest=idTbResultado,
                                         respuestas=respuestas[pregunta]["respuestaOpcionTest"], valorRespuesta=float(respuestas[pregunta]["puntajeOpcionTest"]))
        db.session.add(RespuestaTest)
    TbRangosPuntaje = tbRangosPuntaje.query.filter(
        and_(
            tbRangosPuntaje.maximoPuntaje > puntajeTotal,
            tbRangosPuntaje.minimoPuntaje <= puntajeTotal
        )
    ).all()
    infoResultado = TbRangosPuntaje[0].interpretacionPuntaje
    tbResultadoModificar.infoResultado = infoResultado
    tbResultadoModificar.puntajeResultadoTest = puntajeTotal
    db.session.commit()
    resultado = tbResultadoTest.query.all()[-1]
    result = {
        "puntajeResultadoTest": resultado.puntajeResultadoTest,
        "infoResultado": resultado.infoResultado,
        "fechaResultado": resultado.fechaResultadoTest,
        "revisado": resultado.revisadoResultadoTest
    }
    return jsonify(result), 200