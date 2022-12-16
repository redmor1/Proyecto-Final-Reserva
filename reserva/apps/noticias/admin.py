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


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)




   
