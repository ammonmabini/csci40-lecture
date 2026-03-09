from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('list/', TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('add/', TaskAddView.as_view(), name='task_add'),
]

app_name = "blogpage" #blogpage application
