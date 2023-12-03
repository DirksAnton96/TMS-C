from flask import Flask, Response, request
from sqlalchemy import exc
from models import create_tables, drop_tables, add_notes

from crud import get_note,create_note

app = Flask(__name__)

create_tables()

@app.route("/",methods=["GET"])
def home_page_view():
    return "<h1>Hi</h1>"

@app.route("/create_notes",methods=["GET"])
def get_createrpost_view():
    return (     
        "<h1>Create note</h1>"
        '<form action="/create_notes" method="post">'
        '<p>title: <input type="text" name="title"></p>'
        '<p>content: <input type="text" name="content"></p>'
        '<p>time creation: <input type="datetime-local" name="create_at"></p>'
        '<p> <input type="submit"> </p>'
        '</form>'
        )

@app.route("/create_notes",methods=["POST"])
def createrpost_view():
    notes_data = request.form
    
    try:
        note = create_note(
            title = notes_data["title"],
            content = notes_data["content"],
            time_creation = notes_data["create_at"]
        )
    except exc.IntegrityError:
        return f""" У нас такой заголовок уже есть: {notes_data["title"]}"""
    return f""" <h1> Пост добавлен </h1>
                <p> UUID: {note.uuid} </p>
            """

@app.route("/<uuid>",methods=["GET"])
def get_note_uuid(uuid: str):
    try:
        note = get_note(uuid)
    except exc.NoResultFound:
        return Response("Note not found.",status=404)
    return f"""
            <h1> you connect to note with uuid: {note.uuid} </h1>
            <p> content: {note.content} </p>
            <p> date creation: {note.create_at} </p>
            """