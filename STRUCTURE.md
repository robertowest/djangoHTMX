# Estructura del Proyecto Django + HTMX

## Árbol de directorios

```
django-htmx/
├── config/                         # Configuración de Django
│   ├── settings.py                 # Ajustes principales
│   ├── urls.py                     # Enrutamiento global
│   ├── wsgi.py                     # Interfaz WSGI
│   └── asgi.py                     # Interfaz ASGI
│
├── core/                           # Aplicación principal
│   ├── migrations/                 # Migraciones de BD
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── admin.py                    # Admin de Django
│   ├── apps.py                     # Config de la app
│   ├── forms.py                    # Formularios
│   ├── models.py                   # Modelos (Task)
│   ├── services.py                 # Lógica de negocio
│   ├── urls.py                     # Rutas de la app
│   ├── views.py                    # Vistas con HTMX
│   └── __init__.py
│
├── templates/                      # Plantillas HTML
│   ├── base.html                   # Template base
│   └── core/                       # Templates de core
│       ├── task_form.html          # Formulario de tarea
│       ├── task_form_modal.html    # Modal del formulario
│       ├── task_list.html          # Listado principal
│       ├── task_row.html           # Fila individual
│       └── task_table.html         # Tabla de tareas
│
├── static/                         # Archivos estáticos
│   ├── css/                        # Hojas de estilos
│   └── js/                         # JavaScript personalizado
│
├── media/                          # Archivos de usuario
│
├── scripts/                        # Scripts útiles
│   ├── seed_data.py                # Datos de prueba
│   └── __init__.py
│
├── .venv                           # Enlace al virtualenv
├── db.sqlite3                      # Base de datos (desarrollo)
├── manage.py                       # CLI de Django
│
├── pyproject.toml                  # Dependencias y config
├── Dockerfile                      # Imagen Docker
├── docker-compose.yml              # Orquestación Docker
│
├── README.md                       # Documentación principal
├── QUICKSTART.md                   # Inicio rápido
├── STRUCTURE.md                    # Este archivo
├── .gitignore                      # Archivos a ignorar
├── .env.example                    # Variables de ejemplo
└── .claude/                        # Config de Claude Code
    └── settings.local.json
```

## Descripción de archivos clave

### Config

#### `config/settings.py`
Configuración central de Django con:
- INSTALLED_APPS: apps instaladas
- TEMPLATES: configuración de templates
- DATABASES: conexión a BD
- CRISPY_FORMS: bootstrap5
- REST_FRAMEWORK: DRF
- DJANGO_TABLES2: templates

### Core

#### `core/models.py`
- **Task**: Modelo principal con campos:
  - title: CharField
  - description: TextField
  - priority: Choices (low, medium, high)
  - status: Choices (pending, in_progress, completed)
  - created_at / updated_at: TimeStamp
  - history: HistoricalRecords para auditoría

#### `core/services.py`
Lógica de negocio centralizada:
- `TaskService.create_task()`: crear tarea
- `TaskService.update_task()`: actualizar
- `TaskService.delete_task()`: eliminar
- `TaskService.get_task()`: obtener una
- `TaskService.list_tasks()`: listar con filtros

#### `core/views.py`
Vistas que devuelven HTML parcial para HTMX:
- `task_list()`: listado principal con filtros
- `create_task()`: crear desde formulario
- `edit_task()`: editar tarea
- `delete_task()`: eliminar (DELETE)
- `task_form_modal()`: cargar formulario en modal

#### `core/forms.py`
- **TaskForm**: Formulario crispy-forms con:
  - Validación integrada
  - Bootstrap 5 styling
  - Layouts responsivos

### Templates

#### `templates/base.html`
- Estructura HTML principal
- CDN de Bootstrap 5 y HTMX
- Navbar y contenedor
- Bloque para mensajes

#### `templates/core/task_list.html`
Página principal:
- Encabezado con botón "Nueva Tarea"
- Panel de filtros (HTMX)
- Contenedor de tabla (se reemplaza con HTMX)
- Modal vacío para formularios

#### `templates/core/task_table.html`
Tabla de tareas reutilizable:
- Encabezados
- Bucle sobre tareas
- Incluye task_row.html

#### `templates/core/task_row.html`
Una fila de la tabla:
- Badge de estado y prioridad
- Botones editar/eliminar con HTMX
- Confirmación de eliminar

#### `templates/core/task_form.html`
Formulario crispy-forms:
- Campos de tarea
- Manejo de errores
- Botones guardar/cancelar
- Target HTMX a #taskTableContainer

### Docker

#### `Dockerfile`
- Python 3.11
- Instala dependencias
- Expone puerto 8000
- Comando: gunicorn

#### `docker-compose.yml`
- PostgreSQL 16
- Django con runserver
- Volumen para código
- Health check en BD

## Flujo de datos HTMX

### Ejemplo: Crear tarea

```
1. Usuario hace clic en "Nueva Tarea"
2. HTMX GET a /form-modal/
3. Servidor devuelve task_form_modal.html
4. Muestra en #taskModalContent
5. Usuario completa formulario
6. HTMX POST a /create/
7. Servidor valida y crea
8. Devuelve task_table.html
9. HTMX reemplaza #taskTableContainer
10. Modal se cierra automáticamente
```

### Ejemplo: Filtrar tareas

```
1. Usuario elige filtro (status/priority)
2. HTMX GET a / con parámetros
3. Servidor aplica filtros
4. Devuelve task_table.html (solo tabla)
5. HTMX reemplaza #taskTableContainer
```

## Comandos de desarrollo

```bash
# Crear migraciones
python manage.py makemigrations core

# Aplicar migraciones
python manage.py migrate

# Crear datos de prueba
python scripts/seed_data.py

# Ejecutar servidor
python manage.py runserver

# Admin
python manage.py createsuperuser

# Shell interactivo
python manage.py shell_plus

# Linting
ruff check .
ruff check --fix .

# Tests
python manage.py test
```

## Dependencias principales

- **Django 5.2**: Framework web
- **django-htmx**: Soporte para HTMX
- **django-crispy-forms**: Formularios con templates
- **crispy-bootstrap5**: Bootstrap para crispy
- **django-filter**: Filtrado de QuerySets
- **django-tables2**: Tablas HTML
- **django-simple-history**: Historial de cambios
- **djangorestframework**: API REST (opcional)
- **ruff**: Linter y formatter

## Variables de entorno clave

```
DEBUG=True                      # Modo desarrollo
SECRET_KEY=...                  # Clave secreta
ALLOWED_HOSTS=localhost         # Hosts permitidos
DATABASE_URL=...                # Conexión BD
LANGUAGE_CODE=es-es             # Idioma
TIME_ZONE=Europe/Madrid         # Zona horaria
```

## Convenciones del proyecto

- Comentarios en español
- Lógica siempre en `services.py`
- Formularios con crispy-forms
- Templates modularizados
- HTMX para interactividad
- 4 espacios de indentación
- Comillas simples en Python
