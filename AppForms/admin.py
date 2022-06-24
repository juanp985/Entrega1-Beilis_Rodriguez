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

"""
@admin.register(Detalle_curso)
class DetallecursoAdmin(admin.ModelAdmin):
    list_display = ['anio_materia','materia','detalle_materia']

@admin.register(Detalle_materia)
class DetallemateriaoAdmin(admin.ModelAdmin):
    list_display = ['parcial','final','estado_materia']
"""

