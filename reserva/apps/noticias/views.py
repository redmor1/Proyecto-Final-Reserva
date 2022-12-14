from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator




# Create your views here.

class MostrarPost(View):
    template = 'index.html'

    def get(self, request):
        posteos = Post.objects.all().order_by('-id')
        categorias = Categoria.objects.all()

        page_number = request.GET.get('page', 1)
        paginator = Paginator(posteos, 3)
        page_obj = paginator.page(page_number)
        is_paginated = page_obj.paginator.num_pages > 1

        
        contexto = {
            'posteos': page_obj,
            'categorias': categorias,
            'is_paginated': is_paginated,
        }
        return render(request, 'index.html', contexto)

    def post(self, request):
        posteos = Post.objects.all().order_by('-id')
        categorias = Categoria.objects.all()
        cate = request.POST.get('categoria', None)
        fecha = request.POST.get('fecha', None)
        print(fecha)
        if cate and fecha:
            posteos = Post.objects.filter(categoria__nombre=cate, fecha_creacion=fecha).order_by('-id')
        elif cate:
            posteos = Post.objects.filter(categoria__nombre=cate).order_by('-id')
        elif fecha:
            posteos = Post.objects.filter(fecha_creacion=fecha).order_by('-id')

        contexto = {
            'posteos': posteos,
            'categorias': categorias
            }
        return render(request, 'index.html', contexto)


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

@login_required
def crear_post(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post')
    else:
        post_form = PostForm()
    return render(request, 'crear_post.html', {'post_form': post_form})

def publicaciones(request):
    return render(request, 'publicaciones.html')

def leer_post(request, id):

    if request.method == 'GET':
        post = Post.objects.get(id=id)
        comentarios = Comentario.objects.filter(post__id=id)
        form = ComentarioForm()
        imagen_url = post.imagen.url
        context = {
            'post': post,
            'comentarios': comentarios,
            'form': form,
            'imagen_url': imagen_url
        }
        return render(request, 'post.html', context)

    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        post = Post.objects.get(id=id)
        form = ComentarioForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = user
            form.post = post
            form.save()
            return redirect('post', id=id)
    else:
        form = ComentarioForm()
    return render(request, 'post.html', {'form': form, 'imagen_url': imagen_url})


    





