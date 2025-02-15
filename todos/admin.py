from django.contrib import admin
from .models import TodoItem

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created', 'update')
    list_filter = ('completed', 'created')
    search_fields = ('title', 'body')


admin.site.register(TodoItem, TodoItemAdmin)