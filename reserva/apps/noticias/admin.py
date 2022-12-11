from django.contrib import admin
from apps.noticias.models import *


# Register your models here.

class MensajesContactoAdmin(admin.ModelAdmin):
    ordering = ('nombre', 'email', 'asunto', 'mensaje')
    search_fields =  ('nombre', 'email', 'asunto', 'mensaje')
    list_display =  ('nombre', 'email', 'asunto')
    list_filter = ( 'nombre', 'email',)


admin.site.register(MensajesContacto, MensajesContactoAdmin)
   
