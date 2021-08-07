from django.urls import path
import user.views

urlpatterns = [
    path('login/', user.views.user_login, name='user_login'),
    path('registration/', user.views.registration, name='registration'),
    path('logout/', user.views.user_logout, name='logout'),

]
