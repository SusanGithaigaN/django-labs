from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    password= models.CharField(max_length=10)
    # make username unique to ensure every user has a unique username
    username = models.CharField(max_length=30, unique=True)