from werkzeug.exceptions import HTTPException
from flask import request, Response
from functools import update_wrapper
from pydantic import ValidationError


def schema(val):
    """
    Permite validar un esquema según una plantilla en pydantic.
    En caso de ser valido, retorna los datos como una instancia del validador
    :param val: Validador de Pydantic
    :return: Los datos validados
    """
    def decorator(f):
        def validation(*args, **kwargs):
            try:
                data = request.get_json()
                body_data = val(**data)
            except ValidationError as e:
                error_response = Response(e.json(), mimetype="application/json", status=400)
                raise HTTPException(response=error_response)

            data = body_data
            return f(data, *args, **kwargs)
        return update_wrapper(validation, f)
    return decorator
