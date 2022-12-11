from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajesContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
