from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    mail = models.EmailField(max_length=20)
    #category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='products')
    imagen = models.ImageField(upload_to = 'users', blank=True, null=True)

def __str__(self):
        return self.name