from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField
