from __future__ import unicode_literals
from django.db import models

class UserHack(models.Model):
    _gender = ((1, 'Female'), (2, 'Male'))
    id = models.AutoField(primary_key=True)
    gender = models.SmallIntegerField(choices=_gender)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        app_label = 'userHack'
        db_table = 'user_hack'
