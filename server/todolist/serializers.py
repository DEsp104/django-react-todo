from rest_framework import routers, serializers, viewsets
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Todo
    fields = ('id', 'uuid', 'title', 'description', 'completed')