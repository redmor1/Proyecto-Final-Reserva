from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *


class ContactoForm(forms.Form):
    email = forms.EmailField()
    asunto = forms.CharField(max_length=150)
    mensaje = forms.CharField(max_length=2000)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'texto', 'imagen', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']