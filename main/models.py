from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/images/categories/')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/product/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Travel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/travel/')
    url = models.URLField()

    def __str__(self):
        return self.title
