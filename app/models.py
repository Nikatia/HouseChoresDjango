from django.db import models
from django.contrib.auth.models import User

class ChoreType(models.Model):
    name = models.CharField(max_length=100, default='')

class Chore(models.Model):
    name = models.CharField(max_length=100, default='')
    type = models.ForeignKey(ChoreType, null=True, on_delete=models.SET_NULL)

class ChoreDone(models.Model):
    chore = models.ForeignKey(Chore, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()