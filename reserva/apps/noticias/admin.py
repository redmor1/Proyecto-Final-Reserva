from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    ordering = ('id', 'titulo', 'fecha_creacion', 'comentarios_activados')
    search_fields = ('id', 'titulo', 'fecha_creacion', 'resumen', 'texto')
    list_display = ('id', 'titulo', 'fecha_creacion', 'comentarios_activados')
    list_filter = ('fecha_creacion', 'comentarios_activados')


admin.site.register(Post, PostAdmin)



   
