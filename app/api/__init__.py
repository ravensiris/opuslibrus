from flask import Blueprint
from flask_restplus import Api, Resource
import os

def init_api(route):
    api_blueprint = Blueprint('api', __name__, url_prefix=route)
    api = Api()
    api.init_app(api_blueprint)
    return api, api_blueprint