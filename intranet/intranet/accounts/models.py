from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Utilisateur(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=True)
    hours_left = models.IntegerField(null=True)
    hours_total = models.IntegerField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    password_changed = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name


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
    instructor = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='instructor')
    student = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='student')


class link(models.Model):
    instructor = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='linkedInstructor')
    student = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE, related_name='linkedStudent')

    def __str__(self):
        return self.student

