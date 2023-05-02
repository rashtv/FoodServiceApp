from django.contrib import admin

from .models import RestaurantCategory, FoodCategory, Food, Restaurant, BasketItem, Order

admin.site.register(RestaurantCategory)
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(BasketItem)
admin.site.register(Order)
