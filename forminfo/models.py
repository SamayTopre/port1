from django.db import models

# Create your models here.


class forminfo(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)