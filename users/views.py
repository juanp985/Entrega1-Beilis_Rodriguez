from django.shortcuts import render

def editarperfil (request):
    context = {'perfil':'perfil'}
    return render(request,'editarperfil.html', context = context)