from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your forms here.
from .models import Role, Bundle


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'


class BundleForm(ModelForm):
    class Meta:
        model = Bundle
        fields = '__all__'

