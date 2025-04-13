# BARBARABOLE_Entrega3 

Este repositorio contiene el entregable3 previo al proyecto final desarrollado en Django.

## Descripción general

Este proyecto es una aplicación web de tipo blog cultural, donde se pueden agregar, buscar y visualizar datos relacionados con **libros**, **películas** y **conciertos**.

### Funcionalidades:

- Agregar y buscar libros, películas y conciertos mediante formularios.
- Listar todos los datos ingresados de forma ordenada por fecha.
- Visualización en el inicio de la base de datos con buscador por nombre
- Visualización en el sitio y acceso desde el panel de administración con Django Admin (Usuario: admin, Contraseña: bole1234).
- Navegación mediante barra de enlaces superior.

---

## Estructura del proyecto

```
BARBARABOLE_Entrega3/
├── Entrega3/
│   ├── templates/Entrega3/         # Plantillas HTML para cada vista
│   │   ├── Base.html               # Template base común con herencia
│   │   ├── inicio.html             # Página de inicio
│   │   ├── ver_datos.html          # Vista de todos los datos cargados
│   │   ├── libros.html             # Página principal de libros
│   │   ├── agregar_libro.html      # Formulario para agregar libros
│   │   ├── buscar_libro.html       # Buscador de libros
│   │   ├── peliculas.html          # Página principal de películas
│   │   ├── agregar_pelicula.html   # Formulario para agregar películas
│   │   ├── buscar_pelicula.html    # Buscador de películas
│   │   ├── conciertos.html         # Página principal de conciertos
│   │   ├── agregar_concierto.html  # Formulario para agregar conciertos
│   │   ├── buscar_concierto.html   # Buscador de conciertos
│   ├── forms.py                    # Formularios de Libro, Película y Concierto
│   ├── models.py                   # Modelos de base de datos
│   ├── views.py                    # Vistas principales del sitio
│   ├── urls.py                     # Enrutamiento interno de la app
│
├── Proyecto1/
│   ├── settings.py                 # Configuración general del proyecto
│   ├── urls.py                     # Enrutamiento global
│
├── .gitignore                     # Archivos y carpetas que no se deben subir al repositorio
├── db.sqlite3                     # Base de datos SQLite
├── manage.py                      # Punto de entrada para ejecutar comandos
├── README.md                      # Documentación del proyecto
├── requirements.txt               # Dependencias del proyecto

```

---

## Instrucciones de uso

### 1. Clonar el repositorio
```bash
git clone <URL-del-repo>
cd BARBARABOLE_Entrega3
```

### 2. Crear entorno virtual (opcional pero recomendado)
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

Abrir en el navegador: [http://127.0.0.1:8000/blog/]

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

