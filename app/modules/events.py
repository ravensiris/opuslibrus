import requests
from app.modules.login_flow import get_token_jar
from bs4 import BeautifulSoup as bs
from datetime import datetime

TODAY = datetime.today()

def cancelled_event(event_lines):
    info = event_lines[1]
    teacher = info.split(" na lekcji nr: ")
    lesson_id = teacher[1]
    teacher = teacher[0]
    lesson_name = lesson_id.split(" (")
    lesson_id = int(lesson_name[0])
    lesson_name = lesson_name[1][:-1]
    return {"type": "cancelled", "message": event_lines[0], "lesson_name": lesson_name, "lesson_id": lesson_id, "teacher": teacher}

def exam_event(event_lines):
    lesson_id = event_lines[0].split("Nr lekcji: ")[1]
    lesson_name = event_lines[1]
    exam_type = event_lines[2][2:]
    room = None
    if len(event_lines)==5:
        room = event_lines[4].split("\xa0")[1]
    return {"type": "exam", "lesson_name": lesson_name, "lesson_id": lesson_id, "exam_type": exam_type, "room": room}

def substitution_event(event_lines):
    info = event_lines[0]
    teacher = info.split("stwo z ")[1]
    lesson_id = teacher.split(" na lekcji nr: ")
    teacher = lesson_id[0]
    lesson_id = lesson_id[1]
    lesson_name = lesson_id.split(" (")
    lesson_id = lesson_name[0]
    lesson_name = lesson_name[1][:-1]
    return {"type": "substitution", "teacher": teacher, "lesson_id": lesson_id, "lesson_name": lesson_name}

def parse_event(event_lines):
    if len(event_lines)==1:
        if "Zastępstwo" in event_lines[0]:
            return substitution_event(event_lines)
        return {"type": "misc", "message": event_lines[0]}
    if "Odwołane zajęcia" in event_lines[0]:
        return cancelled_event(event_lines)
    if len(event_lines)>=4:
        return exam_event(event_lines)

def get_events_html(token, month=TODAY.month, year=TODAY.year):
    s = requests.Session()
    r = s.post(
        "https://synergia.librus.pl/terminarz",
        data={"miesiac": month, "rok": year},
        cookies=get_token_jar(token),
    )
    return r.text

def parse_events_html(html):
    b = bs(html, features="lxml")
    days = b.find_all("div", class_="kalendarz-dzien")
    out = []
    for day_index, day in enumerate(days):
        table = day.find("table")
        if table:
            for event in table.find_all("td"):
                lines = []
                for s in event.stripped_strings:
                    lines.append(s)
                ev = parse_event(lines)
                ev["day_index"] = day_index
                out.append(ev)
    return out
            