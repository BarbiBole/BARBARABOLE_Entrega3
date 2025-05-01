from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {field: "" for field in fields}

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nombre',
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    last_name = forms.CharField(
        label='Apellido',
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', required=False)
    preferencias = forms.CharField(
        label='Preferencias',
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = Perfil
        fields = ['avatar', 'preferencias']
