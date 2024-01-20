from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest

from .models import User
from .forms import RegisterForm


# def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if username and User.objects.filter(username=username).exists():
#             raise forms.ValidationError('Пользователь с таким username уже существует')
#         return username

def register_view(request: WSGIRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register-form.html', {'form': form})
# Create your views here.
