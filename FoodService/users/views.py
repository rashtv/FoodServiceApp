from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import sys

sys.path.append('C:/MyFiles/KBTU_docs/sem_6/Django/FinalProject/FoodService/restaurants')
from restaurants.models import BasketItem


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
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    basket_items = BasketItem.objects.filter(user=request.user)

    total_sum = 0
    total_quantity = 0
    for basket_item in basket_items:
        total_sum += basket_item.sum()
        total_quantity += basket_item.quantity

    context = {'title': "FoodService - Профиль",
               'form': form,
               'basket_items': basket_items,
               'total_sum': total_sum,
               'total_quantity': total_quantity,
               }
    return render(request, 'users/profile.html', context)
