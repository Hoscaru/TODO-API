from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.
class ListTodoItem(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class DetailTodoItem(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer