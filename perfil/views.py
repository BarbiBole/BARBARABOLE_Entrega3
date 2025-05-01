from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm
from perfil.models import Perfil 
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import FormularioRegistro


def login_view(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('Entrega3:inicio')  
    else:
        formulario = AuthenticationForm()

    return render(request, 'perfil/login.html', {'formulario': formulario})
    
def logout_view(request):
    logout(request)
    return redirect('perfil:login') 

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Entrega3:inicio')
    else:
        form = FormularioRegistro()

    return render(request, 'perfil/registro.html', {'form': form})


@login_required
def editar_perfil(request):
    user = request.user
    perfil, _ = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil:ver_perfil')
    else:
        user_form = UserUpdateForm(instance=user)
        perfil_form = PerfilUpdateForm(instance=perfil)
    
    return render(request, 'perfil/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


@login_required
def ver_perfil(request):
    Perfil.objects.get_or_create(user=request.user)
    return render(request, 'perfil/ver_perfil.html')

class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'perfil/cambiar_password.html'
    success_url = reverse_lazy('perfil:ver_perfil')