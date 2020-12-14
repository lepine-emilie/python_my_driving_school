from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.home),
    path('contact/', views.contact, name='contact'),
    path('prices/', views.prices, name='prices'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('create_user/', views.usercreation, name='register'),
]

