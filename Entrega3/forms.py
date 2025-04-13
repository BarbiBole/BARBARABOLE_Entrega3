from django import forms
from .models import Libro, Pelicula, Concierto

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'})}

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'})}

class ConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = '__all__'
        widgets = {
            'fecha_evento': forms.DateInput(attrs={'type': 'date'})}

