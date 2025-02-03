from django.contrib import admin
from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'due_date', 'completed')
    search_fields = ('title',)
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
