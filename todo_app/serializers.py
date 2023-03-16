from rest_framework import serializers

from .models import ToDo

class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(required=False)
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()

class UpdateToDoSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)
    deadline = serializers.DateTimeField(required=False)
    
    def update(self, instance: ToDo, validated_data: dict):
        # instance.title = validated_data.get('title', instance.title)
        # instance.completed = validated_data.get('completed', instance.completed)
        # instance.deadline = validated_data.get('deadline', instance.deadline)
        
        # оптимизированная версия кода 
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        return instance 