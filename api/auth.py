from flask import Blueprint, request
from injector import inject
from flask_jwt_extended import  create_access_token

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/token', methods=['POST'])
@inject
def post():        
    if request.get_json() is None:
        return {"error": "No request provided."}, 400
    
    token = create_access_token(identity=request.json["username"])
    return {"success": "Successful login.", "token": token}