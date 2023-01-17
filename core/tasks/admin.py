from django.contrib import admin

from core.tasks.models import Task


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'status', 'start_date', 'end_date']


admin.site.register(Task, TaskModelAdmin)
