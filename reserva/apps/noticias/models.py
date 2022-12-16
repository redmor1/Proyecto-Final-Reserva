from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    imagen = models.ImageField(upload_to='post', null=True)
    resumen = models.TextField(max_length=350, blank=False, null=False)
    texto = models.TextField(max_length=None, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    comentarios_activados = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.titulo)
