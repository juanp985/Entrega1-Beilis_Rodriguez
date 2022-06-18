from django.urls import path
from users.views import perfil, Update_perfil, Perfil

urlpatterns =[

    ## Perfil ##
    path('perfil/', Perfil.as_view(), name = 'perfil'),
    path('update_perfil/<int:pk>/', Update_perfil.as_view(), name = 'update_perfil'),
]