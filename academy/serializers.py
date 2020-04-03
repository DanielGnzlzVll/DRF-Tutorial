from rest_framework import serializers

from . import models


class TopicSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Topic
        fields = '__all__' 


class CourseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Course
        fields = '__all__' 


class DocumentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Document
        fields = '__all__' 
