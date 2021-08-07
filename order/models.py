from django.contrib.auth.models import User
from django.db import models

from main.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.products.title

    @property
    def amount(self):
        return self.quantity * self.products.price
