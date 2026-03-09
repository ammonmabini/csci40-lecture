from django.contrib import admin
from .models import Profile, Task, TaskGroup
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
        inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup

class TaskAdmin(admin.ModelAdmin):
    model = Task
    search_fields = ('name', )
    list_display =('name', 'due_date', )
    list_filter = ('due_date', )

class TaskInLine(admin.TabularInline):
    model = Task

class TaskGroupAdmin(admin.ModelAdmin):
    inlines = [TaskInLine,]

class TaskAdmin(admin.ModelAdmin):
    model = Task
    
    fieldsets = [
        ('Details',{
            'fields': [
                ('name', 'due_date'), 
                'taskgroup',
                'profile',
                'task_image',
        ]
        }),
    ]

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)



    