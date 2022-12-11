from django.db import models

# Create your models here.

class MensajesContacto(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    asunto = models.CharField(max_length=150, blank=False, null=False)
    mensaje = models.TextField(max_length=2000, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Mensajes del formulario de contacto'

    def __str__(self):
        return str(self.asunto)
