from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    puntuacion = models.IntegerField()
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    puntuacion = models.IntegerField()
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Concierto(models.Model):
    banda = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_evento = models.DateField()
    puntuacion = models.IntegerField()
    imagen = models.ImageField(upload_to='conciertos/', blank=True, null=True)

    def __str__(self):
        return self.banda

