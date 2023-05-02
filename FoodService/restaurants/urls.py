from django.urls import path

from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('restaurants/<int:restaurant_id>', views.restaurant_details, name='restaurant'),
    path('restaurants/category/<int:category_id>/', views.restaurants, name='category'),
]
