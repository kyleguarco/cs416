from django import forms

from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ('task', 'completed')
        exclude = ('created',)

        widgets = {
            'task': forms.TextInput(attrs={ 'class': 'form-control no-border' }),
            'completed': forms.CheckboxInput(attrs={ 'class': 'form-check-input', 'role': 'switch' })
        }
