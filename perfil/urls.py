from django.urls import path
from . import views
from .views import login_view, logout_view

app_name = 'perfil'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ver/', views.ver_perfil, name='ver_perfil'),
    path('cambiar-password/', views.CambiarPasswordView.as_view(), name='cambiar_password'),

]
