from app.modules.timetable import get_week_html, parse_timetable_html
from datetime import datetime
from enum import Enum, auto

class TIMETABLE_STATUSES(Enum):
    DATE_PARSE_FAIL = auto()
    GET_HTML_FAIL = auto()
    PARSE_FAIL = auto()
    OK = auto()
    def explain(self):
        message = {'result': False}
        code = 200
        if self is self.PARSE_FAIL:
            code = 500
            message['message'] = 'Unable to parse data'
        if self is self.DATE_PARSE_FAIL:
            code = 500
            message['message'] = 'Unable to parse timestamp provided'
        if self is self.GET_HTML_FAIL:
            code = 503
            message['message'] = 'Unable to fetch html from Librus'
        if self is self.OK:
            message['result'] = True
        return message, code

class WeekStart(datetime):
    def __new__(self, timestamp):
        d = datetime.fromtimestamp(int(timestamp))
        d = datetime(year=d.year, month=d.month, day=d.day - d.weekday())
        return d

def get_timetable(token, timestamp):
    try:
        if timestamp is None:
            date = WeekStart(datetime.now().timestamp())
        else:
            date = WeekStart(timestamp)
    except:
        return None, TIMETABLE_STATUSES.DATE_PARSE_FAIL
    
    try:
        html = get_week_html(token, date)
    except:
        return None, TIMETABLE_STATUSES.GET_HTML_FAIL
    try:
        timetable = list(parse_timetable_html(html))
    except:
        return None, TIMETABLE_STATUSES.PARSE_FAIL
    return timetable, TIMETABLE_STATUSES.OK
