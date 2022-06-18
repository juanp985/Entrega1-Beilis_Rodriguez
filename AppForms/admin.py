from django.contrib import admin
from AppForms.models import Profesor, Estudiante, Curso

# Register your models here.
@admin.register(Estudiante)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['legajo','nombre', 'apellido', 'email']

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['legajo','nombre','apellido', 'email', 'profesion']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre','comision']





