from ast import mod
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    address= models.TextField(null=True, blank=True)
    city= models.CharField(max_length=100, null=True, blank=True)
    state= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username