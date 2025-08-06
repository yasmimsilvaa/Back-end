from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'completed', 'due_date', 'created_at')
    list_filter = ('completed', 'created_by')
    search_fields = ('title', 'description', 'created_by__user.modename')

admin.site.register(Task, TaskAdmin)
