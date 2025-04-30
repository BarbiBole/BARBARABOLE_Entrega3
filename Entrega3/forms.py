from django import forms
from .models import Libro, Pelicula, Concierto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User
from .models import Perfil

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)
    preferencias = forms.CharField(label='Preferencias', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'preferencias']