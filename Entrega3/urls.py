from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Entrega3'

urlpatterns = [
    # INICIO Y ACERCA DE MÍ
    path('', views.resenias_home, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),

    # LIBROS
    path('libros/', views.libros, name='libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),

    # PELÍCULAS
    path('peliculas/', views.peliculas, name='peliculas'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),

    # CONCIERTOS
    path('conciertos/', views.conciertos, name='conciertos'),
    path('agregar_concierto/', views.agregar_concierto, name='agregar_concierto'),
    path('buscar_concierto/', views.buscar_concierto, name='buscar_concierto'),

    # RESEÑAS    
    path('resenias/', views.resenias_home, name='resenias_home'),
    path('resenias/listado/', views.resenias_listado, name='resenias_listado'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('editar_pelicula/<int:id>/', views.editar_pelicula, name='editar_pelicula'),
    path('editar_concierto/<int:id>/', views.editar_concierto, name='editar_concierto'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('eliminar_pelicula/<int:id>/', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('eliminar_concierto/<int:id>/', views.eliminar_concierto, name='eliminar_concierto'),
    path('detalle_libro/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('detalle_pelicula/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('detalle_concierto/<int:id>/', views.detalle_concierto, name='detalle_concierto'),

]









