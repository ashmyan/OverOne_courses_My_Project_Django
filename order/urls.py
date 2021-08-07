from django.urls import path

from order import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.add_to_shop_cart, name='add_to_shop_cart'),
    path('shopcart/', views.shop_cart, name='shop_cart'),
]