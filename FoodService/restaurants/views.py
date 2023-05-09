from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import FoodCategory, RestaurantCategory, Restaurant, Food, BasketItem, Order


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

    drink_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=1))
    dessert_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=2))
    pizza_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=3))
    burger_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=4))
    chicken_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=5))
    sushi_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=6))
    doner_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=7))
    hot_dishes_list = restaurant_menu.filter(category=FoodCategory.objects.get(id=8))

    context = {
        'title': "FoodService - Restaurant Details",
        'restaurant': restaurant,
        'menu': restaurant_menu,

        'drink_list': drink_list,
        'dessert_list': dessert_list,
        'pizza_list': pizza_list,
        'burger_list': burger_list,
        'chicken_list': chicken_list,
        'sushi_list': sushi_list,
        'doner_list': doner_list,
        'hot_dishes_list': hot_dishes_list,
    }
    return render(request, 'restaurants/restaurant_detail.html', context)


@login_required
def basket_item_add(request, product_id):
    food = Food.objects.get(id=product_id)
    basket_items = BasketItem.objects.filter(user=request.user, food=food)

    if not basket_items.exists():
        BasketItem.objects.create(user=request.user, food=food, quantity=1)
    else:
        basket_item = basket_items.first()
        basket_item.quantity += 1
        basket_item.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_item_remove(request, basket_item_id):
    basket_item = BasketItem.objects.get(id=basket_item_id)
    basket_item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def make_order(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    restaurant = basket_items.first().food.restaurant
    d = dict()

    for basket_item in basket_items:
        food = basket_item.food.name
        d[food] = basket_item.quantity
        basket_item.delete()

    Order.objects.create(restaurant=restaurant, user=request.user, items=d, isConfirmed=True)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
