from dataclasses import fields
from rest_framework import serializers
from .models import Note

# class NoteSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     text = serializers.CharField(max_length=200)
    
#     def create(self, validated_data):
#         return Note.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','text']