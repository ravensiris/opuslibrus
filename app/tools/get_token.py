from app.modules.login_flow import get_token as token_get, is_token_valid
from enum import Enum, auto
from base64 import b64decode

class TOKEN_STATUESES(Enum):
    INVALID = auto()
    VALID = auto()
    ERROR = auto()
    def explain(self):
        message = {'result': False}
        code = 200
        if self is self.INVALID:
            code = 401
            message['message'] = 'Your token is invalid or expired'
        if self is self.ERROR:
            code = 500
            message['message'] = 'An error has occurred'
        if self is self.VALID:
            message['result'] = True

        return message, code

class LOGIN_STATUSES(Enum):
    EMPTY_HEADER = auto()
    BASE64_ERROR = auto()
    NO_SEPARATOR = auto()
    NO_USERNAME = auto()
    NO_PASSWORD = auto()
    WRONG_CREDENTIALS = auto()
    WRONG_AUTH_TYPE = auto()
    OK = auto()
    
    def explain(self):
        message = {'result': False}
        code = 200
        if self is self.WRONG_CREDENTIALS:
            code = 401
            message['message'] = 'Wrong username and/or password'
        if self is self.NO_SEPARATOR:
            code = 400
            message['message'] = 'Your username and password have to be separated by ":"'
        if self is self.BASE64_ERROR:
            code = 400
            message['message'] = 'Your username and password have to be base64 encoded.'
        if self is self.EMPTY_HEADER:
            code = 400
            message['message'] = 'Specify your username and password in Authorization: Basic header.'
        if self is self.WRONG_AUTH_TYPE:
            code = 401
            message['message'] = 'Use a proper header. Authorization: Basic ***base64(username:password)***'
        if self is self.NO_USERNAME:
            code = 401
            message['message'] = 'No username provided'
        if self is self.NO_PASSWORD:
            code = 401
            message['message'] = 'No password provided'
        if self is self.OK:
            message['result'] = True
        
        return message, code

def check_token(header):
    try:
        if is_token_valid(header):
            return True, TOKEN_STATUESES.VALID
        else:
            return False, TOKEN_STATUESES.INVALID
    except:
        return False, TOKEN_STATUESES.ERROR

def get_token(header):
    token = None
    if header is None:
        return token, LOGIN_STATUSES.EMPTY_HEADER
    if not header.startswith('Basic '):
        return LOGIN_STATUSES.WRONG_AUTH_TYPE
    header = header[5:].strip()
    try:
        header = b64decode(header).decode('utf-8')
    except:
        return token, LOGIN_STATUSES.BASE64_ERROR
    if ':' in header:
        username, password = header.split(':')
        if username == '':
            return token, LOGIN_STATUSES.NO_USERNAME
        if password == '':
            return token, LOGIN_STATUSES.NO_PASSWORD
        try:
            token = token_get(username, password)
        except:
            return token, LOGIN_STATUSES.WRONG_CREDENTIALS
    else:
        return LOGIN_STATUSES.NO_SEPARATOR
    return token, LOGIN_STATUSES.OK