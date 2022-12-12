from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UsuarioRegistroForm

def registro(request):
    if request.method == 'POST':    
        form = UsuarioRegistroForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada, ahora puedes logearte!')
            return redirect('login')
    else:
        form = UsuarioRegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login(request):
    return render(request, 'usuarios/login.html')


