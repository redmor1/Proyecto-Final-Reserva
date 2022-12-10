from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def areas_de_estudio(request):
    return render(request, 'areas_de_estudio.html')

def proyectos(request):
    return render(request, 'proyectos.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def crear_post(request):
    return render(request, 'crear_post.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def publicaciones(request):
    return render(request, 'publicaciones.html')