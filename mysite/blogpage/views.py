from django.views.generic import CreateView, FormView, UpdateView #handles forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task, TaskGroup, Profile
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
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST) #handles data sent by user

        if form.is_valid():
            task = form.save(commit=False) #creates a Task object but doesn't save to database yet
            task.profile = Profile.objects.get(user=request.user)
            task.save() #saves to database
            return redirect("blogpage:task_detail", pk=task.pk) #redirects to task list page
            
            # task = Task()
            # task.name = form.cleaned_data.get("task_name")
            # task.date = form.cleaned_data.get("task_date")
            # task.taskgroup = form.cleaned_data.get("taskgroup")
            # task.profile = Profile.objects.get(user=request.user)
            # task.save() #saves to database

        
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

class TaskListView(ListView):
    model = Task
    template_name = 'blogpage/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(profile__user=self.request.user)
        return context
    
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST) #handles data sent by user

        if form.is_valid():
            task = form.save(commit=False) #creates a Task object but doesn't save to database yet
            task.profile = Profile.objects.get(user=request.user)
            task.save() #saves to database
            return self.get(request, *args, **kwargs) #redirects to task list page
         
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form 
            return self.render_to_response(context)
         

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'blogpage/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'blogpage/task_update.html'
