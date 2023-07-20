import requests
from pprint import pprint
from flask_app import app
from flask import redirect, render_template, request, session


def make_request(url):
    response = requests.get(url)
    return response.json()


@app.get("/")
def index():
    """ Get request to Rick and Morty API for all characters. """

    if not 'url' in session:
        session["url"] = "https://rickandmortyapi.com/api/character"

    json = make_request(session["url"])

    results = json["results"]
    info = json["info"]

    print('*'*20)
    pprint(info)
    print('*'*20)

    characters = []

    for result in results:
        character = {
            "id": result["id"],
            "gender": result["gender"],
            "name": result["name"],
            "species": result["species"],
            "image": result["image"]
        }
        characters.append(character)

    return render_template("/index.html", characters=characters, info=info)


@app.post("/url/set")
def set_url():
    session["url"] = request.form["url"]
    return redirect("/")
