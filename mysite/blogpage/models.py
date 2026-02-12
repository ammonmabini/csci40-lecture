from django.db import models
from datetime import datetime
from django.urls import reverse

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, 
                                  related_name='tasks')
    
    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)#Assignment due on 2026-02-13
    
    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.name)])
    
    @property

    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date']
        unique_together = ['due_date', 'name']
        verbose_name = 'task'
        verbose_name_plural = 'tasks'