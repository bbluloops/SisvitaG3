from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from model.resultadoTest import tbResultadoTest
from model.recomendacionApoyo import tbRecomendacionApoyoTratamiento
from utils.db import db

EvaluarResults = Blueprint('EvaluarResults', __name__)

@EvaluarResults.route('/EvaluarResults/v1/actualizar', methods=['POST'])
def actualizar_resultados():
    result = {}
    body = request.get_json()
    idResultadoTest = body.get('idResultadoTest')
    idEspecialista = body.get('idEspecialista')
    infoResultado = body.get('infoResultado')
    descripcionRecomendacionApoyo = body.get('descripcionRecomendacionApoyo')

    if not idResultadoTest or not idEspecialista or not infoResultado or not descripcionRecomendacionApoyo:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400

    # Actualizar la tabla tbResultadoTest
    resultado_test = tbResultadoTest.query.get(idResultadoTest)
    resultado_test.infoResultado = infoResultado
    db.session.commit()

    # Establecer fechaInicioRecomendacionApoyo y fechaFinRecomendacionApoyo
    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=30)  # Por ejemplo, 30 días después del inicio

    # Crear una nueva tupla en la tabla tbRecomendacionApoyoTratamiento
    nueva_recomendacion = tbRecomendacionApoyoTratamiento(
        idEspecialista=idEspecialista,
        idResultadoTest=idResultadoTest,
        descripcionRecomendacionApoyo=descripcionRecomendacionApoyo,
        fechaInicioRecomendacionApoyo=fecha_inicio,
        fechaFinRecomendacionApoyo=fecha_fin
    )

    db.session.add(nueva_recomendacion)
    db.session.commit()

    result["status_code"] = 200
    result["msg"] = "Evaluación exitosa"
    return jsonify(result),200
