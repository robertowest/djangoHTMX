# Django + HTMX

Proyecto Django configurado con HTMX para crear aplicaciones web modernas con actualizaciones parciales del DOM sin necesidad de JavaScript personalizado.

## Stack

- **Backend:** Django 5.2 + Django REST Framework
- **Frontend:** HTMX + Bootstrap 5 + django-crispy-forms
- **Base de datos:** PostgreSQL (desarrollo con SQLite)
- **Herramientas:** ruff (linter), django-simple-history, django-filter, django-tables2
- **Contenedores:** Docker / Docker Compose

## Instalación local

### Requisitos
- Python 3.11+
- pip / uv

### Pasos

1. **Clonar el repositorio**
```bash
cd /home/roberto/Programacion/django/HTMX
```

2. **Crear entorno virtual** (si es necesario)
```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -e .
pip install -e ".[dev]"
```

4. **Ejecutar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor**
```bash
python manage.py runserver
```

Accede a `http://localhost:8000`

## Ejecución con Docker

```bash
docker-compose up -d
```

La aplicación estará disponible en `http://localhost:8000`

### Crear superusuario en Docker
```bash
docker-compose exec web python manage.py createsuperuser
```

## Estructura del proyecto

```
.
├── config/             # Configuración de Django
│   ├── settings.py     # Configuración principal
│   ├── urls.py         # URLs principales
│   └── wsgi.py         # WSGI
├── core/               # Aplicación principal
│   ├── models.py       # Modelos (Task)
│   ├── views.py        # Vistas con HTMX
│   ├── services.py     # Lógica de negocio
│   ├── forms.py        # Formularios
│   ├── admin.py        # Admin de Django
│   └── urls.py         # URLs de core
├── templates/          # Plantillas HTML
│   ├── base.html       # Plantilla base
│   └── core/           # Plantillas de core
├── static/             # Archivos estáticos
├── manage.py           # CLI de Django
├── pyproject.toml      # Dependencias
├── Dockerfile          # Imagen Docker
└── docker-compose.yml  # Configuración Docker Compose
```

## Características principales

### 1. Gestión de Tareas con HTMX

La aplicación incluye un ejemplo completo de un sistema de gestión de tareas:

- **Listar tareas** con filtros en tiempo real
- **Crear tareas** desde un modal
- **Editar tareas** sin recarga de página
- **Eliminar tareas** con confirmación
- **Filtros dinámicos** por estado, prioridad y búsqueda

### 2. Arquitectura Clean

- **Services:** Toda la lógica de negocio en la capa de servicios
- **Forms:** Formularios con crispy-forms y Bootstrap 5
- **Admin:** Administrador personalizado con historial de cambios

### 3. Historial de cambios

Usa `django-simple-history` para auditoría automática:

```python
# Ver cambios en admin
python manage.py shell
from core.models import Task
from simple_history.models import HistoricalRecord
Task.history.all()
```

### 4. HTMX Features

- `hx-get` para cargar contenido sin recargar
- `hx-post` para enviar formularios
- `hx-delete` para eliminar
- `hx-confirm` para confirmaciones
- `hx-target` para especificar dónde insertar la respuesta
- `hx-swap` para definir cómo se inserta el contenido

## Linting y formato

```bash
# Verificar con ruff
ruff check .

# Corregir automáticamente
ruff check --fix .
```

## Comandos útiles

```bash
# Crear nueva app
python manage.py startapp nombre_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear datos de prueba
python manage.py shell

# Ejecutar shell interactivo
python manage.py shell_plus  # requiere django-extensions

# Ejecutar tests
python manage.py test

# Ver logs
docker-compose logs -f web
```

## Extensiones recomendadas para VS Code

- Django
- HTMX in Django
- Pylance
- Ruff

## Configuración para desarrollo

En `.venv/pyvenv.cfg` asegúrate que tienes:

```
home = /media/ssd1tb/virtualenv/django5
```

## Notas de desarrollo

- Todos los comentarios en código están en español
- Usar comilla simple (') en Python, excepto docstrings
- Indentar con 4 espacios
- Commits en español, presente indicativo
- Lógica siempre en `services.py`, nunca en vistas

## Troubleshooting

### Error: "No such table"
```bash
python manage.py migrate
```

### Error: "404 Not Found" en static files
```bash
python manage.py collectstatic --noinput
```

### Error de conexión a BD en Docker
```bash
docker-compose down -v
docker-compose up -d
```

## Licencia

MIT
