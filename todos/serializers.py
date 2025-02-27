from rest_framework import serializers
from todos.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        