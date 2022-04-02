from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.lista_negra import Lista_negra, lista_negra_parser
from middleware.request import schema
import socket


lista_negra_api = Blueprint('lista_negra_api', __name__)





# Adición de correos a la lista negra

@lista_negra_api.route('', methods=['POST'])
@inject
def post(db_connection: DBConnection):
## importing socket module

## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address

    nuevo_correo=Lista_negra(email=request.json["email"], app_uuid=request.json["app_uuid"],blocked_reason=request.json["blocked_reason"],ip=ip_address)
    db_connection.db.session.add(nuevo_correo)
    db_connection.db.session.commit()
    return "Agregado exitosamente el correo " + request.json["email"] + " a la lista negra global", 200



@lista_negra_api.route('/<email_verificar>', methods=['GET'])
@inject
def get(email_verificar: str, db_connection: DBConnection):
        result = db_connection.db.session.query(Lista_negra).filter(Lista_negra.email == email_verificar).first()
        if result is None:
            return "El email " + email_verificar + " no está incluido en la lista negra global", 205
        else:
            return "El email " + email_verificar + " se encuentra en la lista negra global", 200