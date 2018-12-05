from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from datetime import datetime


from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

class Users(models.Model):
    user = models.ForeignKey(User, default=1)
    #num = models.IntegerField()
    nickname = models.CharField(max_length=250)

    def __str__(self):
        return self.nickname
