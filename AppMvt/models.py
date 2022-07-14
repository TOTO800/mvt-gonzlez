from django.db import models

# Create your models here.
class Padre(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    profesion= models.CharField(max_length=50)

class Madre(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    profesion= models.CharField(max_length=50)

class Hermano(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    profesion= models.CharField(max_length=50)