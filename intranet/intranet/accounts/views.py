from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from .models import Bundle, Role
from .forms import CreateUserForm, UserInfoForm, RoleForm, BundleForm

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def prices(request):
    bundles = Bundle.objects.all()

    return render(request, 'accounts/prices.html', {'bundles': bundles})


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Les identifiants ne correspondent pas à ceux que nous avons')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def usercreation(request):
    form = CreateUserForm()
    form2 = UserInfoForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # form2 = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Le compte a bien été créé pour: ' + user)

    context = {'form': form}
    return render(request, 'accounts/usercreation.html', context)


def showRole(request):
    roles = Role.objects.get()
    context = {'roles': roles}
    return render(request, 'accounts/show_role.html', context)


def createRole(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = RoleForm()
        context = {'form': form}
        return render(request, 'accounts/create_role.html', context)


def updateRole(request, pk):
    role = Role.objects.get(id=pk)
    form = RoleForm(instance=role)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        context = {'form': form}
        return render(request, 'accounts/create_role.html', context)


def deleteRole(request, pk):
    role = Role.objects.get(id=pk)
    if request.method == "POST":
        role.delete()
        return render(request, 'admin_panel')
    else:
        context = {'role': role}
        return render(request, 'accounts/delete_role.html', context)


def showBundle(request):
    bundles = Bundle.objects.get()
    context = {'bundles': bundles}
    return render(request, 'accounts/show_bundle.html', context)


def createBundle(request):
    if request.method == 'POST':
        form = BundleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = BundleForm()
        context = {'form': form}
        return render(request, 'accounts/create_bundle.html', context)


def updateBundle(request, pk):
    bundle = Bundle.objects.get(id=pk)
    form = BundleForm(instance=bundle)
    if request.method == 'POST':
        form = BundleForm(request.POST, instance=bundle)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        context = {'form': form}
        return render(request, 'accounts/create_bundle.html', context)


def deleteBundle(request, pk):
    bundle = Bundle.objects.get(id=pk)
    if request.method == "POST":
        bundle.delete()
        return render(request, 'admin_panel')
    else:
        context = {'Bundle': bundle}
        return render(request, 'accounts/delete_bundle.html', context)


def adminPanel(request):
    bundles = Bundle.objects.all()
    roles = Role.objects.all().order_by('id')[:10]
    context = {'bundles': bundles, 'roles': roles}
    return render(request, 'accounts/admin_panel.html', context)

