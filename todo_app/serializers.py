from rest_framework import serializers

from .models import ToDo

class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField()
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()
    