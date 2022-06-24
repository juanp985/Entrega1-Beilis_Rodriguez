from django.db import models

## Curso ##
class Curso(models.Model):
    comision = models.IntegerField()
    nombre=models.CharField(max_length=40)
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)
    #detalle_curso = models.ForeignKey('Detalle_curso', on_delete=models.CASCADE, related_name='detalle_curso')
    activo = models.BooleanField(default=True)

class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

def __str__(self):
        return self.name


## Estudiante##
class Estudiante(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)
    activo = models.BooleanField(default=True)

class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

def __str__(self):
        return self.name

"""
class Detalle_curso(models.Model):
    anios = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
    )
    
    anio_materia = models.CharField(max_length=1, choices=anios)
    materia = models.CharField(max_length=100)
    detalle_materia = models.ForeignKey('Detalle_materia', on_delete=models.CASCADE, related_name='estudiante')

    class Meta:
        verbose_name = 'detalle_materia'
        verbose_name_plural = 'detalles_materia'

    def __str__(self):
        return self.name

class Detalle_materia(models.Model):
    estados = (
        ('0', 'Aprobado'),
        ('1', 'Recursa'),
    )
    
    parcial = models.CharField(max_length=50)
    final = models.CharField(max_length=100)
    estado_materia = models.CharField(max_length=1, choices=estados)

    class Meta:
        verbose_name = 'detalle_materia'
        verbose_name_plural = 'detalles_materia'

    def __str__(self):
        return self.name
"""

## Profesor ##
class Profesor(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    imagen = models.ImageField(upload_to = 'AppForms', blank=True, null=True)
    activo = models.BooleanField(default=True)

class Meta:
        verbose_name = 'profesor'
        verbose_name_plural = 'profesores'

def __str__(self):
        return self.name




