import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs
from .login_flow import get_token_jar
from collections import namedtuple

TimetableLesson = namedtuple(
    "TimetableLesson", "index name teacher room start end flag break_start break_end day"
)


def valid_week(date):
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return start.strftime("%Y-%m-%d") + "_" + end.strftime("%Y-%m-%d")


def parse_timetable_html(html):
    b = bs(html, features="lxml")
    #html with invalid date won't have a selected date
    try:
        current_week = b.find("option", attrs={"selected": "selected"}).text
    except:
        return []
    current_week = datetime.strptime(current_week.split(" ")[0], "%Y-%m-%d")
    breaks = []
    for brk in b.find_all("tr", class_="line0"):
        brk = brk.text.split("\xa0-\xa0")
        brk[0] = datetime.strptime(brk[0], "%H:%M").time()
        brk[1] = datetime.strptime(brk[1], "%H:%M").time()
        breaks.append(brk)
    rows = b.find_all("tr", class_="line1")
    for row in rows:
        lesson_index = int(row.find("td", class_="center").text)
        time_span = row.find("th", class_="center").text.split("-")
        # \xa0hh:mm
        start = datetime.strptime(time_span[0][:-1], "%H:%M").time()
        # hh:mm\xa0
        end = datetime.strptime(time_span[1][1:], "%H:%M").time()
        del time_span
        for day, segment in enumerate(row.find_all("td", class_="line1")):
            if segment.text == "&nbsp;" or segment.text == "" or segment.text == "\xa0":
                pass
            else:
                flag = segment.find("div", class_="plan-lekcji-info")
                if flag is not None:
                    flag = flag.text.strip()
                current_day = current_week + timedelta(days=day)
                lesson_start = datetime.combine(current_day, start)
                lesson_end = datetime.combine(current_day, end)
                lesson_data = segment.find("div", class_="text")
                lesson_name = lesson_data.find("b").text.strip()
                break_start = datetime.combine(current_day, breaks[lesson_index][0])
                break_end = datetime.combine(current_day, breaks[lesson_index][1])
                teacher = (
                    lesson_data.find("br")
                    .next.replace("-", "")
                    .strip()
                    .replace("\xa0", " ")
                )
                room = teacher.split("&nbsp")
                room = None if len(room) < 2 else room[1].replace("s.", "").strip()
                teacher = teacher.split("&nbsp")[0]
                yield TimetableLesson(
                    lesson_index,
                    lesson_name,
                    teacher,
                    room,
                    lesson_start,
                    lesson_end,
                    flag,
                    break_start,
                    break_end,
                    day
                )._asdict()


def get_week_html(token, week):
    s = requests.Session()
    r = s.post(
        "https://synergia.librus.pl/przegladaj_plan_lekcji",
        data={"tydzien": valid_week(week)},
        cookies=get_token_jar(token),
    )
    return r.text
