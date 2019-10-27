from flask_restplus import Namespace, Resource, fields
from flask import request
from app.tools.check_token import check_token
from app.tools.get_timetable import get_timetable


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

ns = Namespace('timetable', security='X-API-KEY', authorizations=authorizations, description='Getting data related to the timetable')

timetable_model = ns.model('Timetable',{
            'break_end': fields.String(description="Time represented in yyyy-mm-dd HH:MM:ss"),
            'break_start': fields.String(description="Time represented in yyyy-mm-dd HH:MM:ss"),
            'day': fields.Integer(description="Weekday: \n-   0 - Monday\n-    6 - Sunday"),
            'flag': fields.String(description="Message attatched to lesson.\nUsually informs about lesson getting cancelled or getting a susbstitution teacher."),
            'index': fields.Integer(description="Lesson's index from 0.\n0 meaning its a first lesson in the **school**"),
            'name': fields.String(description="Name of the lesson\nSometimes it has a module ID attached to it at the begining.\nIt is up to you to format such info"),
            'room': fields.String(description="Lesson's room"),
            'start': fields.String(description="Time represented in yyyy-mm-dd HH:MM:ss"),
            'teacher': fields.String(description="Teacher entire name.\nSometimes names have class groups attached to them.\nIt is up to you to format such info"),
}, description="An unordered list of lessons.")

response_model = ns.model('TimetableResponse', {
    'result': fields.Boolean(default=False, title="Result"),
    'message': fields.String(default='No message', title="Error message"),
    'timetable': fields.List(
        fields.Nested(timetable_model)
        )
})

@ns.route('/get', methods=["GET"])
@ns.route('/get/<timestamp>', methods=["GET"])
@ns.header('X-API-KEY', 'TOKEN AUTH', required=True)
@ns.doc(security='Token Auth',params={'timestamp': 'Timestamp for a day'})
class TimetableGet(Resource):
    @ns.marshal_with(response_model)
    def get(self, timestamp=None):
        token = request.headers.get('X-API-KEY')
        message, code = check_token(token).explain()
        if code is not 200:
            return message, code
        timetable, status = get_timetable(token, timestamp)
        message, code = status.explain()
        if code is not 200:
            return message, code
        message['timetable'] = timetable
        return message, code