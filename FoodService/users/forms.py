from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
    }))

    class Meta:
        model = User
        field = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите номер телефона'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_number', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={}))

    image = forms.ImageField(widget=forms.FileInput(attrs={}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'image', 'username',)
