from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    ordering = ('id', 'titulo', 'fecha_creacion', 'comentarios_activados')
    search_fields = ('id', 'titulo', 'fecha_creacion', 'resumen', 'texto')
    list_display = ('id', 'titulo', 'fecha_creacion', 'comentarios_activados')
    list_filter = ('categoria', 'fecha_creacion', 'comentarios_activados')

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('id', 'nombre', 'activado', 'fecha_creacion')
    search_fields = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_display = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_filter = ('activado',)

class ComentarioAdmin(admin.ModelAdmin):
    ordering = ('id', 'usuario', 'post', 'contenido')
    search_fields = ('id', 'usuario', 'post', 'contenido')
    list_display = ('id', 'usuario', 'post', 'fecha_creacion', 'contenido')
    list_filter = ('usuario', 'post', 'fecha_creacion')


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)




   
