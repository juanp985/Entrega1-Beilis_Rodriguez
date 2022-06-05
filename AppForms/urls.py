from django.urls import path
from AppForms.views import create_cursos, create_profesor, create_estudiante

urlpatterns =[
    path('create_cursos', create_cursos, name = 'create_cursos'),
    path('create_profesor', create_profesor, name = 'create_profesor'),
    path('create_estudiante', create_estudiante, name = 'create_estudiante'),
]