from django.shortcuts import render, redirect
from .models import Libro, Pelicula, Concierto
from .forms import LibroForm, PeliculaForm, ConciertoForm

# INICIO
def inicio(request):
    contexto = {"mensaje": "Bienvenido/a al Blog Cultural. Podrás encontrar reseñas de libros, películas y conciertos."}
    return render(request, 'Entrega3/inicio.html', contexto)

# LIBROS
def libros(request):
    return render(request, 'Entrega3/libros.html')

def agregar_libro(request):
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('libros')
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
            return redirect('peliculas')
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
            return redirect('conciertos')  # Redirige a la vista con name="conciertos"
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
