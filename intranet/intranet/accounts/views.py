from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users
from .models import Bundle, Role, UserInfo
from .forms import CreateUserForm, UserInfoForm, RoleForm, BundleForm

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def prices(request):
    bundles = Bundle.objects.all()

    return render(request, 'accounts/prices.html', {'bundles': bundles})


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            logged_user_role = UserInfo.objects.filter(user_id=request.user.id).first()
            if logged_user_role.role_id > 2:
                return redirect('admin_panel')
            else:
                return redirect('single_profile', request.user.id)
        else:
            messages.info(request, 'Les identifiants ne correspondent pas à ceux que nous avons')

    context = {}
    return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
def usercreation(request):
    form = CreateUserForm()
    form2 = UserInfoForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Le compte a bien été créé pour: ' + user)

    context = {'form': form}
    return render(request, 'accounts/usercreation.html', context)


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
def showRole(request):
    roles = Role.objects.get()
    context = {'roles': roles}
    return render(request, 'accounts/show_role.html', context)


@login_required(login_url='login')
@allowed_users(allowed=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed=['admin'])
def deleteRole(request, pk):
    role = Role.objects.get(id=pk)
    if request.method == "POST":
        role.delete()
        return render(request, 'admin_panel')
    else:
        context = {'role': role}
        return render(request, 'accounts/delete_role.html', context)


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
def showBundle(request):
    bundles = Bundle.objects.get()
    context = {'bundles': bundles}
    return render(request, 'accounts/show_bundle.html', context)


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
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


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
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


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
def deleteBundle(request, pk):
    bundle = Bundle.objects.get(id=pk)
    if request.method == "POST":
        bundle.delete()
        return render(request, 'admin_panel')
    else:
        context = {'Bundle': bundle}
        return render(request, 'accounts/delete_bundle.html', context)


@login_required(login_url='login')
@allowed_users(allowed=['secretary', 'admin'])
def adminPanel(request):
    bundles = Bundle.objects.all()
    roles = Role.objects.all().order_by('id')[:5]
    users = get_user_model().objects.all()
    context = {'bundles': bundles, 'roles': roles, 'users': users}
    return render(request, 'accounts/admin_panel.html', context)


@login_required(login_url='login')
def singleProfile(request, pk):
    group = request.user.groups.all()[0].name
    admin = False
    if group == 'student':
        user = get_user_model().objects.get(id=request.user.id)
        user_info = UserInfo.objects.filter(user_id=request.user.id).first()
    else:
        user = get_user_model().objects.get(id=pk)
        user_info = UserInfo.objects.filter(user_id=pk).first()
    if group == 'admin' or group == 'secretary':
        admin = True
    context = {'user': user, 'user_info': user_info, 'admin': admin}
    return render(request, 'accounts/profile.html', context)


