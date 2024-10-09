from django.db import models

# Create your models here.


class SyslogModel(models.Model):
    datetime = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    alert = models.TextField()
