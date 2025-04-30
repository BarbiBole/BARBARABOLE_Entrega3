from django.shortcuts import render, redirect
from .models import Libro, Pelicula, Concierto
from .forms import LibroForm, PeliculaForm, ConciertoForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm

# Pantalla de inicio general
def inicio_general(request):
    return render(request, 'Entrega3/inicio.html')

# Pantalla de inicio del blog
def inicio_blog(request):
    contexto = {"mensaje": "Bienvenido/a al Blog Cultural. Podrás encontrar reseñas de libros, películas y conciertos."}
    return render(request, 'Entrega3/inicio_blog.html', contexto)

# LIBROS
def libros(request):
    return render(request, 'Entrega3/libros.html')

def agregar_libro(request):
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:libros')
    else:
        formulario = LibroForm()
    return render(request, 'Entrega3/agregar_libro.html', {'formulario': formulario})

def buscar_libro(request):
    resultados = []
    query = request.GET.get('titulo', '')
    if query:
        resultados = Libro.objects.filter(titulo__icontains=query).order_by('fecha_publicacion')
    todos = Libro.objects.all().order_by('fecha_publicacion')
    return render(request, 'Entrega3/buscar_libro.html', {
        'resultados': resultados,
        'todos': todos,
        'query': query
    })

# PELÍCULAS
def peliculas(request):
    return render(request, 'Entrega3/peliculas.html')

def agregar_pelicula(request):
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:peliculas')
    else:
        formulario = PeliculaForm()
    return render(request, 'Entrega3/agregar_pelicula.html', {'formulario': formulario})

def buscar_pelicula(request):
    resultados = []
    query = request.GET.get('titulo', '')
    if query:
        resultados = Pelicula.objects.filter(titulo__icontains=query).order_by('fecha_estreno')
    todos = Pelicula.objects.all().order_by('fecha_estreno')
    return render(request, 'Entrega3/buscar_pelicula.html', {
        'resultados': resultados,
        'todos': todos,
        'query': query
    })

# CONCIERTOS
def conciertos(request):
    return render(request, 'Entrega3/conciertos.html')

def agregar_concierto(request):
    if request.method == 'POST':
        formulario = ConciertoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:conciertos')
    else:
        formulario = ConciertoForm()
    return render(request, 'Entrega3/agregar_concierto.html', {'formulario': formulario})

def buscar_concierto(request):
    resultados = []
    query = request.GET.get('banda', '')
    if query:
        resultados = Concierto.objects.filter(banda__icontains=query).order_by('fecha_evento')
    todos = Concierto.objects.all().order_by('fecha_evento')
    return render(request, 'Entrega3/buscar_concierto.html', {
        'resultados': resultados,
        'todos': todos,
        'query': query
    })

# Ver todos los datos
def ver_datos(request):
    query = request.GET.get('buscar', '')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query).order_by('fecha_publicacion')
        peliculas = Pelicula.objects.filter(titulo__icontains=query).order_by('fecha_estreno')
        conciertos = Concierto.objects.filter(banda__icontains=query).order_by('fecha_evento')
    else:
        libros = Libro.objects.all().order_by('fecha_publicacion')
        peliculas = Pelicula.objects.all().order_by('fecha_estreno')
        conciertos = Concierto.objects.all().order_by('fecha_evento')
    return render(request, 'Entrega3/ver_datos.html', {
        'libros': libros,
        'peliculas': peliculas,
        'conciertos': conciertos,
        'query': query
    })

def acerca_de_mi(request):
    return render(request, 'Entrega3/acerca_de_mi.html')


# 🔵 Listar Posts
class PostListView(ListView):
    model = Post
    template_name = 'Entrega3/post_list.html'
    context_object_name = 'posts'

# 🔵 Ver Detalle de un Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'Entrega3/post_detail.html'
    context_object_name = 'post'

# 🔵 Crear un Post (solo usuarios logueados)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'Entrega3/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('Entrega3:post_list')

# 🔵 Editar un Post (solo usuarios logueados)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'Entrega3/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('Entrega3:post_list')

# 🔵 Borrar un Post (solo usuarios logueados)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'Entrega3/post_confirm_delete.html'
    success_url = reverse_lazy('Entrega3:post_list')


class CustomLoginView(LoginView):
    template_name = 'Entrega3/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = '/login/'


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Guardamos datos extra en el perfil
            perfil = user.perfil
            perfil.avatar = form.cleaned_data.get('avatar')
            perfil.preferencias = form.cleaned_data.get('preferencias')
            perfil.save()

            login(request, user)  # Loguearlo automáticamente
            return redirect('inicio_general')
    else:
        form = UserRegisterForm()
    
    return render(request, 'Entrega3/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    user = request.user
    perfil = user.perfil

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('Entrega3:ver_perfil')
    else:
        user_form = UserUpdateForm(instance=user)
        perfil_form = PerfilUpdateForm(instance=perfil)
    
    return render(request, 'Entrega3/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

@login_required
def ver_perfil(request):
    return render(request, 'Entrega3/ver_perfil.html')

class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Entrega3/cambiar_password.html'
    success_url = reverse_lazy('Entrega3:ver_perfil')