from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.TextField(max_length=1000)
    salt = models.TextField(max_length=1000)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
