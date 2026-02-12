from django.views.generic import FormView #handles forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task, TaskGroup
from .forms import TaskForm

# Create your views here.
def index (request):
    return HttpResponse("Hello, world. You're home.")

def task_list (request):

    if request.method == "POST":
        form = TaskForm(request.POST) #handles data sent by user

        if form.is_valid():
            tasks.append((form.cleaned_data["task_name"], form.cleaned_data["task_date"]))
            return redirect ("/blogpage/list")
        
    elif request.method == "UPDATE":
        pass

    else:
        form = TaskForm() #empty form

    tasks = Task.objects.all() #fetches all tasks from database

    return render (request, "blogpage/task_list.html" , {
        "form": form,
        "tasks": tasks,
    })

class TaskAddView(FormView):
    template_name = 'blogpage/task_add.html'
    form_class = TaskForm
    success_url = '/blogpage/list'

    def form_valid(self, form):
        tasks.append ( (form.cleaned_data["task_name"], 
                        form.cleaned_data["task_date"]) )
        return super().form_valid(form)