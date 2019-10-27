from .timetable import ns as timetable_ns
from .token import ns as token_ns

def add_namespaces(api):
    api.add_namespace(timetable_ns)
    api.add_namespace(token_ns)