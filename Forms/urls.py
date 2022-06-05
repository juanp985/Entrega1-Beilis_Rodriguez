from django.contrib import admin
from django.urls import path, include
from AppForms.views import home

urlpatterns = [
    path('home', home),
    path('crear/', include('AppForms.urls')),
    path('admin/', admin.site.urls),
]