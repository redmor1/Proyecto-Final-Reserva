from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def areas_de_estudio(request):
    return render(request, 'areas_de_estudio.html')

def proyectos(request):
    return render(request, 'proyectos.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            asunto = f'Consulta de Sitio Web Senderos: {asunto}'
            mensaje = form.cleaned_data['mensaje']
            mensaje = f"{mensaje}\n\n Este es mi email: {email}"
            email_sitio = settings.EMAIL_HOST_USER

            try:
                send_mail(subject=asunto, message=mensaje, from_email=email_sitio, recipient_list=[email_sitio,])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("contacto")
    else:
        form = ContactoForm()
        return render(request, "contacto.html", {'form':form}) 


def crear_post(request):
    return render(request, 'crear_post.html')

def publicaciones(request):
    return render(request, 'publicaciones.html')

def post(request):
    return render(request, 'post.html')

