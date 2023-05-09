from django.urls import path

from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('restaurants/<int:restaurant_id>', views.restaurant_details, name='restaurant'),
    path('restaurants/category/<int:category_id>/', views.restaurants, name='category'),
    path('baskets/add/<int:product_id>/', views.basket_item_add, name='basket_item_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_item_remove, name='basket_item_remove'),
    path('orders/make/', views.make_order, name='make_order'),
]
