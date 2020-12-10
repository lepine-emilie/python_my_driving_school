from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import CreateUserForm

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')


def prices(request):
    bundles = Bundle.objects.all()

    return render(request, 'accounts/prices.html', {'bundles': bundles})


def login(request):
    return render(request, 'accounts/login.html')


def usercreation(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/usercreation.html', context)

