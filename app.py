from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

SQLAlchemy(app)
app.register_blueprint(estudiantes)

with app.app_context():
    db.create_all

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)

'''from flask import Flask, jsonify
from utils.db import db
from services.estudiante import estudiantes
from config import DATABASE_CONNECTION

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(estudiantes)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a SisvitaG3"})

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)'''

'''print(DATABASE_CONNECTION)  # Añade esta línea para verificar la cadena de conexión
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
'''