from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)
from django.contrib.auth.views import LogoutView

app_name = 'Entrega3'

urlpatterns = [
    # 🔵 INICIO Y ACERCA DE MÍ
    path('', views.inicio_blog, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),

    # 🔵 CRUD LIBROS
    path('libros/', views.libros, name='libros'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),

    # 🔵 CRUD PELÍCULAS
    path('peliculas/', views.peliculas, name='peliculas'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),

    # 🔵 CRUD CONCIERTOS
    path('conciertos/', views.conciertos, name='conciertos'),
    path('agregar_concierto/', views.agregar_concierto, name='agregar_concierto'),
    path('buscar_concierto/', views.buscar_concierto, name='buscar_concierto'),

    # 🔵 VER TODOS LOS DATOS
    path('ver_datos/', views.ver_datos, name='ver_datos'),

    # 🔵 POSTS
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/crear/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/borrar/', PostDeleteView.as_view(), name='post_delete'),

    # LOGIN, LOGOUT, REGISTRO
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio_general'), name='logout'),
    path('registro/', views.registro, name='registro'),

    # PERFIL
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', views.CambiarPasswordView.as_view(), name='cambiar_password'),

]









