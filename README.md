# Trabajo final Django

Este repositorio contiene el proyecto final desarrollado en Django.
Proyecto configurado para correr de manera local.

## Descripción general

Este proyecto es una aplicación web de tipo blog cultural, donde se pueden agregar, buscar y visualizar datos relacionados con **libros**, **películas** y **conciertos**.

La aplicación permite:

- Registrarse, iniciar sesión y cerrar sesión.
- Gestionar un perfil de usuario (nombre, apellido, email, avatar, preferencias).
- Editar datos del perfil y cambiar la contraseña.
- Crear, ver, editar y eliminar publicaciones (Posts).
- Subir imágenes asociadas a los posts.
- Buscar objetos y mostrar mensajes si no hay resultados.
- Acceder a una sección "Acerca de mí".

### Funcionalidades:

- Agregar y buscar libros, películas y conciertos mediante formularios.
- Listar todos los datos ingresados de forma ordenada por fecha.
- Visualización en el inicio de la base de datos con buscador por nombre
- Visualización en el sitio y acceso desde el panel de administración con Django Admin (Usuario: admin, Contraseña: bole1234).
- Navegación mediante barra de enlaces superior.

- Vista de inicio (`/`) con mensaje de bienvenida.
- Página "Acerca de mí" con información personal.
- Blog de Posts: Crear, listar, ver, editar y borrar.
- Gestión de usuarios: Login, logout, registro, perfil y edición.
- Protección de vistas para usuarios autenticados usando mixins y decoradores.

---

## Estructura del proyecto

```
BARBARABOLE_Entrega3/
├── Entrega3/
│   ├── templates/Entrega3/         # Plantillas HTML
│   │   ├── base.html               # Template base común con herencia
│   │   ├── inicio.html             # Página de inicio general
│   │   ├── acerca_de_mi.html       # Página de "Acerca de mí"
│   │   ├── ver_datos.html          # Vista para elegir entre Libros / Películas / Conciertos
│   │   ├── libros.html             # Listado de libros
│   │   ├── agregar_libro.html      # Formulario para agregar libro
│   │   ├── buscar_libro.html       # Buscador de libros
│   │   ├── peliculas.html          # Listado de películas
│   │   ├── agregar_pelicula.html   # Formulario para agregar película
│   │   ├── buscar_pelicula.html    # Buscador de películas
│   │   ├── conciertos.html         # Listado de conciertos
│   │   ├── agregar_concierto.html  # Formulario para agregar concierto
│   │   ├── buscar_concierto.html   # Buscador de conciertos
│   │   ├── post_list.html          # Listado de posts (blog)
│   │   ├── post_detail.html        # Detalle de post
│   │   ├── post_form.html          # Formulario para crear y editar posts
│   │   ├── post_confirm_delete.html# Confirmación de borrado de post
│   │   ├── login.html              # Página de login
│   │   ├── registro.html           # Formulario de registro de usuario
│   │   ├── perfil.html             # Perfil de usuario
│   │   ├── editar_perfil.html      # Formulario para editar perfil
│   │   ├── cambiar_password.html   # Formulario de cambio de contraseña
│   ├── forms.py                    # Formularios (Libros, Películas, Conciertos, Usuario, Perfil)
│   ├── models.py                   # Modelos de base de datos (Libros, Películas, Conciertos, Posts, Perfil de usuario)
│   ├── views.py                    # Vistas principales
│   ├── urls.py                     # Enrutamiento interno de la app
│   ├── signals.py                  # Señales para creación automática de perfil
│
├── Proyecto1/
│   ├── settings.py                 # Configuración del proyecto
│   ├── urls.py                     # Enrutamiento global (incluye la app Entrega3)
│
├── media/                          # Carpeta para imágenes subidas por los usuarios (no se sube a GitHub)
├── static/                         # Carpeta para archivos estáticos
├── .gitignore                      # Ignora venv, __pycache__, db.sqlite3, media/
├── requirements.txt                # Dependencias del proyecto
├── manage.py                       # Comando principal de Django
├── README.md                       # Documentación del proyecto


```

---

## Tecnologías utilizadas

- Python 3.13
- Django 5.2
- Bootstrap 5.3 (para el diseño frontend)

## Instrucciones de uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd BARBARABOLE_Entrega3
```

### 2. Crear entorno virtual 
```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
pip install django
```

### 4. Migrar base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

Abrir en el navegador: [http://127.0.0.1:8000/]

---

## Enlaces útiles

- [http://127.0.0.1:8000/admin/] – Panel de administración
- [http://127.0.0.1:8000/blog/] – Página de inicio
- [http://127.0.0.1:8000/ver_datos/] – Visualización de todos los datos cargados

- [http://127.0.0.1:8000/libros/] – Visualización del módulo Libros
- [http://127.0.0.1:8000/agregar_libro/] – Visualización del formulario para agregar un libro
- [http://127.0.0.1:8000/buscar_libro/] – Visualización para buscar un libro cargado por su título

- [http://127.0.0.1:8000/peliculas/] – Visualización del módulo Películas
- [http://127.0.0.1:8000/agregar_pelicula/] – Visualización del formulario para agregar una pelicula
- [http://127.0.0.1:8000/buscar_pelicula/] – Visualización para buscar una película cargado por su título

- [http://127.0.0.1:8000/conciertos/] – Visualización del módulo Conciertos
- [http://127.0.0.1:8000/agregar_concierto/] – Visualización del formulario para agregar un concierto
- [http://127.0.0.1:8000/buscar_concierto/] – Visualización para buscar un concierto cargado por su título
---

## Consideraciones
La base de datos (db.sqlite3) y las imágenes subidas no están en el repositorio (ver .gitignore).

Las imágenes se almacenan en la carpeta /media/.

Se utilizaron Class-Based Views (CBV) y decoradores para la protección de rutas.

## Autor
Bárbara Bole