from flask import Blueprint, request
from connections.db_connection import DBConnection
from injector import inject
from sqlalchemy.exc import NoResultFound
from model.lista_negra import Lista_negra, lista_negra_parser
from middleware.request import schema
import socket


index_api = Blueprint('index_api', __name__)


@index_api.route('/', methods=['GET'])
@inject
def get():
    return "Soy otra la tercera versión", 200