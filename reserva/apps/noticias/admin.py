from django.contrib import admin
from apps.noticias.models import *


# Register your models here.

class MensajesContactoAdmin(admin.ModelAdmin):
    ordering = ('nombre', 'email', 'asunto', 'mensaje', 'fecha_creacion')
    search_fields =  ('nombre', 'email', 'asunto', 'mensaje', 'fecha_creacion')
    list_display =  ('nombre', 'email', 'asunto', 'fecha_creacion')
    list_filter = ( 'nombre', 'email', 'fecha_creacion')


admin.site.register(MensajesContacto, MensajesContactoAdmin)
   
