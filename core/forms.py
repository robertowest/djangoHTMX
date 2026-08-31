from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Task


class TaskForm(forms.ModelForm):
    """formulario para crear/editar tareas."""

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='col-md-12'),
            ),
            Row(
                Column('description', css_class='col-md-12'),
            ),
            Row(
                Column('priority', css_class='col-md-6'),
                Column('status', css_class='col-md-6'),
            ),
            Row(
                Column(
                    Submit('submit', 'Guardar', css_class='btn btn-primary'),
                    css_class='col-md-12'
                ),
            ),
        )
