from flask import Blueprint, request, jsonify
from model.estudiante import tbEstudiante
from utils.db import db 

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

@estudiantes.route('/Estudiantes/v1/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    nombreEstudiante=body.get('nombreEstudiante')
    apellidoEstudiante=body.get('apellidoEstudiante')
    correoEstudiante=body.get('correoEstudiante')
    contraseñaEstudiante=body.get('contraseñaEstudiante')

    if not nombreEstudiante or not apellidoEstudiante or not correoEstudiante or not contraseñaEstudiante:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    Estudiante=tbEstudiante(nombreEstudiante, apellidoEstudiante, correoEstudiante, contraseñaEstudiante)
    db.session.add(Estudiante)
    db.session.commit()
    result["data"]=Estudiante
    result["status_code"]=201
    result["msg"]="Se agrego el estudiante"
    return jsonify(result),201