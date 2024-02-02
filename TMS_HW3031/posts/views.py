from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

import uuid
from django.db.models import Case, When

from django.views import View

from django.urls import reverse
from django.http import HttpResponseRedirect, Http404,HttpRequest
from django.core.handlers.wsgi import WSGIRequest

from .models import Note, User, Tag
from .service import create_note, filter_notes, queryset_optimization, update_note, update_user
from .history import HistoryPageNotes
from .email import ConfirmUserRegisterEmailSender


def home_page_view(request: WSGIRequest):
    # Обязательно! каждая функция view должна принимать первым параметром request.
    all_notes = Note.objects.all()  # Получение всех записей из таблицы этой модели.
    
    queryset = queryset_optimization(Note.objects.all())
     
    context: dict = {
        "notes": all_notes
    }
    
    #return render(request, "home.html", context)
    return render(request, "home.html", {"notes": queryset[:100]})

@login_required
def create_note_view(request: WSGIRequest):
    if request.method == "POST":
        note = create_note(request)
        # note = Note.objects.create(
        #     title=request.POST["title"],
        #     content=request.POST["content"],
        # )
        return HttpResponseRedirect(reverse('show-note', args=[note.uuid]))

    # Вернется только, если метод не POST.
    return render(request, "create_form.html")


def show_note_view(request: WSGIRequest, note_uuid):
    try:
        note = Note.objects.get(uuid=note_uuid)  # Получение только ОДНОЙ записи.

    except Note.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404
    
    history_service = HistoryPageNotes(request)
    history_service.add_page(note)
    
    return render(request, "note.html", {"note": note})
# Create your views here.


def filter_notes_view(request: WSGIRequest):
    """
    Фильтруем записи по запросу пользователя.
    HTTP метод - GET.
    Обрабатывает URL вида: /filter/?search=<text>
    """

    search: str = request.GET.get("search", "")  # `get` - получение по ключу. Если такого нет, то - "",
    queryset = queryset_optimization(
        filter_notes(search)
    )

    context: dict = {
        "notes": queryset[:100],
        "search_value_form": search,
    }
    return render(request, "home.html", context)

def delete_node(request: WSGIRequest, note_uuid):
    try: 
        note = Note.objects.get(uuid=note_uuid)
        note.delete()
        return HttpResponseRedirect("/")
    except Note.DoesNotExist:
        raise Http404
    
def profile_update_view(request: WSGIRequest, username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        update_user(request, user)
        return HttpResponseRedirect("/")
    user = User.objects.get(username=username)
    tags_queryset = Tag.objects.filter(notes__user=user).distinct()
          
    return render(request, 'profile.html',{'tags': tags_queryset} )


@login_required
def update_note_view(request: WSGIRequest, note_uuid):
    try:
        note = Note.objects.get(uuid=note_uuid)
        
        if note.user == request.user:
            if request.method == "POST":
                note = update_note(request, note)
                # note.title = request.POST.get("title")
                # note.content = request.POST.get("content")
                # note.save()
                return HttpResponseRedirect("/")
            else:
                return render(request, "edit_form.html", {"note": note})
        else:
            return HttpResponseRedirect("/")
             
        
        # if request.method == "POST":
        #     note = update_note(request, note)
        #     # note.title = request.POST.get("title")
        #     # note.content = request.POST.get("content")
        #     # note.save()
        #     return HttpResponseRedirect("/")
        # else:
        #     return render(request, "edit_form.html", {"note": note})
    except Note.DoesNotExist:
        raise Http404



def show_about_view(request: WSGIRequest):
    return render(request, "show-about.html")

def user_notes(request: WSGIRequest, username: str):
    queryset = queryset_optimization(
        Note.objects.filter(user__username=username)
    )
    # SELECT * FROM "posts_note"
    # INNER JOIN "users" ON ("posts_note"."user_id" = "users"."id")
    # WHERE "users"."username" = boris1992
    # ORDER BY "posts_note"."created_at" DESC

    print(Note.objects.filter(user__username=username).query)

    return render(request, "posts-list.html", {"notes": queryset})


def register(request: WSGIRequest):
    if request.method != "POST":
        return render(request, "registration/register.html")
    print(request.POST)
    if not request.POST.get("username") or not request.POST.get("email") or not request.POST.get("password1"):
        return render(
            request,
            "registration/register.html",
            {"errors": "Укажите все поля!"}
        )
    print(User.objects.filter(
            Q(username=request.POST["username"]) | Q(email=request.POST["email"])
    ))
    # Если уже есть такой пользователь с username или email.
    if User.objects.filter(
            Q(username=request.POST["username"]) | Q(email=request.POST["email"])
    ).count() > 0:
        return render(
            request,
            "registration/register.html",
            {"errors": "Если уже есть такой пользователь с username или email"}
        )

    # Сравниваем два пароля!
    if request.POST.get("password1") != request.POST.get("password2"):
        return render(
            request,
            "registration/register.html",
            {"errors": "Пароли не совпадают"}
        )

    # Создадим учетную запись пользователя.
    # Пароль надо хранить в БД в шифрованном виде.
    user = User.objects.create_user(
        username=request.POST["username"],
        email=request.POST["email"],
        password=request.POST["password1"]
    )
    
    ConfirmUserRegisterEmailSender(request,user).send_mail()
    
    if user is not None:
        return HttpResponseRedirect(reverse("login"))
    
    return HttpResponseRedirect(reverse('home'))

def confirm_register_view(request: WSGIRequest, uidb64: str, token: str):
    username = force_str(urlsafe_base64_decode(uidb64))

    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save(update_fields=["is_active"])
        return HttpResponseRedirect(reverse("login"))

    return render(request, "registration/invalid_email_confirm.html", {"username": user.username})


class ListHistoryOfPages(View):
    def get(self, request: WSGIRequest):
        history_service = HistoryPageNotes(request)
        uuids = history_service.history_uuids[::-1]
        ordering = Case(*(When (uuid=ident, then=pos) for pos, ident in enumerate(uuids)))
        queryset = queryset_optimization(Note.objects.filter(uuid__in = history_service.history_uuids)).order_by(ordering)
        #queryset = queryset_optimization_history(Note.objects.filter(uuid__in = history_service.history_uuids))
        return render(request, "home.html", {"notes": queryset[:100]})
        


# class AddPagesToHistory(View):
#     def get(self, request: WSGIRequest, note_uuid: uuid):
#         note: Note = get_object_or_404(Note, uuid=note_uuid)
#         self.add_to_history(request, note)
#         return HttpResponseRedirect(reverse("show-note", args=(note.uuid,)))
    
#     @staticmethod
#     def add_to_history(request: WSGIRequest, note: Note):
#         history_service = HistoryPageNotes(request)
#         history_service.add_page(note)