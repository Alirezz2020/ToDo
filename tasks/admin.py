from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ['created_at']  # Order tasks by due date in the admin panel
