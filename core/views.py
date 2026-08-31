from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Task
from .services import TaskService
from .forms import TaskForm


def task_list(request):
    """listamos las tareas con HTMX."""
    # aplicamos filtros si existen
    filters = {}
    if request.GET.get('status'):
        filters['status'] = request.GET.get('status')
    if request.GET.get('priority'):
        filters['priority'] = request.GET.get('priority')
    if request.GET.get('search'):
        filters['search'] = request.GET.get('search')

    tasks = TaskService.list_tasks(filters)

    # verificamos si es una petición HTMX por el header
    is_htmx = request.headers.get('HX-Request') == 'true'

    if is_htmx:
        # si es una petición HTMX, retornamos solo la tabla
        return render(request, 'core/task_table.html', {'tasks': tasks})

    # si es una petición normal, retornamos la página completa
    return render(request, 'core/task_list.html', {'tasks': tasks})


@require_http_methods(['POST'])
def create_task(request):
    """creamos una tarea desde un formulario HTMX."""
    form = TaskForm(request.POST)
    if form.is_valid():
        TaskService.create_task(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            priority=form.cleaned_data['priority']
        )
        # retornamos la lista actualizada
        tasks = TaskService.list_tasks()
        return render(request, 'core/task_table.html', {'tasks': tasks})
    # si hay errores, retornamos el formulario con errores
    return render(request, 'core/task_form.html', {'form': form}, status=400)


def edit_task(request, pk):
    """mostramos o actualizamos una tarea."""
    task = TaskService.get_task(pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            TaskService.update_task(
                pk,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                priority=form.cleaned_data['priority'],
                status=form.cleaned_data['status']
            )
            # retornamos solo la fila actualizada
            return render(request, 'core/task_row.html', {'task': task})
        # si hay errores, retornamos el formulario
        return render(request, 'core/task_form.html', {'form': form, 'task': task}, status=400)

    # si es GET, mostramos el formulario
    form = TaskForm(instance=task)
    return render(request, 'core/task_form.html', {'form': form, 'task': task})


@require_http_methods(['DELETE'])
def delete_task(request, pk):
    """eliminamos una tarea."""
    TaskService.delete_task(pk)
    return HttpResponse(status=204)


def task_form_modal(request):
    """mostramos el formulario de creación en un modal."""
    form = TaskForm()
    return render(request, 'core/task_form_modal.html', {'form': form})
