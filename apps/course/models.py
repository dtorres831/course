from __future__ import unicode_literals

from django.db import models
from ..loginandreg.models import User
# Create your models here.
# class Users(models.Model):
#     class_user = models.ForeignKey(User)
#     created_at = models.DateField(auto_now_add =True)
#     updated_at = models.DateField(auto_now =True)

class Class(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length = 1000)
    created_at = models.DateField(auto_now_add =True)
    updated_at = models.DateField(auto_now =True)
    users = models.ManyToManyField(User, related_name = "courses")

class User_Class(models.Model):
    users = models.ForeignKey(User, related_name="user_users")
    title = models.ForeignKey(Class, related_name="title_class")
