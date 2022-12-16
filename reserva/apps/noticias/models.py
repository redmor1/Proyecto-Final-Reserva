from django.db import models

# Create your models here.





class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return str(self.nombre)
        
        
        
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    imagen = models.ImageField(upload_to='post', null=True)
    resumen = models.TextField(max_length=350, blank=False, null=False)
    texto = models.TextField(max_length=None, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    comentarios_activados = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.titulo)