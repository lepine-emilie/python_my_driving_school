from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.home),
    path('contact/', views.contact, name='contact'),
    path('prices/', views.prices, name='prices'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create_user/', views.usercreation, name='register'),
    path('create_role/', views.createRole, name='create_role'),
    path('update_role/<str:pk>/', views.updateRole, name='update_role'),
    path('delete_role/<str:pk>/', views.deleteRole, name='delete_role'),
]

