from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/accounts', views.home),
    path('/prices', views.home),
]