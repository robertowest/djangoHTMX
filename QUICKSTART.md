# Inicio rápido

## Ejecución local

```bash
# 1. Instalar dependencias
pip install -e . -e ".[dev]"

# 2. Hacer migraciones (solo primera vez)
python manage.py makemigrations core
python manage.py migrate

# 3. Crear datos de ejemplo (opcional)
python scripts/seed_data.py

# 4. Crear superusuario (opcional)
python manage.py createsuperuser

# 5. Ejecutar servidor
python manage.py runserver
```

Accede a:
- 🌐 Aplicación: http://localhost:8000
- 🔑 Admin: http://localhost:8000/admin

## Con Docker

```bash
# Iniciar
docker-compose up -d

# Crear superusuario
docker-compose exec web python manage.py createsuperuser

# Ver logs
docker-compose logs -f web

# Detener
docker-compose down
```

## Características

### 📝 Gestionar Tareas
- Crear, editar, eliminar tareas
- Filtrar por estado y prioridad
- Buscar por título
- Todo sin recargar la página gracias a HTMX

### 🎨 Interfaz moderna
- Bootstrap 5
- Animaciones suaves
- Responsive design
- Modal dinámico

### 🔧 Arquitectura limpia
- Lógica en `services.py`
- Formularios con crispy-forms
- Historial de cambios automático

### 📊 Admin avanzado
- Simple History para auditoría
- Búsqueda y filtros
- Interfaz personalizada

## Próximos pasos

1. **Explorar el admin** en http://localhost:8000/admin
2. **Ver el código** de `core/services.py` para entender la lógica
3. **Personalizar** los templates en `templates/core/`
4. **Agregar nuevos modelos** siguiendo el patrón de Task

## Troubleshooting

### BD vacía
```bash
python scripts/seed_data.py
```

### Error de puerto en uso
```bash
python manage.py runserver 0.0.0.0:8001
```

### Instalar dev dependencies
```bash
pip install -e ".[dev]"
```

### Ver estadísticas
```bash
python manage.py shell

# En la shell de Python
from core.models import Task
print(f"Total de tareas: {Task.objects.count()}")
print(f"Por estado:")
for status, label in Task.STATUS_CHOICES:
    count = Task.objects.filter(status=status).count()
    print(f"  {label}: {count}")
```

## HTMX

Documentación sobre este tema [HTMX Docs](https://htmx.org/docs/)
