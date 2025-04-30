from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    puntuacion = models.IntegerField()
    
    def __str__(self):
        return self.titulo

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    puntuacion = models.IntegerField()

class Concierto(models.Model):
    banda = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_evento = models.DateField()
    puntuacion = models.IntegerField()

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# Modelo para extender los datos del Usuario
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    preferencias = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return f"Perfil de {self.user.username}"

