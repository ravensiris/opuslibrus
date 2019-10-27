from flask_restplus import Namespace, Resource, fields
from flask import request
from app.tools.get_token import get_token, check_token

authorizations = {
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    },
    'Token Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-Key'
    },
}

ns = Namespace('token', security='Basic Auth', authorizations=authorizations, description='Getting data related to the librus\' token')

response_model = ns.model('TokenResponse', {
    'result': fields.Boolean(default=False, title="Result"),
    'message': fields.String(default='No message', title="Error message"),
    'token': fields.String(description="Librus' token")
})

validity_response_model = ns.model('TokenValid', {
    'result': fields.Boolean(default=False, title="Result"),
    'message': fields.String(default='No message', title="Error message"),
    'valid': fields.Boolean(default=False, description="True if token is valid, false when not or on error")
})

@ns.route('/get', methods=["GET"])
@ns.header('Authorization: Basic', 'BASIC AUTH', required=True)
@ns.doc(security='Basic Auth')
class TimetableGet(Resource):
    @ns.marshal_with(response_model)
    def get(self):
        credentials = request.headers.get('Authorization')
        token, message = get_token(credentials)
        message, code = message.explain()
        message['token'] = token
        return message, code

@ns.route('/check', methods=["GET"])
@ns.header('X-API-KEY', 'TOKEN AUTH', required=True)
@ns.doc(security='Token Auth')
class TimetableGet(Resource):
    @ns.marshal_with(validity_response_model)
    def get(self):
        token = request.headers.get('X-API-KEY')
        validity, message = check_token(token)
        message, code = message.explain()
        message['valid'] = validity
        return message, code
