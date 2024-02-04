from django import forms

from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150)
    email = forms.EmailField(max_length=256)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    # Методы для валидации полей называются: `clean_` + `название поля`
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким username уже существует')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    # Общая проверка после проверки всех полей.
    def clean(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return data
    
    
class ResetForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150)
    email = forms.EmailField(max_length=256)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    # Методы для валидации полей называются: `clean_` + `название поля`
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            return username
        raise forms.ValidationError('Пользователь с таким username не существует')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Пользователь с таким email не существует')

    # Общая проверка после проверки всех полей.
    def clean(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return data