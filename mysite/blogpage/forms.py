from django import forms
from .models import *

class TaskForm (forms.Form):
    task_name = forms.CharField(label="Task Name", max_length=100)
    task_date = forms.DateField(label="Task Date")
    taskgroup = forms.ModelChoiceField(label="Task Group", queryset=TaskGroup.objects.all())