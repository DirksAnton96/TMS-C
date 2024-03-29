from aiohttp import web

from . import views

routes = [
    web.get("/", handler=views.HomeView),  # Только метод get!
    web.route("*", "/login", handler=views.LoginView),
    web.route("*", "/register", handler=views.RegisterView),
    web.route("*", "/notes/create", handler=views.NoteCreateView),
    web.route("*", "/notes/update/{post_id}", handler=views.NoteUpdateView),
    web.route("*", "/notes/delete/{post_id}", handler=views.NoteDeleteView),
]