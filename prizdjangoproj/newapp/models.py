from ctypes import addressof
from django.db import models
from django.forms import CharField

# Create your models here.
class schools(models.Model):
    name = models.CharField(max_length= 23)
    address = models.CharField(max_length= 23)

class country(models.Model):
    name = models.CharField(max_length= 23)
    
