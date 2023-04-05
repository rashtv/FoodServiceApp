from django.db import models
# from ..users.models import User
import sys
sys.path.append('C:/MyFiles/KBTU_docs/sem_6/Django/FinalProject/FoodService/users')
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='food_image')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BasketItem(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Корзина товаров для {self.user.username}"


class Order(models.Model):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    items = models.TextField(max_length=1024)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    isConfirmed = models.BooleanField(default=False)
    isCooked = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Заказ товаров для {self.user.username}"