from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

db.init_app(app)

app.register_blueprint(estudiantes)

with app.app_context():
    # Crea todas las tablas definidas en los modelos
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
