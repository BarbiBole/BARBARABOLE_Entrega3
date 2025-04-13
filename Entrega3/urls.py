from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.inicio, name='inicio'),
    path('ver_datos/', views.ver_datos, name='ver_datos'),

    path('libros/', views.libros, name='libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),

    path('peliculas/', views.peliculas, name='peliculas'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),

    path('conciertos/', views.conciertos, name='conciertos'),
    path('agregar_concierto/', views.agregar_concierto, name='agregar_concierto'),
    path('buscar_concierto/', views.buscar_concierto, name='buscar_concierto'),
]




