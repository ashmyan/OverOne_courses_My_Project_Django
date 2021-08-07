from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main.models import Product, Category, Travel
from order.models import ShopCart
from user.forms import CreateUserForm


def home(request):
    return render(request, 'main/home.html')


def main_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main/home.html', context)


def main_categories(request):

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'main/categories.html', context)


def category_pick(request, pk=0):
    category = Category.objects.all()
    if pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=pk)

    context = {
        'categories': category,
        'products': products,
    }
    return render(request, 'main/products.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    return render(request, 'main/product_details.html', {'product': product})


def travel_detail(request, pk):
    traveling = Travel.objects.get(pk=pk)
    return render(request, 'main/travel_details.html', {'traveling': traveling})


def travel_pick(request):
    travels = Travel.objects.all()
    return render(request, 'main/travel.html', {'travels': travels})


