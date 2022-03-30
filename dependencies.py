from injector import singleton
from connections.db_connection import DBConnection

# Vinculación de las dependencias inyectables
def configure(binder):
    binder.bind(DBConnection, to=DBConnection, scope=singleton)
 