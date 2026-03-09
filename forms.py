from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "due_date", "taskgroup", "task_image"]
        Widgets = {
            'due_date': forms.TextInput(
                attrs = {'type': 'datetime-local'}
                )
        }

    task_name = forms.CharField(label='Task Name', max_length=100)
    task_date = forms.DateField(label='Due date')
    taskgroup = forms.ModelChoiceField(label='Task Group', queryset=TaskGroup.objects.all())