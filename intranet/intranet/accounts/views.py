from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *
from .forms import CreateUserForm

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def contact(request):
    return render(request, 'accounts/contact.html')


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
            user = form.cleaned_data.get('email')
            messages.success(request, 'Le compte a bien été créé pour: ' + user)

    context = {'form': form}
    return render(request, 'accounts/usercreation.html', context)

