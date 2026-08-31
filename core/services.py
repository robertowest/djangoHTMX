from django.shortcuts import get_object_or_404
from .models import Task


class TaskService:
    """servicio para operaciones de tareas."""

    @staticmethod
    def create_task(title, description='', priority='medium'):
        """creamos una nueva tarea."""
        return Task.objects.create(
            title=title,
            description=description,
            priority=priority
        )

    @staticmethod
    def update_task(task_id, **kwargs):
        """actualizamos una tarea."""
        task = get_object_or_404(Task, pk=task_id)
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task_id):
        """eliminamos una tarea."""
        task = get_object_or_404(Task, pk=task_id)
        task.delete()

    @staticmethod
    def get_task(task_id):
        """obtenemos una tarea por id."""
        return get_object_or_404(Task, pk=task_id)

    @staticmethod
    def list_tasks(filters=None):
        """listamos todas las tareas con filtros opcionales."""
        queryset = Task.objects.all()

        if filters:
            if 'status' in filters:
                queryset = queryset.filter(status=filters['status'])
            if 'priority' in filters:
                queryset = queryset.filter(priority=filters['priority'])
            if 'search' in filters:
                queryset = queryset.filter(title__icontains=filters['search'])

        return queryset
