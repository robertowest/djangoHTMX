from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',                 views.task_list,       name='task_list'),
    path('create/',          views.create_task,     name='create_task'),
    path('<int:pk>/edit/',   views.edit_task,       name='edit_task'),
    path('<int:pk>/delete/', views.delete_task,     name='delete_task'),
    path('form-modal/',      views.task_form_modal, name='task_form_modal'),
]
