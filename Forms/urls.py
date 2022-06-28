from django.contrib import admin
from django.urls import path, include
from Forms.views import home, about, login_view, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('about/', about),
    path('appforms/', include('AppForms.urls')),
    path('perfil/', include('users.urls')),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)