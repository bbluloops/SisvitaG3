from flask import Blueprint, request, jsonify
from model.estudiante import tbEstudiante

estudiantes=Blueprint('estudiantes', __name__)

@estudiantes.route('/Estudiantes/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]= 'sisvitag3'
    return jsonify(result)

@estudiantes.route('/Estudiantes/v1/listar',methods=['GET'])
def getEstudiantes():
    result={}
    Estudiantes = tbEstudiante.query.all()
    result["data"]=Estudiantes
    result["status_code"]=200
    result["msg"]="Se recupero los contactos sin incovenientes"
    return jsonify(result), 200

