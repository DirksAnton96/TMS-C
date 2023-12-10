from flask import Flask, Response, request, render_template, redirect, url_for
from sqlalchemy import exc
from models import create_tables, drop_tables, add_notes

from crud import get_note,create_note,get_all_notes

app = Flask(__name__,
            template_folder="templates",
            static_folder="static",
            static_url_path="/static-files/")

create_tables()

@app.route("/",methods=["GET"])
def home_page_view():
    all_notes = get_all_notes()
    return render_template("home.html", notes=all_notes)

@app.route("/create_notes",methods=["GET"])
def get_createrpost_view():
    return render_template("createpost.html")

@app.route("/create_notes",methods=["POST"])
def createrpost_view():
    notes_data = request.form
    
    try:
        note = create_note(
            title = notes_data["title"],
            content = notes_data["content"]
        )
    except exc.IntegrityError:
        return f""" У нас такой заголовок уже есть: {notes_data["title"]}"""
    return redirect(url_for("get_note_uuid", uuid = note.uuid))

@app.route("/<uuid>",methods=["GET"])
def get_note_uuid(uuid: str):
    try:
        note = get_note(uuid)
    except exc.NoResultFound:
        return Response("Note not found.",status=404)
    return render_template(
        "notes_view.html",
        uuid = note.uuid,
        title = note.title,
        content = note.content,
        create_at = note.create_at
    )