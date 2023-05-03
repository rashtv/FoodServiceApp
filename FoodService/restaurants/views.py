from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import FoodCategory, RestaurantCategory, Restaurant, Food


def index(request):
    context = {'title': "FoodService - Main Page"}
    return render(request, 'restaurants/index.html', context)


def restaurants(request, category_id=None):
    if category_id:
        category = RestaurantCategory.objects.get(id=category_id)
        restaurant_list = Restaurant.objects.filter(category=category)
    else:
        restaurant_list = Restaurant.objects.all()

    p = Paginator(restaurant_list, 6)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'title': "FoodService - Restaurants",
        'restaurants': restaurant_list,
        'categories': RestaurantCategory.objects.all(),
        'page_obj': page_obj,
    }

    return render(request, 'restaurants/restaurants.html', context)


def restaurant_details(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant_menu = Food.objects.filter(restaurant=restaurant)

    restaurant_list = Restaurant.objects.all()
    p = Paginator(restaurant_list, 6)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'title': "FoodService - Restaurant Details",
        'restaurant': restaurant,
        'menu': restaurant_menu,
        'restaurants': restaurant_list,
        'page_obj': page_obj,

    }
    return render(request, 'restaurants/restaurant_detail.html', context)
