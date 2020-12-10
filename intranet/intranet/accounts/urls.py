from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts', views.home),
    path('contact', views.contact, name='contact'),
    path('prices', views.prices, name='prices'),
    path('login', views.login, name='login'),
    path('create_user', views.usercreation, name='register'),
]

