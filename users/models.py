from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200)
