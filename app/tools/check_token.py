from app.modules.login_flow import is_token_valid
from enum import Enum, auto

class TOKEN_STATUSES(Enum):
    NO_KEY_SPECIFIED = auto()
    SERVER_ERROR = auto()
    VALID = auto()
    INVALID = auto()
    def explain(self):
        message = {'result': False}
        code = 200
        if self is self.SERVER_ERROR:
            code = 503
            message['message'] = 'Librus unavailable or there has been a change in its website preventing our scraper to get the data'
        if self is self.NO_KEY_SPECIFIED:
            code = 400
            message['message'] = 'Specify your key in X-API-KEY header'
        if self is self.INVALID:
            code = 401
            message['message'] = 'Your key has expired or is invalid'
        if self is self.VALID:
            message['result'] = True
        
        return message, code

def check_token(header):
    if header is None:
        return TOKEN_STATUSES.NO_KEY_SPECIFIED
    try:
        if is_token_valid(header):
            return TOKEN_STATUSES.VALID
        else:
            return TOKEN_STATUSES.INVALID
    except Exception as e:
        return TOKEN_STATUSES.SERVER_ERROR
