import requests


def get_token_jar(token):
    j = requests.cookies.RequestsCookieJar()
    j.set_cookie(
        requests.cookies.create_cookie(
            "DZIENNIKSID",
            token,
            domain="synergia.librus.pl",
            path="/",
            secure=True,
            rest={"HttpOnly": None},
        )
    )
    return j


def is_token_valid(token):
    if not token:
        return False
    s = requests.Session()
    r = s.get("https://synergia.librus.pl/moje_zadania", cookies=get_token_jar(token))
    if "Brak dost\u0119pu" in str(r.text):
        return False
    if r.status_code == 200:
        return True
    else:
        return False


def get_token(login, password):
    s = requests.Session()
    s.get(
        url="https://api.librus.pl/OAuth/Authorization?\
                client_id=46&response_type=code&scope=mydata"
    )
    response = s.post(
        url="https://api.librus.pl/OAuth/Authorization?client_id=46",
        data={"action": "login", "login": login, "pass": password},
    )
    json = response.json()
    assert "status" in json
    token = None
    if "errors" in json:
        raise Exception(json["errors"][0]["message"])

    if "goTo" in json:
        r = s.get("https://api.librus.pl" + json["goTo"])
        token = str(r.cookies.get("DZIENNIKSID"))
    return token
