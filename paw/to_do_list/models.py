from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100 , null=True)
    username = models.CharField(max_length=100 , null=True)
    email = models.EmailField(null=True , blank=True)
    time = models.DateTimeField(null=True , blank=True)
    notify = models.DateTimeField(null=True , blank=True)
