from django.contrib import admin
from AppForms.models import Profesor, Estudiante, Curso#, Detalle_curso, Detalle_materia

# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['legajo','nombre', 'apellido', 'email','activo']

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['legajo','nombre','apellido', 'email', 'profesion','activo']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre','comision','activo']

