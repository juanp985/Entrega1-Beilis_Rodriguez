from django.shortcuts import render
from django.urls import reverse
from AppForms.models import Curso, Profesor, Estudiante#, Detalle_curso, Detalle_materia
from AppForms.forms import Curso_form, Profesor_form, Estudiante_form#, Detalle_curso_form, Detalle_materia_form
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import date

## Cursos ##
@login_required
def create_curso(request):
      
      if request.method == 'GET':
            cursos = Curso_form ()
            context = {'cursos':cursos}
            return render(request,'curso/create_curso.html', context=context)
      else:
            cursos = Curso_form(request.POST, request.FILES)
            if cursos.is_valid():
                  new_curso = Curso.objects.create(
                        nombre = cursos.cleaned_data['nombre'],
                        comision = cursos.cleaned_data['comision'],
                        imagen = cursos.cleaned_data['imagen'],
                        activo = cursos.cleaned_data['activo'],
                  )
                  context = {'new_curso':new_curso}
            else:
                  context = {'errors': cursos.errors}
            return render(request,'curso/create_curso.html', context = context)

class Cursos(LoginRequiredMixin, ListView):
    model = Curso
    template_name= 'curso/cursos.html'
    queryset = Curso.objects.filter(activo = True)

class Detail_curso(LoginRequiredMixin, DetailView):
    model = Curso
    template_name= 'curso/detail_curso.html'

class Edit_curso(LoginRequiredMixin, ListView):
    model = Curso
    template_name= 'curso/edit_curso.html'

class Delete_curso(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name= 'curso/delete_curso.html'

    def get_success_url(self):
        return reverse('cursos')

class Update_curso(LoginRequiredMixin, UpdateView):
    model = Curso
    template_name= 'curso/update_curso.html'
    fields = '__all__'
    queryset = Curso.objects.filter(activo = True)

    def get_success_url(self):
      return reverse('cursos')

## Profesores ##
@login_required
def create_profesor(request):
      
      if request.method == 'GET':
            profesores = Profesor_form ()
            context = {'profesores':profesores}
            return render(request,'profesor/create_profesor.html', context=context)
      else:
            profesores = Profesor_form(request.POST, request.FILES)
            if profesores.is_valid():
                  new_profesor = Profesor.objects.create(
                        legajo = profesores.cleaned_data['legajo'],
                        nombre = profesores.cleaned_data['nombre'],
                        apellido = profesores.cleaned_data['apellido'],
                        email = profesores.cleaned_data['email'],
                        profesion = profesores.cleaned_data['profesion'],
                        imagen = profesores.cleaned_data['imagen'],
                        activo = profesores.cleaned_data['activo'],
                  )
                  context = {'new_profesor':new_profesor}
            else:
                  context = {'errors': profesores.errors}
            return render(request,'profesor/create_profesor.html', context=context)  


class Profesores(LoginRequiredMixin, ListView):
    model = Profesor
    template_name= 'profesor/profesores.html'
    queryset = Profesor.objects.filter(activo = True)

class Detail_profesor(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name= 'profesor/detail_profesor.html'

class Edit_profesor(LoginRequiredMixin, ListView):
    model = Profesor
    template_name= 'profesor/edit_profesor.html'

class Delete_profesor(LoginRequiredMixin, DeleteView):
    model = Profesor
    template_name= 'profesor/delete_profesor.html'

    def get_success_url(self):
        return reverse('profesores')

class Update_profesor(LoginRequiredMixin, UpdateView):
    model = Profesor
    template_name= 'profesor/update_profesor.html'
    fields = '__all__'
    queryset = Profesor.objects.filter(activo = True)
    
    def get_success_url(self):
      return reverse('profesores')

## Estudiantes ##
@login_required
def create_estudiante(request):
      
      if request.method == 'GET':
            estudiantes = Estudiante_form ()
            context = {'estudiantes':estudiantes}
            return render(request,'estudiante/create_estudiante.html', context=context)
      else:
            estudiantes = Estudiante_form(request.POST, request.FILES)
            if estudiantes.is_valid():
                  new_estudiante = Estudiante.objects.create(
                        legajo = estudiantes.cleaned_data['legajo'],
                        nombre = estudiantes.cleaned_data['nombre'],
                        apellido = estudiantes.cleaned_data['apellido'],
                        email = estudiantes.cleaned_data['email'],
                        imagen = estudiantes.cleaned_data['imagen'],
                        activo = estudiantes.cleaned_data['activo'],
                  )
                  context = {'new_estudiante':new_estudiante}
            else:
                  context = {'errors': estudiantes.errors}
            return render(request,'estudiante/create_estudiante.html', context=context)                   

class Estudiantes(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name= 'estudiante/estudiantes.html'
    queryset = Estudiante.objects.filter(activo = True)

class Detail_estudiante(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name= 'estudiante/detail_estudiante.html'

class Edit_estudiante(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name= 'estudiante/edit_estudiante.html'

class Delete_estudiante(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name= 'estudiante/delete_estudiante.html'

    def get_success_url(self):
        return reverse('estudiantes')

class Update_estudiante(LoginRequiredMixin, UpdateView):
    model = Estudiante
    template_name= 'estudiante/update_estudiante.html'
    fields = '__all__'
    queryset = Estudiante.objects.filter(activo = True)

    
    def get_success_url(self):
      return reverse('estudiantes')

@login_required
def search_estudiante(request):

    print(request.GET)
    
    nombre_busqueda = request.GET['search']
    if nombre_busqueda:
      estudiantes = Estudiante.objects.filter(nombre__contains = nombre_busqueda)
      if estudiantes.exists():
            context = {'estudiantes':estudiantes}
      else:
            context = {'errors':f'El estudiante con el siguiente nombre no se encuentra creado: {nombre_busqueda}'}
      return render(request, 'estudiante/search_estudiante.html', context = context)
    else:
      context = {'errors':'No se ha escrito nada en la barra de busqueda.'}
      return render(request, 'estudiante/search_estudiante.html', context = context)