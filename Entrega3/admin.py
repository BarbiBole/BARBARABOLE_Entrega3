from django.contrib import admin
from .models import Libro, Pelicula, Concierto

admin.site.register(Libro)
admin.site.register(Pelicula)
admin.site.register(Concierto)
