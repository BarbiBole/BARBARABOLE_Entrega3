from django.shortcuts import render, redirect
from .models import Libro, Pelicula, Concierto
from .forms import LibroForm, PeliculaForm, ConciertoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods


# Pantalla de inicio general
def inicio_general(request):
    return render(request, 'Entrega3/inicio.html')

# Pantalla acerca de mí
def acerca_de_mi(request):
    return render(request, 'Entrega3/acerca_de_mi.html')

# LIBROS
@login_required
def libros(request):
    return render(request, 'Entrega3/libros.html')

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        formulario = LibroForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:libros')
    else:
        formulario = LibroForm()
    return render(request, 'Entrega3/agregar_libro.html', {'formulario': formulario})

@login_required
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
@login_required
def peliculas(request):
    return render(request, 'Entrega3/peliculas.html')

@login_required
def agregar_pelicula(request):
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:peliculas')
    else:
        formulario = PeliculaForm()
    return render(request, 'Entrega3/agregar_pelicula.html', {'formulario': formulario})

@login_required
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
@login_required
def conciertos(request):
    return render(request, 'Entrega3/conciertos.html')

@login_required
def agregar_concierto(request):
    if request.method == 'POST':
        formulario = ConciertoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Entrega3:conciertos')
    else:
        formulario = ConciertoForm()
    return render(request, 'Entrega3/agregar_concierto.html', {'formulario': formulario})

@login_required
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


# Ver todas las reseñas
@login_required
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

@login_required
def resenias_home(request):
    return render(request, 'Entrega3/resenias_home.html')

@login_required
def resenias_listado(request):
    query = request.GET.get('buscar', '')
    libros = Libro.objects.filter(titulo__icontains=query).order_by('-fecha_publicacion')
    peliculas = Pelicula.objects.filter(titulo__icontains=query).order_by('-fecha_estreno')
    conciertos = Concierto.objects.filter(banda__icontains=query).order_by('-fecha_evento')
    return render(request, 'Entrega3/resenias_listado.html', {
        'libros': libros,
        'peliculas': peliculas,
        'conciertos': conciertos,
        'query': query
    })

# Editar libro
@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)  
        if form.is_valid():
            form.save()
            return redirect('Entrega3:resenias_listado')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'Entrega3/agregar_libro.html', {'formulario': form})

# Eliminar libro
@login_required
@require_http_methods(["GET", "POST"])
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('Entrega3:resenias_listado')
    return render(request, 'Entrega3/confirmar_eliminar.html', {'objeto': libro})

# Detalle libro
@login_required
def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, 'Entrega3/detalle_libro.html', {'libro': libro})

# Editar película
@login_required
def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula) 
        if form.is_valid():
            form.save()
            return redirect('Entrega3:resenias_listado')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'Entrega3/agregar_pelicula.html', {'formulario': form})

# Eliminar película
@login_required
@require_http_methods(["GET", "POST"])
def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('Entrega3:resenias_listado')
    return render(request, 'Entrega3/confirmar_eliminar.html', {'objeto': pelicula})

# Detalle película
@login_required
def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'Entrega3/detalle_pelicula.html', {'pelicula': pelicula})

# Editar concierto
@login_required
def editar_concierto(request, id):
    concierto = Concierto.objects.get(id=id)
    if request.method == 'POST':
        form = ConciertoForm(request.POST, request.FILES, instance=concierto) 
        if form.is_valid():
            form.save()
            return redirect('Entrega3:resenias_listado')
    else:
        form = ConciertoForm(instance=concierto)
    return render(request, 'Entrega3/agregar_concierto.html', {'formulario': form})

# Eliminar concierto
@login_required
@require_http_methods(["GET", "POST"])
def eliminar_concierto(request, id):
    concierto = get_object_or_404(Concierto, id=id)
    if request.method == 'POST':
        concierto.delete()
        return redirect('Entrega3:resenias_listado')
    return render(request, 'Entrega3/confirmar_eliminar.html', {'objeto': concierto})

# Detalle concierto
@login_required
def detalle_concierto(request, id):
    concierto = get_object_or_404(Concierto, id=id)
    return render(request, 'Entrega3/detalle_concierto.html', {'concierto': concierto})