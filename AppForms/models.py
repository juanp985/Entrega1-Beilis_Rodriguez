from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)





