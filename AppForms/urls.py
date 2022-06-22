from django.urls import path
from AppForms.views import create_curso, create_profesor, create_estudiante, search_estudiante
from AppForms.views import Cursos, Delete_curso, Update_curso, Detail_curso, Profesores, Detail_profesor, Delete_profesor,Edit_curso
from AppForms.views import Edit_profesor, Update_profesor, Estudiantes, Edit_estudiante, Delete_estudiante, Update_estudiante, Detail_estudiante

urlpatterns =[

    ## Curso ##
    path('curso/create_curso', create_curso, name = 'create_curso'),
    path('curso/cursos', Cursos.as_view(), name = 'cursos'),
    path('curso/detail_curso/<int:pk>/', Detail_curso.as_view(), name = 'detail_curso'),
    path('curso/edit_curso/', Edit_curso.as_view(), name = 'edit_curso'),
    path('curso/delete_curso/<int:pk>/', Delete_curso.as_view(), name = 'delete_curso'),
    path('curso/update_curso/<int:pk>/', Update_curso.as_view(), name = 'update_curso'),
    
    ## Profesor ##
    path('profesor/create_profesor', create_profesor, name = 'create_profesor'),
    path('profesor/profesores', Profesores.as_view(), name = 'profesores'),
    path('profesor/detail_profesor/<int:pk>/', Detail_profesor.as_view(), name = 'detail_profesor'),
    path('profesor/edit_profesor/', Edit_profesor.as_view(), name = 'edit_profesor'),
    path('profesor/delete_profesor/<int:pk>/', Delete_profesor.as_view(), name = 'delete_profesor'),
    path('profesor/update_profesor/<int:pk>/', Update_profesor.as_view(), name = 'update_profesor'),
    
    ## Estudiante ##
    path('estudiante/create_estudiante', create_estudiante, name = 'create_estudiante'),
    path('estudiante/estudiantes', Estudiantes.as_view(), name = 'estudiantes'),
    path('estudiante/detail_estudiante/<int:pk>/', Detail_estudiante.as_view(), name = 'detail_estudiante'),
    path('estudiante/edit_estudiante/', Edit_estudiante.as_view(), name = 'edit_estudiante'),
    path('estudiante/delete_estudiante/<int:pk>/', Delete_estudiante.as_view(), name = 'delete_estudiante'),
    path('estudiante/update_estudiante/<int:pk>/', Update_estudiante.as_view(), name = 'update_estudiante'),
    path('estudiante/search_estudiante', search_estudiante, name = 'search_estudiante'),
]