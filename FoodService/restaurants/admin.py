from django.contrib import admin

from .models import Category, Food, Restaurant, BasketItem, Order

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(BasketItem)
admin.site.register(Order)
