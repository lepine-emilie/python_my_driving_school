from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')
def prices(request):
    return render(request, 'accounts/prices.html')
def login(request):
    return render(request, 'accounts/login.html')
