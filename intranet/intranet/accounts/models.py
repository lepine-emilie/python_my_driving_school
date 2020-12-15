from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    phone = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    postal_code = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    hours_left = models.IntegerField(null=True)
    hours_total = models.IntegerField(null=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return User.username


class Bundle(models.Model):
    name = models.CharField(max_length=255, null=False)
    hours = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=True)
    picture_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date_start = models.DateTimeField()
    instructor = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='instructor')
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='student')


class link(models.Model):
    instructor = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='linkedInstructor')
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='linkedStudent')

    def __str__(self):
        return self.student

