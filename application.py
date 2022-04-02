import os
from flask import Flask
from model.init import instantiate_db
from flask_injector import FlaskInjector
from model.model import Base
from flask_jwt_extended import JWTManager

# Instancia de la aplicación en Flask
application = Flask(__name__)

application.config.from_object('config.default_settings.Config')
application.config.from_envvar('APPLICATION_SETTINGS', True)
application.config.from_envvar('APPLICATION_SECRETS', True)
application.config["JWT_SECRET_KEY"] = "devops-jwt"

jwt = JWTManager(application)

with application.app_context():
    from connections.db_connection import db
    db.Model = Base

from dependencies import configure
from api.lista_negra import lista_negra_api
from api.index import index_api
from api.auth import auth_api

application.register_blueprint(index_api, url_prefix='/')
application.register_blueprint(lista_negra_api, url_prefix='/blacklists')
application.register_blueprint(auth_api, url_prefix='/auth')

# Agregamos el inyector de dependencias 
FlaskInjector(app=application, modules=[configure])

# Punto de arranque: gunicorn
def gunicorn():
    # Iniciar la base de datos si no existe
    with application.app_context():
        instantiate_db(db=db)

    # Retornar el objeto de la aplicacion
    return application

# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    # Iniciar la base de datos si no existe
    with application.app_context():
        instantiate_db(db=db)

    application.run(
        host="0.0.0.0", port=3000, debug=True
    )