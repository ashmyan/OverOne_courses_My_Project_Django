from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.main_product, name='products'),
    path('categories/', views.main_categories, name='main_categories'),
    path('category_pick/<int:pk>', views.category_pick, name='category_pick'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('travel_detail/<int:pk>', views.travel_detail, name='travel_detail'),
    path('travel/', views.travel_pick, name='travel_pick'),


]