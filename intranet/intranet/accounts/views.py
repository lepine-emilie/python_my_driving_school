from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')


def prices(request):
    bundles = Bundle.objects.all()

    return render(request, 'accounts/prices.html', {'bundles': bundles})


def login(request):
    return render(request, 'accounts/login.html')
