from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    course = models.CharField(max_length=67)


    def __str__(self):
        return self.user.username

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name#Assignment due on 2026-02-13
    
    def get_absolute_url(self):
        return reverse('task_list', args=[str(self.name)])
    
    @property

    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['name']
        verbose_name = 'task group'
        verbose_name_plural = 'tasks groups'

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, 
                                  related_name='tasks')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, 
                                   related_name='task_list', null=True, blank=True)
    task_image = models.ImageField(upload_to='images/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)#Assignment due on 2026-02-13
    
    def get_absolute_url(self):
        return reverse('blogpage:task_detail', args=[str(self.pk)])
    
    @property

    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['-due_date']
        unique_together = ['due_date', 'name']
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

