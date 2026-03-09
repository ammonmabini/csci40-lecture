from django.views.generic import FormView #handles forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task, TaskGroup
from .forms import TaskForm
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


tasks = []
# Create your views here.
def index (request):
    return HttpResponse("Hello, world. You're home.")

def task_list (request):

    if request.method == "POST":
        form = TaskForm(request.POST) #handles data sent by user
    
        if form.is_valid():
            task = Task()
            task.name = form.cleaned_data["task_name"]
            task.due_date = form.cleaned_data["task_date"]
            task.taskgroup = form.cleaned_data["taskgroup"]
            task.save()
            return redirect ("blogpage:task_detail", pk=task.pk)
        
    elif request.method == "UPDATE":
        pass

    else:
        form = TaskForm() #empty form

    tasks = Task.objects.all() #fetches all tasks from database

    return render (request, "blogpage/task_list.html" , {
        "form": form,
        "task_list": tasks,
        "taskgroups": TaskGroup.objects.all(),
    })

@login_required
def task_detail (request, id):
    task= Task.objects.get(pk=id)
    return render (request, "blogpage/task_detail.html", {
        "task": task,
    })

class TaskAddView(FormView):
    template_name = 'blogpage/task_add.html'
    form_class = TaskForm
    success_url = '/blogpage/list'

    def form_valid(self, form):
        tasks.append ( (form.cleaned_data["task_name"], 
                        form.cleaned_data["task_date"]) )
        return super().form_valid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'blogpage/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(profile__user=self.request.user)
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'blogpage/task_detail.html'

class taskCreateView(LoginRequiredMixin, FormView):
    template_name = 'blogpage/task_add.html'
    form_class = TaskForm
    success_url = '/blogpage/list'

    def form_valid(self, form):
        task = Task()
        task.name = form.cleaned_data["task_name"]
        task.due_date = form.cleaned_data["task_date"]
        task.taskgroup = form.cleaned_data["taskgroup"]
        task.save()
        return super().form_valid(form) 
