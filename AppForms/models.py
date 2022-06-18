from django.db import models

# Create your models here.
class Curso(models.Model):
    comision = models.IntegerField()
    nombre=models.CharField(max_length=40)
    #category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='products')
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)

class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

def __str__(self):
        return self.name

class Estudiante(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    #category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='products')
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)

class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

def __str__(self):
        return self.name

class Profesor(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    #category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='products')
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)

class Meta:
        verbose_name = 'profesor'
        verbose_name_plural = 'profesores'

def __str__(self):
        return self.name




