import os
from flask import Flask
from model.init import instantiate_db
from flask_injector import FlaskInjector
from model.model import Base




# Instancia de la aplicación en Flask
app = Flask(__name__)

app.config.from_object('config.default_settings.Config')
app.config.from_envvar('APPLICATION_SETTINGS', True)
app.config.from_envvar('APPLICATION_SECRETS', True)

with app.app_context():
    from connections.db_connection import db
    db.Model = Base

from dependencies import configure
from api.lista_negra import lista_negra_api

app.register_blueprint(lista_negra_api, url_prefix='/blacklists')
# Agregamos el inyector de dependencias 
FlaskInjector(app=app, modules=[configure])

# Punto de arranque: gunicorn
def gunicorn():
    # Iniciar la base de datos si no existe
    with app.app_context():
        instantiate_db(db=db)

    # Retornar el objeto de la aplicacion
    return app

# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    # Iniciar la base de datos si no existe
    with app.app_context():
        instantiate_db(db=db)

    app.run(
        host="0.0.0.0", port=3000, debug=True
    )