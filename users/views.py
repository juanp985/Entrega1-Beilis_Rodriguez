from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User_profile
from django.views.generic import UpdateView, ListView

@login_required
def perfil(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, 'perfil/perfil.html')
    else:
        return redirect('login')

class Perfil(LoginRequiredMixin, ListView):
    model = User_profile
    template_name= 'perfil/perfil.html'

class Update_perfil(LoginRequiredMixin, UpdateView):
    model = User_profile
    template_name= 'perfil/update_perfil.html'
    fields = '__all__'
    
    def get_success_url(self):
      return reverse('perfil')