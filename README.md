# Trabajo final Django

Este repositorio contiene el proyecto final desarrollado en Django.
Proyecto configurado para correr de manera local.

## Descripción general

Este proyecto es una aplicación web de tipo blog cultural, donde se pueden agregar, buscar y visualizar datos relacionados con **libros**, **películas** y **conciertos**.

La aplicación permite:

- Registrarse, iniciar sesión y cerrar sesión.
- Gestionar un perfil de usuario (nombre, apellido, email, avatar, preferencias).
- Editar datos del perfil y cambiar la contraseña.
- Crear, ver, editar y eliminar reseñas.
- Subir imágenes asociadas a las reseñas.
- Buscar objetos y mostrar mensajes si no hay resultados.
- Acceder a una sección "Acerca de mí".

### Funcionalidades:

- Agregar y buscar libros, películas y conciertos mediante formularios.
- Listar todos los datos ingresados.
- Visualización en el inicio de la base de datos con buscador por nombre.
- Visualización en el sitio y acceso desde el panel de administración con Django Admin (Usuario: barbi, Contraseña: 123).
- Navegación mediante barra de enlaces superior.

- Vista de inicio (`/`) con mensaje de bienvenida.
- Página "Acerca de mí" con información personal.
- Gestión de usuarios: Login, logout, registro, perfil y edición.

---

## Estructura del proyecto

```
BARBARABOLE_Entrega3/
├── Entrega3/
│   ├── templates/Entrega3/         # Plantillas HTML
│   │  ├── base.html                # Template base común con herencia
│   │   ├── acerca_de_mi.html       # Página de "Acerca de mí"
│   │   ├── agregar_libro.html      # Formulario para agregar libro
│   │   ├── agregar_pelicula.html   # Formulario para agregar película
│   │   ├── agregar_concierto.html  # Formulario para agregar concierto
│   │   ├── buscar_pelicula.html    # Buscador de películas
│   │   ├── buscar_libro.html       # Buscador de libros
│   │   ├── buscar_concierto.html   # Buscador de conciertos
│   │   ├── conciertos.html         # Listado de conciertos
│   │   ├── libros.html             # Listado de libros
│   │   ├── peliculas.html          # Listado de películas
│   │   ├── detalle_libro.html      # Visualización de libro
│   │   ├── detalle_pelicula.html   # Visualización de película
│   │   ├── detalle_concierto.html  # Visualización de concierto
│   │   ├── confirmar_eliminar.html # Visualización de confirmación de eliminar
│   │   ├── inicio.html             # Página de inicio
│   │   ├── resenias_home.html      # Página de inicio de reseñas
│   │   ├── resenias_listado.html   # VIsualización de listado de reseñas
│   ├── forms.py                    # Formularios (Libros, Películas, Conciertos)
│   ├── models.py                   # Modelos de base de datos (Libros, Películas, Conciertos)
│   ├── views.py                    # Vistas principales
│   ├── urls.py                     # Enrutamiento interno de la app
│
├── perfil/
│   ├── templates/perfil/           # Plantillas HTML
│   │   ├── cambiar_password.html   # Página para cambiar contraseña
│   │   ├── editar_perfil.html      # Página para editar perfil
│   │   ├── login.html              # Página para loguearte
│   │   ├── registro.html           # Página para registrar usuario
│   │   ├── ver_perfil.html         # Página para ver usuario
│   ├── forms.py                    # Formularios (Usuario, Perfil)
│   ├── models.py                   # Modelos de base de datos (Perfil de usuario)
│   ├── views.py                    # Vistas principales
│   ├── urls.py                     # Enrutamiento interno de la app
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
- asgiref==3.8.1
- sqlparse==0.5.3
- tzdata==2025.2


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

---

## Enlaces útiles

Abrir en el navegador: [http://127.0.0.1:8000/]

- [http://127.0.0.1:8000/admin/] – Panel de administración
- [http://127.0.0.1:8000/perfil/login/] – Página para loguearte
- [http://127.0.0.1:8000/perfil/editar/] – Visualización para editar perfil
- [http://127.0.0.1:8000/perfil/registro/] – Página para registrarte

- [http://127.0.0.1:8000/blog/acerca-de-mi/] – Acerca de mí
- [http://127.0.0.1:8000/resenias/] – Página para ver reseñas
- [http://127.0.0.1:8000/resenias/listado/] – Visualización de todos los datos cargados

- [http://127.0.0.1:8000/blog/libros/] – Visualización del módulo Libros
- [http://127.0.0.1:8000/blog/agregar_libro/] – Visualización del formulario para agregar un libro
- [http://127.0.0.1:8000/blog/buscar_libro/] – Visualización para buscar un libro cargado por su título

- [http://127.0.0.1:8000/blog/peliculas/] – Visualización del módulo Películas
- [http://127.0.0.1:8000/blog/agregar_pelicula/] – Visualización del formulario para agregar una pelicula
- [http://127.0.0.1:8000/blog/buscar_pelicula/] – Visualización para buscar una película cargado por su título

- [http://127.0.0.1:8000/blog/conciertos/] – Visualización del módulo Conciertos
- [http://127.0.0.1:8000/blog/agregar_concierto/] – Visualización del formulario para agregar un concierto
- [http://127.0.0.1:8000/blog/buscar_concierto/] – Visualización para buscar un concierto cargado por su título] – Panel de administración

---

## Consideraciones
La base de datos (db.sqlite3) y las imágenes subidas no están en el repositorio (ver .gitignore).

Las imágenes se almacenan en la carpeta /media/.

Se utilizaron Class-Based Views (CBV) y decoradores para la protección de rutas.

## Autor
Bárbara Bole