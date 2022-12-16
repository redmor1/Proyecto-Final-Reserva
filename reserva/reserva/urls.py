"""reserva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from apps.noticias.views import *
from apps.usuarios.views import registro, login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('areas_de_estudio/', areas_de_estudio, name='areas_de_estudio'),
    path('proyectos/', proyectos, name='proyectos'),
    path('servicios/', servicios, name='servicios'),
    path('contacto/', contacto, name='contacto'),
    path('crear_post/', crear_post, name='crear_post'),
    path('usuarios/login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('usuarios/logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('usuarios/registro/', registro, name='registro'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('post/', post, name='post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


