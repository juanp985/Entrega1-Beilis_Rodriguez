from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    comision = models.IntegerField()

class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

class Estudiante(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Meta:
        verbose_name = 'profesor'
        verbose_name_plural = 'profesores'




