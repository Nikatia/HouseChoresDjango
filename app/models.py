from django.db import models
from django.contrib.auth.models import User
import datetime

class ChoreType(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=300, default='')

class Chore(models.Model):
    name = models.CharField(max_length=100, default='')
    type = models.ForeignKey(ChoreType, null=True, on_delete=models.SET_NULL)

class ChoreDone(models.Model):
    chore = models.ForeignKey(Chore, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, null=False)
    duration = models.IntegerField(default= 15,null=False)