from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context = {'title': 'FoodService - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'title': 'FoodService - Регистрация', 'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
