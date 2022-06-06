from django.shortcuts import render
from AppForms.models import Curso, Profesor, Estudiante
from AppForms.forms import Curso_form, Profesor_form, Estudiante_form


def create_curso(request):
      
      if request.method == 'GET':
            curso = Curso_form ()
            context = {'curso':curso}
            return render(request,'create_curso.html', context=context)
      else:
            curso = Curso_form(request.POST)
            if curso.is_valid():
                  new_curso = Curso.objects.create(
                        nombre = curso.cleaned_data['nombre'],
                        camada = curso.cleaned_data['camada']
                  )
            context = {'new_curso':new_curso}
            return render(request,'create_curso.html', context = context)


def create_profesor(request):
      
      if request.method == 'GET':
            profesor = Profesor_form ()
            context = {'profesor':profesor}
            return render(request,'create_profesor.html', context=context)
      else:
            profesor = Profesor_form(request.POST)
            if profesor.is_valid():
                  new_profesor = Profesor.objects.create(
                        nombre = profesor.cleaned_data['nombre'],
                        apellido = profesor.cleaned_data['apellido'],
                        email = profesor.cleaned_data['email'],
                        profesion = profesor.cleaned_data['profesion']
                  )
            context = {'new_profesor':new_profesor}
            return render(request,'create_profesor.html', context=context)  


def create_estudiante(request):
      
      if request.method == 'GET':
            estudiante = Estudiante_form ()
            context = {'estudiante':estudiante}
            return render(request,'create_estudiante.html', context=context)
      else:
            estudiante = Estudiante_form(request.POST)
            if estudiante.is_valid():
                  new_estudiante = Estudiante.objects.create(
                        legajo = estudiante.cleaned_data['legajo'],
                        nombre = estudiante.cleaned_data['nombre'],
                        apellido = estudiante.cleaned_data['apellido'],
                        email = estudiante.cleaned_data['email']
                  )
            context = {'new_estudiante':new_estudiante}
            return render(request,'create_estudiante.html', context=context)                   

def search_alumno(request):
    print(request.GET)
    estudiantes = Estudiante.objects.filter(nombre = request.GET['search'])
    context = {'estudiantes':estudiantes}
    return render(request, 'search_alumno.html', context = context)